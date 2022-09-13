from PyQt6 import QtCore, QtGui, QtWidgets

from controller.orcamentoController import OrcamentoController

class TelaConsultaOrcamento(QtWidgets.QMainWindow):
    def __init__(self):
        super(TelaConsultaOrcamento, self).__init__()
        self.controller = OrcamentoController(view=self)
        self.setupUi()

    def setupUi(self):
        self.mainwidget = QtWidgets.QWidget(self)
        self.glayout = QtWidgets.QGridLayout(self.mainwidget)
        self.frameBusca = QtWidgets.QFrame(self.mainwidget)
        self.glayout.addWidget(self.frameBusca, 0, 0, 1, -1)
        self.hlayoutBusca = QtWidgets.QHBoxLayout(self.frameBusca)
        self.lineEditBusca = QtWidgets.QLineEdit(self.frameBusca)
        self.lineEditBusca.setPlaceholderText("Pesquisar")
        self.lineEditBusca.setClearButtonEnabled(True)
        iconBusca = QtGui.QIcon("./resources/search-icon.png")
        self.lineEditBusca.addAction(iconBusca, QtWidgets.QLineEdit.ActionPosition.LeadingPosition)
        self.hlayoutBusca.addWidget(self.lineEditBusca)
        self.botaoRefresh = QtWidgets.QPushButton(self.frameBusca)
        self.botaoRefresh.setIcon(QtGui.QIcon("./resources/refresh-icon.png"))
        self.hlayoutBusca.addWidget(self.botaoRefresh)
        self.framedados = QtWidgets.QFrame(self.mainwidget)
        self.glayout.addWidget(self.framedados, 1, 0, 1, 1)
        self.vlayoutdados = QtWidgets.QVBoxLayout(self.framedados)
        self.tabela = QtWidgets.QTableView(self.framedados)
        self.vlayoutdados.addWidget(self.tabela)
        self.tabela.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tabela.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.tabela.verticalHeader().setVisible(False)
        self.filter = QtCore.QSortFilterProxyModel()
        self.filter.setFilterCaseSensitivity(QtCore.Qt.CaseSensitivity.CaseInsensitive)
        
        self.framedetalhes = QtWidgets.QFrame(self.mainwidget)
        self.glayout.addWidget(self.framedetalhes, 1, 1, 1, 1)
        self.glayout.setColumnStretch(0,2)
        self.glayout.setColumnStretch(1,1)

        self.vlayoutdetalhes = QtWidgets.QVBoxLayout(self.framedetalhes)
        self.labelDetalhesT = QtWidgets.QLabel(self.framedetalhes)
        self.vlayoutdetalhes.addWidget(self.labelDetalhesT)
        self.labelDetalhesD = QtWidgets.QLabel(self.framedetalhes)
        self.labelDetalhesD.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        self.vlayoutdetalhes.addWidget(self.labelDetalhesD)
        self.labelDetalhesT.setText("DETALHES")
        
        self.framebotoes = QtWidgets.QFrame(self.mainwidget)
        self.glayout.addWidget(self.framebotoes, 2, 0, 1, -1)
        self.hlayoutbotoes = QtWidgets.QHBoxLayout(self.framebotoes)
        spacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.hlayoutbotoes.addItem(spacer)
        self.botaoEditar = QtWidgets.QPushButton(self.framebotoes)
        self.botaoEditar.setFixedSize(100, 25)
        self.hlayoutbotoes.addWidget(self.botaoEditar)
        self.model = QtGui.QStandardItemModel()
        self.filter.setSourceModel(self.model)
        self.filter.setFilterKeyColumn(-1)
        self.lineEditBusca.textChanged.connect(self.filter.setFilterRegularExpression)
        self.tabela.setModel(self.filter)
        self.setCentralWidget(self.mainwidget)
        self.retranslateUi()
        self.selectionModel = self.tabela.selectionModel()
        self.selectionModel.selectionChanged.connect(self.mostrarDetalhes)
        self.listarOrcamentos()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Busca"))
        self.botaoEditar.setText(_translate("MainWindow", "Editar"))


    def listarOrcamentos(self):
        orcamentos = self.controller.getOrcamentos()
        self.model.setRowCount(len(orcamentos))
        listaHeader = ['ID', 'Data', 'Cliente','Veículo']
        self.model.setHorizontalHeaderLabels(listaHeader)
        row=0
        for orcamento in orcamentos:
            item = QtGui.QStandardItem(str(orcamento.idOrcamento))
            item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.model.setItem(row, 0, item)
            item = QtGui.QStandardItem(str(orcamento.dataOrcamento))
            item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.model.setItem(row, 1, item)
            cliente = self.controller.getClienteByID(orcamento.cliente)
            item = QtGui.QStandardItem(cliente.nome)
            item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.model.setItem(row, 2, item)
            veiculo = self.controller.getVeiculoByID(orcamento.veiculo)               
            item = QtGui.QStandardItem(veiculo.modelo)
            item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.model.setItem(row, 3, item)
            row=row+1    
        header = self.tabela.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Interactive)
        header.setSectionResizeMode(0,QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        header.setStretchLastSection(True)

    def mostrarDetalhes(self):
        self.linha = self.tabela.selectionModel().selectedRows()
        if self.linha:
            id = self.tabela.model().index(self.linha[0].row(),0).data()
            orcamento = self.controller.getOrcamentoByID(id)
            self.labelDetalhesD.setText(
f"""ID: {orcamento.idOrcamento}
Data do orçamento: {str(orcamento.dataOrcamento)}        
""")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    ui = TelaConsultaOrcamento()
    ui.setupUi()
    ui.show()

    style = open('./ui/styles.qss').read()
    app.setStyleSheet(style)

    sys.exit(app.exec())

