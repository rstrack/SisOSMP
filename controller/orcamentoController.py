from datetime import datetime
from winreg import QueryReflectionKey
from PyQt6 import QtWidgets, QtGui, QtCore
from controller.clienteController import ClienteController
from controller.pecaController import PecaController
from controller.servicoController import ServicoController
from controller.veiculoController import VeiculoController
from model.modelo import *
from ui.telaCadastroOrcamento import TelaCadastroOrcamento
from ui.telaConsultaAux import TelaConsultaAux

class OrcamentoController():
    def __init__(self):
        super(OrcamentoController, self).__init__()
        self.viewCadastro = TelaCadastroOrcamento()
        self.ctrlPecas = PecaController()
        self.ctrlServicos = ServicoController()
        self.ctrlCliente = ClienteController()
        self.ctrlVeiculo = VeiculoController(self.viewCadastro)
        self.marcas()
        self.atualizarCompleters()
        self.initConnections()

    def atualizarCompleters(self):
        qPecas = Peca.select()
        pecas = []
        qServicos = Servico.select()
        servicos = []
        for peca in qPecas:
            pecas.append(peca.descricao)
        modelPeca = QtCore.QStringListModel()
        modelPeca.setStringList(pecas)
        self.viewCadastro.completerPeca.setModel(modelPeca)

        for servico in qServicos:
            servicos.append(servico.descricao)
        modelServico = QtCore.QStringListModel()
        modelServico.setStringList(servicos)
        self.viewCadastro.completerServico.setModel(modelServico)

    def initConnections(self):
        self.viewCadastro.botaobuscarcliente.clicked.connect(self.buscarCliente)
        self.viewCadastro.botaobuscarveiculo.clicked.connect(self.buscarVeiculo)
        self.viewCadastro.botaoSalvar.clicked.connect(self.salvarOrcamento)
        self.viewCadastro.botaoSalvareImprimir.clicked.connect(self.salvareImprimir)
        self.viewCadastro.checkboxNovoCliente.stateChanged.connect(self.habilitarCamposCliente)
        self.viewCadastro.checkboxNovoVeiculo.stateChanged.connect(self.habilitarCamposVeiculo)


    def marcas(self):
        self.viewCadastro.comboBoxMarca.clear()
        marcas = Marca.select(Marca.marca)
        for marca in marcas:
            self.viewCadastro.comboBoxMarca.addItem(marca.marca)
        self.viewCadastro.comboBoxMarca.setCurrentIndex(-1)


    def habilitarCamposCliente(self):

        if self.viewCadastro.checkboxNovoCliente.isChecked():
            self.viewCadastro.setClienteReadOnly(False)
        else:
            self.viewCadastro.setClienteReadOnly(True)


    def habilitarCamposVeiculo(self):
        if self.viewCadastro.checkboxNovoVeiculo.isChecked():
            self.viewCadastro.setVeiculoReadOnly(False)
        else:
            self.viewCadastro.setVeiculoReadOnly(True)

    
    def buscarCliente(self):
        try:
            self.window = QtWidgets.QMainWindow()
            self.viewCadastroBusca = TelaConsultaAux(self.window)
            queryCliente = Cliente.select()
            self.viewCadastroBusca.model.setRowCount(len(queryCliente))
            listaHeader = ['ID', 'Nome', 'CPF', 'CNPJ','Veículos']
            self.viewCadastroBusca.model.setHorizontalHeaderLabels(listaHeader)
            row=0
            for cliente in queryCliente:
                item = QtGui.QStandardItem(str(cliente.idCliente))
                item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
                self.viewCadastroBusca.model.setItem(row, 0, item)
                item = QtGui.QStandardItem(cliente.nome)
                item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
                self.viewCadastroBusca.model.setItem(row, 1, item)
                item = QtGui.QStandardItem(cliente.cpf)
                item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
                self.viewCadastroBusca.model.setItem(row, 2, item)               
                item = QtGui.QStandardItem(cliente.cnpj)
                item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
                self.viewCadastroBusca.model.setItem(row, 3, item)
                queryVeiculo = Veiculo.select().join(Veiculo_Cliente).join(Cliente).where((Veiculo_Cliente.cliente == cliente))
                nomes=[]
                for veiculo in queryVeiculo:
                    nomes.append(': '.join([veiculo.modelo, veiculo.placa]))
                item = QtGui.QStandardItem(', '.join(nomes))
                self.viewCadastroBusca.model.setItem(row, 4, item)
                row=row+1    
            header = self.viewCadastroBusca.tabela.horizontalHeader()
            header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Interactive)
            header.setSectionResizeMode(0,QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
            header.setStretchLastSection(True)
            self.viewCadastroBusca.botaoSelecionar.clicked.connect(self.usarCliente)
            self.window.show()
        except Exception as e:
            msg =  QtWidgets.QMessageBox()
            msg.setWindowTitle("Erro")
            msg.setText(str(e))
            msg.exec()

    def usarCliente(self):
        self.linha = self.viewCadastroBusca.tabela.selectionModel().selectedRows()[0]
        id = self.viewCadastroBusca.tabela.model().index(self.linha.row(),0).data()
        queryCliente = Cliente.select().where(Cliente.idCliente==int(id))[0]
        self.cliente=queryCliente
        if(queryCliente.cpf):
            cpf=queryCliente.cpf
            cnpj=None
        else: 
            cnpj=queryCliente.cnpj
            cpf=None
        queryCidade = Cidade.select().join(Cliente).where(queryCliente.cidade_id==Cidade.idCidade)
        if queryCidade:
            cidade=queryCidade[0].nome
            queryEstado = Estado.select().join(Cidade).where(queryCidade[0].estado_id==Estado.UF)
            if queryEstado:
                uf = queryEstado[0].UF
        else: 
            cidade = None
            uf = None

        qTel = Fone.select().where(Fone.cliente==queryCliente)
        if len(qTel)==0:
            tel1 = None
            tel2 = None
        elif len(qTel)==1:
            tel1 = qTel[0].fone
            tel2 = None
        else:
            tel1 = qTel[0].fone
            tel2 = qTel[1].fone    
        self.viewCadastro.setCliente(queryCliente.nome, cpf, cnpj, queryCliente.cep, queryCliente.endereco, queryCliente.numero,
            queryCliente.bairro, cidade, uf, tel1, tel2)
        self.viewCadastro.checkboxNovoCliente.setChecked(False)
        self.window.close()

    def buscarVeiculo(self):
        try:    
            self.window = QtWidgets.QMainWindow()
            self.viewCadastroBusca = TelaConsultaAux(self.window)
            listaHeader = ['ID', 'Marca','Modelo', 'Ano', 'Placa','Clientes Vinculados']
            self.viewCadastroBusca.model.setHorizontalHeaderLabels(listaHeader)
            queryVeiculo = Veiculo.select()
            self.viewCadastroBusca.model.setRowCount(len(queryVeiculo))
            row=0
            for veiculo in queryVeiculo:
                item = QtGui.QStandardItem(str(veiculo.idVeiculo))
                item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
                self.viewCadastroBusca.model.setItem(row, 0, item)
                querymarca = Marca.select().join(Veiculo).where(Marca.idMarca==veiculo.marca_id)
                item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
                item = QtGui.QStandardItem(querymarca[0].marca)
                item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
                self.viewCadastroBusca.model.setItem(row, 1, item)
                item = QtGui.QStandardItem(veiculo.modelo)
                item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
                self.viewCadastroBusca.model.setItem(row, 2, item)
                item = QtGui.QStandardItem(veiculo.ano)
                item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
                self.viewCadastroBusca.model.setItem(row, 3, item)
                item = QtGui.QStandardItem(veiculo.placa)
                item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
                self.viewCadastroBusca.model.setItem(row, 4, item)
                queryCliente = Cliente.select().join(Veiculo_Cliente).where(Veiculo_Cliente.veiculo==veiculo)
                nomes = []
                for cliente in queryCliente:
                    nomes.append(cliente.nome)
                item = QtGui.QStandardItem(', '.join(nomes))
                self.viewCadastroBusca.model.setItem(row, 5, item)
                row=row+1
            self.viewCadastroBusca.filter.setSourceModel(self.viewCadastroBusca.model)
            header = self.viewCadastroBusca.tabela.horizontalHeader()
            header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Interactive)
            header.setSectionResizeMode(0,QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
            header.setSectionResizeMode(3,QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
            header.setStretchLastSection(True)
            self.viewCadastroBusca.botaoSelecionar.clicked.connect(self.usarVeiculo)
            botaoVinculo = QtWidgets.QPushButton(self.viewCadastroBusca.framebotoes)
            botaoVinculo.setText("Desvincular")
            botaoVinculo.setFixedSize(100, 25)
            self.viewCadastroBusca.hlayoutbotoes.addWidget(botaoVinculo)
            self.veiculo = queryVeiculo
            self.window.show()
        except Exception as e:
                msg =  QtWidgets.QMessageBox()
                msg.setWindowTitle("Erro")
                msg.setText(str(e))
                msg.exec()

    def usarVeiculo(self):
        self.linha = self.viewCadastroBusca.tabela.selectionModel().selectedRows()[0]
        id = self.viewCadastroBusca.tabela.model().index(self.linha.row(),0).data()
        queryVeiculo = Veiculo.select().where(Veiculo.idVeiculo==int(id))[0]
        queryMarca = Marca.select().join(Veiculo).where(queryVeiculo.marca_id==Marca.idMarca)[0]
        self.veiculo=queryVeiculo
        self.viewCadastro.setVeiculo(queryMarca.marca, queryVeiculo.modelo, queryVeiculo.placa, queryVeiculo.ano)
        self.viewCadastro.checkboxNovoVeiculo.setChecked(False)
        self.window.close()
        
    def limparCampos(self):
        for lineedit in self.viewCadastro.framedados.findChildren(QtWidgets.QLineEdit):
            lineedit.clear()
        self.viewCadastro.checkboxNovoCliente.setChecked(True)
        self.viewCadastro.checkboxNovoVeiculo.setChecked(True)

    def salvarItemPeca(self, orcamento):
        if len(self.viewCadastro.linhasPeca) == 1 and not (self.viewCadastro.lineEditNomePeca.text() and self.viewCadastro.lineEditValorPeca.text()):
            raise Exception("Erro: campos vazios!")
        for desc, qtde, un, valor in self.viewCadastro.linhasPeca:
            if desc.text() and valor.text():
                qPeca = Peca.select().where(Peca.descricao==desc)
                if not qPeca:
                    aux = valor.text().replace(',','',1)
                    if aux.isdigit():
                        peca = (Peca.create(descricao=desc.text(), valor=valor.text().replace(',','.',1)))
                    else: raise Exception("Erro: digite apenas números no valor!")
                else: peca = qPeca[0]
                if not qtde.text():
                    _qtde = 1
                else: _qtde = qtde.text()
                ItemPeca.create(peca=peca, orcamento=orcamento, qtde=_qtde, un=un.currentText())
            elif desc.text() or valor.text():
                raise Exception("Preencha todos os campos!")


    def salvarOrcamento(self):
        with db.atomic() as transaction:
            try:
                if self.viewCadastro.checkboxNovoCliente.isChecked():
                    cliente = self.ctrlCliente.salvarCliente(self.viewCadastro)
                else:
                    cliente = self.cliente
                
                if self.viewCadastro.checkboxNovoVeiculo.isChecked():
                    veiculo = self.ctrlVeiculo.salvarVeiculo()
                else: veiculo = self.veiculo
                query = Veiculo_Cliente.select().where(Veiculo_Cliente.cliente==cliente and  Veiculo_Cliente.veiculo==veiculo)
                if not query:
                    Veiculo_Cliente.create(cliente=cliente, veiculo=veiculo)
                
                #servicos = self.salvarServicos()

                valorTotal = 'FUNÇÃO PRA CALCULAR O VALOR'

                data = datetime.strptime(self.viewCadastro.lineEditData.text(), "%d/%m/%Y")
                data = data.strftime("%Y-%m-%d")
                dataPrev = datetime.strptime(self.viewCadastro.lineEditDataPrev.text(), "%d/%m/%Y")
                dataPrev = dataPrev.strftime("%Y-%m-%d")
                orcamento = Orcamento.create(dataOrcamento=data, cliente=cliente, veiculo=veiculo,
                                km = self.viewCadastro.lineEditKm.text(), valorTotal=valorTotal, dataPrevista=dataPrev,
                                observacoes=self.viewCadastro.textEdit.toPlainText())
                
                self.salvarItemPeca(orcamento)


                msg =  QtWidgets.QMessageBox()
                msg.setWindowTitle("Aviso")
                msg.setText("Dados inseridos ")
                msg.exec()
                self.limparCampos()
                self.marcas()
            
            except Exception as e:
                transaction.rollback()
                msg =  QtWidgets.QMessageBox()
                msg.setWindowTitle("Erro")
                msg.setText(str(e))
                msg.exec()

    @db.atomic
    def salvareImprimir(self):
        pass

    

if __name__ == "__main__":
    c = OrcamentoController()
    c.run()

