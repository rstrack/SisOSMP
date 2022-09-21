import sys
from PyQt6 import QtWidgets, QtCore, QtGui

from routes import handleRoutes
from ui.telaConsultaCliente import TelaConsultaCliente

from util.buscaCEP import BuscaCEP

from ui.telaInicial import TelaInicial
from ui.telaCadastroCliente import TelaCadastroCliente
from ui.telaCadastroOrcamento import TelaCadastroOrcamento
from ui.telaCadastroPeca import TelaCadastroPeca
from ui.telaCadastroServico import TelaCadastroServico
from ui.telaConsultaOrcamento import TelaConsultaOrcamento

from controller.marcaController import MarcaController
from controller.pecaController import PecaController
from controller.servicoController import ServicoController
from controller.clienteController import ClienteController
from controller.cidadeController import CidadeController
from controller.orcamentoController import OrcamentoController

class MainController():

    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        style = open('./resources/styles.qss').read()
        self.app.setStyleSheet(style)
        QtGui.QFontDatabase.addApplicationFont("./resources/Helvetica.ttf")
        font = QtGui.QFont('Helvetica')
        self.app.setFont(font)
        self.setRoutes()

        self.telaInicio = TelaInicial()
        self.telaCadastroPeca = TelaCadastroPeca()
        self.telaCadastroServico = TelaCadastroServico()
        self.telaCadastroCliente = TelaCadastroCliente()
        #self.telaCadastroOrcamento = TelaCadastroOrcamento()

        self.telaConsultaCliente = TelaConsultaCliente()
        #self.telaConsultaOrcamento = TelaConsultaOrcamento()

        self.telaInicio.stackedWidget.addWidget(self.telaCadastroPeca)
        self.telaInicio.stackedWidget.addWidget(self.telaCadastroServico)
        self.telaInicio.stackedWidget.addWidget(self.telaCadastroCliente)
        #self.telaInicio.stackedWidget.addWidget(self.telaCadastroOrcamento)

        self.telaInicio.stackedWidget.addWidget(self.telaConsultaCliente)
        #self.telaInicio.stackedWidget.addWidget(self.telaConsultaOrcamento)
        self.initConnections()

    #função que instancia uma unica vez cada controller, que podem ser acessados onde necessário
    def setRoutes(self):
        pecaController = PecaController()
        handleRoutes.setRoute('PECA', pecaController)
        servicoController = ServicoController()
        handleRoutes.setRoute('SERVICO', servicoController)
        clienteController = ClienteController()
        handleRoutes.setRoute('CLIENTE', clienteController)
        orcamentoController = OrcamentoController()
        handleRoutes.setRoute('ORCAMENTO', orcamentoController)
        marcaController = MarcaController()
        handleRoutes.setRoute('MARCA', marcaController)
        cidadeController = CidadeController()
        handleRoutes.setRoute('CIDADE', cidadeController)

    def initConnections(self):
        #conectando botões do menu
        self.telaInicio.botao_pecas.clicked.connect(lambda: self.telaInicio.stackedWidget.setCurrentWidget(self.telaCadastroPeca))
        self.telaInicio.botao_servicos.clicked.connect(lambda: self.telaInicio.stackedWidget.setCurrentWidget(self.telaCadastroServico))
        self.telaInicio.botao_clientes.clicked.connect(lambda: self.telaInicio.stackedWidget.setCurrentWidget(self.telaCadastroCliente))
        #self.telaInicio.botao_orcamentos.clicked.connect(lambda: self.telaInicio.stackedWidget.setCurrentWidget(self.telaCadastroOrcamento))

        self.telaInicio.botao_clientes_2.clicked.connect(lambda: self.telaInicio.stackedWidget.setCurrentWidget(self.telaConsultaCliente))
        #self.telaInicio.botao_orcamentos_2.clicked.connect(lambda: self.telaInicio.stackedWidget.setCurrentWidget(self.telaConsultaOrcamento))
        self.telaCadastroCliente.lineEditCEP.editingFinished.connect(lambda: self.buscarDadosCEP(self.telaCadastroCliente))
        #self.telaCadastroOrcamento.lineEditCEP.editingFinished.connect(lambda: self.buscarDadosCEP(self.telaCadastroOrcamento))

    def buscarDadosCEP(self, view):
        cep = view.lineEditCEP.text()
        if len(cep) !=8:
            return
        dados = BuscaCEP.buscarCEP(view.lineEditCEP.text())
        if 'erro' in dados:
            return
        view.lineEditEnder.setText(dados['logradouro'])
        view.lineEditBairro.setText(dados['bairro'])
        view.lineEditCidade.setText(dados['localidade'])
        for index in range(view.comboBoxuf.count()):
            if(view.comboBoxuf.itemText(index)==dados['uf']):
                view.comboBoxuf.setCurrentIndex(index)
                return

    def run(self):
        self.telaInicio.resize(1280,720)
        self.telaInicio.show()
        sys.exit(self.app.exec())


if __name__ == "__main__":

    c = MainController()
    c.run()
