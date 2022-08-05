import sys
from PyQt6 import QtWidgets, QtCore
from controller.pecaController import PecaController
from controller.orcamentoController import OrcamentoController
from controller.clienteController import ClienteController
from controller.servicoController import ServicoController

from ui.telaInicial import TelaInicial

class MainController():

    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        style = open('./ui/styles.qss').read()
        self.app.setStyleSheet(style)
        self.MainWindow = QtWidgets.QMainWindow()
        self.telaInicio = TelaInicial(self.MainWindow)
        self.telaInicio.setupUi(self.MainWindow)
        self.cPec = PecaController()
        self.cSer = ServicoController()
        self.cCli = ClienteController()
        self.cOrc = OrcamentoController()
        self.initConnections()

    def initConnections(self):
        self.telaInicio.botao_pecas.clicked.connect(self.telaCadastroPeca)
        self.telaInicio.botao_servicos.clicked.connect(self.telaCadastroServico)
        self.telaInicio.botao_clientes.clicked.connect(self.telaCadastroCliente)
        self.telaInicio.botao_orcamentos.clicked.connect(self.telaCadastroOrcamento)

        self.cPec.view.botao_servicos.clicked.connect(self.telaCadastroServico)
        self.cPec.view.botao_clientes.clicked.connect(self.telaCadastroCliente)
        self.cPec.view.botao_orcamentos.clicked.connect(self.telaCadastroOrcamento)

        self.cSer.view.botao_pecas.clicked.connect(self.telaCadastroPeca)
        self.cSer.view.botao_clientes.clicked.connect(self.telaCadastroCliente)
        self.cSer.view.botao_orcamentos.clicked.connect(self.telaCadastroOrcamento)

        self.cCli.view.botao_pecas.clicked.connect(self.telaCadastroPeca)
        self.cCli.view.botao_servicos.clicked.connect(self.telaCadastroServico)
        self.cCli.view.botao_orcamentos.clicked.connect(self.telaCadastroOrcamento)

        self.cOrc.view.botao_pecas.clicked.connect(self.telaCadastroPeca)
        self.cOrc.view.botao_servicos.clicked.connect(self.telaCadastroServico)
        self.cOrc.view.botao_clientes.clicked.connect(self.telaCadastroCliente)


    def telaInicial(self):
        self.MainWindow.show()


    def telaCadastroPeca(self):
        window = self.app.activeWindow()
        self.cPec.MainWindow.resize(window.size())
        if window != None:
            self.cPec.MainWindow.resize(window.size())
            if(window.windowState()==QtCore.Qt.WindowState.WindowMaximized):
                self.cPec.MainWindow.setWindowState(QtCore.Qt.WindowState.WindowMaximized)
            self.cPec.MainWindow.move(window.pos())
        self.cPec.run()
        window.close()


    def telaCadastroServico(self):
        window = self.app.activeWindow()
        self.cSer.MainWindow.resize(window.size())
        if window != None:
            self.cSer.MainWindow.resize(window.size())
            if(window.windowState()==QtCore.Qt.WindowState.WindowMaximized):
                self.cSer.MainWindow.setWindowState(QtCore.Qt.WindowState.WindowMaximized)
            self.cSer.MainWindow.move(window.pos())
        self.cSer.run()
        window.close()


    def telaCadastroCliente(self):
        window = self.app.activeWindow()
        self.cCli.MainWindow.resize(window.size())
        self.cCli.MainWindow.resize(window.size())
        if(window.windowState()==QtCore.Qt.WindowState.WindowMaximized):
            self.cCli.MainWindow.setWindowState(QtCore.Qt.WindowState.WindowMaximized)
        self.cCli.MainWindow.move(window.pos())
        self.cCli.run()
        window.close()


    def telaCadastroOrcamento(self):
        window = self.app.activeWindow()     
        self.cOrc.MainWindow.resize(window.size())
        if(window.windowState()==QtCore.Qt.WindowState.WindowMaximized):
            self.cOrc.MainWindow.setWindowState(QtCore.Qt.WindowState.WindowMaximized)
        self.cOrc.MainWindow.move(window.pos())
        self.cOrc.run()
        window.close() 


    def run(self):
        self.telaInicial()
        sys.exit(self.app.exec())


if __name__ == "__main__":
    c = MainController()
    c.run()
