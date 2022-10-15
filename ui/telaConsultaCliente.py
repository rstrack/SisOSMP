from PyQt6 import QtCore, QtGui, QtWidgets
from ui.telaVeiculoCliente import TelaVeiculoCliente
from ui.infiniteScroll import AlignDelegate, InfiniteScrollTableModel
from container import handleDeps
from flatdict import FlatDict

class TelaConsultaCliente(QtWidgets.QMainWindow):
    def __init__(self):
        super(TelaConsultaCliente, self).__init__()
        self.clienteCtrl = handleDeps.getDep('CLIENTECTRL')
        self.setupUi()

    def setupUi(self):
        self.resize(1280, 760)
        self.main_frame = QtWidgets.QFrame(self)
        self.main_frame.setObjectName("main_frame")
        self.hlayout = QtWidgets.QHBoxLayout(self.main_frame)
        spacer = QtWidgets.QSpacerItem(
            20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.hlayout.addItem(spacer)
        self.framegeral = QtWidgets.QFrame(self.main_frame)
        self.framegeral.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        self.framegeral.setMaximumWidth(int(QtGui.QGuiApplication.primaryScreen().size().width()*0.6) 
            if QtGui.QGuiApplication.primaryScreen().size().width()> 1280 else QtGui.QGuiApplication.primaryScreen().size().width())
        self.hlayout.addWidget(self.framegeral)
        spacer = QtWidgets.QSpacerItem(
            20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.hlayout.addItem(spacer)
        self.vlayout = QtWidgets.QVBoxLayout(self.framegeral)
        self.vlayout.setContentsMargins(0,0,0,0)
        self.vlayout.setSpacing(0)
        self.frameBusca = QtWidgets.QFrame(self.main_frame)
        self.vlayout.addWidget(self.frameBusca)
        self.hlayoutBusca = QtWidgets.QHBoxLayout(self.frameBusca)
        self.lineEditBusca = QtWidgets.QLineEdit(self.frameBusca)
        self.lineEditBusca.setFixedHeight(30)
        self.lineEditBusca.setPlaceholderText("Pesquisar")
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
        self.framedados = QtWidgets.QFrame(self.main_frame)
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
        # self.delegateLeft = AlignDelegate(QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.delegateRight = AlignDelegate(QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.tabela.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.tabela.verticalHeader().setVisible(False)
        self.filter = QtCore.QSortFilterProxyModel()
        self.filter.setFilterCaseSensitivity(
            QtCore.Qt.CaseSensitivity.CaseInsensitive)

        self.framebotoes = QtWidgets.QFrame(self.main_frame)
        self.vlayout.addWidget(self.framebotoes)
        self.hlayoutbotoes = QtWidgets.QHBoxLayout(self.framebotoes)
        spacer = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.hlayoutbotoes.addItem(spacer)
        self.botaoEditar = QtWidgets.QPushButton(self.framebotoes)
        self.botaoEditar.setFixedSize(100, 35)
        self.botaoEditar.setObjectName('botaoprincipal')
        self.hlayoutbotoes.addWidget(self.botaoEditar)
        self.botaoVeiculos = QtWidgets.QPushButton(self.framebotoes)
        self.botaoVeiculos.setFixedSize(100, 35)
        self.hlayoutbotoes.addWidget(self.botaoVeiculos)
        self.botaoExcluir = QtWidgets.QPushButton(self.framebotoes)
        self.botaoExcluir.setObjectName('excluir')
        self.botaoExcluir.setFixedSize(100, 35)
        self.hlayoutbotoes.addWidget(self.botaoExcluir)
        self.filter.setFilterKeyColumn(-1)
        self.lineEditBusca.textChanged.connect(
            self.filter.setFilterRegularExpression)
        self.tabela.setModel(self.filter)
        self.setCentralWidget(self.main_frame)
        self.retranslateUi()
        self.listarClientes()
        self.botaoRefresh.clicked.connect(self.listarClientes)
        self.botaoVeiculos.clicked.connect(self.veiculos)
        self.botaoExcluir.clicked.connect(self.excluirCliente)
        self.tabela.verticalScrollBar().valueChanged.connect(self.scrolled)
        self.tabela.verticalScrollBar().actionTriggered.connect(self.scrolled)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Busca"))
        self.botaoEditar.setText(_translate("MainWindow", "Editar"))
        self.botaoVeiculos.setText(_translate("MainWindow", "Veiculos"))
        self.botaoExcluir.setText(_translate("MainWindow", "Excluir"))

    def scrolled(self, value):
        if value == self.tabela.verticalScrollBar().maximum():
            self.maisClientes(50)

    def maisClientes(self, qtde):
        clientes = self.clienteCtrl.listarClientes(qtde=self.linhasCarregadas+qtde)
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
        colunas = ['idCliente', 'tipo', 'nome', 'documento', 'endereco', 'numero', 'bairro', 'cidade.nome', 'cidade.uf', 'fones', 'veiculos']
        self.model.colunasDesejadas(colunas)
        self.model.setRowCount(self.linhasCarregadas)
        self.model.setColumnCount(len(colunas))
        self.tabela.hideColumn(0)

    def listarClientes(self):
        self.linhasCarregadas = 0
        self.model = InfiniteScrollTableModel([{}])
        listaHeader = ['ID', 'Tipo', 'Nome', 'Documento', 'Endereço', 'Nº', 'Bairro', 'Cidade', 'UF', 'Telefones', 'Veículos']
        self.model.setHorizontalHeaderLabels(listaHeader)
        self.filter.setSourceModel(self.model)
        self.tabela.setModel(self.filter)
        self.tabela.setItemDelegateForColumn(5, self.delegateRight)
        self.maisClientes(50)
        if self.linhasCarregadas > 0:
            header = self.tabela.horizontalHeader()
            header.setSectionResizeMode(
                QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
            header.setSectionResizeMode(9, 
                QtWidgets.QHeaderView.ResizeMode.Interactive)
            header.setStretchLastSection(True)
            self.model.setHeaderAlignment(5, QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignVCenter)

    def editarCliente(self):
        linha = self.tabela.selectionModel().selectedRows()
        if linha:
            return self.tabela.model().index(linha[0].row(), 0).data()

    def excluirCliente(self):
        try:
            linha = self.tabela.selectionModel().selectedRows()
            if linha:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Aviso")
                msgBox.setText('Tem certeza que deseja excluir?')
                y = msgBox.addButton("Sim", QtWidgets.QMessageBox.ButtonRole.YesRole)
                n = msgBox.addButton("Não", QtWidgets.QMessageBox.ButtonRole.NoRole)
                y.setFixedWidth(60)
                n.setFixedWidth(60)
                msgBox.exec()
                if msgBox.clickedButton() == y:
                    id = self.tabela.model().index(linha[0].row(), 0).data()
                    r = self.clienteCtrl.excluirCliente(id)
                    if isinstance(r, Exception):
                        raise Exception(r)
                    if r:
                        msg = QtWidgets.QMessageBox()
                        msg.setWindowIcon(QtGui.QIcon('./resources/logo-icon.png'))
                        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                        msg.setWindowTitle("Aviso")
                        msg.setText(f"Cliente excluído com sucesso!")
                        msg.exec()
                    else: raise Exception('Erro ao excluir')
        except Exception as e:
            msg = QtWidgets.QMessageBox()
            msg.setWindowIcon(QtGui.QIcon('./resources/logo-icon.png'))
            msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg.setWindowTitle("Erro")
            msg.setText(str(e))
            msg.exec()

    def veiculos(self):
        linha = self.tabela.selectionModel().selectedRows()
        if linha:
            id = self.tabela.model().index(linha[0].row(), 0).data()
            self.telaVeiculoCliente = TelaVeiculoCliente()
            self.telaVeiculoCliente.renderVeiculos(id)
            self.telaVeiculoCliente.show()
