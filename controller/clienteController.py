import sys
from PyQt6 import QtWidgets, QtGui, QtCore
from model.modelo import *
from ui.telaCadastroCliente import TelaCadastroCliente
from ui.telaConsultaAux import TelaConsultaAux
from util.buscaCEP import BuscaCEP

class ClienteController():
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        super(ClienteController, self).__init__()
        self.view = TelaCadastroCliente(self.MainWindow)

    def run(self):
        self.MainWindow.show()

    def exit(self):
        self.MainWindow.hide()