from PyQt6 import QtCore, QtWidgets, QtGui
from container import handleDeps

from datetime import datetime

from ui.telaBuscaCliente import TelaBuscaCliente
from ui.telaBuscaVeiculo import TelaBuscaVeiculo

SIGLAESTADOS = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS',
                'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
UNIDADES = ['CM', 'CM2', 'CM3', 'CX', 'DZ', 'G', 'KG',
            'L', 'M', 'M2', 'M3', 'ML', 'PAR', 'PCT', 'ROLO', 'UN']


class TelaCadastroOrcamento(QtWidgets.QMainWindow):

    def __init__(self):
        super(TelaCadastroOrcamento, self).__init__()
        self.orcamentoCtrl = handleDeps.getDep('ORCAMENTOCTRL')
        self.clienteCtrl = handleDeps.getDep('CLIENTECTRL')
        self.cidadeCtrl = handleDeps.getDep('CIDADECTRL')
        self.marcaCtrl = handleDeps.getDep('MARCACTRL')
        self.pecaCtrl = handleDeps.getDep('PECACTRL')
        self.servicoCtrl = handleDeps.getDep('SERVICOCTRL')
        self.buscaCEP = handleDeps.getDep('CEP')
        self.clienteSelected = None
        self.veiculoSelected = None
        self.valorTotal = 0
        self.setupUi()

    def setupUi(self):
        self.resize(1280, 760)
        self.main_frame = QtWidgets.QFrame(self)
        self.main_frame.setObjectName("main_frame")
        self.vlayout1 = QtWidgets.QVBoxLayout(self.main_frame)
        # frame titulo
        self.frame_titulo = QtWidgets.QFrame(self.main_frame)
        self.vlayout1.addWidget(self.frame_titulo)
        self.labelTitulo = QtWidgets.QLabel(self.frame_titulo)
        self.labelTitulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelTitulo.setObjectName("titulo")
        self.vlayout1.setContentsMargins(18, 18, 18, 18)
        self.vlayout1.setSpacing(18)
        self.vlayout1.addWidget(self.labelTitulo)
        self.framedados = QtWidgets.QFrame(self.main_frame)
        self.gridLayoutGeral = QtWidgets.QGridLayout(self.framedados)
        self.gridLayoutGeral.setVerticalSpacing(6)
        self.gridLayoutGeral.setHorizontalSpacing(9)
        self.vlayout1.addWidget(self.framedados)
        
        # dados do cliente
        self.groupBoxCliente = QtWidgets.QGroupBox(self.framedados)
        self.gridLayoutCliente = QtWidgets.QGridLayout(self.groupBoxCliente)
        self.framebotoesCliente = QtWidgets.QFrame(self.groupBoxCliente)
        self.gridLayoutCliente.addWidget(self.framebotoesCliente, 0, 0, 1, -1)
        self.hlayout1 = QtWidgets.QHBoxLayout(self.framebotoesCliente)
        self.hlayout1.setContentsMargins(0, 0, 0, 0)
        self.botaobuscarCliente = QtWidgets.QPushButton(self.framebotoesCliente)
        self.botaobuscarCliente.setFixedWidth(200)
        self.hlayout1.addWidget(self.botaobuscarCliente)
        self.checkboxNovoCliente = QtWidgets.QCheckBox(self.framebotoesCliente)
        self.checkboxNovoCliente.setFixedWidth(150)
        self.checkboxNovoCliente.setChecked(True)
        self.hlayout1.addWidget(self.checkboxNovoCliente)
        self.hlayout1.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.labelPessoa = QtWidgets.QLabel(self.groupBoxCliente)
        self.gridLayoutCliente.addWidget(self.labelPessoa, 1, 0, 1, 1)
        self.labelDocumento = QtWidgets.QLabel(self.groupBoxCliente)
        self.gridLayoutCliente.addWidget(self.labelDocumento, 1, 1, 1, 1)
        self.labelNome = QtWidgets.QLabel(self.groupBoxCliente)
        self.gridLayoutCliente.addWidget(self.labelNome, 1, 2, 1, 1)
        self.labelFone1 = QtWidgets.QLabel(self.groupBoxCliente)
        self.gridLayoutCliente.addWidget(self.labelFone1, 1, 4, 1, 1)
        self.labelFone2 = QtWidgets.QLabel(self.groupBoxCliente)
        self.gridLayoutCliente.addWidget(self.labelFone2, 1, 5, 1, 1)
        self.comboBoxPessoa = QtWidgets.QComboBox(self.groupBoxCliente)
        self.comboBoxPessoa.addItems(["PESSOA FÍSICA", "PESSOA JURÍDICA", "ESTRANGEIRO"])
        self.gridLayoutCliente.addWidget(self.comboBoxPessoa, 2, 0, 1, 1)
        self.lineEditDocumento = QtWidgets.QLineEdit(self.groupBoxCliente)
        self.gridLayoutCliente.addWidget(self.lineEditDocumento, 2, 1, 1, 1)
        self.lineEditNomeCliente = QtWidgets.QLineEdit(self.groupBoxCliente)
        self.gridLayoutCliente.addWidget(self.lineEditNomeCliente, 2, 2, 1, 2)
        self.lineEditFone1 = QtWidgets.QLineEdit(self.groupBoxCliente)
        self.gridLayoutCliente.addWidget(self.lineEditFone1, 2, 4, 1, 1)
        self.lineEditFone2 = QtWidgets.QLineEdit(self.groupBoxCliente)
        self.gridLayoutCliente.addWidget(self.lineEditFone2, 2, 5, 1, 1)
        self.labelCEP = QtWidgets.QLabel(self.groupBoxCliente)
        self.gridLayoutCliente.addWidget(self.labelCEP, 3, 0, 1, 1)
        self.labelEnder = QtWidgets.QLabel(self.groupBoxCliente)
        self.gridLayoutCliente.addWidget(self.labelEnder, 3, 1, 1, 1)
        self.labelNumero = QtWidgets.QLabel(self.groupBoxCliente)
        self.gridLayoutCliente.addWidget(self.labelNumero, 3, 3, 1, 1)
        self.labelBairro = QtWidgets.QLabel(self.groupBoxCliente)
        self.gridLayoutCliente.addWidget(self.labelBairro, 3, 4, 1, 1)
        self.labelCidade = QtWidgets.QLabel(self.groupBoxCliente)
        self.gridLayoutCliente.addWidget(self.labelCidade, 3, 5, 1, 1)
        self.labelUF = QtWidgets.QLabel(self.groupBoxCliente)
        self.gridLayoutCliente.addWidget(self.labelUF, 3, 6, 1, 1)
        self.lineEditCEP = QtWidgets.QLineEdit(self.groupBoxCliente)
        self.gridLayoutCliente.addWidget(self.lineEditCEP, 4, 0, 1, 1)
        self.lineEditEnder = QtWidgets.QLineEdit(self.groupBoxCliente)
        self.gridLayoutCliente.addWidget(self.lineEditEnder, 4, 1, 1, 2)
        self.lineEditNumero = QtWidgets.QLineEdit(self.groupBoxCliente)
        self.gridLayoutCliente.addWidget(self.lineEditNumero, 4, 3, 1, 1)
        self.lineEditBairro = QtWidgets.QLineEdit(self.groupBoxCliente)
        self.gridLayoutCliente.addWidget(self.lineEditBairro, 4, 4, 1, 1)
        self.lineEditCidade = QtWidgets.QLineEdit(self.groupBoxCliente)
        self.gridLayoutCliente.addWidget(self.lineEditCidade, 4, 5, 1, 1)
        self.comboBoxuf = QtWidgets.QComboBox(self.groupBoxCliente)
        self.comboBoxuf.addItems(SIGLAESTADOS)
        self.comboBoxuf.setCurrentIndex(15)
        self.gridLayoutCliente.addWidget(self.comboBoxuf, 4, 6, 1, 1)
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
        self.framebotoesVeiculo = QtWidgets.QFrame(self.groupBoxCliente)
        self.gridLayoutVeiculo.addWidget(self.framebotoesVeiculo, 0, 0, 1, -1)
        self.hlayout2 = QtWidgets.QHBoxLayout(self.framebotoesVeiculo)
        self.hlayout2.setContentsMargins(0, 0, 0, 0)
        self.botaoBuscarVeiculo = QtWidgets.QPushButton(self.framebotoesVeiculo)
        self.botaoBuscarVeiculo.setFixedWidth(200)
        self.hlayout2.addWidget(self.botaoBuscarVeiculo)
        self.checkboxNovoVeiculo = QtWidgets.QCheckBox(self.framebotoesVeiculo)
        self.checkboxNovoVeiculo.setFixedWidth(150)
        self.checkboxNovoVeiculo.setChecked(True)
        self.hlayout2.addWidget(self.checkboxNovoVeiculo)
        self.hlayout2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.labelMarca = QtWidgets.QLabel(self.groupBoxVeiculo)
        self.gridLayoutVeiculo.addWidget(self.labelMarca, 1, 0, 1, 1)
        self.labelModelo = QtWidgets.QLabel(self.groupBoxVeiculo)
        self.gridLayoutVeiculo.addWidget(self.labelModelo, 1, 1, 1, 1)
        self.labelPlaca = QtWidgets.QLabel(self.groupBoxVeiculo)
        self.gridLayoutVeiculo.addWidget(self.labelPlaca, 1, 2, 1, 1)
        self.labelAno = QtWidgets.QLabel(self.groupBoxVeiculo)
        self.gridLayoutVeiculo.addWidget(self.labelAno, 1, 3, 1, 1)
        self.labelKm = QtWidgets.QLabel(self.groupBoxVeiculo)
        self.gridLayoutVeiculo.addWidget(self.labelKm, 1, 4, 1, 1)
        self.comboBoxMarca = QtWidgets.QComboBox(self.groupBoxVeiculo)
        self.comboBoxMarca.setEditable(True)
        self.gridLayoutVeiculo.addWidget(self.comboBoxMarca, 2, 0, 1, 1)
        self.lineEditModelo = QtWidgets.QLineEdit(self.groupBoxVeiculo)
        self.gridLayoutVeiculo.addWidget(self.lineEditModelo, 2, 1, 1, 1)
        self.lineEditPlaca = QtWidgets.QLineEdit(self.groupBoxVeiculo)
        self.gridLayoutVeiculo.addWidget(self.lineEditPlaca, 2, 2, 1, 1)
        self.lineEditAno = QtWidgets.QLineEdit(self.groupBoxVeiculo)
        self.gridLayoutVeiculo.addWidget(self.lineEditAno, 2, 3, 1, 1)
        self.lineEditKm = QtWidgets.QLineEdit(self.groupBoxVeiculo)
        self.gridLayoutVeiculo.addWidget(self.lineEditKm, 2, 4, 1, 1)
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
        self.labelQtde = QtWidgets.QLabel(self.framegroupboxpecas)
        self.gridLayoutPecas.addWidget(self.labelQtde, 0, 1, 1, 1)
        self.labelUn = QtWidgets.QLabel(self.framegroupboxpecas)
        self.gridLayoutPecas.addWidget(self.labelUn, 0, 2, 1, 1)
        self.labelValorPeca = QtWidgets.QLabel(self.framegroupboxpecas)
        self.gridLayoutPecas.addWidget(self.labelValorPeca, 0, 3, 1, 1)
        self.lineEditNomePeca = QtWidgets.QLineEdit(self.framegroupboxpecas)
        self.gridLayoutPecas.addWidget(self.lineEditNomePeca, 1, 0, 1, 1)
        self.lineEditQtdeP = QtWidgets.QLineEdit(self.framegroupboxpecas)
        self.gridLayoutPecas.addWidget(self.lineEditQtdeP, 1, 1, 1, 1)
        self.comboBoxUn = QtWidgets.QComboBox(self.framegroupboxpecas)
        self.comboBoxUn.addItems(UNIDADES)
        self.comboBoxUn.setMinimumWidth(50)
        self.comboBoxUn.setCurrentIndex(15)
        self.gridLayoutPecas.addWidget(self.comboBoxUn, 1, 2, 1, 1)
        self.lineEditValorPeca = QtWidgets.QLineEdit(self.framegroupboxpecas)
        self.gridLayoutPecas.addWidget(self.lineEditValorPeca, 1, 3, 1, 1)
        self.botaoAddPecas = QtWidgets.QPushButton(self.framegroupboxpecas)
        self.botaoAddPecas.setToolTip('Adicionar linha')
        self.gridLayoutPecas.addWidget(self.botaoAddPecas, 1, 4, 1, 1)
        self.linhasPeca = [
            [self.lineEditNomePeca, self.lineEditQtdeP, self.comboBoxUn, self.lineEditValorPeca]]
        self.spacerpeca = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayoutPecas.addItem(self.spacerpeca, 2, 0, 1, 1)
        self.gridLayoutGeral.addWidget(self.groupBoxPecas, 3, 0, 1, 1)
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
        self.labelQtdeS = QtWidgets.QLabel(self.framegroupboxservicos)
        self.gridLayoutServicos.addWidget(self.labelQtdeS, 0, 1, 1, 1)
        self.labelValorServico = QtWidgets.QLabel(self.framegroupboxservicos)
        self.gridLayoutServicos.addWidget(self.labelValorServico, 0, 2, 1, 1)
        self.lineEditNomeServico = QtWidgets.QLineEdit(self.framegroupboxservicos)
        self.gridLayoutServicos.addWidget(self.lineEditNomeServico, 1, 0, 1, 1)
        self.lineEditQtdeS = QtWidgets.QLineEdit(self.framegroupboxservicos)
        self.gridLayoutServicos.addWidget(self.lineEditQtdeS, 1, 1, 1, 1)
        self.lineEditValorServico = QtWidgets.QLineEdit(self.framegroupboxservicos)
        self.gridLayoutServicos.addWidget(self.lineEditValorServico, 1, 2, 1, 1)
        self.botaoAddServicos = QtWidgets.QPushButton(self.framegroupboxservicos)
        self.botaoAddServicos.setToolTip('Adicionar linha')
        self.gridLayoutServicos.addWidget(self.botaoAddServicos, 1, 3, 1, 1)
        self.linhasServico = [[self.lineEditNomeServico, self.lineEditQtdeS, self.lineEditValorServico]]
        self.spacerservico = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayoutServicos.addItem(self.spacerservico, 2, 0, 1, 1)
        self.gridLayoutGeral.addWidget(self.groupBoxServicos, 3, 1, 1, 1)
        self.gridLayoutServicos.setColumnStretch(0, 6)
        self.gridLayoutServicos.setColumnStretch(1, 1)
        self.gridLayoutServicos.setColumnStretch(2, 1)
        #dados orcamento
        self.groupBoxOrcamento = QtWidgets.QGroupBox(self.framedados)
        self.gridLayoutOrcamento = QtWidgets.QGridLayout(self.groupBoxOrcamento)
        self.labelData = QtWidgets.QLabel(self.groupBoxOrcamento)
        self.lineEditData = QtWidgets.QDateEdit(self.groupBoxOrcamento)
        self.lineEditData.setFixedWidth(125)
        self.lineEditData.setCalendarPopup(True)
        self.lineEditData.setDateTime(QtCore.QDateTime.currentDateTime())
        self.gridLayoutOrcamento.addWidget(self.labelData, 0, 0, 1, 1)
        self.gridLayoutOrcamento.addWidget(self.lineEditData, 1, 0, 1, 1)
        spacer = QtWidgets.QSpacerItem(20,20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayoutOrcamento.addItem(spacer, 0, 1, 1, 1)
        self.labelValorTotal1 = QtWidgets.QLabel(self.groupBoxOrcamento)
        #self.labelValorTotal1.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelValorTotal1.setObjectName('boldText')
        self.labelValorTotal2 = QtWidgets.QLabel(self.groupBoxOrcamento)
        #self.labelValorTotal2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelValorTotal2.setObjectName('boldText')
        self.labelValorTotal2.setText('0,00')
        self.gridLayoutOrcamento.addWidget(self.labelValorTotal1, 0, 2, -1, 1)
        self.gridLayoutOrcamento.addWidget(self.labelValorTotal2, 0, 3, -1, 1)
        self.gridLayoutGeral.addWidget(self.groupBoxOrcamento, 4, 0, 1, -1)
        # campo de observações
        self.groupBoxObs = QtWidgets.QGroupBox(self.framedados)
        self.vlayout2 = QtWidgets.QVBoxLayout(self.groupBoxObs)
        self.textEdit = QtWidgets.QTextEdit(self.groupBoxObs)
        self.groupBoxObs.setMaximumHeight(90)
        self.vlayout2.addWidget(self.textEdit)
        self.gridLayoutGeral.setColumnStretch(0,1)
        self.gridLayoutGeral.setColumnStretch(1,1)
        self.gridLayoutGeral.addWidget(self.groupBoxObs, 5, 0, 1, -1)
        self.gridLayoutGeral.setRowStretch(3, 10)
        # botoes
        self.framebotoes = QtWidgets.QFrame(self.main_frame)
        self.hlayout4 = QtWidgets.QHBoxLayout(self.framebotoes)
        self.labelLegenda = QtWidgets.QLabel(self.framebotoes)
        self.hlayout4.addWidget(self.labelLegenda)
        spacerItem5 = QtWidgets.QSpacerItem(
            40, 10, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.hlayout4.addItem(spacerItem5)
        self.botaoSalvar = QtWidgets.QPushButton(self.framebotoes)
        self.botaoSalvar.setMinimumSize(QtCore.QSize(100, 30))
        self.botaoSalvar.setObjectName('botaoprincipal')
        self.hlayout4.addWidget(self.botaoSalvar)
        self.botaoSalvareGerarPDF = QtWidgets.QPushButton(self.framebotoes)
        self.botaoSalvareGerarPDF.setMinimumSize(QtCore.QSize(150, 30))
        self.hlayout4.addWidget(self.botaoSalvareGerarPDF)
        self.botaolimpar = QtWidgets.QPushButton(self.framebotoes)
        self.botaolimpar.setMinimumSize(QtCore.QSize(100, 30))
        self.hlayout4.addWidget(self.botaolimpar)
        self.hlayout4.setContentsMargins(9, 9, 9, 9)
        self.vlayout1.addWidget(self.framebotoes)
        self.setCentralWidget(self.main_frame)
        self.completerPeca = QtWidgets.QCompleter([])
        self.completerPeca.setMaxVisibleItems(5)
        self.completerPeca.setCaseSensitivity(
            QtCore.Qt.CaseSensitivity.CaseInsensitive)
        self.completerPeca.setCompletionMode(
            QtWidgets.QCompleter.CompletionMode.PopupCompletion)
        self.lineEditNomePeca.setCompleter(self.completerPeca)
        self.completerServico = QtWidgets.QCompleter([])
        self.completerServico.setMaxVisibleItems(5)
        self.completerServico.setCaseSensitivity(
            QtCore.Qt.CaseSensitivity.CaseInsensitive)
        self.completerServico.setCompletionMode(
            QtWidgets.QCompleter.CompletionMode.PopupCompletion)
        self.lineEditNomeServico.setCompleter(self.completerServico)

        self.completerCidade = QtWidgets.QCompleter([])
        self.completerCidade.setMaxVisibleItems(5)
        self.completerCidade.setCaseSensitivity(
            QtCore.Qt.CaseSensitivity.CaseInsensitive)
        self.completerCidade.setCompletionMode(
            QtWidgets.QCompleter.CompletionMode.PopupCompletion)
        self.lineEditCidade.setCompleter(self.completerCidade)

        self.retranslateUi()
        self.setMarcas()
        self.setCompleters()
        self.botaoAddPecas.clicked.connect(self.addLinhaPeca)
        self.botaoAddServicos.clicked.connect(self.addLinhaServico)
        self.botaobuscarCliente.clicked.connect(self.telaBuscaCliente)
        self.botaoBuscarVeiculo.clicked.connect(self.telaBuscaVeiculo)
        self.lineEditCEP.editingFinished.connect(self.buscarDadosCEP)
        self.botaolimpar.clicked.connect(self.resetarTela)
        self.botaoSalvar.clicked.connect(self.salvarOrcamento)
        self.botaoSalvareGerarPDF.clicked.connect(self.gerarPDF)
        self.comboBoxPessoa.currentIndexChanged.connect(self.escolherTipoPessoa)
        self.lineEditNomePeca.textChanged.connect(lambda: self.buscarPeca(self.lineEditNomePeca,self.comboBoxUn, self.lineEditValorPeca))
        self.lineEditNomeServico.textChanged.connect(lambda: self.buscarServico(self.lineEditNomeServico,self.lineEditValorServico))
        self.lineEditQtdeP.textChanged.connect(self.setValor)
        self.lineEditQtdeS.textChanged.connect(self.setValor)
        self.lineEditValorPeca.textChanged.connect(self.setValor)
        self.lineEditValorServico.textChanged.connect(self.setValor)
        self.checkboxNovoCliente.stateChanged.connect(self.verificarCamposCliente)
        self.checkboxNovoVeiculo.stateChanged.connect(self.verificarCamposVeiculo)

    ##############################################################################################################################
                                                            #FUNÇÕES
    ##############################################################################################################################

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Mecânica Pasetto"))
        self.botaoSalvareGerarPDF.setText(_translate("MainWindow", "Salvar e Imprimir"))
        self.botaoSalvar.setText(_translate("MainWindow", "Salvar"))
        self.botaolimpar.setText(_translate("MainWindow", "Limpar"))
        self.labelTitulo.setText(_translate("MainWindow", "Orçamentos"))
        self.labelData.setText(_translate("MainWindow", "Data do Orçamento"))
        self.groupBoxOrcamento.setTitle(_translate("MainWindow", "Dados do Orçamento"))
        self.groupBoxCliente.setTitle(_translate("MainWindow", "Dados do Cliente"))
        self.botaobuscarCliente.setText(_translate("MainWindow", "Selecionar Cliente"))
        self.checkboxNovoCliente.setText(_translate("MainWindow", "Novo Cliente"))
        self.labelNome.setText(_translate("MainWindow", "Nome*"))
        self.labelCEP.setText(_translate("MainWindow", "CEP"))
        self.labelPessoa.setText(_translate("MainWindow", "Pessoa"))
        self.labelDocumento.setText(_translate("MainWindow", "CPF"))
        self.labelUF.setText(_translate("MainWindow", "UF"))
        self.labelCidade.setText(_translate("MainWindow", "Cidade"))
        self.labelEnder.setText(_translate("MainWindow", "Endereço"))
        self.labelNumero.setText(_translate("MainWindow", "Número"))
        self.labelBairro.setText(_translate("MainWindow", "Bairro"))
        self.labelFone1.setText(_translate("MainWindow", "Fone 1*"))
        self.labelFone2.setText(_translate("MainWindow", "Fone 2"))
        self.groupBoxVeiculo.setTitle(_translate("MainWindow", "Dados do veículo"))
        self.botaoBuscarVeiculo.setText(_translate("MainWindow", "Selecionar Veículo"))
        self.checkboxNovoVeiculo.setText(_translate("MainWindow", "Novo Veículo"))
        self.labelMarca.setText(_translate("MainWindow", "Marca*"))
        self.labelPlaca.setText(_translate("MainWindow", "Placa*"))
        self.labelAno.setText(_translate("MainWindow", "Ano"))
        self.labelModelo.setText(_translate("MainWindow", "Modelo*"))
        self.labelKm.setText(_translate("MainWindow", "Km*"))
        self.groupBoxServicos.setTitle(_translate("MainWindow", "Serviços"))
        self.botaoAddServicos.setText(_translate("MainWindow", "+"))
        self.labelValorServico.setText(_translate("MainWindow", "Valor un.*"))
        self.labelNomeServico.setText(_translate("MainWindow", "Serviço*"))
        self.labelQtdeS.setText(_translate("MainWindow", "Qtde*"))
        self.groupBoxObs.setTitle(_translate("MainWindow", "Observações (Max. 200 caracteres)"))
        self.groupBoxPecas.setTitle(_translate("MainWindow", "Peças"))
        self.labelQtde.setText(_translate("MainWindow", "Qtde*"))
        self.labelUn.setText(_translate("MainWindow", "Un*"))
        self.botaoAddPecas.setText(_translate("MainWindow", "+"))
        self.labelNomePeca.setText(_translate("MainWindow", "Peça*"))
        self.labelValorPeca.setText(_translate("MainWindow", "Valor un.*"))
        self.labelLegenda.setText(_translate("MainWindow", "* Campos Obrigatórios"))
        self.labelValorTotal1.setText(_translate("MainWindow", "VALOR TOTAL: R$"))

    def addLinhaPeca(self):
        label1 = QtWidgets.QLabel(text="Peça*")
        label2 = QtWidgets.QLabel(text="Qtde*")
        label3 = QtWidgets.QLabel(text="Un*")
        label4 = QtWidgets.QLabel(text="Valor un.*")
        lineedit1 = QtWidgets.QLineEdit()
        lineedit1.setCompleter(self.completerPeca)
        lineedit2 = QtWidgets.QLineEdit()
        comboBox = QtWidgets.QComboBox()
        comboBox.addItems(UNIDADES)
        comboBox.setCurrentIndex(15)
        lineedit4 = QtWidgets.QLineEdit()
        botaoRemoverLinha = QtWidgets.QPushButton()
        botaoRemoverLinha.setToolTip('Remover linha')
        botaoRemoverLinha.setText("-")
        botaoRemoverLinha.setObjectName('excluir')
        self.gridLayoutPecas.addWidget(label1, len(self.linhasPeca)*2, 0, 1, 1)
        self.gridLayoutPecas.addWidget(label2, len(self.linhasPeca)*2, 1, 1, 1)
        self.gridLayoutPecas.addWidget(label3, len(self.linhasPeca)*2, 2, 1, 1)
        self.gridLayoutPecas.addWidget(label4, len(self.linhasPeca)*2, 3, 1, 1)
        self.gridLayoutPecas.addWidget(lineedit1, len(self.linhasPeca)*2+1, 0, 1, 1)
        self.gridLayoutPecas.addWidget(lineedit2, len(self.linhasPeca)*2+1, 1, 1, 1)
        self.gridLayoutPecas.addWidget(comboBox, len(self.linhasPeca)*2+1, 2, 1, 1)
        self.gridLayoutPecas.addWidget(lineedit4, len(self.linhasPeca)*2+1, 3, 1, 1)
        self.gridLayoutPecas.addWidget(botaoRemoverLinha, len(self.linhasPeca)*2+1, 4, 1, 1)
        self.linhasPeca.append([lineedit1, lineedit2, comboBox, lineedit4])
        self.gridLayoutPecas.removeItem(self.spacerpeca)
        self.gridLayoutPecas.addItem(self.spacerpeca, len(self.linhasPeca)*2, 0, 1, 1)
        lineedit2.textChanged.connect(self.setValor)
        lineedit4.textChanged.connect(self.setValor)
        lineedit1.textChanged.connect(lambda: self.buscarPeca(lineedit1, comboBox, lineedit4))
        botaoRemoverLinha.clicked.connect(lambda: self.removerLinhaPeca(self.gridLayoutPecas.getItemPosition(self.gridLayoutPecas.indexOf(botaoRemoverLinha))[0]))

    def removerLinhaPeca(self, linha):
        for x in range(4):
            w1 = self.gridLayoutPecas.itemAtPosition(linha-1, x).widget()
            w1.hide()
            w1.setParent(None)
            w1.deleteLater()
            w2 = self.gridLayoutPecas.itemAtPosition(linha, x).widget()
            w2.hide()
            w2.setParent(None)
            w2.deleteLater()
        w = self.gridLayoutPecas.itemAtPosition(linha, 4).widget()
        w.hide()
        w.setParent(None)
        w.deleteLater()
        for x in range(self.gridLayoutPecas.rowCount()):
            if x > linha:
                for y in range(5):
                    if not isinstance(self.gridLayoutPecas.itemAtPosition(x, y), QtWidgets.QSpacerItem) and self.gridLayoutPecas.itemAtPosition(x, y) != None:
                        self.gridLayoutPecas.addWidget(self.gridLayoutPecas.itemAtPosition(x, y).widget(), x-2, y, 1, 1)
        del self.linhasPeca[int((linha-1)/2)]
        self.gridLayoutPecas.removeItem(self.spacerpeca)
        self.gridLayoutPecas.addItem(self.spacerpeca, len(self.linhasPeca)*2, 0, 1, 1)

    def addLinhaServico(self):
        label1 = QtWidgets.QLabel(text="Serviço*")
        label2 = QtWidgets.QLabel(text="Qtde*")
        label3 = QtWidgets.QLabel(text="Valor un.*")
        lineedit1 = QtWidgets.QLineEdit()
        lineedit1.setCompleter(self.completerServico)
        lineedit2 = QtWidgets.QLineEdit()
        lineedit3 = QtWidgets.QLineEdit()
        botaoRemoverLinha = QtWidgets.QPushButton()
        botaoRemoverLinha.setToolTip('Remover linha')
        botaoRemoverLinha.setText("-")
        botaoRemoverLinha.setObjectName('excluir')
        self.gridLayoutServicos.addWidget(label1, len(self.linhasServico)*2, 0, 1, 1)
        self.gridLayoutServicos.addWidget(label2, len(self.linhasServico)*2, 1, 1, 1)
        self.gridLayoutServicos.addWidget(label3, len(self.linhasServico)*2, 2, 1, 1)
        self.gridLayoutServicos.addWidget(lineedit1, len(self.linhasServico)*2+1, 0, 1, 1)
        self.gridLayoutServicos.addWidget(lineedit2, len(self.linhasServico)*2+1, 1, 1, 1)
        self.gridLayoutServicos.addWidget(lineedit3, len(self.linhasServico)*2+1, 2, 1, 1)
        self.gridLayoutServicos.addWidget(botaoRemoverLinha, len(self.linhasServico)*2+1, 3, 1, 1)
        self.linhasServico.append([lineedit1, lineedit2, lineedit3])
        self.gridLayoutServicos.removeItem(self.spacerservico)
        self.gridLayoutServicos.addItem(self.spacerservico, len(self.linhasServico)*2, 0, 1, 1)
        lineedit2.textChanged.connect(self.setValor)
        lineedit3.textChanged.connect(self.setValor)
        lineedit1.textChanged.connect(lambda: self.buscarServico(lineedit1, lineedit3))
        botaoRemoverLinha.clicked.connect(lambda: self.removerLinhaServico(self.gridLayoutServicos.getItemPosition(self.gridLayoutServicos.indexOf(botaoRemoverLinha))[0]))

    def removerLinhaServico(self, linha):
        for x in range(3):
            w1 = self.gridLayoutServicos.itemAtPosition(linha-1, x).widget()
            w1.hide()
            w1.setParent(None)
            w1.deleteLater()
            w2 = self.gridLayoutServicos.itemAtPosition(linha, x).widget()
            w2.hide()
            w2.setParent(None)
            w2.deleteLater()
        w = self.gridLayoutServicos.itemAtPosition(linha, 3).widget()
        w.hide()
        w.setParent(None)
        w.deleteLater()
        for x in range(self.gridLayoutServicos.rowCount()):
            if x > linha:
                for y in range(4):
                    if not isinstance(self.gridLayoutServicos.itemAtPosition(x, y), QtWidgets.QSpacerItem) and self.gridLayoutServicos.itemAtPosition(x, y) != None:
                        self.gridLayoutServicos.addWidget(self.gridLayoutServicos.itemAtPosition(x, y).widget(), x-2, y, 1, 1)
        del self.linhasServico[int((linha-1)/2)]
        self.gridLayoutServicos.removeItem(self.spacerservico)
        self.gridLayoutServicos.addItem(self.spacerservico, len(self.linhasServico)*2, 0, 1, 1)

    def limparDadosCliente(self):
        self.lineEditNomeCliente.clear()
        self.lineEditDocumento.clear()
        self.lineEditCEP.clear()
        self.lineEditEnder.clear()
        self.lineEditNumero.clear()
        self.lineEditBairro.clear()
        self.lineEditCidade.clear()
        self.lineEditFone1.clear()
        self.lineEditFone2.clear()

    def limparDadosVeiculo(self):
        self.comboBoxMarca.setCurrentIndex(-1)
        self.lineEditModelo.clear()
        self.lineEditAno.clear()
        self.lineEditPlaca.clear()
        self.lineEditKm.clear()

    def verificarCamposCliente(self):
        if self.checkboxNovoCliente.isChecked():
            self.limparDadosCliente()
            self.clienteSelected = None

    def verificarCamposVeiculo(self):
        if self.checkboxNovoVeiculo.isChecked():
            self.limparDadosVeiculo()
            self.veiculoSelected = None

    def escolherTipoPessoa(self):
        if (self.comboBoxPessoa.currentIndex() == 0):
            self.labelDocumento.setText('CPF')
        elif (self.comboBoxPessoa.currentIndex() == 1):
            self.labelDocumento.setText('CNPJ')
        else: self.labelDocumento.setText('Documento')

    def setCliente(self, tipo, nome, documento=None, tel1=None, tel2=None):
        self.lineEditNomeCliente.setText(nome)
        if documento:
            self.lineEditDocumento.setText(documento)
            if tipo == '0':
                self.labelDocumento.setText("CPF")
            if tipo == '1':
                self.labelDocumento.setText("CNPJ")
            if tipo == '1':
                self.labelDocumento.setText("Documento")
            self.comboBoxPessoa.setCurrentIndex(int(tipo))
        else: self.lineEditDocumento.setText('')
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

    def setMarcas(self):
        self.comboBoxMarca.clear()
        marcas = self.marcaCtrl.listarMarcas()
        for marca in marcas:
            self.comboBoxMarca.addItem(marca['nome'])
        self.comboBoxMarca.setCurrentIndex(-1)

    def setCompleters(self):
        pecas = self.pecaCtrl.listarPecas()
        servicos = self.servicoCtrl.listarServicos()
        cidades = self.cidadeCtrl.listarCidades()
        listaPecas = []
        listaServicos = []
        listaCidades = []
        if pecas:
            for peca in pecas:
                listaPecas.append(peca['descricao'])
        if servicos:
            for servico in servicos:
                listaServicos.append(servico['descricao'])
        if cidades:
            for cidade in cidades:
                listaCidades.append(cidade['nome'])
        modelPecas = QtCore.QStringListModel()
        modelPecas.setStringList(listaPecas)
        self.completerPeca.setModel(modelPecas)
        modelServicos = QtCore.QStringListModel()
        modelServicos.setStringList(listaServicos)
        self.completerServico.setModel(modelServicos)
        modelCidades = QtCore.QStringListModel()
        modelCidades.setStringList(listaCidades)
        self.completerCidade.setModel(modelCidades)

    def getDadosCliente(self):
        dict = {}
        dict['tipo'] = self.comboBoxPessoa.currentIndex()
        if (self.lineEditDocumento.text()):
            if dict['tipo'] == 0:
                documento = 'CPF'
                if len(self.lineEditDocumento.text()) != 11:
                    raise Exception('CPF inválido')
            elif dict['tipo'] == 1:
                documento = 'CNPJ'
                if len(self.lineEditDocumento.text()) != 14:
                    raise Exception('CNPJ inválido')
            else: documento = 'Documento'
            if not self.lineEditDocumento.text().isnumeric():
                raise Exception(f'Digite apenas números no campo {documento}')
            dict['documento'] = self.lineEditDocumento.text()
        else:
            dict['documento'] = None
        if (self.lineEditNomeCliente.text()):
            dict['nome'] = self.lineEditNomeCliente.text().title()
        else:
            raise Exception("Nome do cliente obrigatório")
        if (self.lineEditCEP.text()):
            if len(self.lineEditCEP.text()) != 8 or not self.lineEditCEP.text().isdigit():
                raise Exception("CEP inválido")
            dict['cep'] = self.lineEditCEP.text()
        else:
            dict['cep'] = None
        if (self.lineEditEnder.text()):
            dict['endereco'] = self.lineEditEnder.text()
        else:
            dict['endereco'] = None
        if (self.lineEditNumero.text()):
            if self.lineEditNumero.text().isdigit:
                dict['numero'] = self.lineEditNumero.text()
            else: raise Exception('Número inválido!')
        else:
            dict['numero'] = None
        if (self.lineEditBairro.text()):
            dict['bairro'] = self.lineEditBairro.text()
        else:
            dict['bairro'] = None
        if (self.lineEditCidade.text()):
            dict['cidade'] = self.lineEditCidade.text().title()
        else:
            dict['cidade'] = None
        dict['uf'] = self.comboBoxuf.currentText()
        return dict

    def getFones(self):
        listaFones = []
        fones = 0
        if (self.lineEditFone1.text()):
            listaFones.append(self.lineEditFone1.text())
            fones+=1
        else:
            listaFones.append(None)
        if (self.lineEditFone2.text()):
            listaFones.append(self.lineEditFone2.text())
            fones+=1
        else:
            listaFones.append(None)
        if fones==0:
            raise Exception("Fone obrigatório!")
        return listaFones

    def getDadosVeiculo(self):
        dict = {}
        if self.comboBoxMarca.currentText():
            dict['marca'] = self.comboBoxMarca.currentText().title()
        else: raise Exception("Campo 'Marca' obrigatório!")
        if (self.lineEditModelo.text()):
            dict['modelo'] = self.lineEditModelo.text()[0].upper() + self.lineEditModelo.text()[1:]
        else: raise Exception("Campo 'Modelo' obrigatório!")
        if (self.lineEditPlaca.text()):
            dict['placa'] = self.lineEditPlaca.text().upper()
        else: raise Exception("Campo 'Placa' obrigatório!")
        if (self.lineEditAno.text()):
            dict['ano'] = self.lineEditAno.text()
        else: dict['ano'] = None
        return dict

    def getPecas(self):
        pecas = []
        for desc, qtde, un, valor in self.linhasPeca:
            if desc.text() and valor.text():
                dict = {}
                dict['descricao'] = desc.text()
                if not qtde.text(): dict['qtde'] = 1
                else:
                    if not (qtde.text().replace(',','',1).isnumeric() or qtde.text().replace('.','',1).isnumeric()):
                        raise Exception("Campo 'qtde' inválido!")
                    dict['qtde'] = qtde.text().replace(',','.',1)
                dict['un'] = un.currentText()
                if not (valor.text().replace(',','',1).isnumeric() or valor.text().replace('.','',1).isnumeric()):
                    raise Exception("Campo 'valor' inválido!")
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
                    if not (qtde.text().replace(',','',1).isnumeric() or qtde.text().replace('.','',1).isnumeric()):
                        raise Exception("Campo 'qtde' inválido!")
                    dict['qtde'] = qtde.text().replace(',','.',1)
                if not (valor.text().replace(',','',1).isnumeric() or valor.text().replace('.','',1).isnumeric()):
                    raise Exception("Campo 'valor' inválido!")
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
        data = data.strftime("%Y-%m-%d")
        orcamento['dataOrcamento'] = data
        if self.lineEditKm.text():
            orcamento['km'] = self.lineEditKm.text()
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

    def salvarOrcamento(self):
        try:
            cliente = self.getDadosCliente()
            fones = self.getFones()
            veiculo = self.getDadosVeiculo()
            pecas = self.getPecas()
            servicos  = self.getServicos()
            orcamento = self.getDadosOrcamento()
            orcamento['valorTotal'] = round(self.valorTotal, 2)
            r = self.orcamentoCtrl.salvarOrcamento(cliente, fones, self.clienteSelected, veiculo, self.veiculoSelected, orcamento, pecas, servicos)
            if isinstance(r, Exception):
                raise Exception(r)
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Aviso")
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setText("Orçamento criado com sucesso!")
            msg.exec()
            #RESETA DADOS DA TELA
            self.clienteSelected = None
            self.veiculoSelected = None
            self.valorTotal = 0
            self.setupUi()
            return r
        except Exception as e:
            msg = QtWidgets.QMessageBox()
            msg.setWindowIcon(QtGui.QIcon('./resources/logo-icon.png'))
            msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg.setWindowTitle("Erro")
            msg.setText(str(e))
            msg.exec()

    def gerarPDF(self):
        orcamento = self.salvarOrcamento()
        fones = self.clienteCtrl.listarFones(orcamento['cliente']['idCliente'])
        if fones: fones = list(fones)
        itemPecas = self.orcamentoCtrl.listarItemPecas(orcamento['idOrcamento'])
        if itemPecas: 
            for item in itemPecas:
                item['descricao'] = self.pecaCtrl.getPeca(item['peca'])['descricao']
            itemPecas = list(itemPecas)
        itemServicos = self.orcamentoCtrl.listarItemServicos(orcamento['idOrcamento'])
        if itemServicos: 
            for item in itemServicos:
                item['descricao'] = self.servicoCtrl.getServico(item['servico'])['descricao']
            itemServicos = list(itemServicos)

    def telaBuscaCliente(self):
        self.windowCliente = QtWidgets.QMainWindow()
        self.windowCliente.setWindowIcon(QtGui.QIcon('./resources/logo-icon.png'))
        self.telaCliente = TelaBuscaCliente(self.windowCliente)
        self.telaCliente.botaoSelecionar.clicked.connect(self.retornarDadosCliente)
        self.windowCliente.show()

    def retornarDadosCliente(self):
        linha = self.telaCliente.tabela.selectionModel().selectedRows()
        if linha:
            id = self.telaCliente.tabela.model().index(linha[0].row(), 0).data()
            cliente = self.clienteCtrl.getCliente(id)
            listaFones = [None, None]
            fones = self.clienteCtrl.listarFones(cliente['idCliente'])
            for x in range(len(fones)):
                listaFones[x] = fones[x]['fone']
            if cliente['cidade'] != None:
                cidade = cliente['cidade']['nome']
                uf = cliente['cidade']['uf']
            else:
                cidade = None
                uf = None
            self.setCliente(cliente['tipo'], cliente['nome'], cliente['documento'], listaFones[0], listaFones[1])
            self.setEndereco(cliente['cep'], cliente['endereco'], cliente['numero'], cliente['bairro'], cidade, uf)
            self.clienteSelected = id
            self.checkboxNovoCliente.setChecked(False)
            self.windowCliente.close()

    def telaBuscaVeiculo(self):
        self.windowVeiculo = QtWidgets.QMainWindow()
        self.windowVeiculo.setWindowIcon(QtGui.QIcon('./resources/logo-icon.png'))
        self.telaVeiculo = TelaBuscaVeiculo(self.windowVeiculo)
        self.telaVeiculo.botaoSelecionar.clicked.connect(self.retornarDadosVeiculo)
        self.windowVeiculo.show()

    def retornarDadosVeiculo(self):
        linha = self.telaVeiculo.tabela.selectionModel().selectedRows()
        if linha:
            id = self.telaVeiculo.tabela.model().index(linha[0].row(), 0).data()
            veiculo = self.clienteCtrl.getVeiculo(id)
            self.setVeiculo(veiculo['marca']['nome'], veiculo['modelo'], veiculo['placa'], veiculo['ano'])
            self.veiculoSelected = id
            self.checkboxNovoVeiculo.setChecked(False)
            self.windowVeiculo.close()

    def buscarDadosCEP(self):
        cep = self.lineEditCEP.text()
        if len(cep) !=8:
            return
        dados = self.buscaCEP.buscarCEP(cep)
        if 'erro' in dados:
            return
        self.lineEditEnder.setText(dados['logradouro'])
        self.lineEditBairro.setText(dados['bairro'])
        self.lineEditCidade.setText(dados['localidade'])
        self.comboBoxuf.setCurrentIndex(self.comboBoxuf.findText(dados['uf'], QtCore.Qt.MatchFlag.MatchExactly))
        return

    def limparCampos(self):
        for lineedit in self.framedados.findChildren(QtWidgets.QLineEdit):
            lineedit.clear()
        self.checkboxNovoCliente.setChecked(True)
        self.checkboxNovoVeiculo.setChecked(True)

    def resetarTela(self):
        while len(self.linhasPeca)>1:
            self.removerLinhaPeca(3)
        while len(self.linhasServico)>1:
            self.removerLinhaServico(3)
        self.limparCampos()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = TelaCadastroOrcamento()
    ui.setupUi()
    ui.show()
    style = open('./resources/styles.qss').read()
    app.setStyleSheet(style)
    sys.exit(app.exec())
