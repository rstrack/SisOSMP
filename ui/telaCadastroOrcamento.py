from PyQt6 import QtCore, QtGui, QtWidgets

class TelaCadastroOrcamento(QtWidgets.QWidget):

    def __init__(self, MainWindow):
            super(TelaCadastroOrcamento, self).__init__()
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
            self.logo_label.setPixmap(QtGui.QPixmap("logo.png"))
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
            self.gridLayout = QtWidgets.QGridLayout(self.framedados)
            self.vlayout6.addWidget(self.framedados)
            
            #dados do cliente
            self.groupBoxCliente = QtWidgets.QGroupBox(self.framedados)
            self.gridLayoutCliente = QtWidgets.QGridLayout(self.groupBoxCliente)
            self.labelNome = QtWidgets.QLabel(self.groupBoxCliente)
            self.gridLayoutCliente.addWidget(self.labelNome, 0, 0, 1, 1)
            self.lineEdit = QtWidgets.QLineEdit(self.groupBoxCliente)
            self.gridLayoutCliente.addWidget(self.lineEdit, 0, 1, 1, 1)
            self.labelPessoa = QtWidgets.QLabel(self.groupBoxCliente)
            self.gridLayoutCliente.addWidget(self.labelPessoa, 0, 2, 1, 1)
            self.comboBox = QtWidgets.QComboBox(self.groupBoxCliente)
            self.gridLayoutCliente.addWidget(self.comboBox, 0, 3, 1, 1)
            self.labelcpfj = QtWidgets.QLabel(self.groupBoxCliente)
            self.gridLayoutCliente.addWidget(self.labelcpfj, 1, 0, 1, 1)
            self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBoxCliente)
            self.gridLayoutCliente.addWidget(self.lineEdit_3, 1, 1, 1, 1)         
            self.labelCEP = QtWidgets.QLabel(self.groupBoxCliente)
            self.gridLayoutCliente.addWidget(self.labelCEP, 1, 2, 1, 1)
            self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBoxCliente)
            self.gridLayoutCliente.addWidget(self.lineEdit_4, 1, 3, 1, 1)
            self.labelEnder = QtWidgets.QLabel(self.groupBoxCliente)
            self.gridLayoutCliente.addWidget(self.labelEnder, 2, 0, 1, 1)
            self.lineEditEnder = QtWidgets.QLineEdit(self.groupBoxCliente)
            self.gridLayoutCliente.addWidget(self.lineEditEnder, 2, 1, 1, 1)
            self.labelNumero = QtWidgets.QLabel(self.groupBoxCliente)
            self.gridLayoutCliente.addWidget(self.labelNumero, 2, 2 ,1 ,1)
            self.lineEditNumero = QtWidgets.QLineEdit(self.groupBoxCliente)
            self.gridLayoutCliente.addWidget(self.lineEditNumero, 2, 3, 1, 1)
            self.labelBairro = QtWidgets.QLabel(self.groupBoxCliente)
            self.gridLayoutCliente.addWidget(self.labelBairro, 3, 0, 1, 1)
            self.lineEdit_11 = QtWidgets.QLineEdit(self.groupBoxCliente)
            self.gridLayoutCliente.addWidget(self.lineEdit_11, 3, 1, 1, 1)
            self.labelCidade = QtWidgets.QLabel(self.groupBoxCliente)
            self.gridLayoutCliente.addWidget(self.labelCidade, 3, 2, 1, 1)
            self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBoxCliente)
            self.gridLayoutCliente.addWidget(self.lineEdit_7, 3, 3, 1, 1)
            self.labelUF = QtWidgets.QLabel(self.groupBoxCliente)
            self.gridLayoutCliente.addWidget(self.labelUF, 4, 0, 1, 1)
            self.comboBox_3 = QtWidgets.QComboBox(self.groupBoxCliente)
            self.gridLayoutCliente.addWidget(self.comboBox_3, 4, 1, 1, 1)
            self.labelFone1 = QtWidgets.QLabel(self.groupBoxCliente)
            self.gridLayoutCliente.addWidget(self.labelFone1, 5, 0, 1, 1)            
            self.lineEdit_13 = QtWidgets.QLineEdit(self.groupBoxCliente)
            self.gridLayoutCliente.addWidget(self.lineEdit_13, 5, 1, 1, 1)            
            self.labelFone2 = QtWidgets.QLabel(self.groupBoxCliente)
            self.gridLayoutCliente.addWidget(self.labelFone2, 5, 2, 1, 1)
            self.lineEdit_14 = QtWidgets.QLineEdit(self.groupBoxCliente)
            self.gridLayoutCliente.addWidget(self.lineEdit_14, 5, 3, 1, 1)
 
            spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
            self.gridLayoutCliente.addItem(spacerItem, 5, 0, 1, 1)

            self.gridLayout.addWidget(self.groupBoxCliente, 0, 0, 2, 1)

            #dados do veiculo
            self.groupBoxVeiculo = QtWidgets.QGroupBox(self.framedados)
            self.gridLayoutVeiculo = QtWidgets.QGridLayout(self.groupBoxVeiculo)
            self.labelMarca = QtWidgets.QLabel(self.groupBoxVeiculo)
            self.gridLayoutVeiculo.addWidget(self.labelMarca, 0, 0, 1, 1)
            self.comboBoxMarca = QtWidgets.QComboBox(self.groupBoxVeiculo)
            self.gridLayoutVeiculo.addWidget(self.comboBoxMarca, 0, 1, 1, 1) 
            self.labelModelo = QtWidgets.QLabel(self.groupBoxVeiculo)
            self.gridLayoutVeiculo.addWidget(self.labelModelo, 0, 2, 1, 1)            
            self.lineEdit_12 = QtWidgets.QLineEdit(self.groupBoxVeiculo)
            self.gridLayoutVeiculo.addWidget(self.lineEdit_12, 0, 3, 1, 1)          
            self.labelPlaca = QtWidgets.QLabel(self.groupBoxVeiculo)
            self.gridLayoutVeiculo.addWidget(self.labelPlaca, 1, 0, 1, 1)
            self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBoxVeiculo)
            self.gridLayoutVeiculo.addWidget(self.lineEdit_8, 1, 1, 1, 1)
            self.labelAno = QtWidgets.QLabel(self.groupBoxVeiculo)
            self.gridLayoutVeiculo.addWidget(self.labelAno, 1, 2, 1, 1)
            self.lineEditAno = QtWidgets.QLineEdit(self.groupBoxVeiculo)
            self.gridLayoutVeiculo.addWidget(self.lineEditAno, 1, 3, 1, 1)
            self.labelKm = QtWidgets.QLabel(self.groupBoxVeiculo)
            self.gridLayoutVeiculo.addWidget(self.labelKm, 2, 0, 1, 1)
            self.lineEditKm = QtWidgets.QLineEdit(self.groupBoxVeiculo)
            self.gridLayoutVeiculo.addWidget(self.lineEditKm, 2, 1, 1, 1)

            spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
            self.gridLayoutVeiculo.addItem(spacerItem1, 3, 0, 1, 1)

            self.gridLayout.addWidget(self.groupBoxVeiculo, 0, 1, 1, 1)

            #dados especificos do orçamento

            self.groupBoxOrcamento = QtWidgets.QGroupBox(self.framedados)
            self.gridLayoutOrc = QtWidgets.QGridLayout(self.groupBoxOrcamento)
            self.labelData = QtWidgets.QLabel(self.groupBoxOrcamento)
            self.gridLayoutOrc.addWidget(self.labelData, 0, 0, 1, 1)
            self.lineEditData = QtWidgets.QDateEdit(self.groupBoxOrcamento)
            self.lineEditData.setCalendarPopup(True)
            self.lineEditData.setDateTime(QtCore.QDateTime.currentDateTime())
            self.gridLayoutOrc.addWidget(self.lineEditData, 0, 1, 1, 1)
            self.labelDataPrev = QtWidgets.QLabel(self.groupBoxOrcamento)
            self.gridLayoutOrc.addWidget(self.labelDataPrev, 0, 2, 1, 1)
            self.lineEditDataPrev = QtWidgets.QDateEdit(self.groupBoxOrcamento)
            self.lineEditDataPrev.setCalendarPopup(True)
            self.lineEditDataPrev.setDateTime(QtCore.QDateTime.currentDateTime())
            self.gridLayoutOrc.addWidget(self.lineEditDataPrev, 0, 3, 1, 1)
            self.gridLayout.addWidget(self.groupBoxOrcamento, 1, 1, 1, 1)

            #peças

            self.groupBoxPecas = QtWidgets.QGroupBox(self.framedados)
            self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBoxPecas)
            self.botaoAddPecas = QtWidgets.QPushButton(self.groupBoxPecas)
            self.gridLayout_2.addWidget(self.botaoAddPecas, 0, 4, 1, 1)
            self.labelNomePeca = QtWidgets.QLabel(self.groupBoxPecas)
            self.gridLayout_2.addWidget(self.labelNomePeca, 0, 0, 1, 1)
            self.labelValorPeca = QtWidgets.QLabel(self.groupBoxPecas)
            self.gridLayout_2.addWidget(self.labelValorPeca, 0, 2, 1, 1)
            self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBoxPecas)
            self.gridLayout_2.addWidget(self.lineEdit_5, 0, 1, 1, 1)
            self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBoxPecas)
            self.gridLayout_2.addWidget(self.lineEdit_6, 0, 3, 1, 1)
            spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
            self.gridLayout_2.addItem(spacerItem3, 1, 2, 1, 1)
            self.gridLayout.addWidget(self.groupBoxPecas, 2, 0, 1, 1)

            #serviços
            self.groupBoxServicos = QtWidgets.QGroupBox(self.framedados)
            self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBoxServicos)
            self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBoxServicos)
            self.gridLayout_5.addWidget(self.lineEdit_9, 0, 3, 1, 1)
            self.botaoAddServicos = QtWidgets.QPushButton(self.groupBoxServicos)
            self.gridLayout_5.addWidget(self.botaoAddServicos, 0, 4, 1, 1)
            self.labelValorServico = QtWidgets.QLabel(self.groupBoxServicos)
            self.gridLayout_5.addWidget(self.labelValorServico, 0, 2, 1, 1)
            self.labelNomeServico = QtWidgets.QLabel(self.groupBoxServicos)
            self.gridLayout_5.addWidget(self.labelNomeServico, 0, 0, 1, 1)
            self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBoxServicos)
            self.gridLayout_5.addWidget(self.lineEdit_10, 0, 1, 1, 1)
            spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
            self.gridLayout_5.addItem(spacerItem2, 1, 2, 1, 1)
            self.gridLayout.addWidget(self.groupBoxServicos, 2, 1, 1, 1)

            

            #campo de observações
            self.groupBoxObs = QtWidgets.QGroupBox(self.framedados)
            self.vlayout6_4 = QtWidgets.QVBoxLayout(self.groupBoxObs)
            self.textEdit = QtWidgets.QTextEdit(self.groupBoxObs)
            self.groupBoxObs.setMaximumHeight(120)
            self.vlayout6_4.addWidget(self.textEdit)
            self.gridLayout.addWidget(self.groupBoxObs, 3, 0, -1, -1)

            #botoes
            self.framebotoes = QtWidgets.QFrame(self.main_frame)
            self.hlayout4 = QtWidgets.QHBoxLayout(self.framebotoes)
            spacerItem5 = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
            self.hlayout4.addItem(spacerItem5)
            self.botaoSalvareImprimir = QtWidgets.QPushButton(self.framebotoes)
            self.botaoSalvareImprimir.setMinimumSize(QtCore.QSize(150, 35))
            self.hlayout4.addWidget(self.botaoSalvareImprimir)
            self.botaoSalvar = QtWidgets.QPushButton(self.framebotoes)
            self.botaoSalvar.setMinimumSize(QtCore.QSize(100, 30))
            self.hlayout4.addWidget(self.botaoSalvar)
            self.botaolimpar = QtWidgets.QPushButton(self.framebotoes)
            self.botaolimpar.setMinimumSize(QtCore.QSize(100, 30))
            self.hlayout4.addWidget(self.botaolimpar)
            self.vlayout6.addWidget(self.framebotoes)


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
        self.botaoSalvareImprimir.setText(_translate("MainWindow", "Salvar e Imprimir"))
        self.botaoSalvar.setText(_translate("MainWindow", "Salvar"))
        self.botaolimpar.setText(_translate("MainWindow", "Limpar"))
        self.menuFerramentas.setTitle(_translate("MainWindow", "Ferramentas"))
        self.actionImportar_dados.setText(_translate("MainWindow", "Importar dados"))
        self.actionExportar_dados.setText(_translate("MainWindow", "Exportar dados"))

        self.labelTitulo.setText(_translate("MainWindow", "Orçamentos"))
        self.groupBoxCliente.setTitle(_translate("MainWindow", "Dados do Cliente"))
        self.labelNome.setText(_translate("MainWindow", "Nome*"))
        self.labelCEP.setText(_translate("MainWindow", "CEP"))
        self.labelPessoa.setText(_translate("MainWindow", "Pessoa"))
        self.labelcpfj.setText(_translate("MainWindow", "CPF/CNPJ"))
        self.labelUF.setText(_translate("MainWindow", "UF"))
        self.labelCidade.setText(_translate("MainWindow", "Cidade"))
        self.labelEnder.setText(_translate("MainWindow", "Endereço"))
        self.labelNumero.setText(_translate("MainWindow", "nº"))
        self.labelBairro.setText(_translate("MainWindow", "Bairro"))
        self.labelFone1.setText(_translate("MainWindow", "Fone 1"))
        self.labelFone2.setText(_translate("MainWindow", "Fone 2"))
        self.groupBoxVeiculo.setTitle(_translate("MainWindow", "Dados do veículo"))
        self.labelMarca.setText(_translate("MainWindow", "Marca*"))
        self.labelPlaca.setText(_translate("MainWindow", "Placa*"))
        self.labelAno.setText(_translate("MainWindow", "Ano*"))
        self.labelModelo.setText(_translate("MainWindow", "Modelo*"))
        self.labelKm.setText(_translate("MainWindow", "Km*"))
        self.groupBoxOrcamento.setTitle(_translate("MainWindow", "Dados do Orçamento"))
        self.labelData.setText(_translate("MainWindow", "Data do Orçamento"))
        self.labelDataPrev.setText(_translate("MainWindow", "Data Prevista"))
        self.groupBoxServicos.setTitle(_translate("MainWindow", "Serviços"))
        self.botaoAddServicos.setText(_translate("MainWindow", "+"))
        self.labelValorServico.setText(_translate("MainWindow", "Valor"))
        self.labelNomeServico.setText(_translate("MainWindow", "Serviço"))
        self.groupBoxObs.setTitle(_translate("MainWindow", "Observações"))
        self.groupBoxPecas.setTitle(_translate("MainWindow", "Peças"))
        self.botaoAddPecas.setText(_translate("MainWindow", "+"))
        self.labelNomePeca.setText(_translate("MainWindow", "Nome da peça"))
        self.labelValorPeca.setText(_translate("MainWindow", "Valor"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = TelaCadastroOrcamento(MainWindow)
    ui.setupUi(MainWindow)
    MainWindow.show()

    style = open('./ui/styles.qss').read()
    app.setStyleSheet(style)

    sys.exit(app.exec())