from ctypes import alignment
from PyQt6 import QtCore, QtWidgets

from controller.pecaController import PecaController
from ui.telaCadastroOrcamento import UNIDADES

class TelaCadastroPeca(QtWidgets.QMainWindow):

        def __init__(self):
                super(TelaCadastroPeca, self).__init__()
                self.controller = PecaController(view=self)
                self.setupUi()

        def setupUi(self):
                self.resize(1280, 760)
                self.linhasPeca = []
                self.main_frame = QtWidgets.QFrame(self)
                self.main_frame.setObjectName("main_frame")
                self.vlayout6 = QtWidgets.QVBoxLayout(self.main_frame)               
                self.frame_titulo = QtWidgets.QFrame(self.main_frame)
                self.vlayout6.addWidget(self.frame_titulo)
                self.labelTitulo = QtWidgets.QLabel(self.frame_titulo)
                self.labelTitulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.labelTitulo.setObjectName("titulo")
                self.vlayout6.setContentsMargins(36, 18, 36, 18)
                self.vlayout6.setSpacing(36)
                self.vlayout6.addWidget(self.labelTitulo)          
                self.scrollarea = QtWidgets.QScrollArea(self.main_frame)
                self.scrollarea.setWidgetResizable(True)
                self.scrollarea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
                self.vlayout6.addWidget(self.scrollarea)
                self.framedados = QtWidgets.QFrame(self.scrollarea)
                self.scrollarea.setWidget(self.framedados)
                self.gridLayout = QtWidgets.QGridLayout(self.framedados)  
                 
                self.labelnome = QtWidgets.QLabel(self.framedados)
                self.gridLayout.addWidget(self.labelnome, 0, 0, 1, 1)
                self.labelUn = QtWidgets.QLabel(self.framedados)
                self.gridLayout.addWidget(self.labelUn, 0, 1, 1, 1)
                self.labelvalor = QtWidgets.QLabel(self.framedados)
                self.gridLayout.addWidget(self.labelvalor, 0, 2, 1, 1)

                self.lineEditNomePeca = QtWidgets.QLineEdit(self.framedados)
                self.gridLayout.addWidget(self.lineEditNomePeca, 1, 0, 1, 1)
                self.comboboxun = QtWidgets.QComboBox(self.framedados)
                self.comboboxun.addItems(UNIDADES)
                self.comboboxun.setCurrentIndex(15)
                self.gridLayout.addWidget(self.comboboxun, 1, 1, 1, 1)
                self.lineEditValorPeca = QtWidgets.QLineEdit(self.framedados)
                self.gridLayout.addWidget(self.lineEditValorPeca, 1, 2, 1, 1)

                self.gridLayout.setColumnStretch(0,8)
                self.gridLayout.setColumnStretch(2,1)
                self.linhasPeca.append([self.lineEditNomePeca, self.comboboxun, self.lineEditValorPeca])
                self.botaoadd = QtWidgets.QPushButton(self.framedados)
                self.botaoadd.setFixedSize(QtCore.QSize(26,26))
                self.gridLayout.addWidget(self.botaoadd, 1, 3, 1, 1)
                self.spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
                self.gridLayout.addItem(self.spacer, 2, 0, 1, 1)
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
                #conexoes
                self.botaoadd.clicked.connect(self.addLinhaPeca)
                self.botaolimpar.clicked.connect(self.limparCampos)
                self.botaosalvar.clicked.connect(self.salvarPecas)

             
        def retranslateUi(self):
                _translate = QtCore.QCoreApplication.translate
                self.setWindowTitle(_translate("MainWindow", "MainWindow"))

                self.labelTitulo.setText(_translate("MainWindow", "Cadastro de peças"))
                self.labelnome.setText(_translate("MainWindow", "Nome da peça"))
                self.labelUn.setText(_translate("MainWindow", "Un"))
                self.labelvalor.setText(_translate("MainWindow", "Valor"))
                self.botaoadd.setText(_translate("MainWindow", "+"))
                self.botaolimpar.setText(_translate("MainWindow", "Limpar"))
                self.botaosalvar.setText(_translate("MainWindow", "Salvar"))


        def addLinhaPeca(self):
                label1 = QtWidgets.QLabel(text="Nome da peça")
                lineedit1 = QtWidgets.QLineEdit()
                labelcb = QtWidgets.QLabel(text="Un")
                comboBox = QtWidgets.QComboBox()
                comboBox.addItems(UNIDADES)
                comboBox.setCurrentIndex(15)
                label2 = QtWidgets.QLabel(text="Valor")
                lineedit2 = QtWidgets.QLineEdit()
                self.gridLayout.addWidget(label1, len(self.linhasPeca)*2, 0, 1, 1)
                self.gridLayout.addWidget(labelcb, len(self.linhasPeca)*2, 1, 1, 1)
                self.gridLayout.addWidget(label2, len(self.linhasPeca)*2, 2, 1, 1)
                self.gridLayout.addWidget(lineedit1, len(self.linhasPeca)*2+1, 0, 1, 1)
                self.gridLayout.addWidget(comboBox, len(self.linhasPeca)*2+1, 1, 1, 1)
                self.gridLayout.addWidget(lineedit2, len(self.linhasPeca)*2+1, 2, 1, 1)
                self.linhasPeca.append([lineedit1, comboBox, lineedit2])
                self.gridLayout.addWidget(self.botaoadd, len(self.linhasPeca)*2-1, 3, 1, 1)
                self.gridLayout.removeItem(self.spacer)
                self.gridLayout.addItem(self.spacer, len(self.linhasPeca)*2+1, 0, 1, 1)

        def resetarTela(self):
                for widget in self.framedados.findChildren((QtWidgets.QLabel, QtWidgets.QLineEdit, QtWidgets.QComboBox,QtWidgets.QPushButton)):
                        self.gridLayout.removeWidget(widget)
                        widget.deleteLater()
                self.linhasPeca.clear()
                self.labelnome = QtWidgets.QLabel(self.framedados, text="Nome da peça:")
                self.gridLayout.addWidget(self.labelnome, 0, 0, 1, 1)
                self.lineEditNomePeca = QtWidgets.QLineEdit(self.framedados)
                self.gridLayout.addWidget(self.lineEditNomePeca, 0, 1, 1, 1)
                self.labelUn = QtWidgets.QLabel(self.framedados, text="Un:")
                self.gridLayout.addWidget(self.labelUn, 0, 2, 1, 1)
                self.comboboxun = QtWidgets.QComboBox(self.framedados)
                self.comboboxun.addItems(UNIDADES)
                self.comboboxun.setCurrentIndex(15)
                self.gridLayout.addWidget(self.comboboxun, 0, 3, 1, 1)
                self.labelvalor = QtWidgets.QLabel(self.framedados, text="Valor:")
                self.gridLayout.addWidget(self.labelvalor, 0, 4, 1, 1)
                self.lineEditValorPeca = QtWidgets.QLineEdit(self.framedados)
                self.gridLayout.addWidget(self.lineEditValorPeca, 0, 5, 1, 1)
                self.linhasPeca.append([self.lineEditNomePeca, self.comboboxun, self.lineEditValorPeca])
                self.botaoadd = QtWidgets.QPushButton(self.framedados, text="+")
                self.botaoadd.setFixedSize(QtCore.QSize(26,26))
                self.gridLayout.addWidget(self.botaoadd, 0, 6, 1, 1)
                self.gridLayout.addItem(self.spacer, 1, 0, 1, 1)
                self.botaoadd.clicked.connect(self.addLinhaPeca)


        def salvarPecas(self):
                if(self.controller.salvarPecas()):
                        self.resetarTela()

        def limparCampos(self):
                for lineedit in self.framedados.findChildren(QtWidgets.QLineEdit):
                        lineedit.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = TelaCadastroPeca()
    ui.show()
    style = open('./ui/styles.qss').read()
    app.setStyleSheet(style)
    sys.exit(app.exec())
