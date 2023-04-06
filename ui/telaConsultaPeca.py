from PyQt6 import QtCore, QtGui, QtWidgets

from controller.pecaController import PecaController

from ui.help import HELPCONSULTAPECA, help
from ui.hoverButton import HoverButton
from ui.infiniteScroll import AlignDelegate, InfiniteScrollTableModel


class TelaConsultaPeca(QtWidgets.QMainWindow):
    novaPeca = QtCore.pyqtSignal(int)

    def __init__(self):
        super(TelaConsultaPeca, self).__init__()
        self.busca = ""
        self.orderBy = 0
        self.setupUi()

    def setupUi(self):
        self.resize(1280, 760)
        self.main_frame = QtWidgets.QFrame(self)
        self.main_frame.setObjectName("main_frame")
        self.hlayout = QtWidgets.QHBoxLayout(self.main_frame)
        spacer = QtWidgets.QSpacerItem(
            20,
            10,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        self.hlayout.addItem(spacer)
        self.framegeral = QtWidgets.QFrame(self.main_frame)
        self.framegeral.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        self.framegeral.setMaximumWidth(
            int(QtGui.QGuiApplication.primaryScreen().size().width() * 0.65)
            if QtGui.QGuiApplication.primaryScreen().size().width() > 1280
            else QtGui.QGuiApplication.primaryScreen().size().width()
        )
        self.hlayout.addWidget(self.framegeral)
        spacer = QtWidgets.QSpacerItem(
            20,
            10,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        self.hlayout.addItem(spacer)
        self.vlayout = QtWidgets.QVBoxLayout(self.framegeral)
        self.vlayout.setContentsMargins(0, 0, 0, 0)
        self.vlayout.setSpacing(0)
        self.frameTitulo = QtWidgets.QFrame(self.framegeral)
        self.vlayout.addWidget(self.frameTitulo)
        self.hlayouttitulo = QtWidgets.QHBoxLayout(self.frameTitulo)
        self.hlayouttitulo.setContentsMargins(0, 0, 0, 0)
        self.hlayouttitulo.setSpacing(0)
        self.hlayouttitulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.labelTitulo = QtWidgets.QLabel(self.frameTitulo)
        self.labelTitulo.setFixedHeight(80)
        self.labelTitulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelTitulo.setObjectName("titulo")
        self.hlayouttitulo.addWidget(self.labelTitulo)
        self.botaoHelp = HoverButton(
            "",
            "./resources/help-icon1.png",
            "./resources/help-icon2.png",
            self.frameTitulo,
        )
        self.botaoHelp.setToolTip("Ajuda")
        self.botaoHelp.setObjectName("botaohelp")
        self.botaoHelp.setHelpIconSize(20, 20)
        self.hlayouttitulo.addWidget(self.botaoHelp)
        self.frameBusca = QtWidgets.QFrame(self.main_frame)
        self.vlayout.addWidget(self.frameBusca)
        self.hlayoutBusca = QtWidgets.QHBoxLayout(self.frameBusca)
        self.lineEditBusca = QtWidgets.QLineEdit(self.frameBusca)
        self.lineEditBusca.setFixedHeight(30)
        self.lineEditBusca.setPlaceholderText("Pesquisar por descrição da peça")
        self.lineEditBusca.setClearButtonEnabled(True)
        iconBusca = QtGui.QIcon("resources/search-icon.png")
        self.lineEditBusca.addAction(
            iconBusca, QtWidgets.QLineEdit.ActionPosition.LeadingPosition
        )
        self.hlayoutBusca.addWidget(self.lineEditBusca)
        self.botaoRefresh = QtWidgets.QPushButton(self.frameBusca)
        self.botaoRefresh.setToolTip("Atualizar")
        self.botaoRefresh.setFixedSize(30, 30)
        self.botaoRefresh.setIcon(QtGui.QIcon("resources/refresh-icon.png"))
        self.hlayoutBusca.addWidget(self.botaoRefresh)
        self.frameOrdenacao = QtWidgets.QFrame(self.main_frame)
        self.vlayout.addWidget(self.frameOrdenacao)
        self.hlayoutOrdenacao = QtWidgets.QHBoxLayout(self.frameOrdenacao)
        spacer = QtWidgets.QSpacerItem(
            20,
            10,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        self.hlayoutOrdenacao.addItem(spacer)
        self.botaoNovo = QtWidgets.QPushButton(self.frameOrdenacao)
        self.botaoNovo.setFixedSize(80, 25)
        self.hlayoutOrdenacao.addWidget(self.botaoNovo)
        self.comboBoxOrdenacao = QtWidgets.QComboBox(self.frameOrdenacao)
        self.comboBoxOrdenacao.setFixedHeight(25)
        self.comboBoxOrdenacao.setToolTip("Ordenar")
        self.comboBoxOrdenacao.addItems(["Descrição (A-Z)", "Descrição (Z-A)"])
        self.hlayoutOrdenacao.addWidget(self.comboBoxOrdenacao)
        self.framedados = QtWidgets.QFrame(self.main_frame)
        self.framedados.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        self.vlayout.addWidget(self.framedados)
        self.vlayoutdados = QtWidgets.QVBoxLayout(self.framedados)
        self.tabela = QtWidgets.QTableView(self.framedados)
        self.vlayoutdados.addWidget(self.tabela)
        self.tabela.setEditTriggers(
            QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers
        )
        self.tabela.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows
        )
        self.tabela.setSelectionMode(
            QtWidgets.QAbstractItemView.SelectionMode.SingleSelection
        )
        self.tabela.horizontalHeader().setHighlightSections(False)
        self.tabela.verticalHeader().setVisible(False)
        self.delegateRight = AlignDelegate(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.framebotoes = QtWidgets.QFrame(self.main_frame)
        self.vlayout.addWidget(self.framebotoes)
        self.hlayoutbotoes = QtWidgets.QHBoxLayout(self.framebotoes)
        spacer = QtWidgets.QSpacerItem(
            20,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.hlayoutbotoes.addItem(spacer)
        self.botaoEditar = QtWidgets.QPushButton(self.framebotoes)
        self.botaoEditar.setFixedSize(100, 35)
        self.botaoEditar.setObjectName("botaoprincipal")
        self.hlayoutbotoes.addWidget(self.botaoEditar)
        self.botaoExcluir = QtWidgets.QPushButton(self.framebotoes)
        self.botaoExcluir.setFixedSize(100, 35)
        self.botaoExcluir.setObjectName("excluir")
        self.hlayoutbotoes.addWidget(self.botaoExcluir)
        self.setCentralWidget(self.main_frame)
        self.retranslateUi()
        self.listarPecas()
        self.botaoRefresh.clicked.connect(self.listarPecas)
        self.botaoEditar.clicked.connect(self.editarPeca)
        self.botaoExcluir.clicked.connect(self.excluirPeca)
        self.tabela.verticalScrollBar().valueChanged.connect(self.scrolled)
        self.tabela.verticalScrollBar().actionTriggered.connect(self.scrolled)
        self.lineEditBusca.textChanged.connect(self.buffer)
        self.comboBoxOrdenacao.currentIndexChanged.connect(self.buffer)
        self.botaoNovo.clicked.connect(lambda: self.novaPeca.emit(1))
        self.botaoHelp.clicked.connect(
            lambda: help("Ajuda - Consulta por Peça", HELPCONSULTAPECA)
        )

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Busca"))
        self.botaoNovo.setText(_translate("MainWindow", "+ Novo"))
        self.labelTitulo.setText(_translate("MainWindow", "Peças"))
        self.botaoEditar.setText(_translate("MainWindow", "Editar"))
        self.botaoExcluir.setText(_translate("MainWindow", "Excluir"))

    def scrolled(self, value):
        if value == self.tabela.verticalScrollBar().maximum():
            self.maisPecas(50)

    def buffer(self):
        self.busca = self.lineEditBusca.text()
        self.orderBy = self.comboBoxOrdenacao.currentIndex()
        self.listarPecas()

    def maisPecas(self, qtde):
        pecas = PecaController.buscarPeca(
            self.busca, self.linhasCarregadas + qtde, self.orderBy
        )
        if not pecas:
            return
        maxLength = len(pecas)
        remainderRows = maxLength - self.linhasCarregadas
        rowsToFetch = min(qtde, remainderRows)
        if rowsToFetch <= 0:
            return
        initLen = self.linhasCarregadas
        maxRows = self.linhasCarregadas + rowsToFetch
        while self.linhasCarregadas < maxRows:
            pecas[self.linhasCarregadas]["valor"] = "R$ {:.2f}".format(
                pecas[self.linhasCarregadas]["valor"]
            ).replace(".", ",", 1)
            self.linhasCarregadas += 1
        self.model.addData(pecas[initLen : self.linhasCarregadas])
        colunas = ["idPeca", "descricao", "un", "valor"]
        self.model.colunasDesejadas(colunas)
        self.model.setRowCount(self.linhasCarregadas)
        self.model.setColumnCount(len(colunas))
        self.tabela.hideColumn(0)

    def listarPecas(self):
        self.linhasCarregadas = 0
        self.model = InfiniteScrollTableModel([{}])
        listaHeader = ["ID ", "Descrição ", "Un ", "Valor "]
        self.model.setHorizontalHeaderLabels(listaHeader)
        self.tabela.setModel(self.model)
        self.tabela.setItemDelegateForColumn(3, self.delegateRight)
        self.maisPecas(50)
        if self.linhasCarregadas > 0:
            header = self.tabela.horizontalHeader()
            header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Interactive)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Stretch)
            self.model.setHeaderAlignment(
                3,
                QtCore.Qt.AlignmentFlag.AlignRight
                | QtCore.Qt.AlignmentFlag.AlignVCenter,
            )

    def editarPeca(self):
        linha = self.tabela.selectionModel().selectedRows()
        if linha:
            return self.tabela.model().index(linha[0].row(), 0).data()

    def excluirPeca(self):
        try:
            linha = self.tabela.selectionModel().selectedRows()
            if linha:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Aviso")
                msgBox.setText("Tem certeza que deseja excluir?")
                y = msgBox.addButton("Sim", QtWidgets.QMessageBox.ButtonRole.YesRole)
                n = msgBox.addButton("Não", QtWidgets.QMessageBox.ButtonRole.NoRole)
                y.setFixedWidth(60)
                n.setFixedWidth(60)
                msgBox.exec()
                if msgBox.clickedButton() == y:
                    id = self.tabela.model().index(linha[0].row(), 0).data()
                    r = PecaController.excluirPeca(id)
                    if isinstance(r, Exception):
                        raise Exception(r)
                    elif not r:
                        raise Exception("Erro ao excluir")
                    else:
                        msg = QtWidgets.QMessageBox()
                        msg.setWindowTitle("Aviso")
                        msg.setWindowIcon(QtGui.QIcon("resources/logo-icon.png"))
                        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                        msg.setText(f"Peça excluída com sucesso!")
                        msg.exec()
                        self.listarPecas()
        except Exception as e:
            msg = QtWidgets.QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("resources/logo-icon.png"))
            msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg.setWindowTitle("Erro")
            msg.setText(str(e))
            msg.exec()
