import sys
from PyQt6 import QtWidgets, QtCore, QtGui
from ui.telaCadastroCliente import TelaCadastroCliente
from ui.telaCadastroOrcamento import TelaCadastroOrcamento
from ui.telaCadastroPeca import TelaCadastroPeca
from ui.telaCadastroServico import TelaCadastroServico
from ui.telaConsultaOrcamento import TelaConsultaOrcamento


from ui.telaInicial import TelaInicial
from util.buscaCEP import BuscaCEP

class MainController():

    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        style = open('./ui/styles.qss').read()
        self.app.setStyleSheet(style)
        QtGui.QFontDatabase.addApplicationFont("./ui/Helvetica.ttf")
        font = QtGui.QFont('Helvetica')
        self.app.setFont(font)
        
        self.telaInicio = TelaInicial()
        self.telaCadastroPeca = TelaCadastroPeca()
        self.telaCadastroServico = TelaCadastroServico()
        self.telaCadastroCliente = TelaCadastroCliente()
        self.telaCadastroOrcamento = TelaCadastroOrcamento()
        self.telaBuscaOrcamento = TelaConsultaOrcamento()

        self.telaInicio.stackedWidget.addWidget(self.telaCadastroPeca)
        self.telaInicio.stackedWidget.addWidget(self.telaCadastroServico)
        self.telaInicio.stackedWidget.addWidget(self.telaCadastroCliente)
        self.telaInicio.stackedWidget.addWidget(self.telaCadastroOrcamento)

        self.telaInicio.stackedWidget.addWidget(self.telaBuscaOrcamento)
        self.initConnections()

    def initConnections(self):
        #conectando botões do menu
        self.telaInicio.botao_pecas.clicked.connect(lambda: self.telaInicio.stackedWidget.setCurrentWidget(self.telaCadastroPeca))
        self.telaInicio.botao_servicos.clicked.connect(lambda: self.telaInicio.stackedWidget.setCurrentWidget(self.telaCadastroServico))
        self.telaInicio.botao_clientes.clicked.connect(lambda: self.telaInicio.stackedWidget.setCurrentWidget(self.telaCadastroCliente))
        self.telaInicio.botao_orcamentos.clicked.connect(lambda: self.telaInicio.stackedWidget.setCurrentWidget(self.telaCadastroOrcamento))
        self.telaInicio.botao_orcamentos_2.clicked.connect(lambda: self.telaInicio.stackedWidget.setCurrentWidget(self.telaBuscaOrcamento))
        self.telaCadastroCliente.lineEditCEP.editingFinished.connect(lambda: self.buscarDadosCEP(self.telaCadastroCliente))
        self.telaCadastroOrcamento.lineEditCEP.editingFinished.connect(lambda: self.buscarDadosCEP(self.telaCadastroOrcamento))

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
