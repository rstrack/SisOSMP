from decimal import Decimal
from PyQt6 import QtCore, QtWidgets, QtGui
from datetime import datetime

from util.container import handleDeps
from ui.help import HELPEDITARORCAMENTO, help
from ui.messageBox import MessageBox
from ui.hoverButton import HoverButton
from util.gerar_pdf import GeraPDF

SIGLAESTADOS = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS',
                'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
UNIDADES = ['CM', 'CM2', 'CM3', 'CX', 'DZ', 'G', 'KG',
            'L', 'M', 'M2', 'M3', 'ML', 'PAR', 'PCT', 'ROLO', 'UN']


class TelaEditarOrcamento(QtWidgets.QMainWindow):
    paraTelaConsulta = QtCore.pyqtSignal(int)
    orcamentoAprovado = QtCore.pyqtSignal(int)
    def __init__(self):
        super(TelaEditarOrcamento, self).__init__()
        self.orcamentoCtrl = handleDeps.getDep('ORCAMENTOCTRL')
        self.clienteCtrl = handleDeps.getDep('CLIENTECTRL')
        self.pecaCtrl = handleDeps.getDep('PECACTRL')
        self.servicoCtrl = handleDeps.getDep('SERVICOCTRL')
        self.marcaCtrl = handleDeps.getDep('MARCACTRL')
        self.buscaCEP = handleDeps.getDep('CEP')
        self.setupUi()

    def setupUi(self):
        self.valorTotal = 0
        self.orcamentoID = None
        self.linhasPeca = []
        self.linhasServico = []
        self.resize(1280, 760)
        self.main_frame = QtWidgets.QFrame(self)
        self.main_frame.setObjectName("main_frame")
        self.hlayout = QtWidgets.QHBoxLayout(self.main_frame)
        spacer = QtWidgets.QSpacerItem(
            20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.hlayout.addItem(spacer)
        self.framegeral = QtWidgets.QFrame(self.main_frame)
        self.framegeral.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        self.framegeral.setMaximumWidth(int(QtGui.QGuiApplication.primaryScreen().size().width()*0.65) 
            if QtGui.QGuiApplication.primaryScreen().size().width()> 1280 else QtGui.QGuiApplication.primaryScreen().size().width())
        self.hlayout.addWidget(self.framegeral)
        spacer = QtWidgets.QSpacerItem(
            20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.hlayout.addItem(spacer)
        self.vlayout = QtWidgets.QVBoxLayout(self.framegeral)
        self.vlayout.setContentsMargins(0,0,0,0)
        self.vlayout.setSpacing(0)
        # titulo
        self.frameTitulo = QtWidgets.QFrame(self.framegeral)
        self.vlayout.addWidget(self.frameTitulo)
        self.hlayouttitulo = QtWidgets.QHBoxLayout(self.frameTitulo)
        self.hlayouttitulo.setContentsMargins(0,0,0,0)
        self.hlayouttitulo.setSpacing(0)
        self.hlayouttitulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.labelTitulo = QtWidgets.QLabel(self.frameTitulo)
        self.labelTitulo.setFixedHeight(100)
        self.labelTitulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelTitulo.setObjectName("titulo")
        self.hlayouttitulo.addWidget(self.labelTitulo)
        self.botaoHelp = HoverButton("", "./resources/help-icon1.png", "./resources/help-icon2.png", self.frameTitulo)
        self.botaoHelp.setToolTip('Ajuda')
        self.botaoHelp.setObjectName('botaohelp')
        self.botaoHelp.setHelpIconSize(20,20)
        self.hlayouttitulo.addWidget(self.botaoHelp)
        self.framedados = QtWidgets.QFrame(self.main_frame)
        self.gridLayoutGeral = QtWidgets.QGridLayout(self.framedados)
        self.gridLayoutGeral.setVerticalSpacing(6)
        self.gridLayoutGeral.setHorizontalSpacing(9)
        self.vlayout.addWidget(self.framedados)

        #data
        self.frameData = QtWidgets.QFrame(self.framedados)
        self.gridLayoutGeral.addWidget(self.frameData, 0, 0, 1, -1)
        self.vlayoutData = QtWidgets.QVBoxLayout(self.frameData)
        self.vlayoutData.setContentsMargins(0,0,0,0)
        self.labelData = QtWidgets.QLabel(self.frameData)
        self.lineEditData = QtWidgets.QDateEdit(self.frameData)
        self.lineEditData.setFixedWidth(125)
        self.lineEditData.setCalendarPopup(True)
        self.lineEditData.setDateTime(QtCore.QDateTime.currentDateTime())
        self.vlayoutData.addWidget(self.labelData)
        self.vlayoutData.addWidget(self.lineEditData)

        # dados do cliente
        self.groupBoxCliente = QtWidgets.QGroupBox(self.framedados)
        self.gridLayoutCliente = QtWidgets.QGridLayout(self.groupBoxCliente)
        self.labelTipo = QtWidgets.QLabel(self.groupBoxCliente)
        self.gridLayoutCliente.addWidget(self.labelTipo, 0, 0, 1, 1)
        self.labelDocumento = QtWidgets.QLabel(self.groupBoxCliente)
        self.gridLayoutCliente.addWidget(self.labelDocumento, 0, 1, 1, 1)
        self.labelNome = QtWidgets.QLabel(self.groupBoxCliente)
        self.gridLayoutCliente.addWidget(self.labelNome, 0, 2, 1, 1)
        self.labelFone1 = QtWidgets.QLabel(self.groupBoxCliente)
        self.gridLayoutCliente.addWidget(self.labelFone1, 0, 4, 1, 1)
        self.labelFone2 = QtWidgets.QLabel(self.groupBoxCliente)
        self.gridLayoutCliente.addWidget(self.labelFone2, 0, 5, 1, 1)
        self.comboBoxPessoa = QtWidgets.QComboBox(self.groupBoxCliente)
        self.comboBoxPessoa.addItems(["PESSOA FÍSICA", "PESSOA JURÍDICA", "ESTRANGEIRO"])
        self.gridLayoutCliente.addWidget(self.comboBoxPessoa, 1, 0, 1, 1)
        self.lineEditDocumento = QtWidgets.QLineEdit(self.groupBoxCliente)
        self.gridLayoutCliente.addWidget(self.lineEditDocumento, 1, 1, 1, 1)
        self.lineEditNomeCliente = QtWidgets.QLineEdit(self.groupBoxCliente)
        self.gridLayoutCliente.addWidget(self.lineEditNomeCliente, 1, 2, 1, 2)
        self.lineEditFone1 = QtWidgets.QLineEdit(self.groupBoxCliente)
        self.gridLayoutCliente.addWidget(self.lineEditFone1, 1, 4, 1, 1)
        self.lineEditFone2 = QtWidgets.QLineEdit(self.groupBoxCliente)
        self.gridLayoutCliente.addWidget(self.lineEditFone2, 1, 5, 1, 1)
        self.labelCEP = QtWidgets.QLabel(self.groupBoxCliente)
        self.gridLayoutCliente.addWidget(self.labelCEP, 2, 0, 1, 1)
        self.labelEnder = QtWidgets.QLabel(self.groupBoxCliente)
        self.gridLayoutCliente.addWidget(self.labelEnder, 2, 1, 1, 1)
        self.labelNumero = QtWidgets.QLabel(self.groupBoxCliente)
        self.gridLayoutCliente.addWidget(self.labelNumero, 2, 3, 1, 1)
        self.labelBairro = QtWidgets.QLabel(self.groupBoxCliente)
        self.gridLayoutCliente.addWidget(self.labelBairro, 2, 4, 1, 1)
        self.labelCidade = QtWidgets.QLabel(self.groupBoxCliente)
        self.gridLayoutCliente.addWidget(self.labelCidade, 2, 5, 1, 1)
        self.labelUF = QtWidgets.QLabel(self.groupBoxCliente)
        self.gridLayoutCliente.addWidget(self.labelUF, 2, 6, 1, 1)
        self.lineEditCEP = QtWidgets.QLineEdit(self.groupBoxCliente)
        self.gridLayoutCliente.addWidget(self.lineEditCEP, 3, 0, 1, 1)
        self.lineEditEnder = QtWidgets.QLineEdit(self.groupBoxCliente)
        self.gridLayoutCliente.addWidget(self.lineEditEnder, 3, 1, 1, 2)
        self.lineEditNumero = QtWidgets.QLineEdit(self.groupBoxCliente)
        self.gridLayoutCliente.addWidget(self.lineEditNumero, 3, 3, 1, 1)
        self.lineEditBairro = QtWidgets.QLineEdit(self.groupBoxCliente)
        self.gridLayoutCliente.addWidget(self.lineEditBairro, 3, 4, 1, 1)
        self.lineEditCidade = QtWidgets.QLineEdit(self.groupBoxCliente)
        self.gridLayoutCliente.addWidget(self.lineEditCidade, 3, 5, 1, 1)
        self.comboBoxuf = QtWidgets.QComboBox(self.groupBoxCliente)
        self.comboBoxuf.addItems(SIGLAESTADOS)
        self.comboBoxuf.setCurrentIndex(15)
        self.gridLayoutCliente.addWidget(self.comboBoxuf, 3, 6, 1, 1)
        self.gridLayoutCliente.setColumnStretch(0, 3)
        self.gridLayoutCliente.setColumnStretch(1, 4)
        self.gridLayoutCliente.setColumnStretch(2, 8)
        self.gridLayoutCliente.setColumnStretch(4, 6)
        self.gridLayoutCliente.setColumnStretch(5, 6)
        self.gridLayoutCliente.setColumnStretch(6, 2)
        self.gridLayoutGeral.addWidget(self.groupBoxCliente, 1, 0, 1, -1)
        # dados do veiculo
        self.groupBoxVeiculo = QtWidgets.QGroupBox(self.framedados)
        self.gridLayoutVeiculo = QtWidgets.QGridLayout(self.groupBoxVeiculo)
        self.labelMarca = QtWidgets.QLabel(self.groupBoxVeiculo)
        self.gridLayoutVeiculo.addWidget(self.labelMarca, 0, 0, 1, 1)
        self.labelModelo = QtWidgets.QLabel(self.groupBoxVeiculo)
        self.gridLayoutVeiculo.addWidget(self.labelModelo, 0, 1, 1, 1)
        self.labelPlaca = QtWidgets.QLabel(self.groupBoxVeiculo)
        self.gridLayoutVeiculo.addWidget(self.labelPlaca, 0, 2, 1, 1)
        self.labelAno = QtWidgets.QLabel(self.groupBoxVeiculo)
        self.gridLayoutVeiculo.addWidget(self.labelAno, 0, 3, 1, 1)
        self.labelKm = QtWidgets.QLabel(self.groupBoxVeiculo)
        self.gridLayoutVeiculo.addWidget(self.labelKm, 0, 4, 1, 1)
        self.comboBoxMarca = QtWidgets.QComboBox(self.groupBoxVeiculo)
        self.comboBoxMarca.setEditable(True)
        self.gridLayoutVeiculo.addWidget(self.comboBoxMarca, 1, 0, 1, 1)
        self.lineEditModelo = QtWidgets.QLineEdit(self.groupBoxVeiculo)
        self.gridLayoutVeiculo.addWidget(self.lineEditModelo, 1, 1, 1, 1)
        self.lineEditPlaca = QtWidgets.QLineEdit(self.groupBoxVeiculo)
        self.gridLayoutVeiculo.addWidget(self.lineEditPlaca, 1, 2, 1, 1)
        self.lineEditAno = QtWidgets.QLineEdit(self.groupBoxVeiculo)
        self.gridLayoutVeiculo.addWidget(self.lineEditAno, 1, 3, 1, 1)
        self.lineEditKm = QtWidgets.QLineEdit(self.groupBoxVeiculo)
        self.lineEditKm.setMaxLength(6)
        self.gridLayoutVeiculo.addWidget(self.lineEditKm, 1, 4, 1, 1)
        self.gridLayoutGeral.addWidget(self.groupBoxVeiculo, 2, 0, 1, -1)
        self.gridLayoutVeiculo.setColumnStretch(0, 3)
        self.gridLayoutVeiculo.setColumnStretch(1, 5)
        self.gridLayoutVeiculo.setColumnStretch(2, 1)
        self.gridLayoutVeiculo.setColumnStretch(3, 1)
        self.gridLayoutVeiculo.setColumnStretch(4, 1)
        # peças
        self.groupBoxPecas = QtWidgets.QGroupBox(self.framedados)
        self.vlayoutgpecas = QtWidgets.QVBoxLayout(self.groupBoxPecas)
        self.vlayoutgpecas.setContentsMargins(1, 1, 1, 1)
        self.scrollarea1 = QtWidgets.QScrollArea(self.groupBoxPecas)
        self.scrollarea1.setWidgetResizable(True)
        self.scrollarea1.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.vlayoutgpecas.addWidget(self.scrollarea1)
        self.framegroupboxpecas = QtWidgets.QFrame(self.scrollarea1)
        self.framegroupboxpecas.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        self.scrollarea1.setWidget(self.framegroupboxpecas)
        self.gridLayoutPecas = QtWidgets.QGridLayout(self.framegroupboxpecas)
        self.labelNomePeca = QtWidgets.QLabel(self.framegroupboxpecas)
        self.gridLayoutPecas.addWidget(self.labelNomePeca, 0, 0, 1, 1)
        self.labelQtdePeca = QtWidgets.QLabel(self.framegroupboxpecas)
        self.gridLayoutPecas.addWidget(self.labelQtdePeca, 0, 1, 1, 1)
        self.labelUnPeca = QtWidgets.QLabel(self.framegroupboxpecas)
        self.gridLayoutPecas.addWidget(self.labelUnPeca, 0, 2, 1, 1)
        self.labelValorPeca = QtWidgets.QLabel(self.framegroupboxpecas)
        self.gridLayoutPecas.addWidget(self.labelValorPeca, 0, 3, 1, 1)
        self.botaoAddPecas = QtWidgets.QPushButton(self.framegroupboxpecas)
        self.botaoAddPecas.setFixedSize(25,25)
        self.botaoAddPecas.setToolTip('Adicionar linha')
        self.gridLayoutPecas.addWidget(self.botaoAddPecas, 1, 5, 1, 1)
        self.spacerpeca = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayoutPecas.addItem(self.spacerpeca, 2, 0, 1, 1)
        self.gridLayoutGeral.addWidget(self.groupBoxPecas, 3, 0, 1, 1)
        self.labelNomePeca.hide()
        self.labelQtdePeca.hide()
        self.labelUnPeca.hide()
        self.labelValorPeca.hide()
        self.gridLayoutPecas.setColumnStretch(0, 6)
        self.gridLayoutPecas.setColumnStretch(1, 1)
        self.gridLayoutPecas.setColumnStretch(3, 1)
        # serviços
        self.groupBoxServicos = QtWidgets.QGroupBox(self.framedados)
        self.vlayoutgservicos = QtWidgets.QVBoxLayout(self.groupBoxServicos)
        self.vlayoutgservicos.setContentsMargins(1, 1, 1, 1)
        self.scrollarea2 = QtWidgets.QScrollArea(self.groupBoxServicos)
        self.scrollarea2.setWidgetResizable(True)
        self.scrollarea2.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.vlayoutgservicos.addWidget(self.scrollarea2)
        self.framegroupboxservicos = QtWidgets.QFrame(self.scrollarea2)
        self.framegroupboxservicos.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        self.scrollarea2.setWidget(self.framegroupboxservicos)
        self.gridLayoutServicos = QtWidgets.QGridLayout(self.framegroupboxservicos)
        self.labelNomeServico = QtWidgets.QLabel(self.framegroupboxservicos)
        self.gridLayoutServicos.addWidget(self.labelNomeServico, 0, 0, 1, 1)
        self.labelQtdeServico = QtWidgets.QLabel(self.framegroupboxservicos)
        self.gridLayoutServicos.addWidget(self.labelQtdeServico, 0, 1, 1, 1)
        self.labelValorServico = QtWidgets.QLabel(self.framegroupboxservicos)
        self.gridLayoutServicos.addWidget(self.labelValorServico, 0, 2, 1, 1)
        self.botaoAddServicos = QtWidgets.QPushButton(self.framegroupboxservicos)
        self.botaoAddServicos.setFixedSize(25,25)
        self.botaoAddServicos.setToolTip('Adicionar linha')
        self.gridLayoutServicos.addWidget(self.botaoAddServicos, 1, 4, 1, 1)
        self.spacerservico = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayoutServicos.addItem(self.spacerservico, 2, 0, 1, 1)
        self.gridLayoutGeral.addWidget(self.groupBoxServicos, 3, 1, 1, 1)
        self.labelNomeServico.hide()
        self.labelQtdeServico.hide()
        self.labelValorServico.hide()
        self.gridLayoutServicos.setColumnStretch(0, 6)
        self.gridLayoutServicos.setColumnStretch(1, 1)
        self.gridLayoutServicos.setColumnStretch(2, 1)
        #dados orcamento

        self.frameValorTotal = QtWidgets.QFrame(self.framedados)
        self.gridLayoutGeral.addWidget(self.frameValorTotal, 4, 0, 1, -1)
        self.hlayoutValor = QtWidgets.QHBoxLayout(self.frameValorTotal)
        self.labelValorTotal1 = QtWidgets.QLabel(self.frameValorTotal)
        self.labelValorTotal1.setObjectName('boldText')
        self.labelValorTotal2 = QtWidgets.QLabel(self.frameValorTotal)
        self.labelValorTotal2.setObjectName('boldText')
        self.labelValorTotal2.setText('0,00')
        spacer = QtWidgets.QSpacerItem(
            40, 10, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.hlayoutValor.addItem(spacer)
        self.hlayoutValor.addWidget(self.labelValorTotal1)
        self.hlayoutValor.addWidget(self.labelValorTotal2)
        self.gridLayoutGeral.setRowStretch(5, 10)
        self.gridLayoutGeral.setRowStretch(6, 0)
        # campo de observações
        self.groupBoxObs = QtWidgets.QGroupBox(self.framedados)
        self.vlayout2 = QtWidgets.QVBoxLayout(self.groupBoxObs)
        self.textEdit = QtWidgets.QTextEdit(self.groupBoxObs)
        self.groupBoxObs.setMaximumHeight(100)
        self.vlayout2.addWidget(self.textEdit)
        self.gridLayoutGeral.addWidget(self.groupBoxObs, 5, 0, 1, -1)
        # botoes
        self.framebotoes = QtWidgets.QFrame(self.main_frame)
        self.hlayout4 = QtWidgets.QHBoxLayout(self.framebotoes)
        self.labelLegenda = QtWidgets.QLabel(self.framebotoes)
        self.hlayout4.addWidget(self.labelLegenda)
        spacerItem5 = QtWidgets.QSpacerItem(
            40, 10, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.hlayout4.addItem(spacerItem5)
        self.botaoSalvar = QtWidgets.QPushButton(self.framebotoes)
        self.botaoSalvar.setMinimumSize(100, 35)
        self.botaoSalvar.setObjectName('botaoprincipal')
        self.hlayout4.addWidget(self.botaoSalvar)
        self.botaoSalvareGerarPDF = QtWidgets.QPushButton(self.framebotoes)
        self.botaoSalvareGerarPDF.setMinimumSize(150, 35)
        self.hlayout4.addWidget(self.botaoSalvareGerarPDF)
        self.botaoAprovar = QtWidgets.QPushButton(self.framebotoes)
        self.botaoAprovar.setMinimumSize(130, 35)
        self.hlayout4.addWidget(self.botaoAprovar)
        self.botaoReprovar = QtWidgets.QPushButton(self.framebotoes)
        self.botaoReprovar.setMinimumSize(130, 35)
        self.hlayout4.addWidget(self.botaoReprovar)
        self.botaoCancelar = QtWidgets.QPushButton(self.framebotoes)
        self.botaoCancelar.setMinimumSize(100, 35)
        self.hlayout4.addWidget(self.botaoCancelar)
        self.hlayout4.setContentsMargins(9, 9, 9, 9)
        self.vlayout.addWidget(self.framebotoes)
        self.setCentralWidget(self.main_frame)
        self.completerPeca = QtWidgets.QCompleter([])
        self.completerPeca.setCaseSensitivity(
            QtCore.Qt.CaseSensitivity.CaseInsensitive)
        self.completerPeca.setCompletionMode(
            QtWidgets.QCompleter.CompletionMode.UnfilteredPopupCompletion)
        self.completerServico = QtWidgets.QCompleter([])
        self.completerServico.setCaseSensitivity(
            QtCore.Qt.CaseSensitivity.CaseInsensitive)
        self.completerServico.setCompletionMode(
            QtWidgets.QCompleter.CompletionMode.UnfilteredPopupCompletion)
        for lineedit in self.groupBoxCliente.findChildren((QtWidgets.QLineEdit, QtWidgets.QComboBox)):
            lineedit.setEnabled(False)
        for lineedit in self.groupBoxVeiculo.findChildren((QtWidgets.QLineEdit, QtWidgets.QComboBox)):
            lineedit.setEnabled(False)
        self.lineEditKm.setEnabled(True)
 
        self.retranslateUi()
        self.botaoAddPecas.clicked.connect(self.addLinhaPeca)
        self.botaoAddServicos.clicked.connect(self.addLinhaServico)
        self.setMarcas()
        self.setCompleters()
        self.botaoSalvar.clicked.connect(self.editarOrcamento)
        self.botaoSalvareGerarPDF.clicked.connect(self.salvareGerarPDF)
        self.botaoAprovar.clicked.connect(self.aprovarOrcamento)
        self.botaoReprovar.clicked.connect(self.reprovarOrcamento)
        self.botaoCancelar.clicked.connect(self.cancelarEdicao)
        self.botaoHelp.clicked.connect(lambda: help('Ajuda - Editar Orçamento', HELPEDITARORCAMENTO))

    ##############################################################################################################################
                                                            #FUNÇÕES
    ##############################################################################################################################

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Mecânica Pasetto"))
        self.botaoAprovar.setText(_translate("MainWindow", "Editar e Aprovar"))
        self.botaoReprovar.setText(_translate("MainWindow", "Reprovar"))
        self.botaoSalvar.setText(_translate("MainWindow", "Salvar"))
        self.botaoSalvareGerarPDF.setText(_translate("MainWindow", "Salvar e Gerar PDF"))
        self.botaoCancelar.setText(_translate("MainWindow", "Cancelar"))
        self.labelTitulo.setText(_translate("MainWindow", "Editar Orçamento"))
        self.labelData.setText(_translate("MainWindow", "Data do Orçamento*"))
        self.labelNome.setText(_translate("MainWindow", "Nome*"))
        self.labelCEP.setText(_translate("MainWindow", "CEP"))
        self.labelTipo.setText(_translate("MainWindow", "Tipo"))
        self.labelDocumento.setText(_translate("MainWindow", "CPF"))
        self.labelUF.setText(_translate("MainWindow", "UF"))
        self.labelCidade.setText(_translate("MainWindow", "Cidade"))
        self.labelEnder.setText(_translate("MainWindow", "Logradouro"))
        self.labelNumero.setText(_translate("MainWindow", "Número"))
        self.labelBairro.setText(_translate("MainWindow", "Bairro"))
        self.labelFone1.setText(_translate("MainWindow", "Fone 1*"))
        self.labelFone2.setText(_translate("MainWindow", "Fone 2"))
        self.labelMarca.setText(_translate("MainWindow", "Marca*"))
        self.labelPlaca.setText(_translate("MainWindow", "Placa*"))
        self.labelAno.setText(_translate("MainWindow", "Ano"))
        self.labelModelo.setText(_translate("MainWindow", "Modelo*"))
        self.labelKm.setText(_translate("MainWindow", "Km*"))
        self.labelNomePeca.setText(_translate("MainWindow", "Peça*"))
        self.labelQtdePeca.setText(_translate("MainWindow", "Qtde.*"))
        self.labelUnPeca.setText(_translate("MainWindow", "Un.*"))
        self.labelValorPeca.setText(_translate("MainWindow", "Valor Un.*"))
        self.botaoAddPecas.setText(_translate("MainWindow", "+"))
        self.labelNomeServico.setText(_translate("MainWindow", "Serviço*"))
        self.labelQtdeServico.setText(_translate("MainWindow", "Qtde.*"))
        self.labelValorServico.setText(_translate("MainWindow", "Valor Un.*"))
        self.botaoAddServicos.setText(_translate("MainWindow", "+"))
        self.labelLegenda.setText(_translate("MainWindow", "* Campos Obrigatórios"))
        self.groupBoxObs.setTitle(_translate("MainWindow", "Observações (Max. 200 caracteres)"))
        self.labelValorTotal1.setText(_translate("MainWindow", "VALOR TOTAL: R$"))

    def addLinhaPeca(self):
        lineedit1 = QtWidgets.QLineEdit()
        lineedit1.setMaxLength(80)
        lineedit1.setCompleter(self.completerPeca)
        lineedit2 = QtWidgets.QLineEdit()
        comboBox = QtWidgets.QComboBox()
        comboBox.addItems(UNIDADES)
        comboBox.setCurrentIndex(15)
        lineedit4 = QtWidgets.QLineEdit()
        botaoRemoverLinha = QtWidgets.QPushButton()
        botaoRemoverLinha.setFixedSize(25,25)
        botaoRemoverLinha.setToolTip('Remover linha')
        botaoRemoverLinha.setText("-")
        botaoRemoverLinha.setObjectName('excluir')
        self.gridLayoutPecas.addWidget(lineedit1, len(self.linhasPeca)+1, 0, 1, 1)
        self.gridLayoutPecas.addWidget(lineedit2, len(self.linhasPeca)+1, 1, 1, 1)
        self.gridLayoutPecas.addWidget(comboBox, len(self.linhasPeca)+1, 2, 1, 1)
        self.gridLayoutPecas.addWidget(lineedit4, len(self.linhasPeca)+1, 3, 1, 1)
        self.gridLayoutPecas.addWidget(botaoRemoverLinha, len(self.linhasPeca)+1, 4, 1, 1)
        self.linhasPeca.append([lineedit1, lineedit2, comboBox, lineedit4])
        self.gridLayoutPecas.removeItem(self.spacerpeca)
        self.gridLayoutPecas.addItem(self.spacerpeca, len(self.linhasPeca)+1, 0, 1, 1)
        lineedit1.textChanged.connect(self.setValor)
        lineedit2.textChanged.connect(self.setValor)
        lineedit4.textChanged.connect(self.setValor)
        lineedit1.textChanged.connect(lambda: self.buscarPeca(lineedit1, comboBox, lineedit4))
        botaoRemoverLinha.clicked.connect(lambda: self.removerLinhaPeca(self.gridLayoutPecas.getItemPosition(self.gridLayoutPecas.indexOf(botaoRemoverLinha))[0]))
        self.labelNomePeca.show()
        self.labelQtdePeca.show()
        self.labelUnPeca.show()
        self.labelValorPeca.show()

    def removerLinhaPeca(self, linha):
        for x in range(5):
            if self.gridLayoutPecas.itemAtPosition(linha, x) != None:
                self.gridLayoutPecas.itemAtPosition(linha, x).widget().setParent(None)
        for x in range(self.gridLayoutPecas.rowCount()):
            if x > linha:
                for y in range(5):
                    if not isinstance(self.gridLayoutPecas.itemAtPosition(x, y), QtWidgets.QSpacerItem) and self.gridLayoutPecas.itemAtPosition(x, y) != None:
                        self.gridLayoutPecas.addWidget(self.gridLayoutPecas.itemAtPosition(x, y).widget(), x-1, y, 1, 1)
        del self.linhasPeca[linha-1]
        self.gridLayoutPecas.addItem(self.spacerpeca, len(self.linhasPeca)+2, 0, 1, 1)
        if len(self.linhasPeca) == 0:
            self.labelNomePeca.hide()
            self.labelQtdePeca.hide()
            self.labelUnPeca.hide()
            self.labelValorPeca.hide()

    def addLinhaServico(self):
        lineedit1 = QtWidgets.QLineEdit()
        lineedit1.setMaxLength(80)
        lineedit1.setCompleter(self.completerServico)
        lineedit2 = QtWidgets.QLineEdit()
        lineedit3 = QtWidgets.QLineEdit()
        botaoRemoverLinha = QtWidgets.QPushButton()
        botaoRemoverLinha.setFixedSize(25,25)
        botaoRemoverLinha.setToolTip('Remover linha')
        botaoRemoverLinha.setText("-")
        botaoRemoverLinha.setObjectName('excluir')
        self.gridLayoutServicos.addWidget(lineedit1, len(self.linhasServico)+1, 0, 1, 1)
        self.gridLayoutServicos.addWidget(lineedit2, len(self.linhasServico)+1, 1, 1, 1)
        self.gridLayoutServicos.addWidget(lineedit3, len(self.linhasServico)+1, 2, 1, 1)
        self.gridLayoutServicos.addWidget(botaoRemoverLinha, len(self.linhasServico)+1, 3, 1, 1)
        self.linhasServico.append([lineedit1, lineedit2, lineedit3])
        self.gridLayoutServicos.removeItem(self.spacerservico)
        self.gridLayoutServicos.addItem(self.spacerservico, len(self.linhasServico)+1, 0, 1, 1)
        lineedit1.textChanged.connect(self.setValor)
        lineedit2.textChanged.connect(self.setValor)
        lineedit3.textChanged.connect(self.setValor)
        lineedit1.textChanged.connect(lambda: self.buscarServico(lineedit1, lineedit3))
        botaoRemoverLinha.clicked.connect(lambda: self.removerLinhaServico(self.gridLayoutServicos.getItemPosition(self.gridLayoutServicos.indexOf(botaoRemoverLinha))[0]))
        self.labelNomeServico.show()
        self.labelQtdeServico.show()
        self.labelValorServico.show()

    def removerLinhaServico(self, linha):
        for x in range(4):
            if self.gridLayoutServicos.itemAtPosition(linha, x) != None:
                self.gridLayoutServicos.itemAtPosition(linha, x).widget().setParent(None)
        for x in range(self.gridLayoutServicos.rowCount()):
            if x > linha:
                for y in range(4):
                    if not isinstance(self.gridLayoutServicos.itemAtPosition(x, y), QtWidgets.QSpacerItem) and self.gridLayoutServicos.itemAtPosition(x, y) != None:
                        self.gridLayoutServicos.addWidget(self.gridLayoutServicos.itemAtPosition(x, y).widget(), x-1, y, 1, 1)
        del self.linhasServico[linha-1]
        self.gridLayoutServicos.addItem(self.spacerservico, len(self.linhasServico)+2, 0, 1, 1)
        if len(self.linhasServico) == 0:
            self.labelNomeServico.hide()
            self.labelQtdeServico.hide()
            self.labelValorServico.hide()

    def setCliente(self, tipo, nome, documento=None, tel1=None, tel2=None):
        self.lineEditNomeCliente.setText(nome)
        if documento:
            self.lineEditDocumento.setText(documento)
            if tipo == '0':
                self.labelDocumento.setText("CPF")
                self.comboBoxPessoa.setCurrentIndex(0)
            elif tipo == '1':
                self.labelDocumento.setText("CNPJ")
                self.comboBoxPessoa.setCurrentIndex(1)
            else:
                self.labelDocumento.setText("Documento")
                self.comboBoxPessoa.setCurrentIndex(2)
        self.lineEditFone1.setText(tel1)
        self.lineEditFone2.setText(tel2)

    def setEndereco(self, cep=None, ender=None, num=None, bairro=None, cidade=None, uf=None):
        self.lineEditCEP.setText(cep)
        self.lineEditEnder.setText(ender)
        self.lineEditNumero.setText(num)
        self.lineEditBairro.setText(bairro)
        self.lineEditCidade.setText(cidade)
        if uf:
            self.comboBoxuf.setCurrentIndex(
                self.comboBoxuf.findText(uf, QtCore.Qt.MatchFlag.MatchExactly))

    def setVeiculo(self, marca, modelo, placa, ano=None):
        self.lineEditModelo.setText(modelo)
        self.lineEditAno.setText(ano)
        self.lineEditPlaca.setText(placa)
        self.comboBoxMarca.setCurrentIndex(
            self.comboBoxMarca.findText(marca, QtCore.Qt.MatchFlag.MatchExactly))
    
    def setPecas(self, listaPecas:list):
        for _ in range(len(listaPecas)):
            self.addLinhaPeca()
        for linha in self.linhasPeca:
            linha[0].setText(listaPecas[self.linhasPeca.index(linha)]['descricao'])
            linha[1].setText(str(listaPecas[self.linhasPeca.index(linha)]['qtde']).replace('.',',',1))
            linha[2].setCurrentIndex(linha[2].findText(listaPecas[self.linhasPeca.index(linha)]['un'], QtCore.Qt.MatchFlag.MatchExactly))
            linha[3].setText('{:.2f}'.format(listaPecas[self.linhasPeca.index(linha)]['valor']).replace('.',',',1))

    def setServicos(self, listaServicos:list):
        for _ in range(len(listaServicos)):
            self.addLinhaServico()
        for linha in self.linhasServico:
            linha[0].setText(listaServicos[self.linhasServico.index(linha)]['descricao'])
            linha[1].setText(str(listaServicos[self.linhasServico.index(linha)]['qtde']).replace('.',',',1))
            linha[2].setText('{:.2f}'.format(listaServicos[self.linhasServico.index(linha)]['valor']).replace('.',',',1))

    def setMarcas(self):
        currentText = self.comboBoxMarca.currentText()
        self.comboBoxMarca.clear()
        marcas = self.marcaCtrl.listarMarcas()
        for marca in marcas:
            self.comboBoxMarca.addItem(marca['nome'])
        self.comboBoxMarca.setCurrentIndex(
            self.comboBoxMarca.findText(currentText, QtCore.Qt.MatchFlag.MatchExactly))

    def setCompleters(self):
        pecas = self.pecaCtrl.listarPecas()
        servicos = self.servicoCtrl.listarServicos()
        listaPecas = []
        listaServicos = []
        if pecas:
            for peca in pecas:
                listaPecas.append(peca['descricao'])
        if servicos:
            for servico in servicos:
                listaServicos.append(servico['descricao'])
        modelPecas = QtCore.QStringListModel()
        modelPecas.setStringList(listaPecas)
        self.completerPeca.setModel(modelPecas)
        modelServicos = QtCore.QStringListModel()
        modelServicos.setStringList(listaServicos)
        self.completerServico.setModel(modelServicos)

    def getPecas(self):
        pecas = []
        for desc, qtde, un, valor in self.linhasPeca:
            if desc.text() and valor.text():
                dict = {}
                dict['descricao'] = desc.text()
                if not qtde.text(): dict['qtde'] = 1
                else:
                    if not (qtde.text().replace(',','',1).isnumeric() or qtde.text().replace('.','',1).isnumeric()):
                        raise Exception('Campo "qtde" inválido!')
                    dict['qtde'] = qtde.text().replace(',','.',1)
                dict['un'] = un.currentText()
                if not (valor.text().replace(',','',1).isnumeric() or valor.text().replace('.','',1).isnumeric()):
                    raise Exception('Campo "valor" inválido!')
                if -Decimal(valor.text().replace(',','.',1)).as_tuple().exponent > 2:
                    raise Exception("Valores devem possuir no máximo duas casas decimais!")
                dict['valor'] = valor.text().replace(',','.',1)
                pecas.append(dict)
            elif desc.text() or valor.text():
                raise Exception('Preencha todos os campos de cada peça!')
        return pecas

    def getServicos(self):
        servicos = []
        linhasValidas = 0
        for desc, qtde, valor in self.linhasServico:
            if desc.text() and valor.text():
                linhasValidas+=1
                dict = {}
                dict['descricao'] = desc.text()
                if not qtde.text(): dict['qtde'] = 1
                else:
                    if not qtde.text().isnumeric():
                        raise Exception('Campo "qtde" em "serviços" deve ser um número inteiro!')
                    dict['qtde'] = qtde.text().replace(',','.',1)
                if not (valor.text().replace(',','',1).isnumeric() or valor.text().replace('.','',1).isnumeric()):
                    raise Exception('Campo "valor" inválido!')
                if -Decimal(valor.text().replace(',','.',1)).as_tuple().exponent > 2:
                    raise Exception("Valores devem possuir no máximo duas casas decimais!")
                dict['valor'] = valor.text().replace(',','.',1)
                servicos.append(dict)
            elif desc.text() or valor.text():
                raise Exception('Preencha todos os campos de cada serviço!')
        if linhasValidas==0:
            raise Exception('O orçamento precisa de pelo menos um serviço realizado!')
        return servicos

    def getDadosOrcamento(self):
        orcamento = {}
        self.lineEditKm.text()
        data = datetime.strptime(self.lineEditData.text(), "%d/%m/%Y")
        if data.date() > datetime.now().date():
            raise Exception('Data do orçamento não deve ser no futuro!')
        data = data.strftime("%Y-%m-%d")
        orcamento['dataOrcamento'] = data
        if self.lineEditKm.text():
            if self.lineEditKm.text() > '0' and self.lineEditKm.text().isnumeric():
                orcamento['km'] = self.lineEditKm.text()
            else: raise Exception("Quilometragem do veículo inválida!")
        else: raise Exception("Quilometragem do veículo obrigatória!")
        orcamento['observacoes']=self.textEdit.toPlainText()
        return orcamento

    def setValor(self):
        self.valorTotal=0.00
        for _,qtde,_,valor in self.linhasPeca:
            if not valor.text():
                continue
            if not (valor.text().replace(',','',1).isnumeric() or valor.text().replace('.','',1).isnumeric()):
                self.labelValorTotal2.setText('0,00')
                return
            if qtde.text():
                if not (qtde.text().replace(',','',1).isnumeric() or qtde.text().replace('.','',1).isnumeric()):
                    self.labelValorTotal2.setText('0,00')
                    return 
                self.valorTotal+=float(valor.text().replace(',','.',1))*float(qtde.text().replace(',','.',1))
            else:
                self.valorTotal+=float(valor.text().replace(',','.',1))

        for _,qtde,valor in self.linhasServico:
            if not valor.text():
                continue
            if not (valor.text().replace(',','',1).isnumeric() or valor.text().replace('.','',1).isnumeric()):
                self.labelValorTotal2.setText('0,00')
                return
            if qtde.text():
                if not (qtde.text().replace(',','',1).isnumeric() or qtde.text().replace('.','',1).isnumeric()):
                    self.labelValorTotal2.setText('0,00')
                    return 
                self.valorTotal+=float(valor.text().replace(',','.',1))*float(qtde.text().replace(',','.',1))
            else:
                self.valorTotal+=float(valor.text().replace(',','.',1))
        self.labelValorTotal2.setText(('{:.2f}'.format(self.valorTotal)).replace('.',',',1))

    def buscarPeca(self, lineEditDesc, comboBoxUn, lineEditValor):
        qPeca = self.pecaCtrl.getPecaByDescricao(lineEditDesc.text())
        if qPeca:
            comboBoxUn.setCurrentText(qPeca['un'])
            lineEditValor.setText('{:.2f}'.format(qPeca['valor']).replace('.',',',1))
            self.setValor()

    def buscarServico(self, lineEditDesc, lineEditValor):
        qServico = self.servicoCtrl.getServicoByDescricao(lineEditDesc.text())
        if qServico:
            lineEditValor.setText('{:.2f}'.format(qServico['valor']).replace('.',',',1))
            self.setValor()

    def renderEditar(self, id):
        self.resetarTela()
        self.setCompleters()
        self.orcamentoID = id
        orcamento = self.orcamentoCtrl.getOrcamento(id)
        fones = self.clienteCtrl.listarFones(orcamento['cliente']['idCliente'])
        itemPecas = self.orcamentoCtrl.listarItemPecas(orcamento['idOrcamento'])
        itemServicos = self.orcamentoCtrl.listarItemServicos(orcamento['idOrcamento'])
        if itemPecas:
            for item in itemPecas:
                peca = self.pecaCtrl.getPeca(item['peca'])
                item['descricao'] = peca['descricao']
                item['un'] = peca['un']
        if itemServicos:
            for item in itemServicos:
                servico = self.servicoCtrl.getServico(item['servico'])
                item['descricao'] = servico['descricao']
        listaFones = [None, None]
        if fones:
            for x in range(len(fones)):
                listaFones[x] = fones[x]['fone']
        if orcamento['cliente']['cidade'] != None:
            cidade = orcamento['cliente']['cidade']['nome']
            uf = orcamento['cliente']['cidade']['uf']
        else: 
            cidade = None
            uf = None
        self.setCliente(orcamento['cliente']['tipo'], orcamento['cliente']['nome'], orcamento['cliente']['documento'], listaFones[0], listaFones[1])
        self.setEndereco(orcamento['cliente']['cep'], orcamento['cliente']['endereco'], orcamento['cliente']['numero'], orcamento['cliente']['bairro'],
            cidade, uf)
        self.setVeiculo(orcamento['veiculo']['marca']['nome'], orcamento['veiculo']['modelo'], orcamento['veiculo']['placa'], orcamento['veiculo']['ano'])
        if itemPecas:
            self.setPecas(list(itemPecas))
        self.setServicos(list(itemServicos))
        self.lineEditKm.setText(orcamento['km'])
        self.lineEditData.setDate(orcamento['dataOrcamento'])
        self.textEdit.setText(orcamento['observacoes'])

    # def editarOrcamento(self, id, orcamento:dict, pecas:list, servicos:list):
    def editarOrcamento(self):
        try:
            pecas = self.getPecas()
            servicos  = self.getServicos()
            orcamento = self.getDadosOrcamento()
            orcamento['valorTotal'] = self.valorTotal
            r = self.orcamentoCtrl.editarOrcamento(self.orcamentoID, orcamento, pecas, servicos)
            if isinstance(r, Exception):
                raise Exception(r)
            msg = QtWidgets.QMessageBox()
            msg.setWindowIcon(QtGui.QIcon('resources/logo-icon.png'))
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setWindowTitle("Aviso")
            msg.setText("Orçamento editado com sucesso!")
            msg.exec()
            #RESETA DADOS DA TELA
            self.clienteSelected = None
            self.veiculoSelected = None
            self.valorTotal = 0
            self.orcamentoID = None
            self.paraTelaConsulta.emit(1)
        except Exception as e:
            msg = QtWidgets.QMessageBox()
            msg.setWindowIcon(QtGui.QIcon('resources/logo-icon.png'))
            msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg.setWindowTitle("Erro")
            msg.setText(str(e))
            msg.exec()

    def aprovarOrcamento(self):
        try:
            pecas = self.getPecas()
            servicos  = self.getServicos()
            orcamento = self.getDadosOrcamento()
            orcamento['valorTotal'] = self.valorTotal
            r = self.orcamentoCtrl.editarOrcamento(self.orcamentoID, orcamento, pecas, servicos)
            if isinstance(r, Exception):
                raise Exception(r)
            r = self.orcamentoCtrl.aprovarOrcamento(self.orcamentoID)
            if isinstance(r, Exception):
                raise Exception(r)
            msg = QtWidgets.QMessageBox()
            msg.setWindowIcon(QtGui.QIcon('resources/logo-icon.png'))
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setWindowTitle("Aviso")
            msg.setText("Orçamento editado e aprovado com sucesso!")
            msg.exec()
            self.orcamentoAprovado.emit(1)
        except Exception as e:
            msg = QtWidgets.QMessageBox()
            msg.setWindowIcon(QtGui.QIcon('resources/logo-icon.png'))
            msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg.setWindowTitle("Aviso")
            msg.setText(str(e))
            msg.exec()

    def reprovarOrcamento(self):
        try:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Aviso")
            msgBox.setText('Tem certeza?')
            y = msgBox.addButton("Sim", QtWidgets.QMessageBox.ButtonRole.YesRole)
            n = msgBox.addButton("Não", QtWidgets.QMessageBox.ButtonRole.NoRole)
            y.setFixedWidth(60)
            n.setFixedWidth(60)
            msgBox.exec()
            if msgBox.clickedButton() == y:
                r = self.orcamentoCtrl.reprovarOrcamento(self.orcamentoID)
                if isinstance(r, Exception):
                    raise Exception(r)
                msg = QtWidgets.QMessageBox()
                msg.setWindowIcon(QtGui.QIcon('resources/logo-icon.png'))
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setWindowTitle("Aviso")
                msg.setText("Orçamento reprovado")
                msg.exec()
                self.paraTelaConsulta.emit(1)
        except Exception as e:
            msg = QtWidgets.QMessageBox()
            msg.setWindowIcon(QtGui.QIcon('resources/logo-icon.png'))
            msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg.setWindowTitle("Aviso")
            msg.setText(str(e))
            msg.exec()

    def cancelarEdicao(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Aviso")
        msgBox.setText('Deseja cancelar a edição? Alterações serão perdidas')
        y = msgBox.addButton("Sim", QtWidgets.QMessageBox.ButtonRole.YesRole)
        n = msgBox.addButton("Não", QtWidgets.QMessageBox.ButtonRole.NoRole)
        y.setFixedWidth(60)
        n.setFixedWidth(60)
        msgBox.exec()
        if msgBox.clickedButton() == y:
            self.paraTelaConsulta.emit(1)

    def salvareGerarPDF(self):
        try:
            pecas = self.getPecas()
            servicos  = self.getServicos()
            orcamento = self.getDadosOrcamento()
            orcamento['valorTotal'] = self.valorTotal
            r = self.orcamentoCtrl.editarOrcamento(self.orcamentoID, orcamento, pecas, servicos)
            if isinstance(id, Exception):
                return
            _orcamento = self.orcamentoCtrl.getOrcamento(r['idOrcamento'])
            fones = self.clienteCtrl.listarFones(_orcamento['cliente']['idCliente'])
            if fones: fones = list(fones)
            itemPecas = self.orcamentoCtrl.listarItemPecas(_orcamento['idOrcamento'])
            if itemPecas:
                for item in itemPecas:
                    peca = self.pecaCtrl.getPeca(item['peca'])
                    item['descricao'] = peca['descricao']
                    item['un'] = peca['un']
                itemPecas = list(itemPecas)
            itemServicos = self.orcamentoCtrl.listarItemServicos(_orcamento['idOrcamento'])
            if itemServicos: 
                for item in itemServicos:
                    item['descricao'] = self.servicoCtrl.getServico(item['servico'])['descricao']
                itemServicos = list(itemServicos)
            msg = MessageBox()
            r = msg.question('Deseja salvar o arquivo?')
            if r == 'cancelar':
                msg = QtWidgets.QMessageBox()
                msg.setWindowIcon(QtGui.QIcon('resources/logo-icon.png'))
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setWindowTitle("Aviso")
                msg.setText("Geração do PDF cancelada")
                msg.exec()
            elif r == 'nao':
                pdf = GeraPDF()
                pdf.generatePDF(_orcamento, fones, itemServicos, itemPecas)
            else:
                window = QtWidgets.QMainWindow()
                fd = QtWidgets.QFileDialog()
                path = fd.getExistingDirectory(window, 'Salvar como', './')
                if path == '':
                    return
                pdf = GeraPDF()
                pdf.generatePDF(_orcamento, fones, itemServicos, itemPecas, path)
            self.paraTelaConsulta.emit(1)
        except Exception as e:    
            msg = QtWidgets.QMessageBox()
            msg.setWindowIcon(QtGui.QIcon('resources/logo-icon.png'))
            msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg.setWindowTitle("Erro")
            msg.setText(str(e))
            msg.exec()

    def limparCampos(self):
        for lineedit in self.framedados.findChildren(QtWidgets.QLineEdit):
            lineedit.clear()

    def resetarTela(self):
        while len(self.linhasPeca)>0:
            self.removerLinhaPeca(1)
        while len(self.linhasServico)>0:
            self.removerLinhaServico(1)
        self.limparCampos()
