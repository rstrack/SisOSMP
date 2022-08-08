from PyQt6 import QtCore, QtGui, QtWidgets

class TelaCadastroServico(QtWidgets.QMainWindow):

        def __init__(self):
                super(TelaCadastroServico, self).__init__()
                self.setupUi()

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
                self.gridLayout = QtWidgets.QGridLayout(self.framedados)
                self.gridLayout.setVerticalSpacing(9)
                self.gridLayout.setHorizontalSpacing(9)
                self.vlayout6.addWidget(self.framedados)
                self.scrollarea = QtWidgets.QScrollArea(self.main_frame)
                self.scrollarea.setWidgetResizable(True)
                self.scrollarea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
                self.vlayout6.addWidget(self.scrollarea)
                self.framedados = QtWidgets.QFrame(self.scrollarea)
                self.scrollarea.setWidget(self.framedados)
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
                self.botaoadd = QtWidgets.QPushButton(self.framedados, clicked=lambda:self.addlinhaservico())
                self.botaoadd.setFixedSize(QtCore.QSize(26,26))
                self.linhasservico = [[self.lineEditnome, self.lineEditvalor]]
                self.gridLayout.addWidget(self.botaoadd, 0, 5, 1, 1)
                spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
                self.gridLayout.addItem(spacerItem2, 0, 2, 1, 1)
                self.spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
                self.gridLayout.addItem(self.spacer, 1, 0, 1, 1)
                self.frameBotoes1 = QtWidgets.QFrame(self.main_frame)
                self.hlayout2 = QtWidgets.QHBoxLayout(self.frameBotoes1)
                spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
                self.hlayout2.addItem(spacerItem3)
                self.botaoSalvar = QtWidgets.QPushButton(self.frameBotoes1)
                self.botaoSalvar.setMinimumSize(QtCore.QSize(100, 30))
                self.hlayout2.addWidget(self.botaoSalvar)
                self.botaoLimpar = QtWidgets.QPushButton(self.frameBotoes1)
                self.botaoLimpar.setMinimumSize(QtCore.QSize(100, 30))
                self.hlayout2.addWidget(self.botaoLimpar)
                self.vlayout6.addWidget(self.frameBotoes1)
                self.setCentralWidget(self.main_frame)             
                self.retranslateUi()

        def retranslateUi(self):
                _translate = QtCore.QCoreApplication.translate
                self.setWindowTitle(_translate("MainWindow", "MainWindow"))

                self.labelTitulo.setText(_translate("MainWindow", "Cadastro de serviços"))
                self.labelnome.setText(_translate("MainWindow", "Descrição do serviço"))
                self.labelvalor.setText(_translate("MainWindow", "Valor"))
                self.botaoadd.setText(_translate("MainWindow", "+"))
                self.botaoLimpar.setText(_translate("MainWindow", "Limpar"))
                self.botaoSalvar.setText(_translate("MainWindow", "Salvar"))


        def addlinhaservico(self):
                label1 = QtWidgets.QLabel(text="Descrição do Serviço")
                lineedit1 = QtWidgets.QLineEdit()
                label2 = QtWidgets.QLabel(text="Valor")
                lineedit2 = QtWidgets.QLineEdit()
                self.gridLayout.addWidget(label1, len(self.linhasservico), 0, 1, 1)
                self.gridLayout.addWidget(lineedit1, len(self.linhasservico), 1, 1, 1)
                self.gridLayout.addWidget(label2, len(self.linhasservico), 3, 1, 1)
                self.gridLayout.addWidget(lineedit2, len(self.linhasservico), 4, 1, 1)
                self.linhasservico.append([lineedit1, lineedit2])
                self.gridLayout.addWidget(self.botaoadd, len(self.linhasservico)-1, 5, 1, 1)
                self.gridLayout.addWidget(self.botaoadd, len(self.linhasservico)-1, 5, 1, 1)
                self.gridLayout.removeItem(self.spacer)
                self.gridLayout.addItem(self.spacer, len(self.linhasservico), 0, 1, 1)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TelaCadastroServico()
    ui.setupUi()
    style = open('./ui/styles.qss').read()
    app.setStyleSheet(style)
    ui.show()
    sys.exit(app.exec())