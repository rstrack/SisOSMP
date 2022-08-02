from PyQt6 import QtCore, QtGui, QtWidgets

SIGLAESTADOS = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']

class TelaCadastroOrcamento(QtWidgets.QWidget):

        def __init__(self, MainWindow):
                super(TelaCadastroOrcamento, self).__init__()
                self.setupUi(MainWindow)

        def setupUi(self, MainWindow):

                MainWindow.resize(1280, 760)
                self.mainwidget = QtWidgets.QWidget(MainWindow)

                self.hlayout1 = QtWidgets.QHBoxLayout(self.mainwidget)
                self.hlayout1.setContentsMargins(0, 0, 0, 0)
                self.hlayout1.setSpacing(0)
                #frame lateral
                self.framelateral = QtWidgets.QFrame(self.mainwidget)
                self.framelateral.setMaximumWidth(250)
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
                self.logo_label.setPixmap(QtGui.QPixmap("./resources/logo.png"))
                self.logo_label.setScaledContents(True)
                self.vlayout2.addWidget(self.logo_label)
                self.vlayout1.addWidget(self.logo_frame)
                #frame do menu(dentro do frame lateral)
                self.framemenu = QtWidgets.QFrame(self.framelateral)
                self.framemenu.setObjectName('framemenu')
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
                self.labelcadastro.setFixedHeight(25)
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
                self.botao_orcamentos.setObjectName('atual')
                self.vlayout4.addWidget(self.botao_orcamentos)
                
                #aba "consulta"

                self.labelconsulta = QtWidgets.QLabel(self.framemenu3)
                self.labelconsulta.setText("CONSULTA")
                self.labelconsulta.setFixedHeight(25)
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
                self.labelTitulo.setObjectName("titulo")
                self.vlayout6.setContentsMargins(18, 18, 18, 18)
                self.vlayout6.setSpacing(36)
                self.vlayout6.addWidget(self.labelTitulo)
                self.framedados = QtWidgets.QFrame(self.main_frame)
                self.gridLayout = QtWidgets.QGridLayout(self.framedados)
                self.gridLayout.setVerticalSpacing(9)
                self.gridLayout.setHorizontalSpacing(9)
                self.vlayout6.addWidget(self.framedados)
                
                #dados do cliente
                self.groupBoxCliente = QtWidgets.QGroupBox(self.framedados)
                self.gridLayoutCliente = QtWidgets.QGridLayout(self.groupBoxCliente)
                self.gridLayoutCliente.setVerticalSpacing(9)
                self.gridLayoutCliente.setHorizontalSpacing(9)
                self.botaobuscarcliente = QtWidgets.QPushButton(self.groupBoxCliente)
                self.botaobuscarcliente.setFixedSize(180,25)
                self.gridLayoutCliente.addWidget(self.botaobuscarcliente, 0, 0, 1, 2)
                self.checkboxNovoCliente = QtWidgets.QCheckBox(self.groupBoxCliente)
                self.gridLayoutCliente.addWidget(self.checkboxNovoCliente, 0, 2, 1, 2)
                self.labelPessoa = QtWidgets.QLabel(self.groupBoxCliente)
                self.gridLayoutCliente.addWidget(self.labelPessoa, 1, 0, 1, 1)
                self.comboBox = QtWidgets.QComboBox(self.groupBoxCliente)
                self.comboBox.addItems(["FÍSICA", "JURÍDICA"])
                self.gridLayoutCliente.addWidget(self.comboBox, 1, 1, 1, 1)
                self.labelcpfj = QtWidgets.QLabel(self.groupBoxCliente)
                self.gridLayoutCliente.addWidget(self.labelcpfj, 1, 2, 1, 1)
                self.lineEditCPFJ = QtWidgets.QLineEdit(self.groupBoxCliente)
                self.gridLayoutCliente.addWidget(self.lineEditCPFJ, 1, 3, 1, 2)
                
                self.labelNome = QtWidgets.QLabel(self.groupBoxCliente)
                self.gridLayoutCliente.addWidget(self.labelNome, 2, 0, 1, 1)
                self.lineEditNomeCliente = QtWidgets.QLineEdit(self.groupBoxCliente)
                self.gridLayoutCliente.addWidget(self.lineEditNomeCliente, 2, 1, 1, -1)

                self.labelCEP = QtWidgets.QLabel(self.groupBoxCliente)
                self.gridLayoutCliente.addWidget(self.labelCEP, 3, 0, 1, 1)
                self.lineEditCEP = QtWidgets.QLineEdit(self.groupBoxCliente)
                self.gridLayoutCliente.addWidget(self.lineEditCEP, 3, 1, 1, 1)
                self.labelEnder = QtWidgets.QLabel(self.groupBoxCliente)
                self.gridLayoutCliente.addWidget(self.labelEnder, 3, 2, 1, 1)
                self.lineEditEnder = QtWidgets.QLineEdit(self.groupBoxCliente)
                self.gridLayoutCliente.addWidget(self.lineEditEnder, 3, 3, 1, 2)
                self.labelNumero = QtWidgets.QLabel(self.groupBoxCliente)
                self.gridLayoutCliente.addWidget(self.labelNumero, 3, 5 ,1 ,1)
                self.lineEditNumero = QtWidgets.QLineEdit(self.groupBoxCliente)
                self.gridLayoutCliente.addWidget(self.lineEditNumero, 3, 6, 1, 1)
                self.labelBairro = QtWidgets.QLabel(self.groupBoxCliente)
                self.gridLayoutCliente.addWidget(self.labelBairro, 4, 0, 1, 1)
                self.lineEditBairro = QtWidgets.QLineEdit(self.groupBoxCliente)
                self.gridLayoutCliente.addWidget(self.lineEditBairro, 4, 1, 1, 2)
                self.labelCidade = QtWidgets.QLabel(self.groupBoxCliente)
                self.gridLayoutCliente.addWidget(self.labelCidade, 4, 3, 1, 1)
                self.lineEditCidade = QtWidgets.QLineEdit(self.groupBoxCliente)
                self.gridLayoutCliente.addWidget(self.lineEditCidade, 4, 4, 1, 1)
                self.labelUF = QtWidgets.QLabel(self.groupBoxCliente)
                self.gridLayoutCliente.addWidget(self.labelUF, 4, 5, 1, 1)
                self.comboBoxuf = QtWidgets.QComboBox(self.groupBoxCliente)
                self.comboBoxuf.addItems(SIGLAESTADOS)
                self.comboBoxuf.setCurrentIndex(15)
                self.gridLayoutCliente.addWidget(self.comboBoxuf, 4, 6, 1, 1)
                self.labelFone1 = QtWidgets.QLabel(self.groupBoxCliente)
                self.gridLayoutCliente.addWidget(self.labelFone1, 6, 0, 1, 1)            
                self.lineEditFone1 = QtWidgets.QLineEdit(self.groupBoxCliente)
                self.gridLayoutCliente.addWidget(self.lineEditFone1, 6, 1, 1, 2)            
                self.labelFone2 = QtWidgets.QLabel(self.groupBoxCliente)
                self.gridLayoutCliente.addWidget(self.labelFone2, 6, 3, 1, 1)
                self.lineEditFone2 = QtWidgets.QLineEdit(self.groupBoxCliente)
                self.gridLayoutCliente.addWidget(self.lineEditFone2, 6, 4, 1, 3)
                
                self.gridLayoutCliente.setColumnStretch(1,0)
                self.gridLayoutCliente.setColumnStretch(4,4)
                self.gridLayoutCliente.setColumnStretch(6,2)

                '''spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
                self.gridLayoutCliente.addItem(spacerItem, 6, 0, 1, 1)'''

                self.gridLayout.addWidget(self.groupBoxCliente, 0, 0, 2, 1)

                #dados do veiculo
                self.groupBoxVeiculo = QtWidgets.QGroupBox(self.framedados)
                self.gridLayoutVeiculo = QtWidgets.QGridLayout(self.groupBoxVeiculo)
                self.botaobuscarveiculo = QtWidgets.QPushButton(self.groupBoxVeiculo)
                self.botaobuscarveiculo.setFixedSize(180,25)
                self.gridLayoutVeiculo.addWidget(self.botaobuscarveiculo, 0, 0, 1, 2)
                self.checkboxNovoVeiculo = QtWidgets.QCheckBox(self.groupBoxVeiculo)
                self.gridLayoutVeiculo.addWidget(self.checkboxNovoVeiculo, 0, 2, 1, 1)
                self.labelMarca = QtWidgets.QLabel(self.groupBoxVeiculo)
                self.gridLayoutVeiculo.addWidget(self.labelMarca, 1, 0, 1, 1)
                self.comboBoxMarca = QtWidgets.QComboBox(self.groupBoxVeiculo)
                self.comboBoxMarca.setEditable(True)
                self.gridLayoutVeiculo.addWidget(self.comboBoxMarca, 1, 1, 1, 3) 
                self.labelPlaca = QtWidgets.QLabel(self.groupBoxVeiculo)
                self.gridLayoutVeiculo.addWidget(self.labelPlaca, 1, 4, 1, 1)
                self.lineEditPlaca = QtWidgets.QLineEdit(self.groupBoxVeiculo)
                self.gridLayoutVeiculo.addWidget(self.lineEditPlaca, 1, 5, 1, 1)
                self.labelModelo = QtWidgets.QLabel(self.groupBoxVeiculo)
                self.gridLayoutVeiculo.addWidget(self.labelModelo, 2, 0, 1, 1)            
                self.lineEditModelo = QtWidgets.QLineEdit(self.groupBoxVeiculo)
                self.gridLayoutVeiculo.addWidget(self.lineEditModelo, 2, 1, 1, 3)          
                self.labelAno = QtWidgets.QLabel(self.groupBoxVeiculo)
                self.gridLayoutVeiculo.addWidget(self.labelAno, 2, 4, 1, 1)
                self.lineEditAno = QtWidgets.QLineEdit(self.groupBoxVeiculo)
                self.gridLayoutVeiculo.addWidget(self.lineEditAno, 2, 5, 1, 1)
                self.labelKm = QtWidgets.QLabel(self.groupBoxVeiculo)
                self.gridLayoutVeiculo.addWidget(self.labelKm, 3, 0, 1, 1)
                self.lineEditKm = QtWidgets.QLineEdit(self.groupBoxVeiculo)
                self.gridLayoutVeiculo.addWidget(self.lineEditKm, 3, 1, 1, 1)

                self.gridLayoutVeiculo.setColumnStretch(1,0)
                self.gridLayoutVeiculo.setColumnStretch(2,0)
                self.gridLayoutVeiculo.setColumnStretch(3,4)
                self.gridLayoutVeiculo.setColumnStretch(5,3)

                '''spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
                self.gridLayoutVeiculo.addItem(spacerItem1, 3, 0, 1, 1)'''

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
                self.vlayoutgpecas = QtWidgets.QVBoxLayout(self.groupBoxPecas)
                self.vlayoutgpecas.setContentsMargins(1, 1, 1, 1)

                self.scrollarea1 = QtWidgets.QScrollArea(self.groupBoxPecas)
                self.scrollarea1.setWidgetResizable(True)
                self.scrollarea1.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
                self.vlayoutgpecas.addWidget(self.scrollarea1)
                self.framegroupboxpecas = QtWidgets.QFrame(self.scrollarea1)
                self.framegroupboxpecas.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
                self.scrollarea1.setWidget(self.framegroupboxpecas)

                self.gridLayout_2 = QtWidgets.QGridLayout(self.framegroupboxpecas)
                self.labelNomePeca = QtWidgets.QLabel(self.framegroupboxpecas)
                self.gridLayout_2.addWidget(self.labelNomePeca, 0, 0, 1, 1)
                self.lineEditNomePeca = QtWidgets.QLineEdit(self.framegroupboxpecas)
                self.gridLayout_2.addWidget(self.lineEditNomePeca, 0, 1, 1, 1)
                self.labelValorPeca = QtWidgets.QLabel(self.framegroupboxpecas)
                self.gridLayout_2.addWidget(self.labelValorPeca, 0, 3, 1, 1)
                self.lineEditValorPeca = QtWidgets.QLineEdit(self.framegroupboxpecas)
                self.gridLayout_2.addWidget(self.lineEditValorPeca, 0, 4, 1, 1)
                self.botaoAddPecas = QtWidgets.QPushButton(self.framegroupboxpecas)
                self.gridLayout_2.addWidget(self.botaoAddPecas, 0, 5, 1, 1)
                
                self.linhaspeca = [[self.lineEditNomePeca, self.lineEditValorPeca]]

                self.spacerpeca = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
                self.gridLayout_2.addItem(self.spacerpeca, 1, 0, 1, 1)
                self.gridLayout_2.setColumnStretch(1,4)
                self.gridLayout_2.setColumnStretch(4,1)
                self.gridLayout.addWidget(self.groupBoxPecas, 2, 0, 1, 1)

                #serviços

                self.groupBoxServicos = QtWidgets.QGroupBox(self.framedados)
                self.vlayoutgservicos = QtWidgets.QVBoxLayout(self.groupBoxServicos)
                self.vlayoutgservicos.setContentsMargins(1, 1, 1, 1)
                self.scrollarea2 = QtWidgets.QScrollArea(self.groupBoxServicos)
                self.scrollarea2.setWidgetResizable(True)
                self.scrollarea2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
                self.vlayoutgservicos.addWidget(self.scrollarea2)
                self.framegroupboxservicos = QtWidgets.QFrame(self.scrollarea2)
                self.framegroupboxservicos.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
                self.scrollarea2.setWidget(self.framegroupboxservicos)

                self.gridLayout_5 = QtWidgets.QGridLayout(self.framegroupboxservicos)
                self.labelNomeServico = QtWidgets.QLabel(self.framegroupboxservicos)
                self.gridLayout_5.addWidget(self.labelNomeServico, 0, 0, 1, 1)
                self.lineEditNomeServico = QtWidgets.QLineEdit(self.framegroupboxservicos)
                self.gridLayout_5.addWidget(self.lineEditNomeServico, 0, 1, 1, 1)
                self.labelValorServico = QtWidgets.QLabel(self.framegroupboxservicos)
                self.gridLayout_5.addWidget(self.labelValorServico, 0, 3, 1, 1)
                self.lineEditValorServico = QtWidgets.QLineEdit(self.framegroupboxservicos)
                self.gridLayout_5.addWidget(self.lineEditValorServico, 0, 4, 1, 1)
                self.botaoAddServicos = QtWidgets.QPushButton(self.framegroupboxservicos)
                self.gridLayout_5.addWidget(self.botaoAddServicos, 0, 5, 1, 1)

                self.linhasservicos = [[self.lineEditNomeServico, self.lineEditValorServico]]

                self.spacerservico = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
                self.gridLayout_5.addItem(self.spacerservico, 1, 0, 1, 1)
                self.gridLayout_5.setColumnStretch(1,4)
                self.gridLayout_5.setColumnStretch(4,1)
                self.gridLayout.addWidget(self.groupBoxServicos, 2, 1, 1, 1)

                #valor
                self.framevalor = QtWidgets.QFrame(self.framedados)
                self.hlayoutvalor = QtWidgets.QHBoxLayout(self.framevalor)
                self.labelValorTotal1 = QtWidgets.QLabel(self.framevalor)
                self.labelValorTotal1.setText("VALOR TOTAL: R$")
                self.labelValorTotal2 = QtWidgets.QLabel(self.framevalor)
                spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
                self.hlayoutvalor.addItem(spacerItem)
                self.hlayoutvalor.addWidget(self.labelValorTotal1)
                self.hlayoutvalor.addWidget(self.labelValorTotal2)
                self.gridLayout.addWidget(self.framevalor, 3, 0, 1, -1)

                #campo de observações
                self.groupBoxObs = QtWidgets.QGroupBox(self.framedados)
                self.vlayout6_4 = QtWidgets.QVBoxLayout(self.groupBoxObs)
                self.textEdit = QtWidgets.QTextEdit(self.groupBoxObs)
                self.groupBoxObs.setMaximumHeight(120)
                self.vlayout6_4.addWidget(self.textEdit)
                self.gridLayout.addWidget(self.groupBoxObs, 4, 0, -1, -1)

                self.gridLayout.setColumnStretch(0,1)
                self.gridLayout.setColumnStretch(1,1)

                #botoes
                self.framebotoes = QtWidgets.QFrame(self.main_frame)
                self.hlayout4 = QtWidgets.QHBoxLayout(self.framebotoes)
                spacerItem5 = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
                self.hlayout4.addItem(spacerItem5)
                self.botaoSalvareImprimir = QtWidgets.QPushButton(self.framebotoes)
                self.botaoSalvareImprimir.setMinimumSize(QtCore.QSize(150, 35))
                self.botaoSalvareImprimir.setObjectName('botaoprincipal')
                self.hlayout4.addWidget(self.botaoSalvareImprimir)
                self.botaoSalvar = QtWidgets.QPushButton(self.framebotoes)
                self.botaoSalvar.setMinimumSize(QtCore.QSize(100, 30))
                self.hlayout4.addWidget(self.botaoSalvar)
                self.botaolimpar = QtWidgets.QPushButton(self.framebotoes)
                self.botaolimpar.setMinimumSize(QtCore.QSize(100, 30))
                self.hlayout4.addWidget(self.botaolimpar)
                self.hlayout4.setContentsMargins(9,0,9,9)
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
                MainWindow.setWindowTitle(_translate("MainWindow", "Mecânica Pasetto"))
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
                self.botaobuscarcliente.setText(_translate("MainWindow", "Selecionar Cliente"))
                self.checkboxNovoCliente.setText(_translate("MainWindow", "Novo Cliente"))
                self.labelNome.setText(_translate("MainWindow", "Nome*"))
                self.labelCEP.setText(_translate("MainWindow", "CEP"))
                self.labelPessoa.setText(_translate("MainWindow", "Pessoa"))
                self.labelcpfj.setText(_translate("MainWindow", "CPF"))
                self.labelUF.setText(_translate("MainWindow", "UF"))
                self.labelCidade.setText(_translate("MainWindow", "Cidade"))
                self.labelEnder.setText(_translate("MainWindow", "Endereço"))
                self.labelNumero.setText(_translate("MainWindow", "nº"))
                self.labelBairro.setText(_translate("MainWindow", "Bairro"))
                self.labelFone1.setText(_translate("MainWindow", "Fone 1"))
                self.labelFone2.setText(_translate("MainWindow", "Fone 2"))
                self.groupBoxVeiculo.setTitle(_translate("MainWindow", "Dados do veículo"))
                self.botaobuscarveiculo.setText(_translate("MainWindow", "Selecionar Veículo"))
                self.checkboxNovoVeiculo.setText(_translate("MainWindow", "Novo Veículo"))
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
                self.groupBoxObs.setTitle(_translate("MainWindow", "Observações (Max. 200 caracteres)"))
                self.groupBoxPecas.setTitle(_translate("MainWindow", "Peças"))
                self.botaoAddPecas.setText(_translate("MainWindow", "+"))
                self.labelNomePeca.setText(_translate("MainWindow", "Peça"))
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