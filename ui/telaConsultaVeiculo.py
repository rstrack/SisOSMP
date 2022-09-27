from PyQt6 import QtCore, QtGui, QtWidgets
from routes import handleRoutes

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
        listaHeader = ['ID', 'Marca', 'Modelo', 'Placa', 'Ano', 'Clientes Vinculados']
        self.model.setHorizontalHeaderLabels(listaHeader)
        self.setCentralWidget(self.mainwidget)
        self.retranslateUi()
        self.selectionModel = self.tabela.selectionModel()

        self.listarVeiculos()

        #self.selectionModel.selectionChanged.connect(self.mostrarDetalhes)
        self.botaoRefresh.clicked.connect(self.listarVeiculos)
        '''self.botaoEditar.clicked.connect(self.editarVeiculo2)'''

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Busca"))
        self.botaoEditar.setText(_translate("MainWindow", "Editar"))

    def listarVeiculos(self):
        veiculos = self.clienteCtrl.listarVeiculos()
        if not veiculos:
            return
        self.model.setRowCount(len(veiculos))
        row = 0
        for veiculo in veiculos:
            item = QtGui.QStandardItem()
            item.setData(veiculo['idVeiculo'], QtCore.Qt.ItemDataRole.DisplayRole)
            item.setTextAlignment(
                QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.model.setItem(row, 0, item)
            marca = self.marcaCtrl.getMarca(veiculo['marca'])
            item = QtGui.QStandardItem()
            item.setData(marca['nome'], QtCore.Qt.ItemDataRole.DisplayRole)
            item.setTextAlignment(
                QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.model.setItem(row, 1, item)
            item = QtGui.QStandardItem()
            item.setData(veiculo['modelo'], QtCore.Qt.ItemDataRole.DisplayRole)
            item.setTextAlignment(
                QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.model.setItem(row, 2, item)
            item = QtGui.QStandardItem(str(veiculo['placa'] or ''))
            item.setTextAlignment(
                QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.model.setItem(row, 3, item)
            item = QtGui.QStandardItem(str(veiculo['ano'] or ''))
            item.setTextAlignment(
                QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.model.setItem(row, 4, item)
            row = row+1
        header = self.tabela.horizontalHeader()
        header.setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.Interactive)

    '''def editarVeiculo(self):
        self.linha = self.tabela.selectionModel().selectedRows()
        if self.linha:
            return self.tabela.model().index(self.linha[0].row(), 0).data()

    def editarVeiculo2(self):
        self.linha = self.tabela.selectionModel().selectedRows()
        if self.linha:
            id =  self.tabela.model().index(self.linha[0].row(), 0).data()
        self.telaEditar = TelaCadastroVeiculo()
        self.telaEditar.renderEditar(id)
        self.telaEditar.show()'''
      

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    ui = TelaConsultaVeiculo()
    
    ui.show()

    style = open('./ui/styles.qss').read()
    app.setStyleSheet(style)

    sys.exit(app.exec())
