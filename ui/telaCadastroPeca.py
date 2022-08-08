from PyQt6 import QtCore, QtGui, QtWidgets

class TelaCadastroPeca(QtWidgets.QMainWindow):

        def __init__(self):
                super(TelaCadastroPeca, self).__init__()
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

                self.botaoadd = QtWidgets.QPushButton(self.framedados)

                self.botaoadd.setFixedSize(QtCore.QSize(26,26))

                self.gridLayout.addWidget(self.botaoadd, 0, 5, 1, 1)
                spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
                self.gridLayout.addItem(spacerItem2, 0, 2, 1, 1)
                self.spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
                self.gridLayout.addItem(self.spacer, 1, 0, 1, 1)

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

                self.setCentralWidget(self.main_frame)

                self.retranslateUi()


        def retranslateUi(self):
                _translate = QtCore.QCoreApplication.translate
                self.setWindowTitle(_translate("MainWindow", "MainWindow"))

                self.labelTitulo.setText(_translate("MainWindow", "Cadastro de peças"))
                self.labelvalor.setText(_translate("MainWindow", "Valor"))
                self.labelnome.setText(_translate("MainWindow", "Nome da peça"))
                self.botaoadd.setText(_translate("MainWindow", "+"))
                self.botaolimpar.setText(_translate("MainWindow", "Limpar"))
                self.botaosalvar.setText(_translate("MainWindow", "Salvar"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = TelaCadastroPeca()
    ui.show()
    style = open('./ui/styles.qss').read()
    app.setStyleSheet(style)
    sys.exit(app.exec())
