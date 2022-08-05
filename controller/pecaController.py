from PyQt6 import QtWidgets

from model.modelo import *

from ui.telaCadastroPeca import TelaCadastroPeca

class PecaController():
    def __init__(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.view = TelaCadastroPeca(self.MainWindow)
        self.linhaspeca = [[self.view.lineEditnome, self.view.lineEditvalor]]
        self.initConnections()

    def initConnections(self):
        self.view.botaoadd.clicked.connect(self.addlinhapeca)
        self.view.botaolimpar.clicked.connect(self.limparCampos)

    def run(self):
        self.MainWindow.show()

    def addlinhapeca(self):
        label1 = QtWidgets.QLabel(text="Nome da peça")
        lineedit1 = QtWidgets.QLineEdit()
        label2 = QtWidgets.QLabel(text="Valor")
        lineedit2 = QtWidgets.QLineEdit()
        self.view.gridLayout.addWidget(label1, len(self.linhaspeca), 0, 1, 1)
        self.view.gridLayout.addWidget(lineedit1, len(self.linhaspeca), 1, 1, 1)
        self.view.gridLayout.addWidget(label2, len(self.linhaspeca), 3, 1, 1)
        self.view.gridLayout.addWidget(lineedit2, len(self.linhaspeca), 4, 1, 1)
        self.linhaspeca.append([lineedit1, lineedit2])
        self.view.gridLayout.addWidget(self.view.botaoadd, len(self.linhaspeca)-1, 5, 1, 1)
        self.view.gridLayout.removeItem(self.view.spacer)
        self.view.gridLayout.addItem(self.view.spacer, len(self.linhaspeca), 0, 1, 1)

    def limparCampos(self):
        for lineedit in self.view.framedados.findChildren(QtWidgets.QLineEdit):
            lineedit.clear()

    def salvarPecas(self):
        with db.atomic() as transaction:
            try:
                pass
            except Exception as e:
                transaction.rollback()
                msg =  QtWidgets.QMessageBox()
                msg.setWindowTitle("Erro")
                msg.setText(str(e))
                msg.exec()
