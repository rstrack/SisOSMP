from PyQt6 import QtCore, QtGui, QtWidgets
from flatdict import FlatDict
from util.container import handleDeps
from ui.infiniteScroll import AlignDelegate, InfiniteScrollTableModel
from ui.telaVeiculoCliente import TelaVeiculoCliente

class TelaBuscaCliente(QtWidgets.QMainWindow):
    def __init__(self):
        super(TelaBuscaCliente, self).__init__()
        self.clienteCtrl = handleDeps.getDep('CLIENTECTRL')
        self.busca = ''
        self.orderBy = 0
        self.setupUi()

    def setupUi(self):
        self.resize(800, 600)
        self.mainwidget = QtWidgets.QWidget(self)
        self.vlayout = QtWidgets.QVBoxLayout(self.mainwidget)
        self.frameBusca = QtWidgets.QFrame(self.mainwidget)
        self.vlayout.addWidget(self.frameBusca)
        self.hlayoutBusca = QtWidgets.QHBoxLayout(self.frameBusca)
        self.lineEditBusca = QtWidgets.QLineEdit(self.frameBusca)
        self.lineEditBusca.setFixedHeight(30)
        self.lineEditBusca.setPlaceholderText("Pesquisar por nome, documento, fone, modelo ou placa de um veículo vinculado")
        self.lineEditBusca.setClearButtonEnabled(True)
        iconBusca = QtGui.QIcon("./resources/search-icon.png")
        self.lineEditBusca.addAction(
            iconBusca, QtWidgets.QLineEdit.ActionPosition.LeadingPosition)
        self.hlayoutBusca.addWidget(self.lineEditBusca)
        self.botaoRefresh = QtWidgets.QPushButton(self.frameBusca)
        self.botaoRefresh.setToolTip('Atualizar')
        self.botaoRefresh.setFixedSize(30,30)
        self.botaoRefresh.setIcon(QtGui.QIcon("./resources/refresh-icon.png"))
        self.hlayoutBusca.addWidget(self.botaoRefresh)
        self.frameOrdenacao = QtWidgets.QFrame(self.mainwidget)
        self.vlayout.addWidget(self.frameOrdenacao)
        self.hlayoutOrdenacao = QtWidgets.QHBoxLayout(self.frameOrdenacao)
        spacer = QtWidgets.QSpacerItem(
            20, 10, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        self.hlayoutOrdenacao.addItem(spacer)
        self.comboBoxOrdenacao = QtWidgets.QComboBox(self.frameOrdenacao)
        self.comboBoxOrdenacao.setToolTip('Ordenar')
        self.comboBoxOrdenacao.addItems(['Nome: A-Z', 'Nome: Z-A'])
        self.hlayoutOrdenacao.addWidget(self.comboBoxOrdenacao)
        self.framedados = QtWidgets.QFrame(self.mainwidget)
        self.framedados.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        self.vlayout.addWidget(self.framedados)
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
        self.delegateRight = AlignDelegate(QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.tabela.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.tabela.verticalHeader().setVisible(False)
        self.framebotoes = QtWidgets.QFrame(self.mainwidget)
        self.vlayout.addWidget(self.framebotoes)
        self.hlayoutbotoes = QtWidgets.QHBoxLayout(self.framebotoes)
        spacer = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.hlayoutbotoes.addItem(spacer)
        self.botaoSelecionar = QtWidgets.QPushButton(self.framebotoes)
        self.botaoSelecionar.setFixedSize(100, 25)
        self.hlayoutbotoes.addWidget(self.botaoSelecionar)
        self.botaoVeiculos = QtWidgets.QPushButton(self.framebotoes)
        self.botaoVeiculos.setFixedSize(100, 25)
        self.hlayoutbotoes.addWidget(self.botaoVeiculos)
        self.setCentralWidget(self.mainwidget)
        self.retranslateUi()
        self.listarClientes()
        self.botaoRefresh.clicked.connect(self.listarClientes)
        self.botaoVeiculos.clicked.connect(self.veiculos)
        self.tabela.verticalScrollBar().valueChanged.connect(self.scrolled)
        self.tabela.verticalScrollBar().actionTriggered.connect(self.scrolled)
        self.lineEditBusca.textChanged.connect(self.buffer)
        self.comboBoxOrdenacao.currentIndexChanged.connect(self.buffer)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Busca por Cliente"))
        self.botaoSelecionar.setText(_translate("MainWindow", "Selecionar"))
        self.botaoVeiculos.setText(_translate("MainWindow", "Veiculos"))

    def scrolled(self, value):
        if value == self.tabela.verticalScrollBar().maximum():
            self.maisClientes(50)

    def buffer(self):
        self.busca = self.lineEditBusca.text()
        self.orderBy = self.comboBoxOrdenacao.currentIndex()
        self.listarClientes()

    def maisClientes(self, qtde):
        clientes = self.clienteCtrl.buscarCliente(self.busca, self.linhasCarregadas+qtde, self.orderBy)
        if not clientes:
            return
        maxLength = len(clientes)
        remainderRows = maxLength-self.linhasCarregadas
        rowsToFetch=min(qtde, remainderRows)
        if rowsToFetch<=0:
            return
        initLen = self.linhasCarregadas
        maxRows = self.linhasCarregadas + rowsToFetch
        while self.linhasCarregadas < maxRows:
            if clientes[self.linhasCarregadas]['tipo']=='0': clientes[self.linhasCarregadas]['tipo'] = 'PESSOA FÍSICA'
            elif clientes[self.linhasCarregadas]['tipo']=='1': clientes[self.linhasCarregadas]['tipo'] = 'PESSOA JURIDICA'
            else: clientes[self.linhasCarregadas]['tipo'] = 'ESTRANGEIRO'
            if clientes[self.linhasCarregadas]['cidade'] == None:
                clientes[self.linhasCarregadas]['cidade'] = {'nome':None, 'uf':None}
            queryFones = self.clienteCtrl.listarFones(clientes[self.linhasCarregadas]['idCliente'])
            if queryFones:
                fones = []
                for fone in queryFones:
                    fones.append(fone['fone'])
                clientes[self.linhasCarregadas]['fones'] = (', '.join(fones))
            else: clientes[self.linhasCarregadas]['fones'] = ''
            queryVeiculo = self.clienteCtrl.listarVeiculos(clientes[self.linhasCarregadas]['idCliente'])
            if queryVeiculo:
                nomes = []
                for veiculo in queryVeiculo:
                    nomes.append(': '.join([veiculo['modelo'], veiculo['placa']]))
                clientes[self.linhasCarregadas]['veiculos'] = ', '.join(nomes)
            else: clientes[self.linhasCarregadas]['veiculos'] = ''
            clientes[self.linhasCarregadas] = FlatDict(clientes[self.linhasCarregadas], delimiter='.')
            self.linhasCarregadas+=1
        self.model.addData(clientes[initLen:self.linhasCarregadas])
        colunas = ['idCliente', 'tipo', 'nome', 'documento', 'fones', 'veiculos']
        self.model.colunasDesejadas(colunas)
        self.model.setRowCount(self.linhasCarregadas)
        self.model.setColumnCount(len(colunas))
        self.tabela.hideColumn(0)

    def listarClientes(self):
        self.linhasCarregadas = 0
        self.model = InfiniteScrollTableModel([{}])
        listaHeader = ['ID', 'Tipo', 'Nome', 'Documento', 'Telefones', 'Veículos']
        self.model.setHorizontalHeaderLabels(listaHeader)
        self.tabela.setModel(self.model)
        self.maisClientes(50)
        if self.linhasCarregadas > 0:
            header = self.tabela.horizontalHeader()
            header.setSectionResizeMode(
                QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
            header.setStretchLastSection(True)

    def veiculos(self):
        linha = self.tabela.selectionModel().selectedRows()
        if linha:
            id = self.tabela.model().index(linha[0].row(), 0).data()
            self.telaVeiculoCliente = TelaVeiculoCliente()
            self.telaVeiculoCliente.renderVeiculos(id)
            self.telaVeiculoCliente.botaoConcluir.clicked.connect(self.listarClientes)
            self.telaVeiculoCliente.show()

