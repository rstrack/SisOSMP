from PyQt6 import QtCore, QtGui, QtWidgets


class TelaConsultaPecaServico(QtWidgets.QMainWindow):
    def __init__(self):
        super(TelaConsultaPecaServico, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(1280, 720)
        self.mainwidget = QtWidgets.QWidget(self)
        self.vlayout = QtWidgets.QVBoxLayout(self.mainwidget)
        self.frameBusca = QtWidgets.QFrame(self.mainwidget)
        self.vlayout.addWidget(self.frameBusca)
        self.vlayoutBusca = QtWidgets.QVBoxLayout(self.frameBusca)
        self.lineEditBusca = QtWidgets.QLineEdit(self.frameBusca)
        self.lineEditBusca.setFixedSize(250, 25)
        self.lineEditBusca.setPlaceholderText("Pesquisar")
        self.lineEditBusca.setClearButtonEnabled(True)
        iconBusca = QtGui.QIcon("./resources/search-icon.png")
        self.lineEditBusca.addAction(
            iconBusca, QtWidgets.QLineEdit.ActionPosition.LeadingPosition)
        self.vlayoutBusca.addWidget(
            self.lineEditBusca, 0, QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.framedados = QtWidgets.QFrame(self.mainwidget)
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
        self.tabela.verticalHeader().setVisible(False)
        self.filter = QtCore.QSortFilterProxyModel()
        self.filter.setFilterCaseSensitivity(
            QtCore.Qt.CaseSensitivity.CaseInsensitive)
        self.framebotoes = QtWidgets.QFrame(self.mainwidget)
        self.vlayout.addWidget(
            self.framebotoes, 0, QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.hlayoutbotoes = QtWidgets.QHBoxLayout(self.framebotoes)
        self.botaoEditar = QtWidgets.QPushButton(self.framebotoes)
        self.botaoEditar.setFixedSize(120, 30)
        self.hlayoutbotoes.addWidget(self.botaoEditar)
        self.botaoExcluir = QtWidgets.QPushButton(self.framebotoes)
        self.botaoExcluir.setObjectName("excluir")
        self.botaoExcluir.setFixedSize(120, 30)
        self.hlayoutbotoes.addWidget(self.botaoExcluir)
        self.model = QtGui.QStandardItemModel()
        listaHeader = ['ID', 'Descrição', 'Valor']
        self.model.setHorizontalHeaderLabels(listaHeader)
        self.filter.setSourceModel(self.model)
        self.filter.setFilterKeyColumn(-1)
        self.lineEditBusca.textChanged.connect(
            self.filter.setFilterRegularExpression)
        self.tabela.setModel(self.filter)
        self.header = self.tabela.horizontalHeader()
        self.header.setSectionResizeMode(
            1, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.header.setSectionResizeMode(
            0, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.setCentralWidget(self.mainwidget)
        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Busca"))
        self.botaoEditar.setText(_translate("MainWindow", "Editar"))
        self.botaoExcluir.setText(_translate("MainWindow", "Excluir"))

    def getLinha(self):
        linha = self.viewBusca.tabela.selectionModel().selectedRows()[0]
        id = self.viewBusca.tabela.model().index(linha.row(), 0).data()
        return id


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = TelaConsultaPecaServico()
    ui.setupUi()
    ui.show()

    style = open('./ui/styles.qss').read()
    app.setStyleSheet(style)

    sys.exit(app.exec())
