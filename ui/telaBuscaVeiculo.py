from flatdict import FlatDict
from PyQt6 import QtCore, QtGui, QtWidgets

from ui.help import HELPBUSCAVEICULO, help
from ui.hoverButton import HoverButton
from ui.infiniteScroll import AlignDelegate, InfiniteScrollTableModel
from ui.telaVeiculoCliente import TelaVeiculoCliente
from util.container import handle_deps


class TelaBuscaVeiculo(QtWidgets.QMainWindow):
    def __init__(self):
        super(TelaBuscaVeiculo, self).__init__()
        self.clienteCtrl = handle_deps.getDep("CLIENTECTRL")
        self.busca = ""
        self.orderBy = 0
        self.setupUi()

    def setupUi(self):
        self.resize(800, 600)
        self.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        self.main_frame = QtWidgets.QFrame(self)
        self.main_frame.setObjectName("main_frame")
        self.hlayout = QtWidgets.QHBoxLayout(self.main_frame)
        spacer = QtWidgets.QSpacerItem(
            20,
            10,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        self.hlayout.addItem(spacer)
        self.framegeral = QtWidgets.QFrame(self.main_frame)
        self.framegeral.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        self.framegeral.setMaximumWidth(
            int(QtGui.QGuiApplication.primaryScreen().size().width() * 0.65)
            if QtGui.QGuiApplication.primaryScreen().size().width() > 1280
            else QtGui.QGuiApplication.primaryScreen().size().width()
        )
        self.hlayout.addWidget(self.framegeral)
        spacer = QtWidgets.QSpacerItem(
            20,
            10,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        self.hlayout.addItem(spacer)
        self.vlayout = QtWidgets.QVBoxLayout(self.framegeral)
        self.vlayout.setContentsMargins(0, 0, 0, 0)
        self.vlayout.setSpacing(0)
        self.frameTitulo = QtWidgets.QFrame(self.framegeral)
        self.vlayout.addWidget(self.frameTitulo)
        self.hlayouttitulo = QtWidgets.QHBoxLayout(self.frameTitulo)
        self.hlayouttitulo.setContentsMargins(0, 0, 0, 0)
        self.hlayouttitulo.setSpacing(0)
        self.hlayouttitulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.labelTitulo = QtWidgets.QLabel(self.frameTitulo)
        self.labelTitulo.setFixedHeight(60)
        self.labelTitulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelTitulo.setObjectName("titulo")
        self.hlayouttitulo.addWidget(self.labelTitulo)
        self.botaoHelp = HoverButton(
            "",
            "./resources/help-icon1.png",
            "./resources/help-icon2.png",
            self.frameTitulo,
        )
        self.botaoHelp.setToolTip("Ajuda")
        self.botaoHelp.setObjectName("botaohelp")
        self.botaoHelp.setHelpIconSize(20, 20)
        self.hlayouttitulo.addWidget(self.botaoHelp)
        self.frameBusca = QtWidgets.QFrame(self.main_frame)
        self.vlayout.addWidget(self.frameBusca)
        self.hlayoutBusca = QtWidgets.QHBoxLayout(self.frameBusca)
        self.lineEditBusca = QtWidgets.QLineEdit(self.frameBusca)
        self.lineEditBusca.setFixedHeight(30)
        self.lineEditBusca.setPlaceholderText(
            "Pesquisar por marca, modelo, placa, ano ou nome do cliente"
        )
        self.lineEditBusca.setClearButtonEnabled(True)
        iconBusca = QtGui.QIcon("resources/search-icon.png")
        self.lineEditBusca.addAction(
            iconBusca, QtWidgets.QLineEdit.ActionPosition.LeadingPosition
        )
        self.hlayoutBusca.addWidget(self.lineEditBusca)
        self.botaoRefresh = QtWidgets.QPushButton(self.frameBusca)
        self.botaoRefresh.setToolTip("Atualizar")
        self.botaoRefresh.setFixedSize(30, 30)
        self.botaoRefresh.setIcon(QtGui.QIcon("resources/refresh-icon.png"))
        self.hlayoutBusca.addWidget(self.botaoRefresh)
        self.frameOrdenacao = QtWidgets.QFrame(self.main_frame)
        self.vlayout.addWidget(self.frameOrdenacao)
        self.hlayoutOrdenacao = QtWidgets.QHBoxLayout(self.frameOrdenacao)
        spacer = QtWidgets.QSpacerItem(
            20,
            10,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        self.hlayoutOrdenacao.addItem(spacer)
        self.comboBoxOrdenacao = QtWidgets.QComboBox(self.frameOrdenacao)
        self.comboBoxOrdenacao.setToolTip("Ordenar")
        self.comboBoxOrdenacao.addItems(
            ["Marca (A-Z)", "Marca (Z-A)", "Modelo (A-Z)", "Modelo (Z-A)"]
        )
        self.hlayoutOrdenacao.addWidget(self.comboBoxOrdenacao)
        self.framedados = QtWidgets.QFrame(self.main_frame)
        self.framedados.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        self.vlayout.addWidget(self.framedados)
        self.vlayoutdados = QtWidgets.QVBoxLayout(self.framedados)
        self.tabela = QtWidgets.QTableView(self.framedados)
        self.vlayoutdados.addWidget(self.tabela)
        self.tabela.setEditTriggers(
            QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers
        )
        self.tabela.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows
        )
        self.tabela.setSelectionMode(
            QtWidgets.QAbstractItemView.SelectionMode.SingleSelection
        )
        self.tabela.horizontalHeader().setHighlightSections(False)
        self.tabela.verticalHeader().setVisible(False)
        self.delegateRight = AlignDelegate(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.framebotoes = QtWidgets.QFrame(self.main_frame)
        self.vlayout.addWidget(self.framebotoes)
        self.hlayoutbotoes = QtWidgets.QHBoxLayout(self.framebotoes)
        spacer = QtWidgets.QSpacerItem(
            20,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.hlayoutbotoes.addItem(spacer)
        self.botaoSelecionar = QtWidgets.QPushButton(self.framebotoes)
        self.botaoSelecionar.setFixedSize(100, 25)
        self.hlayoutbotoes.addWidget(self.botaoSelecionar)
        self.botaoClientes = QtWidgets.QPushButton(self.framebotoes)
        self.botaoClientes.setFixedSize(100, 25)
        self.hlayoutbotoes.addWidget(self.botaoClientes)
        self.setCentralWidget(self.main_frame)
        self.retranslateUi()
        self.listarVeiculos()
        self.botaoRefresh.clicked.connect(self.listarVeiculos)
        self.botaoClientes.clicked.connect(self.clientes)
        self.tabela.verticalScrollBar().valueChanged.connect(self.scrolled)
        self.tabela.verticalScrollBar().actionTriggered.connect(self.scrolled)
        self.lineEditBusca.textChanged.connect(self.buffer)
        self.comboBoxOrdenacao.currentIndexChanged.connect(self.buffer)
        self.botaoHelp.clicked.connect(
            lambda: help("Ajuda - Buscar Veículo", HELPBUSCAVEICULO)
        )

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Busca por Veículo"))
        self.labelTitulo.setText(_translate("MainWindow", "Veículos"))
        self.botaoSelecionar.setText(_translate("MainWindow", "Selecionar"))
        self.botaoClientes.setText(_translate("MainWindow", "Clientes"))

    def scrolled(self, value):
        if value == self.tabela.verticalScrollBar().maximum():
            self.maisVeiculos(50)

    def buffer(self):
        self.busca = self.lineEditBusca.text()
        self.orderBy = self.comboBoxOrdenacao.currentIndex()
        self.listarVeiculos()

    def maisVeiculos(self, qtde):
        veiculos = self.clienteCtrl.buscarVeiculo(
            self.busca, self.linhasCarregadas + qtde, self.orderBy
        )
        if not veiculos:
            return
        maxLength = len(veiculos)
        remainderRows = maxLength - self.linhasCarregadas
        rowsToFetch = min(qtde, remainderRows)
        if rowsToFetch <= 0:
            return
        initLen = self.linhasCarregadas
        maxRows = self.linhasCarregadas + rowsToFetch
        while self.linhasCarregadas < maxRows:
            queryClientes = self.clienteCtrl.listarClientes(
                veiculos[self.linhasCarregadas]["idVeiculo"]
            )
            if queryClientes:
                nomes = []
                for cliente in queryClientes:
                    nomes.append(cliente["nome"])
                veiculos[self.linhasCarregadas]["clientes"] = ", ".join(nomes)
            else:
                veiculos[self.linhasCarregadas]["clientes"] = ""
            veiculos[self.linhasCarregadas] = FlatDict(
                veiculos[self.linhasCarregadas], delimiter="."
            )
            self.linhasCarregadas += 1
        self.model.addData(veiculos[initLen : self.linhasCarregadas])
        colunas = ["idVeiculo", "marca.nome", "modelo", "placa", "ano", "clientes"]
        self.model.colunasDesejadas(colunas)
        self.model.setRowCount(self.linhasCarregadas)
        self.model.setColumnCount(len(colunas))
        self.tabela.hideColumn(0)

    def listarVeiculos(self):
        self.linhasCarregadas = 0
        self.model = InfiniteScrollTableModel([{}])
        listaHeader = ["ID", "Marca", "Modelo", "Placa", "Ano", "Clientes Vinculados"]
        self.model.setHorizontalHeaderLabels(listaHeader)
        self.tabela.setModel(self.model)
        self.tabela.setItemDelegateForColumn(4, self.delegateRight)
        self.maisVeiculos(50)
        if self.linhasCarregadas > 0:
            header = self.tabela.horizontalHeader()
            header.setSectionResizeMode(
                QtWidgets.QHeaderView.ResizeMode.ResizeToContents
            )
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.Stretch)
            self.model.setHeaderAlignment(
                4,
                QtCore.Qt.AlignmentFlag.AlignRight
                | QtCore.Qt.AlignmentFlag.AlignVCenter,
            )

    def clientes(self):
        linha = self.tabela.selectionModel().selectedRows()
        if linha:
            id = self.tabela.model().index(linha[0].row(), 0).data()
            self.telaVeiculoCliente = TelaVeiculoCliente()
            self.telaVeiculoCliente.renderClientes(id)
            self.telaVeiculoCliente.botaoConcluir.clicked.connect(self.listarVeiculos)
            self.telaVeiculoCliente.show()

    def keyPressEvent(self, event) -> None:
        if event.key() == QtCore.Qt.Key.Key_F1:
            self.botaoHelp.click()
