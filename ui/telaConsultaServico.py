from PyQt6 import QtCore, QtGui, QtWidgets
from routes import handleRoutes
from ui.infiniteScroll import AlignDelegate, InfiniteScrollTableModel
from ui.telaCadastroServico import TelaCadastroServico

class TelaConsultaServico(QtWidgets.QMainWindow):
    def __init__(self):
        super(TelaConsultaServico, self).__init__()
        self.servicoCtrl = handleRoutes.getRoute('SERVICOCTRL')
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
        self.botaoRefresh.setToolTip('Atualizar')
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
        self.delegateRight = AlignDelegate(QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignVCenter)
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
        self.filter.setFilterKeyColumn(-1)
        self.lineEditBusca.textChanged.connect(
            self.filter.setFilterRegularExpression)
        self.tabela.setModel(self.filter)
        self.setCentralWidget(self.mainwidget)
        self.retranslateUi()
        self.selectionModel = self.tabela.selectionModel()

        self.listarServicos()

        #self.selectionModel.selectionChanged.connect(self.mostrarDetalhes)
        self.botaoRefresh.clicked.connect(self.listarServicos)
        self.botaoEditar.clicked.connect(self.editarServico)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Busca"))
        self.botaoEditar.setText(_translate("MainWindow", "Editar"))

    def scrolled(self, value):
        if value == self.tabela.verticalScrollBar().maximum():
            self.maisServicos(50)

    def maisServicos(self, qtde):
        servicos = self.servicoCtrl.listarServicos()
        if not servicos:
            return
        maxLength = len(servicos)
        remainderRows = maxLength-self.linesShowed
        rowsToFetch=min(qtde, remainderRows)
        if rowsToFetch<=0:
            return
        initLen = self.linesShowed
        maxRows = self.linesShowed + rowsToFetch
        while self.linesShowed < maxRows:
            servicos[self.linesShowed]['valor'] = "R$ {:.2f}".format(servicos[self.linesShowed]['valor']).replace('.',',',1)
            self.linesShowed+=1
        self.model.addData(servicos[initLen:self.linesShowed])
        colunas = ['idServico', 'descricao', 'valor']
        self.model.colunasDesejadas(colunas)
        self.model.setRowCount(self.linesShowed)
        self.model.setColumnCount(len(colunas))
        self.tabela.hideColumn(0)

    def listarServicos(self):
        self.linesShowed = 0
        self.model = InfiniteScrollTableModel([{}])
        listaHeader = ['ID', 'Descrição', 'Valor']
        self.model.setHorizontalHeaderLabels(listaHeader)
        self.filter.setSourceModel(self.model)
        self.tabela.setModel(self.filter)
        self.tabela.setItemDelegateForColumn(3, self.delegateRight)
        self.maisServicos(50)
        if self.linesShowed > 0:
            header = self.tabela.horizontalHeader()
            header.setSectionResizeMode(
                QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
            header.setSectionResizeMode(1, 
                QtWidgets.QHeaderView.ResizeMode.Stretch)

    def editarServico(self):
        self.linha = self.tabela.selectionModel().selectedRows()
        if self.linha:
            return self.tabela.model().index(self.linha[0].row(), 0).data()

    def editarServico2(self):
        self.linha = self.tabela.selectionModel().selectedRows()
        if self.linha:
            id =  self.tabela.model().index(self.linha[0].row(), 0).data()
        self.telaEditar = TelaCadastroServico()
        self.telaEditar.renderEditar(id)
        self.telaEditar.show()
      

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    ui = TelaConsultaServico()
    ui.setupUi()
    ui.show()

    style = open('./ui/styles.qss').read()
    app.setStyleSheet(style)

    sys.exit(app.exec())