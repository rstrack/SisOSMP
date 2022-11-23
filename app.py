import sys
from PyQt6 import QtWidgets, QtGui, QtCore

from util.container import handleDeps
from ui.telaConsultaCliente import TelaConsultaCliente
from ui.telaConsultaOS import TelaConsultaOS
from ui.telaConsultaVeiculo import TelaConsultaVeiculo
from ui.telaEditarOS import TelaEditarOS
from ui.telaEditarPeca import TelaEditarPeca
from ui.telaEditarServico import TelaEditarServico
from ui.telaEditarVeiculo import TelaEditarVeiculo

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

#Classe que instancia views e controllers e faz conexão entre objetos
class APP():

    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.app.setStyle('Fusion')
        self.app.setEffectEnabled(QtCore.Qt.UIEffect.UI_AnimateCombo, False)
        self.splash = QtWidgets.QSplashScreen(QtGui.QPixmap('resources/logo-icon.png').scaled(400,300))
        self.splash.show()
        style = open('resources/styles.qss').read()
        self.app.setStyleSheet(style)
        fontID = QtGui.QFontDatabase.addApplicationFont("resources/Helvetica.ttf")
        if fontID < 0:
            raise Exception('Fonte não carregada')
        font = QtGui.QFont('Helvetica')
        self.app.setFont(font)
        self.app.setWindowIcon(QtGui.QIcon('resources/logo-icon.png'))
        self.setDeps()
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
        self.telaConsultaOS = TelaConsultaOS()

        self.telaEditarPeca = TelaEditarPeca()
        self.telaEditarServico = TelaEditarServico()
        self.telaEditarCliente = TelaEditarCliente()
        self.telaEditarVeiculo = TelaEditarVeiculo()
        self.telaEditarOrcamento = TelaEditarOrcamento()
        self.telaEditarOS = TelaEditarOS()

        self.telaInicio.stackedWidget.addWidget(self.telaCadastroPeca)
        self.telaInicio.stackedWidget.addWidget(self.telaCadastroServico)
        self.telaInicio.stackedWidget.addWidget(self.telaCadastroCliente)
        self.telaInicio.stackedWidget.addWidget(self.telaCadastroOrcamento)

        self.telaInicio.stackedWidget.addWidget(self.telaConsultaPeca)
        self.telaInicio.stackedWidget.addWidget(self.telaConsultaServico)
        self.telaInicio.stackedWidget.addWidget(self.telaConsultaCliente)
        self.telaInicio.stackedWidget.addWidget(self.telaConsultaVeiculo)
        self.telaInicio.stackedWidget.addWidget(self.telaConsultaOrcamento)
        self.telaInicio.stackedWidget.addWidget(self.telaConsultaOS)

        self.telaInicio.stackedWidget.addWidget(self.telaEditarPeca)
        self.telaInicio.stackedWidget.addWidget(self.telaEditarServico)
        self.telaInicio.stackedWidget.addWidget(self.telaEditarCliente)
        self.telaInicio.stackedWidget.addWidget(self.telaEditarVeiculo)
        self.telaInicio.stackedWidget.addWidget(self.telaEditarOrcamento)
        self.telaInicio.stackedWidget.addWidget(self.telaEditarOS)
        self.initConnections()

    #função que instancia uma unica vez cada controller, que podem ser acessados onde necessário
    def setDeps(self):
        pecaController = PecaController()
        handleDeps.setDep('PECACTRL', pecaController)
        servicoController = ServicoController()
        handleDeps.setDep('SERVICOCTRL', servicoController)
        clienteController = ClienteController()
        handleDeps.setDep('CLIENTECTRL', clienteController)
        orcamentoController = OrcamentoController()
        handleDeps.setDep('ORCAMENTOCTRL', orcamentoController)
        marcaController = MarcaController()
        handleDeps.setDep('MARCACTRL', marcaController)
        cidadeController = CidadeController()
        handleDeps.setDep('CIDADECTRL', cidadeController)
        buscaCEP = BuscaCEP()
        handleDeps.setDep('CEP', buscaCEP)

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
        self.telaInicio.botao_os.clicked.connect(lambda: self.telaInicio.stackedWidget.setCurrentWidget(self.telaConsultaOS))    
        self.telaInicio.stackedWidget.currentChanged.connect(self.atualizarJanelas)

        # conectando seleção de edição com respectivas telas de edição
        self.telaConsultaPeca.botaoEditar.clicked.connect(
            lambda: self.consultaParaEditar(self.telaEditarPeca, self.telaEditarPeca.renderEditar, self.telaConsultaPeca.editarPeca))
        self.telaConsultaServico.botaoEditar.clicked.connect(
            lambda: self.consultaParaEditar(self.telaEditarServico, self.telaEditarServico.renderEditar, self.telaConsultaServico.editarServico))
        self.telaConsultaCliente.botaoEditar.clicked.connect(
            lambda: self.consultaParaEditar(self.telaEditarCliente, self.telaEditarCliente.renderEditar, self.telaConsultaCliente.editarCliente))
        self.telaConsultaVeiculo.botaoEditar.clicked.connect(
            lambda: self.consultaParaEditar(self.telaEditarVeiculo, self.telaEditarVeiculo.renderEditar, self.telaConsultaVeiculo.editarVeiculo))
        self.telaConsultaOrcamento.botaoEditar.clicked.connect(
            lambda: self.consultaParaEditar(self.telaEditarOrcamento, self.telaEditarOrcamento.renderEditar, self.telaConsultaOrcamento.editarOrcamento))
        self.telaConsultaOS.botaoEditar.clicked.connect(
            lambda: self.consultaParaEditar(self.telaEditarOS, self.telaEditarOS.renderEditar, self.telaConsultaOS.editarOS))

        # retorno das edições para tela de consulta em caso de cancelamento ou conclusão da operação
        self.telaEditarPeca.paraTelaConsulta.connect(lambda: self.telaInicio.stackedWidget.setCurrentWidget(self.telaConsultaPeca))
        self.telaEditarServico.paraTelaConsulta.connect(lambda: self.telaInicio.stackedWidget.setCurrentWidget(self.telaConsultaServico))
        self.telaEditarCliente.paraTelaConsulta.connect(lambda: self.telaInicio.stackedWidget.setCurrentWidget(self.telaConsultaCliente))
        self.telaEditarVeiculo.paraTelaConsulta.connect(lambda: self.telaInicio.stackedWidget.setCurrentWidget(self.telaConsultaVeiculo))
        self.telaEditarOrcamento.paraTelaConsulta.connect(lambda: self.telaInicio.stackedWidget.setCurrentWidget(self.telaConsultaOrcamento))
        self.telaEditarOS.paraTelaConsulta.connect(lambda: self.telaInicio.stackedWidget.setCurrentWidget(self.telaConsultaOS))
        self.telaConsultaOrcamento.orcamentoAprovado.connect(lambda: self.telaInicio.stackedWidget.setCurrentWidget(self.telaConsultaOS))
        self.telaEditarOrcamento.orcamentoAprovado.connect(lambda: self.telaInicio.stackedWidget.setCurrentWidget(self.telaConsultaOS))

        #consulta para cadastro
        self.telaConsultaPeca.novaPeca.connect(lambda: self.telaInicio.stackedWidget.setCurrentWidget(self.telaCadastroPeca))
        self.telaConsultaServico.novoServico.connect(lambda: self.telaInicio.stackedWidget.setCurrentWidget(self.telaCadastroServico))
        self.telaConsultaCliente.novoCliente.connect(lambda: self.telaInicio.stackedWidget.setCurrentWidget(self.telaCadastroCliente))
        self.telaConsultaVeiculo.novoVeiculo.connect(lambda: self.telaInicio.stackedWidget.setCurrentWidget(self.telaCadastroCliente))
        self.telaConsultaOrcamento.novoOrcamento.connect(lambda: self.telaInicio.stackedWidget.setCurrentWidget(self.telaCadastroOrcamento))

    # função que passa da tela de consulta para a tela de edição da respectiva entidade, passando id a ser alterado como parametro
    def consultaParaEditar(self, pagina, render, param):
        p = param()
        if p == None:
            return
        render(p)
        self.telaInicio.stackedWidget.setCurrentWidget(pagina)

    #função que analiza tela selecionada e as atualiza
    def atualizarJanelas(self):
        match self.telaInicio.stackedWidget.currentWidget():
            case self.telaCadastroCliente:
                self.telaCadastroCliente.setMarcas()
                self.telaCadastroCliente.setCompleters()
            case self.telaCadastroOrcamento:
                self.telaCadastroOrcamento.setMarcas()
                self.telaCadastroOrcamento.setCompleters()
            case self.telaConsultaPeca:
                self.telaConsultaPeca.listarPecas()
            case self.telaConsultaServico:
                self.telaConsultaServico.listarServicos()
            case self.telaConsultaCliente:
                self.telaConsultaCliente.listarClientes()
            case self.telaConsultaVeiculo:
                self.telaConsultaVeiculo.listarVeiculos()
            case self.telaConsultaOrcamento:
                self.telaConsultaOrcamento.listarOrcamentos()
            case self.telaConsultaOS:
                self.telaConsultaOS.listarOS()
            case self.telaEditarVeiculo:
                self.telaEditarVeiculo.setMarcas()
            case self.telaEditarOrcamento:
                self.telaEditarOrcamento.setMarcas()
            case self.telaEditarOS:
                self.telaEditarOS.setMarcas()
            case _:
                return

    def run(self):
        self.telaInicio.resize(1280,800)
        self.telaInicio.show()
        self.splash.finish(self.telaInicio)
        self.app.exec()


if __name__ == "__main__":
    app = APP()
    app.run()
