from PyQt6 import QtCore, QtGui, QtWidgets
from routes import handleRoutes
from ui.infiniteScroll import InfiniteScrollTableModel
from flatdict import FlatDict

class TelaConsultaVeiculo(QtWidgets.QMainWindow):
    def __init__(self):
        super(TelaConsultaVeiculo, self).__init__()
        self.clienteCtrl = handleRoutes.getRoute('CLIENTECTRL')
        self.marcaCtrl = handleRoutes.getRoute('MARCACTRL')
        self.setupUi()

    def setupUi(self):
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
        self.filter = QtCore.QSortFilterProxyModel()
        self.filter.setFilterCaseSensitivity(
            QtCore.Qt.CaseSensitivity.CaseInsensitive)

        self.framebotoes = QtWidgets.QFrame(self.mainwidget)
        self.glayout.addWidget(self.framebotoes, 2, 0, 1, 1)
        self.hlayoutbotoes = QtWidgets.QHBoxLayout(self.framebotoes)
        spacer = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.hlayoutbotoes.addItem(spacer)
        self.botaoEditar = QtWidgets.QPushButton(self.framebotoes)
        self.botaoEditar.setFixedSize(100, 25)
        self.hlayoutbotoes.addWidget(self.botaoEditar)
        self.model = InfiniteScrollTableModel([{}])
        self.filter.setSourceModel(self.model)
        self.filter.setFilterKeyColumn(-1)
        self.lineEditBusca.textChanged.connect(
            self.filter.setFilterRegularExpression)
        self.tabela.setModel(self.filter)
        listaHeader = ['ID', 'Marca', 'Modelo', 'Placa', 'Ano', 'Veiculos Vinculados']
        self.model.setHorizontalHeaderLabels(listaHeader)
        self.setCentralWidget(self.mainwidget)
        self.retranslateUi()
        self.selectionModel = self.tabela.selectionModel()

        self.listarVeiculos()
        self.botaoRefresh.clicked.connect(self.listarVeiculos)
        self.tabela.verticalScrollBar().valueChanged.connect(self.scrolled)
        self.tabela.verticalScrollBar().actionTriggered.connect(self.scrolled)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Busca"))
        self.botaoEditar.setText(_translate("MainWindow", "Editar"))

    def scrolled(self, value):
        if value == self.tabela.verticalScrollBar().maximum():
            self.maisVeiculos(50)
            # threading.Thread(target=self.maisVeiculos, args=(100,)).start()

    def maisVeiculos(self, qtde):
        veiculos = self.clienteCtrl.listarVeiculos()
        if not veiculos:
            return
        veiculos = list(reversed(veiculos))
        maxLength = len(veiculos)
        remainderRows = maxLength-self.linesShowed
        rowsToFetch=min(qtde, remainderRows)
        if rowsToFetch<=0:
            return
        initLen = self.linesShowed
        maxRows = self.linesShowed + rowsToFetch
        while self.linesShowed < maxRows:
            queryClientes = self.clienteCtrl.listarClientes(veiculos[self.linesShowed])
            if queryClientes:
                nomes = []
                for cliente in queryClientes:
                    nomes.append(cliente['nome'])
                veiculos[self.linesShowed]['clientes'] = ', '.join(nomes)
            else: veiculos[self.linesShowed]['clientes'] = ''
            veiculos[self.linesShowed] = FlatDict(veiculos[self.linesShowed], delimiter='.')
            self.linesShowed+=1
        self.model.addData(veiculos[initLen:self.linesShowed])
        colunas = ['idVeiculo', 'marca.nome', 'modelo', 'placa', 'ano', 'clientes']
        self.model.colunasDesejadas(colunas)
        self.model.setRowCount(self.linesShowed)
        self.model.setColumnCount(len(colunas))

    def listarVeiculos(self):
        self.linesShowed = 0
        self.model = InfiniteScrollTableModel([{}])
        listaHeader = ['ID', 'Marca', 'Modelo', 'Placa', 'Ano', 'Veiculos Vinculados']
        self.model.setHorizontalHeaderLabels(listaHeader)
        self.filter.setSourceModel(self.model)
        self.tabela.setModel(self.filter)
        self.maisVeiculos(50)

    def editarVeiculo(self):
        self.linha = self.tabela.selectionModel().selectedRows()
        if self.linha:
            return self.tabela.model().index(self.linha[0].row(), 0).data()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    ui = TelaConsultaVeiculo()
    
    ui.show()

    style = open('./ui/styles.qss').read()
    app.setStyleSheet(style)

    sys.exit(app.exec())
