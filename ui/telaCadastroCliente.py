from PyQt6 import QtCore, QtGui, QtWidgets

from controller.clienteController import ClienteController

SIGLAESTADOS = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']

class TelaCadastroCliente(QtWidgets.QMainWindow):

        def __init__(self):
                super(TelaCadastroCliente, self).__init__()
                self.controller = ClienteController(self)
                self.setupUi()
                self.comboBoxPessoa.currentIndexChanged.connect(self.escolherPessoa)

        def setupUi(self):
                self.resize(1280, 760)
                self.main_frame = QtWidgets.QFrame(self)
                self.main_frame.setObjectName("main_frame")
                self.vlayout6 = QtWidgets.QVBoxLayout(self.main_frame)               
                #frame titulo
                self.frame_titulo = QtWidgets.QFrame(self.main_frame)
                self.vlayout6.addWidget(self.frame_titulo)
                self.labelTitulo = QtWidgets.QLabel(self.frame_titulo)
                self.labelTitulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.labelTitulo.setObjectName("titulo")
                self.vlayout6.setContentsMargins(36, 18, 36, 18)
                self.vlayout6.setSpacing(36)
                self.vlayout6.addWidget(self.labelTitulo)
                self.framedados = QtWidgets.QFrame(self.main_frame)
                self.glayoutp = QtWidgets.QGridLayout(self.framedados)
                #dados do cliente
                self.groupBoxCliente = QtWidgets.QGroupBox(self.framedados)
                self.groupBoxCliente.setTitle("Dados de Identificação")
                self.glayoutp.addWidget(self.groupBoxCliente, 0, 0, 1, -1)
                self.gridLayout = QtWidgets.QGridLayout(self.groupBoxCliente)  
                self.labelPessoa = QtWidgets.QLabel(self.groupBoxCliente)
                self.gridLayout.addWidget(self.labelPessoa, 0, 0, 1, 1)
                self.labelNomeCliente = QtWidgets.QLabel(self.groupBoxCliente)
                self.gridLayout.addWidget(self.labelNomeCliente, 0, 1, 1, 1)
                self.labelCPFJ = QtWidgets.QLabel(self.groupBoxCliente)
                self.gridLayout.addWidget(self.labelCPFJ, 0, 2, 1, 1)
                self.comboBoxPessoa = QtWidgets.QComboBox(self.groupBoxCliente)
                self.comboBoxPessoa.addItems(["FÍSICA", "JURÍDICA"])
                self.gridLayout.addWidget(self.comboBoxPessoa, 1, 0, 1, 1)
                self.lineEditNomeCliente = QtWidgets.QLineEdit(self.groupBoxCliente)
                self.gridLayout.addWidget(self.lineEditNomeCliente, 1, 1, 1, 1)
                self.lineEditCPFJ = QtWidgets.QLineEdit(self.groupBoxCliente)
                self.gridLayout.addWidget(self.lineEditCPFJ, 1, 2, 1, 1)
                self.gridLayout.setColumnStretch(0,1)
                self.gridLayout.setColumnStretch(1,5)
                self.gridLayout.setColumnStretch(2,1)
                spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
                self.glayoutp.addItem(spacerItem2)
                #dados de endereço
                self.groupBoxEnder = QtWidgets.QGroupBox(self.framedados)
                self.groupBoxEnder.setTitle("Endereço")
                self.glayoutp.addWidget(self.groupBoxEnder,1,0)
                self.gridLayout2 = QtWidgets.QGridLayout(self.groupBoxEnder)
                self.groupBoxEnder.setLayout(self.gridLayout2)
                self.labelcep = QtWidgets.QLabel(self.groupBoxEnder)
                self.gridLayout2.addWidget(self.labelcep, 0, 0, 1, 1)
                self.labelender = QtWidgets.QLabel(self.groupBoxEnder)
                self.gridLayout2.addWidget(self.labelender, 0, 1, 1, 2)
                self.labelnumero = QtWidgets.QLabel(self.groupBoxEnder)
                self.gridLayout2.addWidget(self.labelnumero, 0, 3, 1, 1)
                self.lineEditCEP = QtWidgets.QLineEdit(self.groupBoxEnder)
                self.gridLayout2.addWidget(self.lineEditCEP, 1, 0, 1, 1)
                self.lineEditEnder = QtWidgets.QLineEdit(self.groupBoxEnder)
                self.gridLayout2.addWidget(self.lineEditEnder, 1, 1, 1, 2)
                self.lineEditNumero = QtWidgets.QLineEdit(self.groupBoxEnder)
                self.gridLayout2.addWidget(self.lineEditNumero, 1, 3, 1, 1)
                self.labelBairro = QtWidgets.QLabel(self.groupBoxEnder)
                self.gridLayout2.addWidget(self.labelBairro, 2, 0, 1, 2)
                self.labelCidade = QtWidgets.QLabel(self.groupBoxEnder)
                self.gridLayout2.addWidget(self.labelCidade, 2, 2, 1, 1)
                self.labelUF = QtWidgets.QLabel(self.groupBoxEnder)
                self.gridLayout2.addWidget(self.labelUF, 2, 3, 1, 1)
                self.lineEditBairro = QtWidgets.QLineEdit(self.groupBoxEnder)
                self.gridLayout2.addWidget(self.lineEditBairro, 3, 0, 1, 2)
                self.lineEditCidade = QtWidgets.QLineEdit(self.groupBoxEnder)
                self.gridLayout2.addWidget(self.lineEditCidade, 3, 2, 1, 1)
                self.comboBoxuf = QtWidgets.QComboBox(self.groupBoxEnder)
                self.comboBoxuf.addItems(SIGLAESTADOS)
                self.comboBoxuf.setCurrentText('PR')
                self.gridLayout2.addWidget(self.comboBoxuf, 3, 3, 1, 1)
                self.gridLayout2.setColumnStretch(1,2)
                self.gridLayout2.setColumnStretch(2,5)
                self.gridLayout2.setColumnStretch(3,1)
                spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
                self.glayoutp.addItem(spacerItem3)
                #telefone 
                self.groupBoxTel = QtWidgets.QGroupBox(self.framedados)
                self.groupBoxTel.setTitle("Contato")
                self.glayoutp.addWidget(self.groupBoxTel, 1, 1)
                self.vlayout7 = QtWidgets.QVBoxLayout(self.groupBoxTel)
                self.labelTel1 = QtWidgets.QLabel(self.groupBoxTel)
                self.vlayout7.addWidget(self.labelTel1)
                self.lineEditTel1 = QtWidgets.QLineEdit(self.groupBoxTel)
                self.vlayout7.addWidget(self.lineEditTel1)
                self.labelTel2 = QtWidgets.QLabel(self.groupBoxTel)
                self.vlayout7.addWidget(self.labelTel2)
                self.lineEditTel2 = QtWidgets.QLineEdit(self.groupBoxTel)
                self.vlayout7.addWidget(self.lineEditTel2)
                #dados do veiculo
                self.groupBoxCarro = QtWidgets.QGroupBox(self.framedados)
                self.groupBoxCarro.setTitle("Dados do Veículo")
                self.gridLayout4 = QtWidgets.QGridLayout(self.groupBoxCarro)
                self.labelMarca = QtWidgets.QLabel(self.groupBoxCarro)
                self.gridLayout4.addWidget(self.labelMarca, 0, 0, 1, 1)          
                self.labelModelo = QtWidgets.QLabel(self.groupBoxCarro)
                self.gridLayout4.addWidget(self.labelModelo, 0, 1, 1, 1)
                self.labelPlaca = QtWidgets.QLabel(self.groupBoxCarro)
                self.gridLayout4.addWidget(self.labelPlaca, 0, 2, 1, 1)
                self.comboBoxMarca = QtWidgets.QComboBox(self.groupBoxCarro)
                self.comboBoxMarca.setEditable(True)
                self.gridLayout4.addWidget(self.comboBoxMarca, 1, 0, 1, 1)
                self.lineEditModelo = QtWidgets.QLineEdit(self.groupBoxCarro)
                self.gridLayout4.addWidget(self.lineEditModelo, 1, 1, 1, 1)
                self.lineEditPlaca = QtWidgets.QLineEdit(self.groupBoxCarro)
                self.gridLayout4.addWidget(self.lineEditPlaca, 1, 2, 1, 1)
                self.labelAno = QtWidgets.QLabel(self.groupBoxCarro)
                self.gridLayout4.addWidget(self.labelAno, 2, 0, 1, 1)
                self.lineEditAno = QtWidgets.QLineEdit(self.groupBoxCarro)
                self.gridLayout4.addWidget(self.lineEditAno, 3, 0, 1, 1)                
                self.gridLayout4.setColumnStretch(0,1)
                self.gridLayout4.setColumnStretch(1,2)
                self.gridLayout4.setColumnStretch(2,1)
                self.glayoutp.addWidget(self.groupBoxCarro, 2, 0, 1, -1)
                spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
                self.glayoutp.addItem(spacerItem4)
                self.vlayout6.addWidget(self.framedados)
                self.glayoutp.setColumnStretch(0,3)
                self.glayoutp.setColumnStretch(1,1)
                #botoes
                self.framebotoes = QtWidgets.QFrame(self.main_frame)
                self.hlayout4 = QtWidgets.QHBoxLayout(self.framebotoes)
                spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
                self.hlayout4.addItem(spacerItem5)
                self.botaoSalvar = QtWidgets.QPushButton(self.framebotoes)
                self.botaoSalvar.setMinimumSize(QtCore.QSize(120, 35))
                self.botaoSalvar.setObjectName('botaoprincipal')
                self.hlayout4.addWidget(self.botaoSalvar)
                self.botaolimpar = QtWidgets.QPushButton(self.framebotoes)
                self.botaolimpar.setMinimumSize(QtCore.QSize(100, 30))
                self.hlayout4.addWidget(self.botaolimpar)
                self.vlayout6.addWidget(self.framebotoes)
                spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
                self.glayoutp.addItem(spacerItem6)

                self.setCentralWidget(self.main_frame)
                self.retranslateUi()
                self.setMarcas()

                self.botaolimpar.clicked.connect(self.limparCampos)
                self.botaoSalvar.clicked.connect(self.salvarCliente)


        def retranslateUi(self):
                _translate = QtCore.QCoreApplication.translate
                self.setWindowTitle(_translate("MainWindow", "Mecânica Pasetto"))
                self.labelTitulo.setText(_translate("MainWindow", "Cadastro de Clientes"))
                self.labelPessoa.setText(_translate("MainWindow", "Pessoa"))
                self.labelNomeCliente.setText(_translate("MainWindow", "Nome*"))
                self.labelCPFJ.setText(_translate("MainWindow", "CPF"))
                self.labelCidade.setText(_translate("MainWindow", "Cidade"))
                self.labelcep.setText(_translate("MainWindow", "CEP"))
                self.labelBairro.setText(_translate("MainWindow", "Bairro"))
                self.labelender.setText(_translate("MainWindow", "Endereço"))
                self.labelnumero.setText(_translate("MainWindow", "Nº"))
                self.labelUF.setText(_translate("MainWindow", "UF"))
                self.labelTel1.setText(_translate("MainWindow", "Fone 1"))
                self.labelTel2.setText(_translate("MainWindow", "Fone 2"))
                self.labelAno.setText(_translate("MainWindow", "Ano"))
                self.labelPlaca.setText(_translate("MainWindow", "Placa"))
                self.labelModelo.setText(_translate("MainWindow", "Modelo"))
                self.labelMarca.setText(_translate("MainWindow", "Marca"))
                self.botaolimpar.setText(_translate("MainWindow", "Limpar"))
                self.botaoSalvar.setText(_translate("MainWindow", "Salvar"))

        def salvarCliente(self):
                if(self.controller.salvarClienteVeiculo()):
                        self.limparCampos()
                        self.setMarcas()

        def limparCampos(self):
                for lineedit in self.framedados.findChildren(QtWidgets.QLineEdit):
                        lineedit.clear()

        def getDadosCliente(self):
                dict = {}
                if(self.lineEditCPFJ.text()):
                    if(self.comboBoxPessoa.currentIndex()==0):
                        dict['cpf'] = self.lineEditCPFJ.text()
                    else:
                        dict['cnpj'] = self.lineEditCPFJ.text()
                if(self.lineEditNomeCliente.text()):
                    dict['nome'] = self.lineEditNomeCliente.text()
                if(self.lineEditCEP.text()):
                    dict['cep'] = self.lineEditCEP.text()
                if(self.lineEditEnder.text()):
                    dict['endereco'] = self.lineEditEnder.text()
                if(self.lineEditNumero.text()):
                    dict['numero'] = self.lineEditNumero.text()
                if(self.lineEditBairro.text()):
                    dict['bairro'] = self.lineEditBairro.text()
                if(self.lineEditCidade.text()):
                    dict['cidade'] = self.lineEditCidade.text()
                dict['estado'] = self.comboBoxuf.currentText()
                return dict

        def getFones(self):
                fones = []
                if(self.lineEditTel1.text()):
                    fones.append(self.lineEditTel1.text())
                if(self.lineEditTel2.text()):
                    fones.append(self.lineEditTel2.text())
                return fones

        def getDadosVeiculo(self):
                dict = {}
                dict['marca'] = self.comboBoxMarca.currentText()
                if(self.lineEditModelo.text()):
                        dict['modelo'] = self.lineEditModelo.text()
                if(self.lineEditPlaca.text()):
                        dict['placa'] = self.lineEditPlaca.text()
                if(self.lineEditAno.text()):
                        dict['ano'] = self.lineEditAno.text()
                if(self.lineEditEnder.text()):
                        dict['endereco'] = self.lineEditEnder.text()
                return dict

        def setEndereco(self, cep=None, ender=None, numero=None, bairro=None, cidade=None, uf=None):
                if cep:
                        self.lineEditCEP.setText(cep)
                if ender:
                        self.lineEditEnder.setText(ender)
                if numero:
                        self.lineEditNumero.setText(numero)
                if bairro:
                        self.lineEditBairro.setText(bairro)
                if cidade:
                        self.lineEditCidade.setText(cidade)
                if uf:
                        self.comboBoxuf.setCurrentIndex(self.comboBoxuf.findText(uf, QtCore.Qt.MatchFlag.MatchExactly))

        def escolherPessoa(self):
                if(self.comboBoxPessoa.currentIndex() == 0):
                        self.labelCPFJ.setText('CPF')
                elif (self.comboBoxPessoa.currentIndex() == 1):
                        self.labelCPFJ.setText('CNPJ')

        def setMarcas(self):
                marcas = self.controller.getMarcas()
                for marca in marcas:
                        self.comboBoxMarca.addItem(marca.marca)
                self.comboBoxMarca.setCurrentIndex(-1)

if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        ui = TelaCadastroCliente()

        ui.show()

        style = open('./ui/styles.qss').read()
        app.setStyleSheet(style)
        
        sys.exit(app.exec())
