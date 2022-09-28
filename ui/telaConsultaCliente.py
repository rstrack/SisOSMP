from PyQt6 import QtCore, QtGui, QtWidgets
from routes import handleRoutes
from ui.telaCadastroCliente import TelaCadastroCliente

class TelaConsultaCliente(QtWidgets.QMainWindow):
    def __init__(self):
        super(TelaConsultaCliente, self).__init__()
        self.clienteCtrl = handleRoutes.getRoute('CLIENTECTRL')
        self.cidadeCtrl = handleRoutes.getRoute('CIDADECTRL')
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
        self.lineEditBusca.addAction(
            iconBusca, QtWidgets.QLineEdit.ActionPosition.LeadingPosition)
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

        self.tabela.setSortingEnabled(True)

        self.framebotoes = QtWidgets.QFrame(self.mainwidget)
        self.glayout.addWidget(self.framebotoes, 2, 0, 1, 1)
        self.hlayoutbotoes = QtWidgets.QHBoxLayout(self.framebotoes)
        spacer = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.hlayoutbotoes.addItem(spacer)
        self.botaoEditar = QtWidgets.QPushButton(self.framebotoes)
        self.botaoEditar.setFixedSize(100, 25)
        self.hlayoutbotoes.addWidget(self.botaoEditar)
        self.model = QtGui.QStandardItemModel()
        self.filter.setSourceModel(self.model)
        self.filter.setFilterKeyColumn(-1)
        self.lineEditBusca.textChanged.connect(
            self.filter.setFilterRegularExpression)
        self.tabela.setModel(self.filter)
        listaHeader = ['ID', 'Tipo', 'Nome', 'Documento', 'Endereço', 'Nº', 'Bairro', 'Cidade', 'UF', 'Telefones', 'Veículos']
        self.model.setHorizontalHeaderLabels(listaHeader)
        self.setCentralWidget(self.mainwidget)
        self.retranslateUi()
        self.selectionModel = self.tabela.selectionModel()
        self.listarClientes()
        #self.selectionModel.selectionChanged.connect(self.mostrarDetalhes)
        self.botaoRefresh.clicked.connect(self.listarClientes)
        self.botaoEditar.clicked.connect(self.editarCliente2)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Busca"))
        self.botaoEditar.setText(_translate("MainWindow", "Editar"))

    def listarClientes(self):
        clientes = self.clienteCtrl.listarClientes()
        if not clientes:
            return
        self.model.setRowCount(len(clientes))
        row = 0
        for cliente in reversed(clientes):
            #item = QtGui.QStandardItem(str(cliente['idCliente']))
            item = QtGui.QStandardItem()
            item.setData(cliente['idCliente'], QtCore.Qt.ItemDataRole.DisplayRole)
            item.setTextAlignment(
                QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.model.setItem(row, 0, item)
            if cliente['tipo']=='0': tipo = 'PESSOA FÍSICA'
            elif cliente['tipo']=='1': tipo = 'PESSOA JURIDICA'
            elif cliente['tipo']=='2': tipo = 'ESTRANGEIRO'
            else: tipo = ''
            item = QtGui.QStandardItem()
            item.setData(tipo, QtCore.Qt.ItemDataRole.DisplayRole)
            item.setTextAlignment(
                QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.model.setItem(row, 1, item)
            item = QtGui.QStandardItem()
            item.setData(cliente['nome'], QtCore.Qt.ItemDataRole.DisplayRole)
            item.setTextAlignment(
                QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.model.setItem(row, 2, item)
            item = QtGui.QStandardItem()
            item.setData(cliente['documento'], QtCore.Qt.ItemDataRole.DisplayRole)
            item.setTextAlignment(
                QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.model.setItem(row, 3, item)
            item = QtGui.QStandardItem(str(cliente['endereco'] or ''))
            item.setTextAlignment(
                QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.model.setItem(row, 4, item)
            item = QtGui.QStandardItem(str(cliente['numero'] or ''))
            item.setTextAlignment(
                QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.model.setItem(row, 5, item)
            item = QtGui.QStandardItem(str(cliente['bairro'] or ''))
            item.setTextAlignment(
                QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.model.setItem(row, 6, item)
            if cliente['cidade'] != None:
                cidade = self.cidadeCtrl.getCidade(cliente['cidade'])
                item = QtGui.QStandardItem(str(cidade['nome'] or ''))
                item.setTextAlignment(
                    QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
                self.model.setItem(row, 7, item)
                item = QtGui.QStandardItem(str(cidade['uf'] or ''))
                item.setTextAlignment(
                    QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
                self.model.setItem(row, 8, item)
            queryFones = self.clienteCtrl.listarFones(cliente)
            if queryFones:
                fones = []
                for fone in queryFones:
                    fones.append(fone['fone'])
                item = QtGui.QStandardItem(', '.join(fones))
                self.model.setItem(row, 9, item)
            queryVeiculo = self.clienteCtrl.listarVeiculos(cliente)
            if queryVeiculo:
                nomes = []
                for veiculo in queryVeiculo:
                    nomes.append(': '.join([veiculo['modelo'], veiculo['placa']]))
                item = QtGui.QStandardItem(', '.join(nomes))
                self.model.setItem(row, 10, item)
            row = row+1
        header = self.tabela.horizontalHeader()
        header.setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.Interactive)
        header.setSectionResizeMode(0, 
            QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(5, 
            QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(8, 
            QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        header.setStretchLastSection(True)

    def editarCliente(self):
        self.linha = self.tabela.selectionModel().selectedRows()
        if self.linha:
            return self.tabela.model().index(self.linha[0].row(), 0).data()

    def editarCliente2(self):
        self.linha = self.tabela.selectionModel().selectedRows()
        if self.linha:
            id =  self.tabela.model().index(self.linha[0].row(), 0).data()
        self.telaEditar = TelaCadastroCliente()
        self.telaEditar.renderEditar(id)
        self.telaEditar.show()
      

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    ui = TelaConsultaCliente()
    ui.setupUi()
    ui.show()

    style = open('./ui/styles.qss').read()
    app.setStyleSheet(style)

    sys.exit(app.exec())
