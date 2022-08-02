import sys
from PyQt6 import QtWidgets, QtGui, QtCore
from model.modelo import *
from ui.telaCadastroOrcamento import TelaCadastroOrcamento
from ui.telaConsultaAux import TelaConsultaAux
from util.buscaCEP import BuscaCEP

class OrcamentoController():
    def __init__(self):
        super(OrcamentoController, self).__init__()
        self.MainWindow = QtWidgets.QMainWindow()
        self.view = TelaCadastroOrcamento(self.MainWindow)
        self.initConnections()
        self.marcas()
        self.idCliente = 0
        self.idVeiculo =0

    def run(self):
        self.MainWindow.show()

    def exit(self):
        self.MainWindow.hide()

    def initConnections(self):
        self.view.botaoAddPecas.clicked.connect(self.addLinhaPeca)
        self.view.botaoAddServicos.clicked.connect(self.addLinhaServico)
        self.view.botaobuscarcliente.clicked.connect(self.buscarCliente)
        self.view.botaobuscarveiculo.clicked.connect(self.buscarVeiculo)
        self.view.lineEditCEP.returnPressed.connect(self.buscarDadosCEP)
        self.view.botaolimpar.clicked.connect(self.limparCampos)
        self.view.botaoSalvar.clicked.connect(self.salvarOrcamento)
        self.view.botaoSalvareImprimir.clicked.connect(self.salvareImprimir)
        self.view.comboBox.currentIndexChanged.connect(self.escolherPessoa)

    def marcas(self):
        self.view.comboBoxMarca.clear()
        marcas = Marca.select(Marca.marca)
        for marca in marcas:
            self.view.comboBoxMarca.addItem(marca.marca)
        self.view.comboBoxMarca.setCurrentIndex(-1)

    def addLinhaPeca(self):
        label1 = QtWidgets.QLabel(text="Peça")
        lineedit1 = QtWidgets.QLineEdit()
        label2 = QtWidgets.QLabel(text="Valor")
        lineedit2 = QtWidgets.QLineEdit()
        self.view.gridLayout_2.addWidget(label1, len(self.view.linhaspeca), 0, 1, 1)
        self.view.gridLayout_2.addWidget(lineedit1, len(self.view.linhaspeca), 1, 1, 1)
        self.view.gridLayout_2.addWidget(label2, len(self.view.linhaspeca), 3, 1, 1)
        self.view.gridLayout_2.addWidget(lineedit2, len(self.view.linhaspeca), 4, 1, 1)
        self.view.linhaspeca.append([lineedit1, lineedit2])
        self.view.gridLayout_2.addWidget(self.view.botaoAddPecas, len(self.view.linhaspeca)-1, 5, 1, 1)
        self.view.gridLayout_2.removeItem(self.view.spacerpeca)
        self.view.gridLayout_2.addItem(self.view.spacerpeca, len(self.view.linhaspeca), 0, 1, 1)

    def addLinhaServico(self):
        label1 = QtWidgets.QLabel(text="Serviço")
        lineedit1 = QtWidgets.QLineEdit()
        label2 = QtWidgets.QLabel(text="Valor")
        lineedit2 = QtWidgets.QLineEdit()
        self.view.gridLayout_5.addWidget(label1, len(self.view.linhasservicos), 0, 1, 1)
        self.view.gridLayout_5.addWidget(lineedit1, len(self.view.linhasservicos), 1, 1, 1)
        self.view.gridLayout_5.addWidget(label2, len(self.view.linhasservicos), 3, 1, 1)
        self.view.gridLayout_5.addWidget(lineedit2, len(self.view.linhasservicos), 4, 1, 1)
        self.view.linhasservicos.append([lineedit1, lineedit2])
        self.view.gridLayout_5.addWidget(self.view.botaoAddServicos, len(self.view.linhasservicos)-1, 5, 1, 1)
        self.view.gridLayout_5.removeItem(self.view.spacerservico)
        self.view.gridLayout_5.addItem(self.view.spacerservico, len(self.view.linhasservicos), 0, 1, 1)

    def buscarCliente(self):
        try:
            self.window = QtWidgets.QMainWindow()
            self.viewBusca = TelaConsultaAux(self.window)
            listaHeader = ['ID', 'Nome', 'CPF', 'CNPJ','Veiculos']
            queryCliente = Cliente.select()
            model = QtGui.QStandardItemModel(len(queryCliente),1)
            model.setHorizontalHeaderLabels(listaHeader)
            row=0
            for cliente in queryCliente:
                item = QtGui.QStandardItem(str(cliente.idCliente))
                item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
                model.setItem(row, 0, item)
                item = QtGui.QStandardItem(cliente.nome)
                item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
                model.setItem(row, 1, item)
                item = QtGui.QStandardItem(cliente.cpf)
                item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
                model.setItem(row, 2, item)               
                item = QtGui.QStandardItem(cliente.cnpj)
                item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
                model.setItem(row, 3, item)
                queryVeiculo = Veiculo.select().join(Veiculo_Cliente).join(Cliente).where((Veiculo_Cliente.cliente == cliente))
                nomes=[]
                for veiculo in queryVeiculo:
                    nomes.append(': '.join([veiculo.modelo, veiculo.placa]))
                item = QtGui.QStandardItem(', '.join(nomes))
                model.setItem(row, 4, item)

                row=row+1
            
            self.viewBusca.filter.setSourceModel(model)
            self.viewBusca.filter.setFilterKeyColumn(-1)
            self.viewBusca.lineEditBusca.textChanged.connect(self.viewBusca.filter.setFilterRegularExpression)
            self.viewBusca.tabela.setModel(self.viewBusca.filter)
            header = self.viewBusca.tabela.horizontalHeader()
            header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Interactive)
            header.setSectionResizeMode(0,QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
            header.setStretchLastSection(True)
            
            self.viewBusca.botaoSelecionar.clicked.connect(self.usarCliente)
            self.window.show()
        except Exception as e:
            msg =  QtWidgets.QMessageBox()
            msg.setWindowTitle("Erro")
            msg.setText(str(e))
            msg.exec()

    def usarCliente(self):
        self.linha = self.viewBusca.tabela.selectionModel().selectedRows()[0]
        id = self.viewBusca.tabela.model().index(self.linha.row(),0).data()
        queryCliente = Cliente.select().where(Cliente.idCliente==int(id))
        self.view.lineEditNomeCliente.setText(queryCliente[0].nome)
        self.view.lineEditCEP.setText(queryCliente[0].cep)
        self.view.lineEditEnder.setText(queryCliente[0].endereco)
        self.view.lineEditNumero.setText(queryCliente[0].numero)
        self.view.lineEditBairro.setText(queryCliente[0].bairro)
        if(queryCliente[0].cpf):
            self.view.lineEditCPFJ.setText(queryCliente[0].cpf)
            self.view.labelcpfj.setText("CPF")
            self.view.comboBox.setCurrentIndex(0)
        if(queryCliente[0].cnpj):
            self.view.lineEditCPFJ.setText(queryCliente[0].cnpj)
            self.view.labelcpfj.setText("CNPJ")
            self.view.comboBox.setCurrentIndex(1)
        queryCidade = Cidade.select().join(Cliente).where(queryCliente[0].cidade_id==Cidade.idCidade)
        self.view.lineEditCidade.setText(queryCidade[0].nome)
        queryEstado = Estado.select().join(Cidade).where(queryCidade[0].estado_id==Estado.UF)
        for index in range(self.view.comboBoxuf.count()):
            if(self.view.comboBoxuf.itemText(index)==queryEstado[0].UF):
                self.view.comboBoxuf.setCurrentIndex(index)
                break
        self.idCliente = queryCliente[0].idCliente
        self.window.close()

    def buscarVeiculo(self):
        try:    
            self.window = QtWidgets.QMainWindow()
            self.viewBusca = TelaConsultaAux(self.window)
            listaHeader = ['ID', 'Marca','Modelo', 'Ano', 'Placa','Clientes Vinculados']
            queryVeiculo = Veiculo.select()
            model = QtGui.QStandardItemModel(len(queryVeiculo),1)
            model.setHorizontalHeaderLabels(listaHeader)
            row=0
            for veiculo in queryVeiculo:
                item = QtGui.QStandardItem(str(veiculo.idVeiculo))
                item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
                model.setItem(row, 0, item)
                querymarca = Marca.select().join(Veiculo).where(Marca.idMarca==veiculo.marca_id)
                item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
                item = QtGui.QStandardItem(querymarca[0].marca)
                item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
                model.setItem(row, 1, item)
                item = QtGui.QStandardItem(veiculo.modelo)
                item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
                model.setItem(row, 2, item)
                item = QtGui.QStandardItem(veiculo.ano)
                item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
                model.setItem(row, 3, item)
                item = QtGui.QStandardItem(veiculo.placa)
                item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
                model.setItem(row, 4, item)
                ##############################################################################################
                queryCliente = Cliente.select().join(Veiculo_Cliente).where(Veiculo_Cliente.veiculo==veiculo)
                nomes = []
                for cliente in queryCliente:
                    nomes.append(cliente.nome)
                item = QtGui.QStandardItem(', '.join(nomes))
                model.setItem(row, 5, item)
                row=row+1
            self.viewBusca.filter.setSourceModel(model)
            self.viewBusca.filter.setFilterKeyColumn(-1)
            self.viewBusca.lineEditBusca.textChanged.connect(self.viewBusca.filter.setFilterRegularExpression)
            self.viewBusca.tabela.setModel(self.viewBusca.filter)
            header = self.viewBusca.tabela.horizontalHeader()
            header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Interactive)
            header.setSectionResizeMode(0,QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
            header.setSectionResizeMode(3,QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
            header.setStretchLastSection(True)

            self.viewBusca.botaoSelecionar.clicked.connect(self.usarVeiculo)

            botaoVinculo = QtWidgets.QPushButton(self.viewBusca.framebotoes)
            botaoVinculo.setText("Desvincular")
            botaoVinculo.setFixedSize(100, 25)
            self.viewBusca.hlayoutbotoes.addWidget(botaoVinculo)

            self.window.show()
        except Exception as e:
                msg =  QtWidgets.QMessageBox()
                msg.setWindowTitle("Erro")
                msg.setText(str(e))
                msg.exec()

    def usarVeiculo(self):
        self.linha = self.viewBusca.tabela.selectionModel().selectedRows()[0]
        id = self.viewBusca.tabela.model().index(self.linha.row(),0).data()
        queryVeiculo = Veiculo.select().where(Veiculo.idVeiculo==int(id))
        self.view.lineEditModelo.setText(queryVeiculo[0].modelo)
        self.view.lineEditPlaca.setText(queryVeiculo[0].placa)
        self.view.lineEditAno.setText(queryVeiculo[0].ano)
        queryMarca = Marca.select().join(Veiculo).where(queryVeiculo[0].marca_id==Marca.idMarca)
        for index in range(self.view.comboBoxMarca.count()):
            if(self.view.comboBoxMarca.itemText(index)==queryMarca[0].marca):
                self.view.comboBoxMarca.setCurrentIndex(index)
                break
        self.idVeiculo = queryVeiculo[0].idVeiculo
        self.view.comboBoxMarca.setEnabled(False)
        self.view.lineEditModelo.setReadOnly(True)
        self.view.lineEditAno.setReadOnly(True)
        self.view.lineEditPlaca.setReadOnly(True)
        self.window.close()

    def buscarDadosCEP(self):
        cep = self.view.lineEditCEP.text()
        if len(cep) !=8:
            return
        dados = BuscaCEP.buscarCEP(self.view.lineEditCEP.text())
        if 'erro' in dados:
            return
        self.view.lineEditEnder.setText(dados['logradouro'])
        self.view.lineEditBairro.setText(dados['bairro'])
        self.view.lineEditCidade.setText(dados['localidade'])
        for index in range(self.view.comboBoxuf.count()):
            if(self.view.comboBoxuf.itemText(index)==dados['uf']):
                self.view.comboBoxuf.setCurrentIndex(index)
                return
        
    def limparCampos(self):
        for lineedit in self.view.framedados.findChildren(QtWidgets.QLineEdit):
            lineedit.clear()
        self.marcas()

    def salvarCliente(self):
        dict = {}
        if(self.view.lineEditCPFJ.text()):
            if(self.view.comboBox.currentIndex()==0):
                dict['cpf'] = self.view.lineEditCPFJ.text()
            else:
                dict['cnpj'] = self.view.lineEditCPFJ.text()
        if(self.view.lineEditNomeCliente.text()):
            dict['nome'] = self.view.lineEditNomeCliente.text()
        else: raise Exception("Campo 'Nome' obrigatório")
        if(self.view.lineEditCEP.text()):
            dict['cep'] = self.view.lineEditCEP.text()
        if(self.view.lineEditEnder.text()):
            dict['endereco'] = self.view.lineEditEnder.text()
        if(self.view.lineEditNumero.text()):
            dict['numero'] = self.view.lineEditNumero.text()
        if(self.view.lineEditBairro.text()):
            dict['bairro'] = self.view.lineEditBairro.text()

        if(self.view.lineEditCidade.text()):
            queryCliente = Cidade.select().where(Cidade.nome==self.view.lineEditCidade.text())
            estado = Estado.select(Estado.UF).where(Estado.UF==self.view.comboBoxuf.currentText())
            if not estado:
                estado = Estado.create(UF=self.view.comboBoxuf.currentText())
            if queryCliente:
                dict['cidade'] = list(queryCliente)[0]
            else:
                cidade = Cidade.create(nome=self.view.lineEditCidade.text(), estado=estado)
                dict['cidade'] = cidade
        return Cliente.create(**dict)
    
    def salvarVeiculo(self):
        dict = {}
        marca = Marca.select(Marca.idMarca).where(Marca.marca==self.view.comboBoxMarca.currentText()) 
        if not marca:
            marca = Marca.create(marca=self.view.comboBoxMarca.currentText())
        dict['marca'] = marca
        if(self.view.lineEditModelo.text()):
            dict['modelo'] = self.view.lineEditModelo.text()
        if(self.view.lineEditPlaca.text()):
            dict['placa'] = self.view.lineEditPlaca.text()
        if(self.view.lineEditAno.text()):
            dict['ano'] = self.view.lineEditAno.text()
        if(self.view.lineEditEnder.text()):
            dict['endereco'] = self.view.lineEditEnder.text()
        if(self.view.lineEditKm.text()):
            dict['km'] = self.view.lineEditKm.text()

        return Veiculo.create(**dict)

    def salvarPecas(self):
        pass

    def salvarServicos(self):
        pass

    def salvarOrcamento(self):
        with db.atomic() as transaction:
            try:
                if not self.idCliente:
                    cliente = self.salvarCliente()
                    self.idCliente = 0
                else:
                    cliente = Cliente.select().where(Cliente.nome==self.view.lineEditNomeCliente.text())
                if not self.idVeiculo:
                    veiculo = self.salvarVeiculo()
                    self.idVeiculo = 0
                else: veiculo = Veiculo.select().where(Veiculo.modelo==self.view.lineEditModelo.text())
                veiculocliente = Veiculo_Cliente.create(cliente=cliente, veiculo=veiculo)
                
                pecas = self.salvarPecas()
                servicos = self.salvarServicos()
                
                msg =  QtWidgets.QMessageBox()
                msg.setWindowTitle("Aviso")
                msg.setText("Dados inseridos ")
                msg.exec()
            
            except Exception as e:
                transaction.rollback()
                msg =  QtWidgets.QMessageBox()
                msg.setWindowTitle("Erro")
                msg.setText(str(e))
                msg.exec()

    @db.atomic
    def salvareImprimir(self):
        pass

    def escolherPessoa(self):
        if(self.view.comboBox.currentIndex() == 0):
            self.view.labelcpfj.setText('CPF')
        elif (self.view.comboBox.currentIndex() == 1):
            self.view.labelcpfj.setText('CNPJ')

    

if __name__ == "__main__":
    c = OrcamentoController()
    c.run()

