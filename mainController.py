import sys
from types import NoneType
from PyQt6 import QtWidgets, QtCore
from controller.orcamentoController import OrcamentoController
from controller.clienteController import ClienteController


class MainController():

    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        style = open('./ui/styles.qss').read()
        self.app.setStyleSheet(style)
        self.cCli = ClienteController()
        self.cOrc = OrcamentoController()

        self.cOrc.view.botao_clientes.clicked.connect(self.telaCadastroCliente)
        self.cOrc.view.botao_orcamentos.clicked.connect(self.telaCadastroOrcamento)
        self.cCli.view.botao_clientes.clicked.connect(self.telaCadastroCliente)
        self.cCli.view.botao_orcamentos.clicked.connect(self.telaCadastroOrcamento)

    def telaInicial(self):
        pass

    def telaCadastroPeca(self):
        pass

    def telaCadastroServico(self):
        pass

    def telaCadastroCliente(self):

        window = self.app.activeWindow()
        self.cCli.MainWindow.resize(window.size())

        if window != None:
            self.cCli.MainWindow.resize(window.size())
            if(window.windowState()==QtCore.Qt.WindowState.WindowMaximized):
                self.cCli.MainWindow.setWindowState(QtCore.Qt.WindowState.WindowMaximized)
            self.cCli.MainWindow.move(window.pos())

        self.cCli.run()
        self.cOrc.exit()

    def telaCadastroOrcamento(self):

        window = self.app.activeWindow()
        if window != None:
            self.cOrc.MainWindow.resize(window.size())
            if(window.windowState()==QtCore.Qt.WindowState.WindowMaximized):
                self.cOrc.MainWindow.setWindowState(QtCore.Qt.WindowState.WindowMaximized)
            self.cOrc.MainWindow.move(window.pos())
        self.cOrc.run()
        self.cCli.exit()

    def run(self):
        self.telaCadastroOrcamento()
        sys.exit(self.app.exec())


if __name__ == "__main__":
    c = MainController()
    c.run()

