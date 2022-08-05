from PyQt6 import QtWidgets

from model import *

from ui.telaCadastroServico import TelaCadastroServico

class ServicoController():
    def __init__(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.view = TelaCadastroServico(self.MainWindow)
        self.linhasservico = [[self.view.lineEditnome, self.view.lineEditvalor]]
        self.initConnections()

    def initConnections(self):
        self.view.botaoadd.clicked.connect(self.addlinhaservico)

    def run(self):
        self.MainWindow.show()

    def addlinhaservico(self):
        label1 = QtWidgets.QLabel(text="Nome do Serviço")
        lineedit1 = QtWidgets.QLineEdit()
        label2 = QtWidgets.QLabel(text="Valor")
        lineedit2 = QtWidgets.QLineEdit()
        self.view.gridLayout.addWidget(label1, len(self.linhasservico), 0, 1, 1)
        self.view.gridLayout.addWidget(lineedit1, len(self.linhasservico), 1, 1, 1)
        self.view.gridLayout.addWidget(label2, len(self.linhasservico), 3, 1, 1)
        self.view.gridLayout.addWidget(lineedit2, len(self.linhasservico), 4, 1, 1)
        self.linhasservico.append([lineedit1, lineedit2])
        self.view.gridLayout.addWidget(self.view.botaoadd, len(self.linhasservico)-1, 5, 1, 1)
        self.view.gridLayout.removeItem(self.view.spacer)
        self.view.gridLayout.addItem(self.view.spacer, len(self.linhasservico), 0, 1, 1)