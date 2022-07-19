from PyQt6 import QtCore, QtGui, QtWidgets

class TelaCadastroCliente(QtWidgets.QWidget):

    def __init__(self, MainWindow):
            super(TelaCadastroCliente, self).__init__()
            self.setupUi(MainWindow)

    def setupUi(self, MainWindow):
            MainWindow.resize(1280, 720)
            self.mainwidget = QtWidgets.QWidget(MainWindow)

            self.hlayout1 = QtWidgets.QHBoxLayout(self.mainwidget)
            self.hlayout1.setContentsMargins(0, 0, 0, 0)
            self.hlayout1.setSpacing(0)
            #frame lateral
            self.framelateral = QtWidgets.QFrame(self.mainwidget)
            self.framelateral.setMaximumWidth(300)
            self.framelateral.setObjectName("framelateral")
            self.vlayout1 = QtWidgets.QVBoxLayout(self.framelateral)
            self.vlayout1.setContentsMargins(0, 0, 0, 0)
            self.vlayout1.setSpacing(0)
            #frame da logo(dentro do frame lateral)
            self.logo_frame = QtWidgets.QFrame(self.framelateral)
            self.vlayout2 = QtWidgets.QVBoxLayout(self.logo_frame)
            self.vlayout2.setContentsMargins(8, 0, 8, 0)
            self.vlayout2.setSpacing(0)
            #logo
            self.logo_label = QtWidgets.QLabel(self.logo_frame)
            self.logo_label.setMaximumHeight(150)
            self.logo_label.setPixmap(QtGui.QPixmap(u"logo.png"))
            self.logo_label.setScaledContents(True)
            self.vlayout2.addWidget(self.logo_label)
            self.vlayout1.addWidget(self.logo_frame)
            #frame do menu(dentro do frame lateral)
            self.framemenu = QtWidgets.QFrame(self.framelateral)
            self.vlayout3 = QtWidgets.QVBoxLayout(self.framemenu)
            self.vlayout3.setContentsMargins(9, -1, -1, -1)
            
            ##########################################################################################################################

            #frames do menu
            
            self.framemenu1 = QtWidgets.QFrame(self.framemenu)
            self.vlayout3.addWidget(self.framemenu1)
            self.framemenu2 = QtWidgets.QFrame(self.framemenu)
            self.vlayout3.addWidget(self.framemenu2)
            self.framemenu3 = QtWidgets.QFrame(self.framemenu)
            self.vlayout3.addWidget(self.framemenu3)
            self.framemenu4 = QtWidgets.QFrame(self.framemenu)
            self.vlayout3.addWidget(self.framemenu4)
    
            #aba "cadastro"

            self.labelcadastro = QtWidgets.QLabel(self.framemenu1)
            self.labelcadastro.setText("CADASTRO")
            self.vlayoutlabel1 = QtWidgets.QVBoxLayout(self.framemenu1)
            self.vlayoutlabel1.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
            self.vlayoutlabel1.setSpacing(10)
            self.vlayoutlabel1.addWidget(self.labelcadastro)
            self.vlayout4 = QtWidgets.QVBoxLayout(self.framemenu2)
            self.vlayout4.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
            self.vlayout4.setSpacing(10)
    
            #opçoes da aba

            self.botao_pecas = QtWidgets.QPushButton(self.framemenu2)
            self.vlayout4.addWidget(self.botao_pecas)
            self.botao_servicos = QtWidgets.QPushButton(self.framemenu2)
            self.vlayout4.addWidget(self.botao_servicos)
            self.botao_clientes = QtWidgets.QPushButton(self.framemenu2)
            self.vlayout4.addWidget(self.botao_clientes)
            self.botao_orcamentos = QtWidgets.QPushButton(self.framemenu2)
            self.vlayout4.addWidget(self.botao_orcamentos)
            
            #aba "consulta"

            self.labelconsulta = QtWidgets.QLabel(self.framemenu3)
            self.labelconsulta.setText("CONSULTA")
            self.vlayoutlabel2 = QtWidgets.QVBoxLayout(self.framemenu3)
            self.vlayoutlabel2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
            self.vlayoutlabel2.setSpacing(10)
            self.vlayoutlabel2.addWidget(self.labelconsulta)
            self.vlayout5 = QtWidgets.QVBoxLayout(self.framemenu4)
            self.vlayout5.setSpacing(9)

            #opçoes da aba
            self.botao_pecas_2 = QtWidgets.QPushButton(self.framemenu4)
            self.vlayout5.addWidget(self.botao_pecas_2)
            self.botao_servicos_2 = QtWidgets.QPushButton(self.framemenu4)
            self.vlayout5.addWidget(self.botao_servicos_2)
            self.botao_clientes_2 = QtWidgets.QPushButton(self.framemenu4)
            self.vlayout5.addWidget(self.botao_clientes_2)
            self.botao_orcamentos_2 = QtWidgets.QPushButton(self.framemenu4)
            self.vlayout5.addWidget(self.botao_orcamentos_2)
            self.botao_os = QtWidgets.QPushButton(self.framemenu4)
            self.vlayout5.addWidget(self.botao_os)
            spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
            self.vlayout3.addItem(spacerItem1)
            
            self.vlayout1.addWidget(self.framemenu)
            self.hlayout1.addWidget(self.framelateral)
            self.main_frame = QtWidgets.QFrame(self.mainwidget)
            self.main_frame.setObjectName("main_frame")
            self.hlayout1.addWidget(self.main_frame)
            self.vlayout6 = QtWidgets.QVBoxLayout(self.main_frame)
            self.vlayout6.setContentsMargins(0, 0, 0, 0)
            self.vlayout6.setSpacing(0)
            
            #####################################################################################

            #frame titulo

            self.frame_titulo = QtWidgets.QFrame(self.main_frame)
            self.vlayout6.addWidget(self.frame_titulo)
            self.labelTitulo = QtWidgets.QLabel(self.frame_titulo)
            self.labelTitulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.vlayout6.setContentsMargins(18, 18, 18, 18)
            self.vlayout6.setSpacing(50)
            self.vlayout6.addWidget(self.labelTitulo)


            self.framedados = QtWidgets.QFrame(self.main_frame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
            self.framedados.setSizePolicy(sizePolicy)
            self.glayoutp = QtWidgets.QGridLayout(self.framedados)
            #dados do cliente
            self.groupBoxCliente = QtWidgets.QGroupBox(self.framedados)
            self.groupBoxCliente.setTitle("Dados de Identificação")
            self.glayoutp.addWidget(self.groupBoxCliente, 0, 0, 1, -1)
        
            self.gridLayout = QtWidgets.QGridLayout(self.groupBoxCliente)  
            self.labelNome = QtWidgets.QLabel(self.groupBoxCliente)
            self.gridLayout.addWidget(self.labelNome, 0, 0, 1, 1)
            self.labelcpfj = QtWidgets.QLabel(self.groupBoxCliente)
            self.gridLayout.addWidget(self.labelcpfj, 0, 1, 1, 1)
            self.lineEditNome = QtWidgets.QLineEdit(self.groupBoxCliente)
            self.gridLayout.addWidget(self.lineEditNome, 1, 0, 1, 1)
            self.lineEditcpfj = QtWidgets.QLineEdit(self.groupBoxCliente)
            self.gridLayout.addWidget(self.lineEditcpfj, 1, 1, 1, 1)
            self.gridLayout.setColumnStretch(0,4)
            self.gridLayout.setColumnStretch(1,1)
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
            self.lineEditcep = QtWidgets.QLineEdit(self.groupBoxEnder)
            self.gridLayout2.addWidget(self.lineEditcep, 1, 0, 1, 1)
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
            self.comboBoxUF = QtWidgets.QComboBox(self.groupBoxEnder)
            self.gridLayout2.addWidget(self.comboBoxUF, 3, 3, 1, 1)

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
            self.gridLayout4.addWidget(self.comboBoxMarca, 1, 0, 1, 1)
            self.lineEdit_15 = QtWidgets.QLineEdit(self.groupBoxCarro)
            self.gridLayout4.addWidget(self.lineEdit_15, 1, 1, 1, 1)
            self.lineEdit_12 = QtWidgets.QLineEdit(self.groupBoxCarro)
            self.gridLayout4.addWidget(self.lineEdit_12, 1, 2, 1, 1)
            self.labelNome3 = QtWidgets.QLabel(self.groupBoxCarro)
            self.gridLayout4.addWidget(self.labelNome3, 2, 0, 1, 1)
            self.lineEdit_13 = QtWidgets.QLineEdit(self.groupBoxCarro)
            self.gridLayout4.addWidget(self.lineEdit_13, 3, 0, 1, 1)
            
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
            self.botaoSalvar.setMinimumSize(QtCore.QSize(100, 30))
            self.hlayout4.addWidget(self.botaoSalvar)
            self.botaolimpar = QtWidgets.QPushButton(self.framebotoes)
            self.botaolimpar.setMinimumSize(QtCore.QSize(100, 30))
            self.hlayout4.addWidget(self.botaolimpar)
            self.vlayout6.addWidget(self.framebotoes)
            spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
            self.glayoutp.addItem(spacerItem6)

            #####################################################################################
            
            #barra de menu
            
            MainWindow.setCentralWidget(self.mainwidget)
            self.menubar = QtWidgets.QMenuBar(MainWindow)
            self.menubar.setGeometry(QtCore.QRect(0, 0, 948, 21))
            self.menubar.setDefaultUp(False)
            self.menuFerramentas = QtWidgets.QMenu(self.menubar)
            MainWindow.setMenuBar(self.menubar)
            self.actionImportar_dados = QtGui.QAction(MainWindow)
            self.actionExportar_dados = QtGui.QAction(MainWindow)
            self.menuFerramentas.addAction(self.actionImportar_dados)
            self.menuFerramentas.addAction(self.actionExportar_dados)
            self.menubar.addAction(self.menuFerramentas.menuAction())

            self.retranslateUi(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.botao_pecas.setText(_translate("MainWindow", "PEÇAS"))
        self.botao_servicos.setText(_translate("MainWindow", "SERVIÇOS"))
        self.botao_clientes.setText(_translate("MainWindow", "CLIENTES"))
        self.botao_orcamentos.setText(_translate("MainWindow", "ORÇAMENTOS"))
        self.botao_pecas_2.setText(_translate("MainWindow", "PEÇAS"))
        self.botao_servicos_2.setText(_translate("MainWindow", "SERVIÇOS"))
        self.botao_clientes_2.setText(_translate("MainWindow", "CLIENTES"))
        self.botao_orcamentos_2.setText(_translate("MainWindow", "ORÇAMENTOS"))
        self.botao_os.setText(_translate("MainWindow", "ORDENS DE SERVIÇO"))

        self.menuFerramentas.setTitle(_translate("MainWindow", "Ferramentas"))
        self.actionImportar_dados.setText(_translate("MainWindow", "Importar dados"))
        self.actionExportar_dados.setText(_translate("MainWindow", "Exportar dados"))

        self.labelTitulo.setText(_translate("MainWindow", "Cadastro de Clientes"))
        self.labelNome.setText(_translate("MainWindow", "Nome*"))
        self.labelcpfj.setText(_translate("MainWindow", "CPF/CNPJ"))
        self.labelCidade.setText(_translate("MainWindow", "Cidade"))
        self.labelcep.setText(_translate("MainWindow", "CEP"))
        self.labelBairro.setText(_translate("MainWindow", "Bairro"))
        self.labelender.setText(_translate("MainWindow", "Endereço"))
        self.labelnumero.setText(_translate("MainWindow", "Nº"))
        self.labelUF.setText(_translate("MainWindow", "UF"))
        self.labelTel1.setText(_translate("MainWindow", "Fone 1"))
        self.labelTel2.setText(_translate("MainWindow", "Fone 2"))
        self.labelNome3.setText(_translate("MainWindow", "Ano"))
        self.labelPlaca.setText(_translate("MainWindow", "Placa"))
        self.labelModelo.setText(_translate("MainWindow", "Modelo"))
        self.labelMarca.setText(_translate("MainWindow", "Marca"))


        self.botaolimpar.setText(_translate("MainWindow", "Limpar"))
        self.botaoSalvar.setText(_translate("MainWindow", "Salvar"))


    def addlinhapeca(self):
            label1 = QtWidgets.QLabel(text="Nome da peça")
            lineedit1 = QtWidgets.QLineEdit()
            label2 = QtWidgets.QLabel(text="Valor")
            lineedit2 = QtWidgets.QLineEdit()
            self.gridLayout.addWidget(label1, len(self.linhaspeca), 0, 1, 1)
            self.gridLayout.addWidget(lineedit1, len(self.linhaspeca), 1, 1, 1)
            self.gridLayout.addWidget(label2, len(self.linhaspeca), 3, 1, 1)
            lineedit2.setMaximumWidth(100)
            self.gridLayout.addWidget(lineedit2, len(self.linhaspeca), 4, 1, 1)
            self.linhaspeca.append([lineedit1, lineedit2])
            self.gridLayout.addWidget(self.botaoadd, len(self.linhaspeca)-1, 5, 1, 1)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TelaCadastroCliente(MainWindow)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
