import sys
from PyQt6 import QtWidgets
from model.modelo import *
from ui.telaCadastroOrcamento import TelaCadastroOrcamento
from util.buscaCEP import buscarCEP

class OrcamentoController():
    def __init__(self):
        super(OrcamentoController, self).__init__()
        self.app = QtWidgets.QApplication(sys.argv)
        style = open('./ui/styles.qss').read()
        self.app.setStyleSheet(style)
        self.MainWindow = QtWidgets.QMainWindow()
        self.view = TelaCadastroOrcamento(self.MainWindow)
        self.initConnections()
        self.marcas()

    def run(self):
        self.MainWindow.show()
        return self.app.exec()

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
        pass

    def buscarVeiculo(self):
        pass

    def buscarDadosCEP(self):
        cep = self.view.lineEditCEP.text()
        if len(cep) !=8:
            return
        dados = buscarCEP(self.view.lineEditCEP.text())
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
        with db.atomic() as transaction:
            try:
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
                    query = Cidade.select().where(Cidade.nome==self.view.lineEditCidade.text())
                    estado = Estado.select(Estado.UF).where(Estado.UF==self.view.comboBoxuf.currentText())
                    if not estado:
                        estado = Estado.create(UF=self.view.comboBoxuf.currentText())
                    if query:
                        dict['cidade'] = list(query)[0]
                    else:
                        cidade = Cidade.create(nome=self.view.lineEditCidade.text(), estado=estado)
                        dict['cidade'] = cidade
                return Cliente.create(**dict)
            
            except Exception as e:
                msg =  QtWidgets.QMessageBox()
                msg.setWindowTitle("Erro")
                msg.setText(str(e))
                msg.exec()
                transaction.rollback()
                return -1
    
    def salvarVeiculo(self):
        with db.atomic() as transaction:
            try:
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
            
            except Exception as e:
                msg =  QtWidgets.QMessageBox()
                msg.setWindowTitle("Erro")
                msg.setText(str(e))
                msg.exec()
                transaction.rollback()
                return -1


    def salvarOrcamento(self):
        with db.atomic() as transaction:
            try:
                cliente = self.salvarCliente()
                veiculo = self.salvarVeiculo()
                if(cliente == -1 or veiculo ==-1):
                    raise Exception()
                '''pecas = self.salvarPecas()
                servicos = self.salvarServicos()'''

                
                
                
                msg =  QtWidgets.QMessageBox()
                msg.setWindowTitle("Aviso")
                msg.setText("Dados inseridos ")
                msg.exec()
            
            except Exception as e:
                transaction.rollback()



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

