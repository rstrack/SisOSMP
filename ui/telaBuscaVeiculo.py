from PyQt6 import QtCore, QtGui, QtWidgets
from flatdict import FlatDict
from container import handleDeps
from ui.infiniteScroll import AlignDelegate, InfiniteScrollTableModel
from ui.telaVeiculoCliente import TelaVeiculoCliente

class TelaBuscaVeiculo(QtWidgets.QMainWindow):
    def __init__(self):
        super(TelaBuscaVeiculo, self).__init__()
        self.clienteCtrl = handleDeps.getDep('CLIENTECTRL')
        self.setupUi()

    def setupUi(self):
        self.resize(800, 400)
        self.mainwidget = QtWidgets.QWidget(self)
        self.glayout = QtWidgets.QGridLayout(self.mainwidget)
        self.frameBusca = QtWidgets.QFrame(self.mainwidget)
        self.glayout.addWidget(self.frameBusca, 0, 0, 1, 1)
        self.hlayoutBusca = QtWidgets.QHBoxLayout(self.frameBusca)
        self.lineEditBusca = QtWidgets.QLineEdit(self.frameBusca)
        self.lineEditBusca.setFixedHeight(30)
        self.lineEditBusca.setPlaceholderText("Pesquisar")
        self.lineEditBusca.setClearButtonEnabled(True)
        iconBusca = QtGui.QIcon("./resources/search-icon.png")
        self.lineEditBusca.addAction(iconBusca, QtWidgets.QLineEdit.ActionPosition.LeadingPosition)
        self.hlayoutBusca.addWidget(self.lineEditBusca)
        self.botaoRefresh = QtWidgets.QPushButton(self.frameBusca)
        self.botaoRefresh.setToolTip('Atualizar')
        self.botaoRefresh.setFixedSize(30,30)
        self.botaoRefresh.setIcon(QtGui.QIcon("./resources/refresh-icon.png"))
        self.hlayoutBusca.addWidget(self.botaoRefresh)
        self.framedados = QtWidgets.QFrame(self.mainwidget)
        self.framedados.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        self.glayout.addWidget(self.framedados, 1, 0, 1, 1)
        self.vlayoutdados = QtWidgets.QVBoxLayout(self.framedados)
        self.tabela = QtWidgets.QTableView(self.framedados)
        self.vlayoutdados.addWidget(self.tabela)
        self.tabela.setEditTriggers(
            QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tabela.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tabela.setSelectionMode(
            QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.tabela.horizontalHeader().setHighlightSections(False)
        self.tabela.verticalHeader().setVisible(False)
        self.delegateRight = AlignDelegate(QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.filter = QtCore.QSortFilterProxyModel()
        self.filter.setFilterCaseSensitivity(
            QtCore.Qt.CaseSensitivity.CaseInsensitive)

        self.framebotoes = QtWidgets.QFrame(self.mainwidget)
        self.glayout.addWidget(self.framebotoes, 2, 0, 1, 1)
        self.hlayoutbotoes = QtWidgets.QHBoxLayout(self.framebotoes)
        spacer = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.hlayoutbotoes.addItem(spacer)
        self.botaoSelecionar = QtWidgets.QPushButton(self.framebotoes)
        self.botaoSelecionar.setFixedSize(100, 25)
        self.hlayoutbotoes.addWidget(self.botaoSelecionar)
        self.botaoClientes = QtWidgets.QPushButton(self.framebotoes)
        self.botaoClientes.setFixedSize(100, 25)
        self.hlayoutbotoes.addWidget(self.botaoClientes)
        self.filter.setFilterKeyColumn(-1)
        self.lineEditBusca.textChanged.connect(
            self.filter.setFilterRegularExpression)
        self.tabela.setModel(self.filter)
        self.setCentralWidget(self.mainwidget)
        self.retranslateUi()
        self.selectionModel = self.tabela.selectionModel()

        self.listarVeiculos()
        self.botaoRefresh.clicked.connect(self.listarVeiculos)
        self.botaoClientes.clicked.connect(self.clientes)
        self.tabela.verticalScrollBar().valueChanged.connect(self.scrolled)
        self.tabela.verticalScrollBar().actionTriggered.connect(self.scrolled)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Busca por Veículo"))
        self.botaoSelecionar.setText(_translate("MainWindow", "Selecionar"))
        self.botaoClientes.setText(_translate("MainWindow", "Clientes"))

    def scrolled(self, value):
        if value == self.tabela.verticalScrollBar().maximum():
            self.maisVeiculos(50)
            # threading.Thread(target=self.maisVeiculos, args=(100,)).start()

    def maisVeiculos(self, qtde):
        veiculos = self.clienteCtrl.listarVeiculos()
        if not veiculos:
            return
        maxLength = len(veiculos)
        remainderRows = maxLength-self.linhasCarregadas
        rowsToFetch=min(qtde, remainderRows)
        if rowsToFetch<=0:
            return
        initLen = self.linhasCarregadas
        maxRows = self.linhasCarregadas + rowsToFetch
        while self.linhasCarregadas < maxRows:
            queryClientes = self.clienteCtrl.listarClientes(veiculos[self.linhasCarregadas]['idVeiculo'])
            if queryClientes:
                nomes = []
                for cliente in queryClientes:
                    nomes.append(cliente['nome'])
                veiculos[self.linhasCarregadas]['clientes'] = ', '.join(nomes)
            else: veiculos[self.linhasCarregadas]['clientes'] = ''
            veiculos[self.linhasCarregadas] = FlatDict(veiculos[self.linhasCarregadas], delimiter='.')
            self.linhasCarregadas+=1
        self.model.addData(veiculos[initLen:self.linhasCarregadas])
        colunas = ['idVeiculo', 'marca.nome', 'modelo', 'placa', 'ano', 'clientes']
        self.model.colunasDesejadas(colunas)
        self.model.setRowCount(self.linhasCarregadas)
        self.model.setColumnCount(len(colunas))
        self.tabela.hideColumn(0)

    def listarVeiculos(self):
        self.linhasCarregadas = 0
        self.model = InfiniteScrollTableModel([{}])
        listaHeader = ['ID', 'Marca', 'Modelo', 'Placa', 'Ano', 'Clientes Vinculados']
        self.model.setHorizontalHeaderLabels(listaHeader)
        self.filter.setSourceModel(self.model)
        self.tabela.setModel(self.filter)
        self.tabela.setItemDelegateForColumn(4, self.delegateRight)
        self.maisVeiculos(50)
        if self.linhasCarregadas > 0:
            header = self.tabela.horizontalHeader()
            header.setSectionResizeMode(
                QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
            header.setSectionResizeMode(2,
                QtWidgets.QHeaderView.ResizeMode.Stretch)
            self.model.setHeaderAlignment(4, QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignVCenter)

    def clientes(self):
        linha = self.tabela.selectionModel().selectedRows()
        if linha:
            id = self.tabela.model().index(linha[0].row(), 0).data()
            self.telaVeiculoCliente = TelaVeiculoCliente()
            self.telaVeiculoCliente.renderClientes(id)
            self.telaVeiculoCliente.botaoConcluir.clicked.connect(self.listarVeiculos)
            self.telaVeiculoCliente.show()


