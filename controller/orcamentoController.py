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
        self.linhaspecas = [[self.view.lineEditNomePeca, self.view.lineEditValorPeca]]
        self.linhasServicos = [[self.view.lineEditNomeServico, self.view.lineEditValorServico]]
        self.initConnections()
        self.marcas()

    def run(self):
        self.MainWindow.show()

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
        self.view.checkboxNovoCliente.stateChanged.connect(self.habilitarCamposCliente)
        self.view.checkboxNovoVeiculo.stateChanged.connect(self.habilitarCamposVeiculo)

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
        self.view.gridLayout_2.addWidget(label1, len(self.linhaspecas), 0, 1, 1)
        self.view.gridLayout_2.addWidget(lineedit1, len(self.linhaspecas), 1, 1, 1)
        self.view.gridLayout_2.addWidget(label2, len(self.linhaspecas), 3, 1, 1)
        self.view.gridLayout_2.addWidget(lineedit2, len(self.linhaspecas), 4, 1, 1)
        self.linhaspecas.append([lineedit1, lineedit2])
        self.view.gridLayout_2.addWidget(self.view.botaoAddPecas, len(self.linhaspecas)-1, 5, 1, 1)
        self.view.gridLayout_2.removeItem(self.view.spacerpeca)
        self.view.gridLayout_2.addItem(self.view.spacerpeca, len(self.linhaspecas), 0, 1, 1)

    def addLinhaServico(self):
        label1 = QtWidgets.QLabel(text="Serviço")
        lineedit1 = QtWidgets.QLineEdit()
        label2 = QtWidgets.QLabel(text="Valor")
        lineedit2 = QtWidgets.QLineEdit()
        self.view.gridLayout_5.addWidget(label1, len(self.linhasServicos), 0, 1, 1)
        self.view.gridLayout_5.addWidget(lineedit1, len(self.linhasServicos), 1, 1, 1)
        self.view.gridLayout_5.addWidget(label2, len(self.linhasServicos), 3, 1, 1)
        self.view.gridLayout_5.addWidget(lineedit2, len(self.linhasServicos), 4, 1, 1)
        self.linhasServicos.append([lineedit1, lineedit2])
        self.view.gridLayout_5.addWidget(self.view.botaoAddServicos, len(self.linhasServicos)-1, 5, 1, 1)
        self.view.gridLayout_5.removeItem(self.view.spacerservico)
        self.view.gridLayout_5.addItem(self.view.spacerservico, len(self.linhasServicos), 0, 1, 1)

    def habilitarCamposCliente(self):
        for lineEdit in self.view.groupBoxCliente.findChildren(QtWidgets.QLineEdit):
            if self.view.checkboxNovoCliente.isChecked():
                lineEdit.clear()
                lineEdit.setReadOnly(False)
            else:
                lineEdit.setReadOnly(True)

    def habilitarCamposVeiculo(self):
        for lineEdit in self.view.groupBoxVeiculo.findChildren(QtWidgets.QLineEdit):
            if self.view.checkboxNovoVeiculo.isChecked():
                lineEdit.clear()
                lineEdit.setReadOnly(False)
            else:
                lineEdit.setReadOnly(True)
        self.view.lineEditKm.setReadOnly(False)

            

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
        queryCliente = Cliente.select().where(Cliente.idCliente==int(id))[0]
        self.cliente=queryCliente
        self.view.lineEditNomeCliente.setText(queryCliente.nome)
        self.view.lineEditNomeCliente.setReadOnly(True)
        self.view.lineEditCEP.setText(queryCliente.cep)
        self.view.lineEditCEP.setReadOnly(True)
        self.view.lineEditEnder.setText(queryCliente.endereco)
        self.view.lineEditEnder.setReadOnly(True)
        self.view.lineEditNumero.setText(queryCliente.numero)
        self.view.lineEditNumero.setReadOnly(True)
        self.view.lineEditBairro.setText(queryCliente.bairro)
        self.view.lineEditBairro.setReadOnly(True)
        if(queryCliente.cpf):
            self.view.lineEditCPFJ.setText(queryCliente.cpf)
            self.view.labelcpfj.setText("CPF")
            self.view.comboBox.setCurrentIndex(0)
        if(queryCliente.cnpj):
            self.view.lineEditCPFJ.setText(queryCliente.cnpj)
            self.view.labelcpfj.setText("CNPJ")
            self.view.comboBox.setCurrentIndex(1)
        queryCidade = Cidade.select().join(Cliente).where(queryCliente.cidade_id==Cidade.idCidade)
        if queryCidade:
            self.view.lineEditCidade.setText(queryCidade[0].nome)
            queryEstado = Estado.select().join(Cidade).where(queryCidade[0].estado_id==Estado.UF)
            if queryEstado:
                for index in range(self.view.comboBoxuf.count()):
                    if(self.view.comboBoxuf.itemText(index)==queryEstado[0].UF):
                        self.view.comboBoxuf.setCurrentIndex(index)
                        break
        self.view.checkboxNovoCliente.setChecked(False)
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
            self.veiculo = queryVeiculo
            self.window.show()
        except Exception as e:
                msg =  QtWidgets.QMessageBox()
                msg.setWindowTitle("Erro")
                msg.setText(str(e))
                msg.exec()

    def usarVeiculo(self):
        self.linha = self.viewBusca.tabela.selectionModel().selectedRows()[0]
        id = self.viewBusca.tabela.model().index(self.linha.row(),0).data()
        queryVeiculo = Veiculo.select().where(Veiculo.idVeiculo==int(id))[0]
        self.veiculo=queryVeiculo
        self.view.lineEditModelo.setText(queryVeiculo.modelo)
        self.view.lineEditPlaca.setText(queryVeiculo.placa)
        self.view.lineEditAno.setText(queryVeiculo.ano)
        queryMarca = Marca.select().join(Veiculo).where(queryVeiculo.marca_id==Marca.idMarca)
        for index in range(self.view.comboBoxMarca.count()):
            if(self.view.comboBoxMarca.itemText(index)==queryMarca[0].marca):
                self.view.comboBoxMarca.setCurrentIndex(index)
                break
        self.idVeiculo = queryVeiculo.idVeiculo
        self.view.comboBoxMarca.setEnabled(False)
        self.view.lineEditModelo.setReadOnly(True)
        self.view.lineEditAno.setReadOnly(True)
        self.view.lineEditPlaca.setReadOnly(True)
        self.view.checkboxNovoVeiculo.setChecked(False)
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
        self.view.checkboxNovoCliente.setChecked(True)
        self.view.checkboxNovoVeiculo.setChecked(True)

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
                if self.view.checkboxNovoCliente.isChecked():
                    cliente = self.salvarCliente()
                else:
                    cliente = self.cliente
                if self.view.checkboxNovoVeiculo.isChecked():
                    veiculo = self.salvarVeiculo()
                else: veiculo = self.veiculo

                if Veiculo_Cliente.select().where(Veiculo_Cliente.cliente==cliente and  Veiculo_Cliente.veiculo==veiculo) == None:
                    Veiculo_Cliente.create(cliente=cliente, veiculo=veiculo)
                
                pecas = self.salvarPecas()
                servicos = self.salvarServicos()
                
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

    def escolherPessoa(self):
        if(self.view.comboBox.currentIndex() == 0):
            self.view.labelcpfj.setText('CPF')
        elif (self.view.comboBox.currentIndex() == 1):
            self.view.labelcpfj.setText('CNPJ')

    

if __name__ == "__main__":
    c = OrcamentoController()
    c.run()

