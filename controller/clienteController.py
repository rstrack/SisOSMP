import sys
from PyQt6 import QtWidgets, QtGui, QtCore
from model.modelo import *
from ui.telaCadastroCliente import TelaCadastroCliente
from util.buscaCEP import BuscaCEP

class ClienteController():
    def __init__(self):
        super(ClienteController, self).__init__()
        self.MainWindow = QtWidgets.QMainWindow()
        self.view = TelaCadastroCliente(self.MainWindow)

    def run(self):
        self.MainWindow.show()