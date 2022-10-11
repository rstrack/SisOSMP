from PyQt6 import QtCore, QtGui, QtWidgets
from container import handleDeps
from ui.telaClienteVeiculo import TelaClienteVeiculo
from ui.infiniteScroll import AlignDelegate, InfiniteScrollTableModel
from flatdict import FlatDict

from ui.telaMarcas import TelaMarcas

class TelaConsultaVeiculo(QtWidgets.QMainWindow):
    def __init__(self):
        super(TelaConsultaVeiculo, self).__init__()
        self.clienteCtrl = handleDeps.getDep('CLIENTECTRL')
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
        self.botaoMarcas = QtWidgets.QPushButton(self.framebotoes)
        self.botaoMarcas.setFixedSize(100, 35)
        self.hlayoutbotoes.addWidget(self.botaoMarcas)
        spacer = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.hlayoutbotoes.addItem(spacer)
        self.botaoEditar = QtWidgets.QPushButton(self.framebotoes)
        self.botaoEditar.setFixedSize(100, 35)
        self.botaoEditar.setObjectName('botaoprincipal')
        self.hlayoutbotoes.addWidget(self.botaoEditar)
        self.botaoClientes = QtWidgets.QPushButton(self.framebotoes)
        self.botaoClientes.setFixedSize(100, 35)
        self.hlayoutbotoes.addWidget(self.botaoClientes)
        self.botaoExcluir = QtWidgets.QPushButton(self.framebotoes)
        self.botaoExcluir.setObjectName('excluir')
        self.botaoExcluir.setFixedSize(100, 35)
        self.hlayoutbotoes.addWidget(self.botaoExcluir)
        self.filter.setFilterKeyColumn(-1)
        self.lineEditBusca.textChanged.connect(
            self.filter.setFilterRegularExpression)
        self.tabela.setModel(self.filter)
        self.setCentralWidget(self.mainwidget)
        self.retranslateUi()
        self.selectionModel = self.tabela.selectionModel()

        self.listarVeiculos()
        self.botaoRefresh.clicked.connect(self.listarVeiculos)
        self.botaoMarcas.clicked.connect(self.marcas)
        self.botaoClientes.clicked.connect(self.clientes)
        self.botaoExcluir.clicked.connect(self.excluirVeiculo)
        self.tabela.verticalScrollBar().valueChanged.connect(self.scrolled)
        self.tabela.verticalScrollBar().actionTriggered.connect(self.scrolled)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Busca"))
        self.botaoMarcas.setText(_translate("MainWindow", "Marcas"))
        self.botaoEditar.setText(_translate("MainWindow", "Editar"))
        self.botaoClientes.setText(_translate("MainWindow", "Clientes"))
        self.botaoExcluir.setText(_translate("MainWindow", "Excluir"))

    def scrolled(self, value):
        if value == self.tabela.verticalScrollBar().maximum():
            self.maisVeiculos(50)
            # threading.Thread(target=self.maisVeiculos, args=(100,)).start()

    def maisVeiculos(self, qtde):
        veiculos = self.clienteCtrl.listarVeiculos()
        if not veiculos:
            return
        maxLength = len(veiculos)
        remainderRows = maxLength-self.linhasCarregadas
        rowsToFetch=min(qtde, remainderRows)
        if rowsToFetch<=0:
            return
        initLen = self.linhasCarregadas
        maxRows = self.linhasCarregadas + rowsToFetch
        while self.linhasCarregadas < maxRows:
            queryClientes = self.clienteCtrl.listarClientes(veiculos[self.linhasCarregadas]['idVeiculo'])
            if queryClientes:
                nomes = []
                for cliente in queryClientes:
                    nomes.append(cliente['nome'])
                veiculos[self.linhasCarregadas]['clientes'] = ', '.join(nomes)
            else: veiculos[self.linhasCarregadas]['clientes'] = ''
            veiculos[self.linhasCarregadas] = FlatDict(veiculos[self.linhasCarregadas], delimiter='.')
            self.linhasCarregadas+=1
        self.model.addData(veiculos[initLen:self.linhasCarregadas])
        colunas = ['idVeiculo', 'marca.nome', 'modelo', 'placa', 'ano', 'clientes']
        self.model.colunasDesejadas(colunas)
        self.model.setRowCount(self.linhasCarregadas)
        self.model.setColumnCount(len(colunas))
        self.tabela.hideColumn(0)

    def listarVeiculos(self):
        self.linhasCarregadas = 0
        self.model = InfiniteScrollTableModel([{}])
        listaHeader = ['ID', 'Marca', 'Modelo', 'Placa', 'Ano', 'Clientes Vinculados']
        self.model.setHorizontalHeaderLabels(listaHeader)
        self.filter.setSourceModel(self.model)
        self.tabela.setModel(self.filter)
        self.tabela.setItemDelegateForColumn(4, self.delegateRight)
        self.maisVeiculos(50)
        if self.linhasCarregadas > 0:
            header = self.tabela.horizontalHeader()
            header.setSectionResizeMode(
                QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
            header.setSectionResizeMode(2,
                QtWidgets.QHeaderView.ResizeMode.Stretch)
            self.model.setHeaderAlignment(4, QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignVCenter)

    def editarVeiculo(self):
        self.linha = self.tabela.selectionModel().selectedRows()
        if self.linha:
            return self.tabela.model().index(self.linha[0].row(), 0).data()
    
    def excluirVeiculo(self):
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
                    r = self.clienteCtrl.excluirVeiculo(id)
                    if isinstance(r, Exception):
                        raise Exception(r)
                    elif not r:
                        raise Exception('Erro ao excluir')
                    else:    
                        msg = QtWidgets.QMessageBox()
                        msg.setWindowIcon(QtGui.QIcon('./resources/logo-icon.png'))
                        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                        msg.setWindowTitle("Aviso")
                        msg.setText(f"Veiculo excluído com sucesso!")
                        msg.exec()
                        self.listarVeiculos()
        except Exception as e:
            msg = QtWidgets.QMessageBox()
            msg.setWindowIcon(QtGui.QIcon('./resources/logo-icon.png'))
            msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg.setWindowTitle("Erro")
            msg.setText(str(e))
            msg.exec()

    def clientes(self):
        linha = self.tabela.selectionModel().selectedRows()
        if linha:
            id = self.tabela.model().index(linha[0].row(), 0).data()
            self.telaClienteVeiculo = TelaClienteVeiculo()
            self.telaClienteVeiculo.renderClientes(id)
            self.telaClienteVeiculo.show()

    def marcas(self):
        self.telaMarcas = TelaMarcas()
        self.telaMarcas.render()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    ui = TelaConsultaVeiculo()
    
    ui.show()

    style = open('./resources/styles.qss').read()
    app.setStyleSheet(style)

    sys.exit(app.exec())
