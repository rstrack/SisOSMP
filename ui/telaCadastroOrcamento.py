from PyQt6 import QtCore, QtGui, QtWidgets
from routes import handleRoutes

from ui.telaBuscaCliente import TelaBuscaCliente

SIGLAESTADOS = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS',
                'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
UNIDADES = ['CM', 'CM2', 'CM3', 'CX', 'DZ', 'G', 'KG',
            'L', 'M', 'M2', 'M3', 'ML', 'PAR', 'PCT', 'ROLO', 'UN']


class TelaCadastroOrcamento(QtWidgets.QMainWindow):

    def __init__(self):
        super(TelaCadastroOrcamento, self).__init__()
        self.orcamentoCtrl = handleRoutes.getRoute('ORCAMENTO')
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
        self.vlayout1.setContentsMargins(9, 9, 9, 9)
        self.vlayout1.setSpacing(18)
        self.vlayout1.addWidget(self.labelTitulo)
        self.framedados = QtWidgets.QFrame(self.main_frame)
        self.gridLayout = QtWidgets.QGridLayout(self.framedados)
        self.gridLayout.setVerticalSpacing(9)
        self.gridLayout.setHorizontalSpacing(9)
        self.vlayout1.addWidget(self.framedados)
        # dados do cliente
        self.groupBoxCliente = QtWidgets.QGroupBox(self.framedados)
        self.gridLayoutCliente = QtWidgets.QGridLayout(self.groupBoxCliente)
        self.framebotoesCliente = QtWidgets.QFrame(self.groupBoxCliente)
        self.gridLayoutCliente.addWidget(self.framebotoesCliente, 0, 0, 1, -1)
        self.hlayout1 = QtWidgets.QHBoxLayout(self.framebotoesCliente)
        self.hlayout1.setContentsMargins(0, 0, 0, 0)
        self.botaobuscarCliente = QtWidgets.QPushButton(
            self.framebotoesCliente)
        self.botaobuscarCliente.setFixedWidth(200)
        self.hlayout1.addWidget(self.botaobuscarCliente)
        self.checkboxNovoCliente = QtWidgets.QCheckBox(self.framebotoesCliente)
        self.checkboxNovoCliente.setFixedWidth(150)
        self.checkboxNovoCliente.setChecked(True)
        self.hlayout1.addWidget(self.checkboxNovoCliente)
        self.hlayout1.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)

        self.labelPessoa = QtWidgets.QLabel(self.groupBoxCliente)
        self.gridLayoutCliente.addWidget(self.labelPessoa, 1, 0, 1, 1)
        self.labelcpfj = QtWidgets.QLabel(self.groupBoxCliente)
        self.gridLayoutCliente.addWidget(self.labelcpfj, 1, 1, 1, 1)
        self.labelNome = QtWidgets.QLabel(self.groupBoxCliente)
        self.gridLayoutCliente.addWidget(self.labelNome, 1, 2, 1, 1)
        self.labelFone1 = QtWidgets.QLabel(self.groupBoxCliente)
        self.gridLayoutCliente.addWidget(self.labelFone1, 1, 4, 1, 1)
        self.labelFone2 = QtWidgets.QLabel(self.groupBoxCliente)
        self.gridLayoutCliente.addWidget(self.labelFone2, 1, 5, 1, 1)
        self.comboBoxPessoa = QtWidgets.QComboBox(self.groupBoxCliente)
        self.comboBoxPessoa.addItems(["FÍSICA", "JURÍDICA"])
        self.gridLayoutCliente.addWidget(self.comboBoxPessoa, 2, 0, 1, 1)
        self.lineEditCPFJ = QtWidgets.QLineEdit(self.groupBoxCliente)
        self.gridLayoutCliente.addWidget(self.lineEditCPFJ, 2, 1, 1, 1)
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
        self.gridLayoutCliente.setColumnStretch(1, 3)
        self.gridLayoutCliente.setColumnStretch(2, 8)
        self.gridLayoutCliente.setColumnStretch(4, 6)
        self.gridLayoutCliente.setColumnStretch(5, 6)
        self.gridLayoutCliente.setColumnStretch(6, 2)

        self.gridLayout.addWidget(self.groupBoxCliente, 0, 0, 1, -1)
        # dados do veiculo
        self.groupBoxVeiculo = QtWidgets.QGroupBox(self.framedados)
        self.gridLayoutVeiculo = QtWidgets.QGridLayout(self.groupBoxVeiculo)
        self.framebotoesVeiculo = QtWidgets.QFrame(self.groupBoxCliente)
        self.gridLayoutVeiculo.addWidget(self.framebotoesVeiculo, 0, 0, 1, -1)
        self.hlayout2 = QtWidgets.QHBoxLayout(self.framebotoesVeiculo)
        self.hlayout2.setContentsMargins(0, 0, 0, 0)
        self.botaobuscarveiculo = QtWidgets.QPushButton(
            self.framebotoesVeiculo)
        self.botaobuscarveiculo.setFixedWidth(200)
        self.hlayout2.addWidget(self.botaobuscarveiculo)
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

        self.gridLayout.addWidget(self.groupBoxVeiculo, 1, 0, 1, -1)
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
        self.gridLayout_2 = QtWidgets.QGridLayout(self.framegroupboxpecas)

        self.labelNomePeca = QtWidgets.QLabel(self.framegroupboxpecas)
        self.gridLayout_2.addWidget(self.labelNomePeca, 0, 0, 1, 1)
        self.labelQtde = QtWidgets.QLabel(self.framegroupboxpecas)
        self.gridLayout_2.addWidget(self.labelQtde, 0, 1, 1, 1)
        self.labelUn = QtWidgets.QLabel(self.framegroupboxpecas)
        self.gridLayout_2.addWidget(self.labelUn, 0, 2, 1, 1)
        self.labelValorPeca = QtWidgets.QLabel(self.framegroupboxpecas)
        self.gridLayout_2.addWidget(self.labelValorPeca, 0, 3, 1, 1)
        self.lineEditNomePeca = QtWidgets.QLineEdit(self.framegroupboxpecas)
        self.gridLayout_2.addWidget(self.lineEditNomePeca, 1, 0, 1, 1)
        self.lineEditQtdeP = QtWidgets.QLineEdit(self.framegroupboxpecas)
        self.gridLayout_2.addWidget(self.lineEditQtdeP, 1, 1, 1, 1)
        self.comboBoxUn = QtWidgets.QComboBox(self.framegroupboxpecas)
        self.comboBoxUn.addItems(UNIDADES)
        self.comboBoxUn.setMinimumWidth(50)
        self.comboBoxUn.setCurrentIndex(15)
        self.gridLayout_2.addWidget(self.comboBoxUn, 1, 2, 1, 1)
        self.lineEditValorPeca = QtWidgets.QLineEdit(self.framegroupboxpecas)
        self.gridLayout_2.addWidget(self.lineEditValorPeca, 1, 3, 1, 1)
        self.botaoAddPecas = QtWidgets.QPushButton(self.framegroupboxpecas)
        self.gridLayout_2.addWidget(self.botaoAddPecas, 1, 4, 1, 1)
        self.linhasPeca = [
            [self.lineEditNomePeca, self.lineEditQtdeP, self.comboBoxUn, self.lineEditValorPeca]]
        self.spacerpeca = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(self.spacerpeca, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBoxPecas, 2, 0, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 6)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayout_2.setColumnStretch(3, 1)

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
        self.gridLayout_5 = QtWidgets.QGridLayout(self.framegroupboxservicos)

        self.labelNomeServico = QtWidgets.QLabel(self.framegroupboxservicos)
        self.gridLayout_5.addWidget(self.labelNomeServico, 0, 0, 1, 1)
        self.labelQtdeS = QtWidgets.QLabel(self.framegroupboxservicos)
        self.gridLayout_5.addWidget(self.labelQtdeS, 0, 1, 1, 1)
        self.labelValorServico = QtWidgets.QLabel(self.framegroupboxservicos)
        self.gridLayout_5.addWidget(self.labelValorServico, 0, 2, 1, 1)

        self.lineEditNomeServico = QtWidgets.QLineEdit(
            self.framegroupboxservicos)
        self.gridLayout_5.addWidget(self.lineEditNomeServico, 1, 0, 1, 1)
        self.lineEditQtdeS = QtWidgets.QLineEdit(self.framegroupboxservicos)
        self.gridLayout_5.addWidget(self.lineEditQtdeS, 1, 1, 1, 1)
        self.lineEditValorServico = QtWidgets.QLineEdit(
            self.framegroupboxservicos)
        self.gridLayout_5.addWidget(self.lineEditValorServico, 1, 2, 1, 1)
        self.botaoAddServicos = QtWidgets.QPushButton(
            self.framegroupboxservicos)
        self.gridLayout_5.addWidget(self.botaoAddServicos, 1, 3, 1, 1)

        self.linhasServico = [[self.lineEditNomeServico,
                               self.lineEditQtdeS, self.lineEditValorServico]]
        self.spacerservico = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_5.addItem(self.spacerservico, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBoxServicos, 2, 1, 1, 1)

        self.gridLayout_5.setColumnStretch(0, 6)
        self.gridLayout_5.setColumnStretch(1, 1)
        self.gridLayout_5.setColumnStretch(2, 1)

        # frame
        self.framevalor = QtWidgets.QFrame(self.framedados)
        self.hlayoutvalor = QtWidgets.QHBoxLayout(self.framevalor)
        self.hlayoutvalor.setContentsMargins(0, 0, 0, 0)
        # data do orçamento
        self.framedata = QtWidgets.QFrame(self.framevalor)
        self.vlayoutdata = QtWidgets.QVBoxLayout(self.framedata)
        self.labelData = QtWidgets.QLabel(self.framedata)
        self.lineEditData = QtWidgets.QDateEdit(self.framedata)
        self.lineEditData.setFixedWidth(125)
        self.lineEditData.setCalendarPopup(True)
        self.lineEditData.setDateTime(QtCore.QDateTime.currentDateTime())
        self.vlayoutdata.addWidget(self.labelData)
        self.vlayoutdata.addWidget(self.lineEditData)
        self.hlayoutvalor.addWidget(self.framedata)
        # valor
        self.labelValorTotal1 = QtWidgets.QLabel(self.framevalor)
        self.labelValorTotal1.setText("VALOR TOTAL: R$")
        self.labelValorTotal2 = QtWidgets.QLabel(self.framevalor)
        spacerItem = QtWidgets.QSpacerItem(
            10, 10, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.hlayoutvalor.addItem(spacerItem)
        self.hlayoutvalor.addWidget(self.labelValorTotal1)
        self.hlayoutvalor.addWidget(self.labelValorTotal2)
        self.gridLayout.addWidget(self.framevalor, 3, 0, 1, -1)
        self.gridLayout.setRowStretch(2, 10)
        self.gridLayout.setRowStretch(3, 0)

        self.frameobs = QtWidgets.QFrame(self.framedados)
        self.gridLayout.addWidget(self.frameobs, 4, 0, 1, -1)

        # campo de observações
        self.groupBoxObs = QtWidgets.QGroupBox(self.frameobs)
        self.vlayout2 = QtWidgets.QVBoxLayout(self.groupBoxObs)
        self.textEdit = QtWidgets.QTextEdit(self.groupBoxObs)
        self.groupBoxObs.setMaximumHeight(80)
        self.vlayout2.addWidget(self.textEdit)
        self.gridLayout.addWidget(self.groupBoxObs, 5, 0, 1, -1)
        # botoes

        self.framebotoes = QtWidgets.QFrame(self.main_frame)
        self.hlayout4 = QtWidgets.QHBoxLayout(self.framebotoes)
        self.labelLegenda = QtWidgets.QLabel(self.framevalor)
        self.hlayout4.addWidget(self.labelLegenda)
        spacerItem5 = QtWidgets.QSpacerItem(
            40, 10, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.hlayout4.addItem(spacerItem5)
        self.botaoSalvareImprimir = QtWidgets.QPushButton(self.framebotoes)
        self.botaoSalvareImprimir.setMinimumSize(QtCore.QSize(150, 35))
        self.botaoSalvareImprimir.setObjectName('botaoprincipal')
        self.hlayout4.addWidget(self.botaoSalvareImprimir)
        self.botaoSalvar = QtWidgets.QPushButton(self.framebotoes)
        self.botaoSalvar.setMinimumSize(QtCore.QSize(100, 30))
        self.hlayout4.addWidget(self.botaoSalvar)
        self.botaolimpar = QtWidgets.QPushButton(self.framebotoes)
        self.botaolimpar.setMinimumSize(QtCore.QSize(100, 30))
        self.hlayout4.addWidget(self.botaolimpar)
        self.hlayout4.setContentsMargins(9, 0, 9, 9)
        self.vlayout1.addWidget(self.framebotoes)

        self.setCentralWidget(self.main_frame)

        self.completerPeca = QtWidgets.QCompleter([])
        self.completerPeca.setCaseSensitivity(
            QtCore.Qt.CaseSensitivity.CaseInsensitive)
        self.completerPeca.setCompletionMode(
            QtWidgets.QCompleter.CompletionMode.UnfilteredPopupCompletion)
        self.lineEditNomePeca.setCompleter(self.completerPeca)
        self.completerServico = QtWidgets.QCompleter([])
        self.completerServico.setCaseSensitivity(
            QtCore.Qt.CaseSensitivity.CaseInsensitive)
        self.completerServico.setCompletionMode(
            QtWidgets.QCompleter.CompletionMode.UnfilteredPopupCompletion)
        self.lineEditNomeServico.setCompleter(self.completerServico)

        self.retranslateUi()
        self.setMarcas()
        self.setModelCompleters()

        self.botaoAddPecas.clicked.connect(self.addLinhaPeca)
        self.botaoAddServicos.clicked.connect(self.addLinhaServico)
        self.botaobuscarCliente.clicked.connect(self.telaBuscaCliente)
        self.botaobuscarveiculo.clicked.connect(self.telaBuscaVeiculo)
        self.botaolimpar.clicked.connect(self.limparCampos)
        self.botaoSalvar.clicked.connect(self.salvarOrcamento)
        self.botaoSalvareImprimir.clicked.connect(self.salvarImprimirOrcamento)

        self.lineEditNomePeca.editingFinished.connect(lambda: self.controller.buscarPeca(self.lineEditNomePeca,
                                                                                         self.comboBoxUn, self.lineEditValorPeca))
        self.lineEditNomeServico.editingFinished.connect(lambda: self.controller.buscarServico(self.lineEditNomeServico,
                                                                                               self.lineEditValorServico))
        self.lineEditNomePeca.editingFinished.connect(self.setValor)
        self.lineEditNomeServico.editingFinished.connect(self.setValor)
        self.lineEditQtdeP.editingFinished.connect(self.setValor)
        self.lineEditQtdeS.editingFinished.connect(self.setValor)
        self.lineEditValorPeca.editingFinished.connect(self.setValor)
        self.lineEditValorServico.editingFinished.connect(self.setValor)
        self.checkboxNovoCliente.stateChanged.connect(
            self.habilitarCamposCliente)
        self.checkboxNovoVeiculo.stateChanged.connect(
            self.habilitarCamposVeiculo)

    ##############################################################################################################################
                                                            #FUNÇÕES
    ##############################################################################################################################

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Mecânica Pasetto"))
        self.botaoSalvareImprimir.setText(
            _translate("MainWindow", "Salvar e Imprimir"))
        self.botaoSalvar.setText(_translate("MainWindow", "Salvar"))
        self.botaolimpar.setText(_translate("MainWindow", "Limpar"))
        self.labelTitulo.setText(_translate("MainWindow", "Orçamentos"))
        self.labelData.setText(_translate("MainWindow", "Data do Orçamento"))
        self.groupBoxCliente.setTitle(
            _translate("MainWindow", "Dados do Cliente"))
        self.botaobuscarCliente.setText(
            _translate("MainWindow", "Selecionar Cliente"))
        self.checkboxNovoCliente.setText(
            _translate("MainWindow", "Novo Cliente"))
        self.labelNome.setText(_translate("MainWindow", "Nome*"))
        self.labelCEP.setText(_translate("MainWindow", "CEP"))
        self.labelPessoa.setText(_translate("MainWindow", "Pessoa"))
        self.labelcpfj.setText(_translate("MainWindow", "CPF"))
        self.labelUF.setText(_translate("MainWindow", "UF"))
        self.labelCidade.setText(_translate("MainWindow", "Cidade"))
        self.labelEnder.setText(_translate("MainWindow", "Endereço"))
        self.labelNumero.setText(_translate("MainWindow", "Número"))
        self.labelBairro.setText(_translate("MainWindow", "Bairro"))
        self.labelFone1.setText(_translate("MainWindow", "Fone 1"))
        self.labelFone2.setText(_translate("MainWindow", "Fone 2"))
        self.groupBoxVeiculo.setTitle(
            _translate("MainWindow", "Dados do veículo"))
        self.botaobuscarveiculo.setText(
            _translate("MainWindow", "Selecionar Veículo"))
        self.checkboxNovoVeiculo.setText(
            _translate("MainWindow", "Novo Veículo"))
        self.labelMarca.setText(_translate("MainWindow", "Marca*"))
        self.labelPlaca.setText(_translate("MainWindow", "Placa*"))
        self.labelAno.setText(_translate("MainWindow", "Ano*"))
        self.labelModelo.setText(_translate("MainWindow", "Modelo*"))
        self.labelKm.setText(_translate("MainWindow", "Km*"))
        self.groupBoxServicos.setTitle(_translate("MainWindow", "Serviços"))
        self.botaoAddServicos.setText(_translate("MainWindow", "+"))
        self.labelValorServico.setText(_translate("MainWindow", "Valor*"))
        self.labelNomeServico.setText(_translate("MainWindow", "Serviço*"))
        self.labelQtdeS.setText(_translate("MainWindow", "Qtde*"))
        self.labelLegenda.setText(_translate(
            "MainWindow", "* Campos Obrigatórios"))
        self.groupBoxObs.setTitle(_translate(
            "MainWindow", "Observações (Max. 200 caracteres)"))
        self.groupBoxPecas.setTitle(_translate("MainWindow", "Peças"))
        self.labelQtde.setText(_translate("MainWindow", "Qtde*"))
        self.labelUn.setText(_translate("MainWindow", "Un*"))
        self.botaoAddPecas.setText(_translate("MainWindow", "+"))
        self.labelNomePeca.setText(_translate("MainWindow", "Peça*"))
        self.labelValorPeca.setText(_translate("MainWindow", "Valor*"))

    def addLinhaPeca(self):
        label1 = QtWidgets.QLabel(text="Peça*")
        label2 = QtWidgets.QLabel(text="Qtde*")
        label3 = QtWidgets.QLabel(text="Un*")
        label4 = QtWidgets.QLabel(text="Valor*")
        lineedit1 = QtWidgets.QLineEdit()
        lineedit1.setCompleter(self.completerPeca)
        lineedit2 = QtWidgets.QLineEdit()
        comboBox = QtWidgets.QComboBox()
        comboBox.addItems(UNIDADES)
        comboBox.setCurrentIndex(15)
        lineedit4 = QtWidgets.QLineEdit()
        lineedit1.editingFinished.connect(self.setValor)
        lineedit2.editingFinished.connect(self.setValor)
        lineedit4.editingFinished.connect(self.setValor)
        lineedit1.editingFinished.connect(
            lambda: self.controller.buscarPeca(lineedit1, comboBox, lineedit4))
        self.gridLayout_2.addWidget(label1, len(self.linhasPeca)*2, 0, 1, 1)
        self.gridLayout_2.addWidget(label2, len(self.linhasPeca)*2, 1, 1, 1)
        self.gridLayout_2.addWidget(label3, len(self.linhasPeca)*2, 2, 1, 1)
        self.gridLayout_2.addWidget(label4, len(self.linhasPeca)*2, 3, 1, 1)
        self.gridLayout_2.addWidget(
            lineedit1, len(self.linhasPeca)*2+1, 0, 1, 1)
        self.gridLayout_2.addWidget(
            lineedit2, len(self.linhasPeca)*2+1, 1, 1, 1)
        self.gridLayout_2.addWidget(
            comboBox, len(self.linhasPeca)*2+1, 2, 1, 1)
        self.gridLayout_2.addWidget(
            lineedit4, len(self.linhasPeca)*2+1, 3, 1, 1)
        self.linhasPeca.append([lineedit1, lineedit2, comboBox, lineedit4])
        self.gridLayout_2.addWidget(
            self.botaoAddPecas, len(self.linhasPeca)*2-1, 4, 1, 1)
        self.gridLayout_2.removeItem(self.spacerpeca)
        self.gridLayout_2.addItem(
            self.spacerpeca, len(self.linhasPeca)*2, 0, 1, 1)

    def addLinhaServico(self):
        label1 = QtWidgets.QLabel(text="Serviço*")
        label2 = QtWidgets.QLabel(text="Qtde*")
        label3 = QtWidgets.QLabel(text="Valor*")
        lineedit1 = QtWidgets.QLineEdit()
        lineedit1.setCompleter(self.completerServico)
        lineedit2 = QtWidgets.QLineEdit()
        lineedit3 = QtWidgets.QLineEdit()
        lineedit1.editingFinished.connect(self.setValor)
        lineedit2.editingFinished.connect(self.setValor)
        lineedit3.editingFinished.connect(self.setValor)
        lineedit1.editingFinished.connect(
            lambda: self.controller.buscarServico(lineedit1, lineedit3))
        self.gridLayout_5.addWidget(label1, len(self.linhasServico)*2, 0, 1, 1)
        self.gridLayout_5.addWidget(label2, len(self.linhasServico)*2, 1, 1, 1)
        self.gridLayout_5.addWidget(label3, len(self.linhasServico)*2, 2, 1, 1)
        self.gridLayout_5.addWidget(
            lineedit1, len(self.linhasServico)*2+1, 0, 1, 1)
        self.gridLayout_5.addWidget(
            lineedit2, len(self.linhasServico)*2+1, 1, 1, 1)
        self.gridLayout_5.addWidget(
            lineedit3, len(self.linhasServico)*2+1, 2, 1, 1)
        self.linhasServico.append([lineedit1, lineedit2, lineedit3])
        self.gridLayout_5.addWidget(
            self.botaoAddServicos, len(self.linhasServico)*2-1, 3, 1, 1)
        self.gridLayout_5.removeItem(self.spacerservico)
        self.gridLayout_5.addItem(
            self.spacerservico, len(self.linhasServico)*2, 0, 1, 1)

    def limparDadosCliente(self):
        self.lineEditNomeCliente.clear()
        self.lineEditCPFJ.clear()
        self.lineEditCEP.clear()
        self.lineEditEnder.clear()
        self.lineEditNumero.clear()
        self.lineEditBairro.clear()
        self.lineEditCidade.clear()
        self.lineEditFone1.clear()
        self.lineEditFone2.clear()

    def limparDadosVeiculo(self):
        self.comboBoxMarca.clear()
        self.lineEditModelo.clear()
        self.lineEditAno.clear()
        self.lineEditPlaca.clear()
        self.lineEditKm.clear()

    def setCliente(self, nome, cpf=None, cnpj=None, tel1=None, tel2=None):
        self.lineEditNomeCliente.setText(nome)
        if cpf:
            self.lineEditCPFJ.setText(cpf)
            self.labelcpfj.setText("CPF")
            self.comboBoxPessoa.setCurrentIndex(0)
        elif cnpj:
            self.lineEditCPFJ.setText(cnpj)
            self.labelcpfj.setText("CNPJ")
            self.comboBoxPessoa.setCurrentIndex(1)
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
        marcas = self.controller.getMarcas()
        for marca in marcas:
            self.comboBoxMarca.addItem(marca.marca)
        self.comboBoxMarca.setCurrentIndex(-1)

    def setModelCompleters(self):
        list = self.controller.atualizarCompleters()
        self.completerPeca.setModel(list[0])
        self.completerServico.setModel(list[1])

    def getDadosCliente(self):
        dict = {}
        if (self.lineEditCPFJ.text()):
            if (self.comboBoxPessoa.currentIndex() == 0):
                dict['cpf'] = self.lineEditCPFJ.text()
            else:
                dict['cnpj'] = self.lineEditCPFJ.text()
        if (self.lineEditNomeCliente.text()):
            dict['nome'] = self.lineEditNomeCliente.text()
        if (self.lineEditCEP.text()):
            dict['cep'] = self.lineEditCEP.text()
        if (self.lineEditEnder.text()):
            dict['endereco'] = self.lineEditEnder.text()
        if (self.lineEditNumero.text()):
            dict['numero'] = self.lineEditNumero.text()
        if (self.lineEditBairro.text()):
            dict['bairro'] = self.lineEditBairro.text()
        if (self.lineEditCidade.text()):
            dict['cidade'] = self.lineEditCidade.text()
        dict['estado'] = self.comboBoxuf.currentText()
        return dict

    # getFodase(self)

    def getFones(self):
        fones = []
        if (self.lineEditFone1.text()):
            fones.append(self.lineEditFone1.text())
        else:
            fones.append(None)
        if (self.lineEditFone2.text()):
            fones.append(self.lineEditFone2.text())
        else:
            fones.append(None)
        return fones

    def getDadosVeiculo(self):
        dict = {}
        dict['marca'] = self.comboBoxMarca.currentText()
        if (self.lineEditModelo.text()):
            dict['modelo'] = self.lineEditModelo.text()
        if (self.lineEditPlaca.text()):
            dict['placa'] = self.lineEditPlaca.text()
        if (self.lineEditAno.text()):
            dict['ano'] = self.lineEditAno.text()
        return dict

    def limparCampos(self):
        for lineedit in self.framedados.findChildren(QtWidgets.QLineEdit):
            lineedit.clear()

    def setValor(self):
        valor = self.controller.getValorTotal()
        self.labelValorTotal2.setText(str(valor))

    def salvarOrcamento(self):
        if not self.controller.salvarOrcamento():
            pass
        else:
            self.controller.salvarOrcamento()
            self.setMarcas()
            self.setModelCompleters()

    def salvarImprimirOrcamento(self):
        self.setMarcas()
        self.setModelCompleters()
        pass

    def telaBuscaCliente(self):
        window = QtWidgets.QMainWindow()
        tela = TelaBuscaCliente(window)
        tela.botaoSelecionar.connect()

    '''def telaBuscaVeiculo(self):
        self.window = QtWidgets.QMainWindow()
        self.buscaVeiculo = TelaConsultaAux(self.window)
        listaHeader = ['ID', 'Marca', 'Modelo',
                       'Ano', 'Placa', 'Clientes Vinculados']
        self.buscaVeiculo.model.setHorizontalHeaderLabels(listaHeader)
        queryVeiculo = self.controller.getVeiculos()
        self.buscaVeiculo.model.setRowCount(len(queryVeiculo))
        row = 0
        for veiculo in queryVeiculo:
            item = QtGui.QStandardItem(str(veiculo.idVeiculo))
            item.setTextAlignment(
                QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.buscaVeiculo.model.setItem(row, 0, item)
            querymarca = self.controller.getMarcaByID(veiculo.marca_id)
            item.setTextAlignment(
                QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
            item = QtGui.QStandardItem(querymarca[0].marca)
            item.setTextAlignment(
                QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.buscaVeiculo.model.setItem(row, 1, item)
            item = QtGui.QStandardItem(veiculo.modelo)
            item.setTextAlignment(
                QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.buscaVeiculo.model.setItem(row, 2, item)
            item = QtGui.QStandardItem(veiculo.ano)
            item.setTextAlignment(
                QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.buscaVeiculo.model.setItem(row, 3, item)
            item = QtGui.QStandardItem(veiculo.placa)
            item.setTextAlignment(
                QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.buscaVeiculo.model.setItem(row, 4, item)
            queryCliente = self.controller.getClientesByVeiculo(veiculo)
            nomes = []
            for cliente in queryCliente:
                nomes.append(cliente.nome)
            item = QtGui.QStandardItem(', '.join(nomes))
            self.buscaVeiculo.model.setItem(row, 5, item)
            row = row+1
        self.buscaVeiculo.filter.setSourceModel(self.buscaVeiculo.model)
        header = self.buscaVeiculo.tabela.horizontalHeader()
        header.setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.Interactive)
        header.setSectionResizeMode(
            0, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(
            3, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        header.setStretchLastSection(True)
        self.buscaVeiculo.botaoSelecionar.clicked.connect(self.usarVeiculo)
        botaoVinculo = QtWidgets.QPushButton(self.buscaVeiculo.framebotoes)
        botaoVinculo.setText("Desvincular")
        botaoVinculo.setFixedSize(100, 25)
        self.buscaVeiculo.hlayoutbotoes.addWidget(botaoVinculo)
        self.veiculo = queryVeiculo
        self.window.show()

    def usarVeiculo(self):
        self.linha = self.buscaVeiculo.tabela.selectionModel().selectedRows()[
            0]
        id = self.buscaVeiculo.tabela.model().index(self.linha.row(), 0).data()
        [marca, modelo, placa, ano] = self.controller.getDadosVeiculo(id)
        self.setVeiculo(marca, modelo, placa, ano)
        self.checkboxNovoVeiculo.setChecked(False)
        self.controller.setVeiculoSelecionado(id)
        self.window.close()'''

    def limparCampos(self):
        for lineedit in self.framedados.findChildren(QtWidgets.QLineEdit):
            lineedit.clear()
        self.checkboxNovoCliente.setChecked(True)
        self.checkboxNovoVeiculo.setChecked(True)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = TelaCadastroOrcamento()
    ui.setupUi()
    ui.show()
    style = open('./ui/styles.qss').read()
    app.setStyleSheet(style)
    sys.exit(app.exec())
