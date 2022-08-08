import sys
from PyQt6 import QtWidgets, QtCore
from controller.pecaController import PecaController
from controller.orcamentoController import OrcamentoController
from controller.clienteController import ClienteController
from controller.servicoController import ServicoController
from model.modelo import Peca
from ui.telaCadastroCliente import TelaCadastroCliente
from ui.telaCadastroOrcamento import TelaCadastroOrcamento
from ui.telaCadastroPeca import TelaCadastroPeca
from ui.telaCadastroServico import TelaCadastroServico

from ui.telaInicial import TelaInicial
from util.buscaCEP import BuscaCEP

class MainController():

    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        style = open('./ui/styles.qss').read()
        self.app.setStyleSheet(style)
        
        self.telaInicio = TelaInicial()

        self.cPec = PecaController()
        self.cSer = ServicoController()
        self.cCli = ClienteController()
        self.cOrc = OrcamentoController()
        #self.stackedWidget.addWidget(self.telaInicio)
        self.telaInicio.stackedWidget.addWidget(self.cPec.viewCadastro)
        self.telaInicio.stackedWidget.addWidget(self.cSer.viewCadastro)
        self.telaInicio.stackedWidget.addWidget(self.cCli.viewCadastro)
        self.telaInicio.stackedWidget.addWidget(self.cOrc.viewCadastro)

        self.initConnections()

    def initConnections(self):
        #conectando botões do menu
        self.telaInicio.botao_pecas.clicked.connect(self.swTelaCadastroPeca)
        self.telaInicio.botao_servicos.clicked.connect(self.swTelaCadastroServico)
        self.telaInicio.botao_clientes.clicked.connect(self.swTelaCadastroCliente)
        self.telaInicio.botao_orcamentos.clicked.connect(self.swTelaCadastroOrcamento)

        self.cCli.viewCadastro.lineEditCEP.returnPressed.connect(lambda: self.buscarDadosCEP(self.cCli.viewCadastro))
        self.cOrc.viewCadastro.lineEditCEP.returnPressed.connect(lambda: self.buscarDadosCEP(self.cOrc.viewCadastro))

    def swTelaInicial(self):
        self.telaInicio.stackedWidget.setCurrentWidget(self.telaInicio)

    def swTelaCadastroPeca(self):
        self.telaInicio.stackedWidget.setCurrentWidget(self.cPec.viewCadastro)

    def swTelaCadastroServico(self):
        self.telaInicio.stackedWidget.setCurrentWidget(self.cSer.viewCadastro)

    def swTelaCadastroCliente(self):
        self.telaInicio.stackedWidget.setCurrentWidget(self.cCli.viewCadastro)

    def swTelaCadastroOrcamento(self):
        self.telaInicio.stackedWidget.setCurrentWidget(self.cOrc.viewCadastro)
        self.cOrc.atualizarCompleters()

    def swTelaConsultaPeca(self):
        self.telaInicio.stackedWidget.setCurrentWidget(self.cPec.viewConsulta)

    def swTelaConsultaServico(self):
        self.telaInicio.stackedWidget.setCurrentWidget(self.cSer.viewConsulta)

    def swTelaConsultaCliente(self):
        self.telaInicio.stackedWidget.setCurrentWidget(self.cCli.viewConsulta)

    def swTelaConsultaOrcamento(self):
        self.telaInicio.stackedWidget.setCurrentWidget(self.cOrc.viewConsulta)


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
