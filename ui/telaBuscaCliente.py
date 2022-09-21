from PyQt6 import QtCore, QtGui, QtWidgets
from routes import handleRoutes

from controller.clienteController import ClienteController


class TelaBuscaCliente(QtWidgets.QWidget):
    def __init__(self, MainWindow):
        super(TelaBuscaCliente, self).__init__()
        self.setupUi(MainWindow)
        self.clienteCtrl = handleRoutes.getRoute('CLIENTE')

    def setupUi(self, MainWindow):
        MainWindow.resize(600, 400)
        self.mainwidget = QtWidgets.QWidget(MainWindow)
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
        self.botaoSelecionar = QtWidgets.QPushButton(self.framebotoes)
        self.botaoSelecionar.setFixedSize(100, 25)
        self.hlayoutbotoes.addWidget(self.botaoSelecionar)
        self.model = QtGui.QStandardItemModel()
        self.filter.setSourceModel(self.model)
        listaHeader = ['ID', 'Nome', 'Documento', 'Veículos']
        self.model.setHorizontalHeaderLabels(listaHeader)
        self.filter.setFilterKeyColumn(-1)
        self.lineEditBusca.textChanged.connect(
            self.filter.setFilterRegularExpression)
        self.tabela.setModel(self.filter)

        MainWindow.setCentralWidget(self.mainwidget)
        self.retranslateUi(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Selecionar Cliente"))
        self.botaoSelecionar.setText(_translate("MainWindow", "Selecionar"))

    def listarClientes(self):
        clientes = self.clienteCtrl.listarClientes()
        if not clientes:
            return
        self.model.setRowCount(len(clientes))
        row = 0
        for cliente in clientes:
            item = QtGui.QStandardItem(str(cliente['idCliente']))
            item.setTextAlignment(
                QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.model.setItem(row, 0, item)
            item = QtGui.QStandardItem(cliente['nome'])
            item.setTextAlignment(
                QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.model.setItem(row, 1, item)
            item = QtGui.QStandardItem(cliente['documento'])
            item.setTextAlignment(
                QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.model.setItem(row, 2, item)
            queryVeiculo = self.clienteCtrl.listarVeiculos(cliente)
            nomes = []
            if queryVeiculo:
                for veiculo in queryVeiculo:
                    nomes.append(': '.join([veiculo['modelo'], veiculo['placa']]))
                item = QtGui.QStandardItem(', '.join(nomes))
                self.model.setItem(row, 3, item)
            row = row+1
        header = self.tabela.horizontalHeader()
        header.setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.Interactive)
        header.setSectionResizeMode(
            0, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        header.setStretchLastSection(True)

    def usarCliente(self):
        self.linha = self.tabela.selectionModel().selectedRows()
        if self.linha:
            id = self.tabela.model().index(self.linha[0].row(), 0).data()
            cliente = self.clienteCtrl.getCliente(id)
        self.window.close()
        return cliente

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = TelaBuscaCliente(MainWindow)
    ui.listarClientes()
    MainWindow.show()

    style = open('./resources/styles.qss').read()
    app.setStyleSheet(style)

    sys.exit(app.exec())
