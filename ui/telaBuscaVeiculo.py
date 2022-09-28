from PyQt6 import QtCore, QtGui, QtWidgets

from routes import handleRoutes

class TelaBuscaVeiculo(QtWidgets.QWidget):
    def __init__(self, MainWindow):
        super(TelaBuscaVeiculo, self).__init__()
        self.clienteCtrl = handleRoutes.getRoute('CLIENTECTRL')
        self.setupUi(MainWindow)

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
        self.filter.setFilterKeyColumn(-1)
        self.lineEditBusca.textChanged.connect(
            self.filter.setFilterRegularExpression)
        self.tabela.setModel(self.filter)

        MainWindow.setCentralWidget(self.mainwidget)
        self.retranslateUi(MainWindow)
        self.listarVeiculos()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Busca"))
        self.botaoSelecionar.setText(_translate("MainWindow", "Selecionar"))

    def listarVeiculos(self):
        veiculos = self.clienteCtrl.listarVeiculos()
        if not veiculos:
            return
        self.model.setRowCount(len(veiculos))
        row = 0
        for veiculo in veiculos:
            item = QtGui.QStandardItem(str(veiculo['idVeiculo']))
            item.setTextAlignment(
                QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.model.setItem(row, 0, item)
            item = QtGui.QStandardItem(veiculo['modelo'])
            item.setTextAlignment(
                QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.model.setItem(row, 1, item)
            item = QtGui.QStandardItem(veiculo['placa'])
            item.setTextAlignment(
                QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.model.setItem(row, 2, item)
            queryCliente = self.clienteCtrl.listarClientes(veiculo)
            nomes = []
            if queryCliente:
                for cliente in queryCliente:
                    nomes.append(cliente['nome'])
                item = QtGui.QStandardItem(', '.join(nomes))
                self.model.setItem(row, 3, item)
            row = row+1
        header = self.tabela.horizontalHeader()
        header.setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.Interactive)
        header.setSectionResizeMode(
            0, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        header.setStretchLastSection(True)    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = TelaBuscaVeiculo(MainWindow)
    ui.setupUi(MainWindow)
    MainWindow.show()

    style = open('./ui/styles.qss').read()
    app.setStyleSheet(style)

    sys.exit(app.exec())
