from PyQt6 import QtCore, QtGui, QtWidgets
from flatdict import FlatDict
from routes import handleRoutes
from ui.infiniteScroll import AlignDelegate, InfiniteScrollTableModel
from ui.messageBox import MessageBox
from util.gerar_pdf import generatePDF

class TelaConsultaOS(QtWidgets.QMainWindow):
    def __init__(self):
        super(TelaConsultaOS, self).__init__()
        self.orcamentoCtrl = handleRoutes.getRoute('ORCAMENTOCTRL')
        self.clienteCtrl = handleRoutes.getRoute('CLIENTECTRL')
        self.pecaCtrl = handleRoutes.getRoute('PECACTRL')
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
        self.tabela.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tabela.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.tabela.horizontalHeader().setHighlightSections(False)
        self.tabela.verticalHeader().setVisible(False)
        self.delegateRight = AlignDelegate(QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.filter = QtCore.QSortFilterProxyModel()
        self.filter.setFilterCaseSensitivity(QtCore.Qt.CaseSensitivity.CaseInsensitive)
        self.framebotoes = QtWidgets.QFrame(self.mainwidget)
        self.glayout.addWidget(self.framebotoes, 2, 0, 1, 1)
        self.hlayoutbotoes = QtWidgets.QHBoxLayout(self.framebotoes)
        spacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.hlayoutbotoes.addItem(spacer)
        self.botaoEditar = QtWidgets.QPushButton(self.framebotoes)
        self.botaoEditar.setFixedSize(100, 25)
        self.hlayoutbotoes.addWidget(self.botaoEditar)
        self.botaoImprimir = QtWidgets.QPushButton(self.framebotoes)
        self.botaoImprimir.setFixedSize(100, 25)
        self.hlayoutbotoes.addWidget(self.botaoImprimir)
        self.model = QtGui.QStandardItemModel()
        self.filter.setSourceModel(self.model)
        self.filter.setFilterKeyColumn(-1)
        self.lineEditBusca.textChanged.connect(self.filter.setFilterRegularExpression)
        self.tabela.setModel(self.filter)
        listaHeader = ['ID', 'Data do Orçamento', 'Data de aprovação', 'Cliente', 'Marca', 'Modelo', 'Placa', 'Valor Total']
        self.model.setHorizontalHeaderLabels(listaHeader)
        self.setCentralWidget(self.mainwidget)
        self.retranslateUi()
        self.selectionModel = self.tabela.selectionModel()
        self.botaoRefresh.clicked.connect(self.listarOS)
        self.botaoImprimir.clicked.connect(self.imprimir)
        self.listarOS()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Busca"))
        self.botaoEditar.setText(_translate("MainWindow", "Editar"))
        self.botaoImprimir.setText(_translate("MainWindow", "Imprimir"))

    def scrolled(self, value):
        if value == self.tabela.verticalScrollBar().maximum():
            self.maisOS(50)

    def maisOS(self, qtde):
        orcamentos = self.orcamentoCtrl.listarOrcamentos(aprovado=True, limit=self.linesShowed+qtde)
        if not orcamentos:
            return
        maxLength = len(orcamentos)
        remainderRows = maxLength-self.linesShowed
        rowsToFetch=min(qtde, remainderRows)
        if rowsToFetch<=0:
            return
        initLen = self.linesShowed
        maxRows = self.linesShowed + rowsToFetch
        while self.linesShowed < maxRows:
            orcamentos[self.linesShowed]['dataOrcamento'] = orcamentos[self.linesShowed]['dataOrcamento'].strftime("%d/%m/%Y")
            orcamentos[self.linesShowed]['dataAprovacao'] = orcamentos[self.linesShowed]['dataAprovacao'].strftime("%d/%m/%Y")

            orcamentos[self.linesShowed] = FlatDict(orcamentos[self.linesShowed], delimiter='.')
            self.linesShowed+=1
        self.model.addData(orcamentos[initLen:self.linesShowed])
        colunas = ['idOrcamento', 'dataOrcamento', 'dataAprovacao', 'cliente.nome', 'veiculo.marca.nome', 'veiculo.modelo', 'veiculo.placa', 'valorTotal']
        self.model.colunasDesejadas(colunas)
        self.model.setRowCount(self.linesShowed)
        self.model.setColumnCount(len(colunas))
        self.tabela.hideColumn(0)

    def listarOS(self):
        self.linesShowed = 0
        self.model = InfiniteScrollTableModel([{}])
        listaHeader = ['ID', 'Data do Orçamento', 'Data de Aprovação', 'Cliente', 'Marca', 'Modelo', 'Placa', 'Valor Total']
        self.model.setHorizontalHeaderLabels(listaHeader)
        self.filter.setSourceModel(self.model)
        self.tabela.setModel(self.filter)
        self.tabela.setItemDelegateForColumn(5, self.delegateRight)
        self.model.setHeaderData(1, QtCore.Qt.Orientation.Horizontal, 'tipo', 1)
        self.maisOS(50)
        header = self.tabela.horizontalHeader()
        header.setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(3, 
            QtWidgets.QHeaderView.ResizeMode.Stretch)

    '''def listarOS(self):
        orcamentos = self.orcamentoCtrl.listarOrcamentos(True)
        if not orcamentos:
            return
        self.model.setRowCount(len(orcamentos))
        row = 0
        for orcamento in reversed(orcamentos):
            item = QtGui.QStandardItem()
            item.setData(orcamento['idOrcamento'], QtCore.Qt.ItemDataRole.DisplayRole)
            item.setTextAlignment(
                QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.model.setItem(row, 0, item)
            item = QtGui.QStandardItem()
            dataOrcamento = orcamento['dataOrcamento'].strftime("%d/%m/%Y")
            item.setData(dataOrcamento, QtCore.Qt.ItemDataRole.DisplayRole)
            item.setTextAlignment(
                QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.model.setItem(row, 1, item)
            item = QtGui.QStandardItem()
            dataAprovacao = orcamento['dataAprovacao'].strftime("%d/%m/%Y")
            item.setData(dataAprovacao, QtCore.Qt.ItemDataRole.DisplayRole)
            item.setTextAlignment(
                QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.model.setItem(row, 2, item)
            cliente = self.clienteCtrl.getCliente(orcamento['cliente'])
            item = QtGui.QStandardItem()
            item.setData(cliente['nome'], QtCore.Qt.ItemDataRole.DisplayRole)
            item.setTextAlignment(
                QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.model.setItem(row, 3, item)
            #VEICULO
            veiculo = self.clienteCtrl.getVeiculo(orcamento['veiculo'])
            item = QtGui.QStandardItem(str(veiculo['marca']['nome']))
            item.setTextAlignment(
                QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.model.setItem(row, 4, item)
            item = QtGui.QStandardItem(str(veiculo['modelo']))
            item.setTextAlignment(
                QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.model.setItem(row, 5, item)
            item = QtGui.QStandardItem(str(veiculo['placa'] or ''))
            item.setTextAlignment(
                QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.model.setItem(row, 6, item)
            item = QtGui.QStandardItem('R$ {:.2f}'.format(orcamento['valorTotal']))
            item.setTextAlignment(
                QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.model.setItem(row, 7, item)
            row = row+1
        header = self.tabela.horizontalHeader()
        header.setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.Interactive)
        header.setSectionResizeMode(0, 
            QtWidgets.QHeaderView.ResizeMode.ResizeToContents)    
        header.setSectionResizeMode(1, 
            QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, 
            QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(3, 
            QtWidgets.QHeaderView.ResizeMode.Stretch)'''

    def editarOS(self):
        self.linha = self.tabela.selectionModel().selectedRows()
        if self.linha:
            return self.tabela.model().index(self.linha[0].row(), 0).data()

    def imprimir(self):
        self.linha = self.tabela.selectionModel().selectedRows()
        if self.linha:
            id = self.tabela.model().index(self.linha[0].row(), 0).data()
        else: return
        orcamento = self.orcamentoCtrl.getOrcamento(id)
        fones = self.clienteCtrl.listarFones(orcamento['cliente'])
        if fones: fones = list(fones)
        itemPecas = self.orcamentoCtrl.listarItemPecas(orcamento['idOrcamento'])
        if itemPecas:
            for item in itemPecas:
                peca = self.pecaCtrl.getPeca(item['peca'])
                item['descricao'] = peca['descricao']
                item['un'] = peca['un']
            itemPecas = list(itemPecas)
        itemServicos = self.orcamentoCtrl.listarItemServicos(orcamento['idOrcamento'])
        if itemServicos: 
            for item in itemServicos:
                item['descricao'] = self.servicoCtrl.getServico(item['servico'])['descricao']
            itemServicos = list(itemServicos)
        msg = MessageBox()
        r = msg.question('Deseja salvar o arquivo?')
        if r == 'cancelar':
            return
        elif r == 'nao':
            generatePDF(orcamento, fones, itemServicos, itemPecas)
        else:
            window = QtWidgets.QMainWindow()
            fd = QtWidgets.QFileDialog()
            path = fd.getExistingDirectory(window, 'Salvar como', './')
            generatePDF(orcamento, fones, itemServicos, itemPecas, path)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = TelaConsultaOS()
    ui.setupUi()
    ui.show()
    style = open('./resources/styles.qss').read()
    app.setStyleSheet(style)
    sys.exit(app.exec())


'''
fonesTela
fonesBanco

for fone in fonesTela:
    _fone = foneRep.findByFone(fone)
    if _fone and not _fone.cliente == cliente:
        raise Exception(f'Fone {_fone.fone} utilizado por outro cliente')
    elif not _fone:




for fone in fonesBanco:
    if not fone['fone'] in fonesTela:
        rep.delete(fone)

for fone in fonesTela:
    if not fone['fone'] in fonesBanco:
        _fone = foneRep.findByFone(fone)
        if _fone and _fone.cliente != cliente:
            raise Exception(f'Fone {_fone.fone} utilizado por outro cliente')
        rep.save(fone)










'''
