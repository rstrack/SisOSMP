from PyQt6 import QtCore, QtGui, QtWidgets

class TelaConsultaAux(QtWidgets.QWidget):
    def __init__(self, MainWindow):
        super(TelaConsultaAux, self).__init__()
        self.setupUi(MainWindow)

    def setupUi(self, MainWindow):
        MainWindow.resize(800, 600)
        self.mainwidget = QtWidgets.QWidget(MainWindow)
        self.vlayout = QtWidgets.QVBoxLayout(self.mainwidget)
        self.frameBusca = QtWidgets.QFrame(self.mainwidget)
        self.vlayout.addWidget(self.frameBusca)
        self.vlayoutBusca = QtWidgets.QVBoxLayout(self.frameBusca)
        self.lineEditBusca = QtWidgets.QLineEdit(self.frameBusca)
        self.vlayoutBusca.addWidget(self.lineEditBusca)
        
        self.framedados = QtWidgets.QFrame(self.mainwidget)
        self.vlayout.addWidget(self.framedados)
        self.vlayoutdados = QtWidgets.QVBoxLayout(self.framedados)
        self.tabela = QtWidgets.QTableView(self.framedados)
        self.vlayoutdados.addWidget(self.tabela)
        self.tabela.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tabela.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)

        self.filter = QtCore.QSortFilterProxyModel()
        self.filter.setFilterCaseSensitivity(QtCore.Qt.CaseSensitivity.CaseInsensitive)

        self.framebotoes = QtWidgets.QFrame(self.mainwidget)
        self.vlayout.addWidget(self.framebotoes)
        self.hlayoutbotoes = QtWidgets.QHBoxLayout(self.framebotoes)
        self.botaoSelecionar = QtWidgets.QPushButton(self.framebotoes)
        self.hlayoutbotoes.addWidget(self.botaoSelecionar)


        MainWindow.setCentralWidget(self.mainwidget)
        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Busca"))
        self.botaoSelecionar.setText(_translate("MainWindow", "Selecionar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = TelaConsultaAux(MainWindow)
    ui.setupUi(MainWindow)
    MainWindow.show()

    style = open('./ui/styles.qss').read()
    app.setStyleSheet(style)

    sys.exit(app.exec())