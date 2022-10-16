from PyQt6 import QtCore, QtGui, QtWidgets
from flatdict import FlatDict
from container import handleDeps
from ui.infiniteScroll import AlignDelegate, InfiniteScrollTableModel
from ui.messageBox import MessageBox
from util.gerar_pdf import GeraPDF

class TelaConsultaOS(QtWidgets.QMainWindow):
    def __init__(self):
        super(TelaConsultaOS, self).__init__()
        self.orcamentoCtrl = handleDeps.getDep('ORCAMENTOCTRL')
        self.clienteCtrl = handleDeps.getDep('CLIENTECTRL')
        self.pecaCtrl = handleDeps.getDep('PECACTRL')
        self.servicoCtrl = handleDeps.getDep('SERVICOCTRL')
        self.busca = ''
        self.setupUi()

    def setupUi(self):
        self.resize(1280, 760)
        self.main_frame = QtWidgets.QFrame(self)
        self.main_frame.setObjectName("main_frame")
        self.hlayout = QtWidgets.QHBoxLayout(self.main_frame)
        spacer = QtWidgets.QSpacerItem(
            20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.hlayout.addItem(spacer)
        self.framegeral = QtWidgets.QFrame(self.main_frame)
        self.framegeral.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        self.framegeral.setMaximumWidth(int(QtGui.QGuiApplication.primaryScreen().size().width()*0.6) 
            if QtGui.QGuiApplication.primaryScreen().size().width()> 1280 else QtGui.QGuiApplication.primaryScreen().size().width())
        self.hlayout.addWidget(self.framegeral)
        spacer = QtWidgets.QSpacerItem(
            20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.hlayout.addItem(spacer)
        self.vlayout = QtWidgets.QVBoxLayout(self.framegeral)
        self.vlayout.setContentsMargins(0,0,0,0)
        self.vlayout.setSpacing(0)
        self.frameBusca = QtWidgets.QFrame(self.main_frame)
        self.vlayout.addWidget(self.frameBusca)
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
        self.framedados = QtWidgets.QFrame(self.main_frame)
        self.framedados.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        self.vlayout.addWidget(self.framedados)
        self.vlayoutdados = QtWidgets.QVBoxLayout(self.framedados)
        self.tabela = QtWidgets.QTableView(self.framedados)
        self.vlayoutdados.addWidget(self.tabela)
        self.tabela.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tabela.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.tabela.horizontalHeader().setHighlightSections(False)
        self.tabela.verticalHeader().setVisible(False)
        self.delegateRight = AlignDelegate(QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.framebotoes = QtWidgets.QFrame(self.main_frame)
        self.vlayout.addWidget(self.framebotoes)
        self.hlayoutbotoes = QtWidgets.QHBoxLayout(self.framebotoes)
        spacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.hlayoutbotoes.addItem(spacer)
        self.botaoEditar = QtWidgets.QPushButton(self.framebotoes)
        self.botaoEditar.setFixedSize(100, 35)
        self.botaoEditar.setObjectName('botaoprincipal')
        self.hlayoutbotoes.addWidget(self.botaoEditar)
        self.botaoGerarPDF = QtWidgets.QPushButton(self.framebotoes)
        self.botaoGerarPDF.setFixedSize(100, 35)
        self.hlayoutbotoes.addWidget(self.botaoGerarPDF)
        self.botaoExcluir = QtWidgets.QPushButton(self.framebotoes)
        self.botaoExcluir.setFixedSize(100, 35)
        self.botaoExcluir.setObjectName('excluir')
        self.hlayoutbotoes.addWidget(self.botaoExcluir)
        self.model = QtGui.QStandardItemModel()
        self.setCentralWidget(self.main_frame)
        self.retranslateUi()
        self.selectionModel = self.tabela.selectionModel()
        self.botaoRefresh.clicked.connect(self.listarOS)
        self.botaoGerarPDF.clicked.connect(self.gerarPDF)
        self.botaoExcluir.clicked.connect(self.excluirOS)
        self.tabela.verticalScrollBar().valueChanged.connect(self.scrolled)
        self.tabela.verticalScrollBar().actionTriggered.connect(self.scrolled)
        self.lineEditBusca.textChanged.connect(self.buffer)
        self.listarOS()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Busca"))
        self.botaoEditar.setText(_translate("MainWindow", "Editar"))
        self.botaoGerarPDF.setText(_translate("MainWindow", "Gerar PDF"))
        self.botaoExcluir.setText(_translate("MainWindow", "Excluir"))

    def scrolled(self, value):
        if value == self.tabela.verticalScrollBar().maximum():
            self.maisOS(50)

    def buffer(self):
        self.busca = self.lineEditBusca.text()
        self.listarOS()

    def maisOS(self, qtde):
        orcamentos = self.orcamentoCtrl.buscarOrcamento(aprovado=True, input=self.busca, limit=self.linhasCarregadas+qtde)
        if not orcamentos:
            return
        maxLength = len(orcamentos)
        remainderRows = maxLength-self.linhasCarregadas
        rowsToFetch=min(qtde, remainderRows)
        if rowsToFetch<=0:
            return
        initLen = self.linhasCarregadas
        maxRows = self.linhasCarregadas + rowsToFetch
        while self.linhasCarregadas < maxRows:
            orcamentos[self.linhasCarregadas]['dataOrcamento'] = orcamentos[self.linhasCarregadas]['dataOrcamento'].strftime("%d/%m/%Y")
            orcamentos[self.linhasCarregadas]['dataAprovacao'] = orcamentos[self.linhasCarregadas]['dataAprovacao'].strftime("%d/%m/%Y")
            orcamentos[self.linhasCarregadas]['valorTotal'] = "R$ {:.2f}".format(orcamentos[self.linhasCarregadas]['valorTotal']).replace('.',',',1)
            queryFones = self.clienteCtrl.listarFones(orcamentos[self.linhasCarregadas]['cliente']['idCliente'])
            if queryFones:
                fones = []
                for fone in queryFones:
                    fones.append(fone['fone'])
                orcamentos[self.linhasCarregadas]['fones'] = (', '.join(fones))
            else: orcamentos[self.linhasCarregadas]['fones'] = ''
            orcamentos[self.linhasCarregadas] = FlatDict(orcamentos[self.linhasCarregadas], delimiter='.')
            self.linhasCarregadas+=1
        self.model.addData(orcamentos[initLen:self.linhasCarregadas])
        colunas = ['idOrcamento', 'dataOrcamento', 'dataAprovacao', 'cliente.nome', 'cliente.documento', 'fones', 'veiculo.marca.nome', 'veiculo.modelo', 'veiculo.placa', 'valorTotal']
        self.model.colunasDesejadas(colunas)
        self.model.setRowCount(self.linhasCarregadas)
        self.model.setColumnCount(len(colunas))
        self.tabela.hideColumn(0)
        

    def listarOS(self):
        self.linhasCarregadas = 0
        self.model = InfiniteScrollTableModel([{}])
        listaHeader = ['ID', 'Data do Orçamento', 'Data de Aprovação', 'Cliente', ' Documento', 'Fones', 'Marca', 'Modelo', 'Placa', 'Valor Total']
        self.model.setHorizontalHeaderLabels(listaHeader)
        self.tabela.setModel(self.model)
        self.tabela.setItemDelegateForColumn(9, self.delegateRight)
        self.maisOS(50)
        if self.linhasCarregadas > 0:
            header = self.tabela.horizontalHeader()
            header.setSectionResizeMode(
                QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
            header.setSectionResizeMode(3, 
                QtWidgets.QHeaderView.ResizeMode.Stretch)
            self.model.setHeaderAlignment(9, QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignVCenter)

    def editarOS(self):
        self.linha = self.tabela.selectionModel().selectedRows()
        if self.linha:
            return self.tabela.model().index(self.linha[0].row(), 0).data()

    def gerarPDF(self):
        self.linha = self.tabela.selectionModel().selectedRows()
        if self.linha:
            id = self.tabela.model().index(self.linha[0].row(), 0).data()
        else: return
        orcamento = self.orcamentoCtrl.getOrcamento(id)
        fones = self.clienteCtrl.listarFones(orcamento['cliente']['idCliente'])
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
            pdf = GeraPDF()
            pdf.generatePDF(orcamento, fones, itemServicos, itemPecas)
        else:
            window = QtWidgets.QMainWindow()
            fd = QtWidgets.QFileDialog()
            path = fd.getExistingDirectory(window, 'Salvar como', './')
            if path == '':
                return
            pdf = GeraPDF()
            pdf.generatePDF(orcamento, fones, itemServicos, itemPecas, path)
    
    def excluirOS(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Aviso")
        msgBox.setText('Tem certeza que deseja excluir?')
        y = msgBox.addButton("Sim", QtWidgets.QMessageBox.ButtonRole.YesRole)
        n = msgBox.addButton("Não", QtWidgets.QMessageBox.ButtonRole.NoRole)
        y.setFixedWidth(60)
        n.setFixedWidth(60)
        msgBox.exec()
        if msgBox.clickedButton() == y:
            self.linha = self.tabela.selectionModel().selectedRows()
            if self.linha:
                id = self.tabela.model().index(self.linha[0].row(), 0).data()
                r = self.orcamentoCtrl.excluirOrcamento(id)
                if isinstance(r, Exception):
                    raise Exception(r)
                elif not r:
                    raise Exception('Erro ao excluir')
                else:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle("Aviso")
                    msg.setWindowIcon(QtGui.QIcon('./resources/logo-icon.png'))
                    msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    msg.setText(f"Ordem de Serviço excluída com sucesso!")
                    msg.exec()
                    self.listarOS()
