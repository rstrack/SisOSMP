from PyQt6 import QtCore, QtGui, QtWidgets

class TelaCadastroPeca(QtWidgets.QWidget):

        def __init__(self, MainWindow):
                super(TelaCadastroPeca, self).__init__()
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

                self.frame_titulo = QtWidgets.QFrame(self.main_frame)
                self.vlayout6.addWidget(self.frame_titulo)
                self.label = QtWidgets.QLabel(self.frame_titulo)
                self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.vlayout6.addWidget(self.label)
                self.vlayout6.setContentsMargins(18, 18, 18, 18)
                self.vlayout6.setSpacing(50)

                self.framedados = QtWidgets.QFrame(self.main_frame)
                self.gridLayout = QtWidgets.QGridLayout(self.framedados)   
                self.labelnome = QtWidgets.QLabel(self.framedados)
                self.gridLayout.addWidget(self.labelnome, 0, 0, 1, 1)
                self.lineEditnome = QtWidgets.QLineEdit(self.framedados)
                self.gridLayout.addWidget(self.lineEditnome, 0, 1, 1, 1)
                self.labelvalor = QtWidgets.QLabel(self.framedados)
                self.gridLayout.addWidget(self.labelvalor, 0, 3, 1, 1)
                self.lineEditvalor = QtWidgets.QLineEdit(self.framedados)
                self.gridLayout.addWidget(self.lineEditvalor, 0, 4, 1, 1)
                self.gridLayout.setColumnStretch(1,5)
                self.gridLayout.setColumnStretch(4,1)

                self.botaoadd = QtWidgets.QPushButton(self.framedados, clicked=lambda:self.addlinhapeca())

                self.botaoadd.setFixedSize(QtCore.QSize(26,26))

                self.linhaspeca = [[self.lineEditnome, self.lineEditvalor]]

                self.gridLayout.addWidget(self.botaoadd, 0, 5, 1, 1)
                spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
                self.gridLayout.addItem(spacerItem2, 0, 2, 1, 1)
                self.vlayout6.addWidget(self.framedados)
                self.frame_4 = QtWidgets.QFrame(self.main_frame)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
                self.frame_4.setSizePolicy(sizePolicy)
                self.vlayout6.addWidget(self.frame_4)
                
                self.frameBotoes1 = QtWidgets.QFrame(self.main_frame)
                self.hlayout2 = QtWidgets.QHBoxLayout(self.frameBotoes1)
                spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
                self.hlayout2.addItem(spacerItem3)
                self.botaosalvar = QtWidgets.QPushButton(self.frameBotoes1)
                self.botaosalvar.setMinimumSize(QtCore.QSize(100, 30))
                self.hlayout2.addWidget(self.botaosalvar)
                self.botaolimpar = QtWidgets.QPushButton(self.frameBotoes1)
                self.botaolimpar.setMinimumSize(QtCore.QSize(100, 30))
                self.hlayout2.addWidget(self.botaolimpar)
                self.vlayout6.addWidget(self.frameBotoes1)

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

                self.label.setText(_translate("MainWindow", "Cadastro de peças"))
                self.labelvalor.setText(_translate("MainWindow", "Valor"))
                self.labelnome.setText(_translate("MainWindow", "Nome da peça"))
                self.botaoadd.setText(_translate("MainWindow", "+"))
                self.botaolimpar.setText(_translate("MainWindow", "Limpar"))
                self.botaosalvar.setText(_translate("MainWindow", "Salvar"))


        def addlinhapeca(self):
                label1 = QtWidgets.QLabel(text="Nome da peça")
                lineedit1 = QtWidgets.QLineEdit()
                label2 = QtWidgets.QLabel(text="Valor")
                lineedit2 = QtWidgets.QLineEdit()
                self.gridLayout.addWidget(label1, len(self.linhaspeca), 0, 1, 1)
                self.gridLayout.addWidget(lineedit1, len(self.linhaspeca), 1, 1, 1)
                self.gridLayout.addWidget(label2, len(self.linhaspeca), 3, 1, 1)
                self.gridLayout.addWidget(lineedit2, len(self.linhaspeca), 4, 1, 1)
                self.linhaspeca.append([lineedit1, lineedit2])
                self.gridLayout.addWidget(self.botaoadd, len(self.linhaspeca)-1, 5, 1, 1)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TelaCadastroPeca(MainWindow)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
