import sys
from PyQt6 import QtWidgets, QtGui, QtCore

from routes import handleRoutes
from ui.telaConsultaCliente import TelaConsultaCliente
from ui.telaConsultaVeiculo import TelaConsultaVeiculo

from util.buscaCEP import BuscaCEP

from ui.telaInicial import TelaInicial
from ui.telaCadastroPeca import TelaCadastroPeca
from ui.telaCadastroServico import TelaCadastroServico
from ui.telaCadastroCliente import TelaCadastroCliente
from ui.telaCadastroOrcamento import TelaCadastroOrcamento
from ui.telaConsultaPeca import TelaConsultaPeca
from ui.telaConsultaServico import TelaConsultaServico
from ui.telaConsultaOrcamento import TelaConsultaOrcamento

from ui.telaEditarCliente import TelaEditarCliente
from ui.telaEditarOrcamento import TelaEditarOrcamento

from controller.marcaController import MarcaController
from controller.pecaController import PecaController
from controller.servicoController import ServicoController
from controller.clienteController import ClienteController
from controller.cidadeController import CidadeController
from controller.orcamentoController import OrcamentoController

class MainController():

    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.app.setStyle('Fusion')
        self.app.setEffectEnabled(QtCore.Qt.UIEffect.UI_AnimateCombo, False)
        self.splash = QtWidgets.QSplashScreen(QtGui.QPixmap('./resources/logo.png').scaled(300,150))
        self.splash.show()
        style = open('./resources/styles.qss').read()
        self.app.setStyleSheet(style)
        fontID = QtGui.QFontDatabase.addApplicationFont("./resources/Helvetica.ttf")
        if fontID < 0:
            raise Exception('Fonte não carregada')
        font = QtGui.QFont('Helvetica')
        self.app.setFont(font)
        self.app.setWindowIcon(QtGui.QIcon('./resources/logo-icon.png'))
        self.setRoutes()
        self.telaInicio = TelaInicial()
        self.telaInicio.setStyle(QtWidgets.QApplication.setStyle('Fusion'))
        self.telaInicio.setStyleSheet(style)
        self.telaInicio.setFont(font)
        self.telaCadastroPeca = TelaCadastroPeca()
        self.telaCadastroServico = TelaCadastroServico()
        self.telaCadastroCliente = TelaCadastroCliente()
        self.telaCadastroOrcamento = TelaCadastroOrcamento()
        self.telaConsultaPeca = TelaConsultaPeca()
        self.telaConsultaServico = TelaConsultaServico()
        self.telaConsultaCliente = TelaConsultaCliente()
        self.telaConsultaVeiculo = TelaConsultaVeiculo()
        self.telaConsultaOrcamento = TelaConsultaOrcamento()

        self.telaEditarCliente = TelaEditarCliente()
        self.telaEditarOrcamento = TelaEditarOrcamento()

        self.telaInicio.stackedWidget.addWidget(self.telaCadastroPeca)
        self.telaInicio.stackedWidget.addWidget(self.telaCadastroServico)
        self.telaInicio.stackedWidget.addWidget(self.telaCadastroCliente)
        self.telaInicio.stackedWidget.addWidget(self.telaCadastroOrcamento)
        self.telaInicio.stackedWidget.addWidget(self.telaConsultaPeca)
        self.telaInicio.stackedWidget.addWidget(self.telaConsultaServico)
        self.telaInicio.stackedWidget.addWidget(self.telaConsultaCliente)
        self.telaInicio.stackedWidget.addWidget(self.telaConsultaVeiculo)

        self.telaInicio.stackedWidget.addWidget(self.telaEditarCliente)

        self.telaInicio.stackedWidget.addWidget(self.telaConsultaOrcamento)
        self.telaInicio.stackedWidget.addWidget(self.telaEditarOrcamento)
        self.initConnections()

    #função que instancia uma unica vez cada controller, que podem ser acessados onde necessário
    def setRoutes(self):
        pecaController = PecaController()
        handleRoutes.setRoute('PECACTRL', pecaController)
        servicoController = ServicoController()
        handleRoutes.setRoute('SERVICOCTRL', servicoController)
        clienteController = ClienteController()
        handleRoutes.setRoute('CLIENTECTRL', clienteController)
        orcamentoController = OrcamentoController()
        handleRoutes.setRoute('ORCAMENTOCTRL', orcamentoController)
        marcaController = MarcaController()
        handleRoutes.setRoute('MARCACTRL', marcaController)
        cidadeController = CidadeController()
        handleRoutes.setRoute('CIDADECTRL', cidadeController)
        buscaCEP = BuscaCEP()
        handleRoutes.setRoute('CEP', buscaCEP)

    def initConnections(self):
        # conectando botões do menu
        self.telaInicio.botao_pecas.clicked.connect(lambda: self.telaInicio.stackedWidget.setCurrentWidget(self.telaCadastroPeca))
        self.telaInicio.botao_servicos.clicked.connect(lambda: self.telaInicio.stackedWidget.setCurrentWidget(self.telaCadastroServico))
        self.telaInicio.botao_clientes.clicked.connect(lambda: self.telaInicio.stackedWidget.setCurrentWidget(self.telaCadastroCliente))
        self.telaInicio.botao_orcamentos.clicked.connect(lambda: self.telaInicio.stackedWidget.setCurrentWidget(self.telaCadastroOrcamento))

        self.telaInicio.botao_pecas_2.clicked.connect(lambda: self.telaInicio.stackedWidget.setCurrentWidget(self.telaConsultaPeca))
        self.telaInicio.botao_servicos_2.clicked.connect(lambda: self.telaInicio.stackedWidget.setCurrentWidget(self.telaConsultaServico))
        self.telaInicio.botao_clientes_2.clicked.connect(lambda: self.telaInicio.stackedWidget.setCurrentWidget(self.telaConsultaCliente))
        self.telaInicio.botao_veiculos.clicked.connect(lambda: self.telaInicio.stackedWidget.setCurrentWidget(self.telaConsultaVeiculo))
        self.telaInicio.botao_orcamentos_2.clicked.connect(lambda: self.telaInicio.stackedWidget.setCurrentWidget(self.telaConsultaOrcamento))
        '''self.telaCadastroCliente.lineEditCEP.editingFinished.connect(lambda: self.buscarDadosCEP(self.telaCadastroCliente))
        self.telaCadastroOrcamento.lineEditCEP.editingFinished.connect(lambda: self.buscarDadosCEP(self.telaCadastroOrcamento))'''

        # self.telaConsultaCliente.botaoEditar.clicked.connect(lambda: self.telaEditarCliente.renderEditar(self.telaConsultaCliente.editarCliente()))

        self.telaConsultaCliente.botaoEditar.clicked.connect(
            lambda: self.trocaPagina(self.telaEditarCliente, self.telaEditarCliente.renderEditar, self.telaConsultaCliente.editarCliente))
        self.telaConsultaOrcamento.botaoEditar.clicked.connect(
            lambda: self.trocaPagina(self.telaEditarOrcamento, self.telaEditarOrcamento.renderEditar, self.telaConsultaOrcamento.editarOrcamento))

    def trocaPagina(self, pagina, render, param):
        render(param())
        self.telaInicio.stackedWidget.setCurrentWidget(pagina)

    def run(self):
        self.telaInicio.resize(1280,800)
        self.telaInicio.show()
        self.splash.finish(self.telaInicio)
        sys.exit(self.app.exec())


if __name__ == "__main__":

    c = MainController()
    c.run()
