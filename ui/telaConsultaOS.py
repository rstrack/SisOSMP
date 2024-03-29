from flatdict import FlatDict
from PyQt6 import QtCore, QtGui, QtWidgets

from controller.clienteController import ClienteController
from controller.orcamentoController import OrcamentoController
from controller.pecaController import PecaController
from controller.servicoController import ServicoController

from ui.help import HELPCONSULTAOS, help
from ui.hoverButton import HoverButton
from ui.infiniteScroll import AlignDelegate, InfiniteScrollTableModel
from ui.messageBox import MessageBox
from util.gerar_pdf import GeraPDF


class TelaConsultaOS(QtWidgets.QMainWindow):
    def __init__(self):
        super(TelaConsultaOS, self).__init__()
        self.status = "2"
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

        """self.labelTitulo = QtWidgets.QLabel(self.framegeral)
        self.labelTitulo.setFixedHeight(80)
        self.labelTitulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelTitulo.setObjectName('titulo')
        self.vlayout.addWidget(self.labelTitulo)"""
        self.frameBusca = QtWidgets.QFrame(self.main_frame)
        self.vlayout.addWidget(self.frameBusca)
        self.hlayoutBusca = QtWidgets.QHBoxLayout(self.frameBusca)
        self.lineEditBusca = QtWidgets.QLineEdit(self.frameBusca)
        self.lineEditBusca.setFixedHeight(30)
        self.lineEditBusca.setPlaceholderText(
            "Pesquisar por data do orçamento ou de aprovação, dados do cliente ou dados do veículo"
        )
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
        self.comboBoxStatus = QtWidgets.QComboBox(self.frameOrdenacao)
        self.comboBoxStatus.addItems(["Não finalizadas", "Finalizadas"])
        self.hlayoutOrdenacao.addWidget(self.comboBoxStatus)
        self.comboBoxOrdenacao = QtWidgets.QComboBox(self.frameOrdenacao)
        self.comboBoxOrdenacao.setToolTip("Ordenar")
        self.comboBoxOrdenacao.addItems(
            [
                "Data do Orçamento (recente primeiro)",
                "Data do Orçamento (antigo primeiro)",
                "Data de Aprovação (recente primeiro)",
                "Data de Aprovação (antigo primeiro)",
            ]
        )
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
        self.botaoGerarPDF = QtWidgets.QPushButton(self.framebotoes)
        self.botaoGerarPDF.setFixedSize(100, 35)
        self.hlayoutbotoes.addWidget(self.botaoGerarPDF)
        self.botaoFinalizar = QtWidgets.QPushButton(self.framebotoes)
        self.botaoFinalizar.setFixedSize(100, 35)
        self.hlayoutbotoes.addWidget(self.botaoFinalizar)
        self.botaoExcluir = QtWidgets.QPushButton(self.framebotoes)
        self.botaoExcluir.setFixedSize(100, 35)
        self.botaoExcluir.setObjectName("excluir")
        self.hlayoutbotoes.addWidget(self.botaoExcluir)
        self.model = QtGui.QStandardItemModel()
        self.setCentralWidget(self.main_frame)
        self.retranslateUi()
        self.botaoRefresh.clicked.connect(self.listarOS)
        self.botaoFinalizar.clicked.connect(self.finalizarOS)
        self.botaoGerarPDF.clicked.connect(self.gerarPDF)
        self.botaoExcluir.clicked.connect(self.excluirOS)
        self.tabela.verticalScrollBar().valueChanged.connect(self.scrolled)
        self.tabela.verticalScrollBar().actionTriggered.connect(self.scrolled)
        self.lineEditBusca.textChanged.connect(self.buffer)
        self.comboBoxOrdenacao.currentIndexChanged.connect(self.buffer)
        self.comboBoxStatus.currentIndexChanged.connect(self.buffer)
        self.comboBoxStatus.currentIndexChanged.connect(self.renderBotoes)
        self.botaoHelp.clicked.connect(
            lambda: help("Ajuda - Consulta por O.S.", HELPCONSULTAOS)
        )
        self.listarOS()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.labelTitulo.setText(_translate("MainWindow", "Ordens de Serviço"))
        self.setWindowTitle(_translate("MainWindow", "Busca"))
        self.botaoEditar.setText(_translate("MainWindow", "Editar"))
        self.botaoFinalizar.setText(_translate("MainWindow", "Finalizar"))
        self.botaoGerarPDF.setText(_translate("MainWindow", "Gerar PDF"))
        self.botaoExcluir.setText(_translate("MainWindow", "Excluir"))

    def scrolled(self, value):
        if value == self.tabela.verticalScrollBar().maximum():
            self.maisOS(50)

    def buffer(self):
        self.busca = self.lineEditBusca.text()
        self.orderBy = self.comboBoxOrdenacao.currentIndex()
        self.status = "3" if self.comboBoxStatus.currentIndex() == 1 else "2"
        self.listarOS()

    def maisOS(self, qtde):
        orcamentos = OrcamentoController.buscarOrcamento(
            self.status, self.busca, self.linhasCarregadas + qtde, self.orderBy
        )
        if not orcamentos:
            return
        maxLength = len(orcamentos)
        remainderRows = maxLength - self.linhasCarregadas
        rowsToFetch = min(qtde, remainderRows)
        if rowsToFetch <= 0:
            return
        initLen = self.linhasCarregadas
        maxRows = self.linhasCarregadas + rowsToFetch
        while self.linhasCarregadas < maxRows:
            orcamentos[self.linhasCarregadas]["dataOrcamento"] = orcamentos[
                self.linhasCarregadas
            ]["dataOrcamento"].strftime("%d/%m/%Y")
            orcamentos[self.linhasCarregadas]["dataAprovacao"] = orcamentos[
                self.linhasCarregadas
            ]["dataAprovacao"].strftime("%d/%m/%Y")
            orcamentos[self.linhasCarregadas]["valorTotal"] = "R$ {:.2f}".format(
                orcamentos[self.linhasCarregadas]["valorTotal"]
            ).replace(".", ",", 1)
            queryFones = ClienteController.listarFones(
                orcamentos[self.linhasCarregadas]["cliente"]["idCliente"]
            )
            if queryFones:
                fones = []
                for fone in queryFones:
                    fones.append(fone["fone"])
                orcamentos[self.linhasCarregadas]["fones"] = ", ".join(fones)
            else:
                orcamentos[self.linhasCarregadas]["fones"] = ""
            orcamentos[self.linhasCarregadas] = FlatDict(
                orcamentos[self.linhasCarregadas], delimiter="."
            )
            self.linhasCarregadas += 1
        self.model.addData(orcamentos[initLen : self.linhasCarregadas])
        colunas = [
            "idOrcamento",
            "dataOrcamento",
            "dataAprovacao",
            "cliente.nome",
            "cliente.documento",
            "fones",
            "veiculo.marca.nome",
            "veiculo.modelo",
            "veiculo.placa",
            "valorTotal",
        ]
        self.model.colunasDesejadas(colunas)
        self.model.setRowCount(self.linhasCarregadas)
        self.model.setColumnCount(len(colunas))
        self.tabela.hideColumn(0)

    def listarOS(self):
        self.linhasCarregadas = 0
        self.model = InfiniteScrollTableModel([{}])
        listaHeader = [
            "ID",
            "Data do Orçamento",
            "Data de Aprovação",
            "Cliente",
            " Documento",
            "Fones",
            "Marca",
            "Modelo",
            "Placa",
            "Valor Total",
        ]
        self.model.setHorizontalHeaderLabels(listaHeader)
        self.tabela.setModel(self.model)
        self.tabela.setItemDelegateForColumn(9, self.delegateRight)
        self.maisOS(50)
        if self.linhasCarregadas > 0:
            header = self.tabela.horizontalHeader()
            header.setSectionResizeMode(
                QtWidgets.QHeaderView.ResizeMode.ResizeToContents
            )
            header.setStretchLastSection(True)
            self.model.setHeaderAlignment(
                9,
                QtCore.Qt.AlignmentFlag.AlignRight
                | QtCore.Qt.AlignmentFlag.AlignVCenter,
            )

    def editarOS(self):
        linha = self.tabela.selectionModel().selectedRows()
        if linha:
            return self.tabela.model().index(linha[0].row(), 0).data()

    def finalizarOS(self):
        linha = self.tabela.selectionModel().selectedRows()
        if linha:
            id = self.tabela.model().index(linha[0].row(), 0).data()
            r = OrcamentoController.finalizarOrcamento(id)
            if isinstance(r, Exception):
                raise Exception(r)
            msg = QtWidgets.QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("resources/logo-icon.png"))
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setWindowTitle("Aviso")
            msg.setText("Ordem de serviço finalizada com sucesso!")
            msg.exec()
            self.listarOS()

    def gerarPDF(self):
        linha = self.tabela.selectionModel().selectedRows()
        if linha:
            id = self.tabela.model().index(linha[0].row(), 0).data()
            orcamento = OrcamentoController.getOrcamento(id)
            fones = ClienteController.listarFones(orcamento["cliente"]["idCliente"])
            if fones:
                fones = list(fones)
            itemPecas = OrcamentoController.listarItemPecas(orcamento["idOrcamento"])
            if itemPecas:
                for item in itemPecas:
                    peca = PecaController.getPeca(item["peca"])
                    item["descricao"] = peca["descricao"]
                    item["un"] = peca["un"]
                itemPecas = list(itemPecas)
            itemServicos = OrcamentoController.listarItemServicos(orcamento["idOrcamento"])
            if itemServicos:
                for item in itemServicos:
                    item["descricao"] = ServicoController.getServico(item["servico"])[
                        "descricao"
                    ]
                itemServicos = list(itemServicos)
            msg = MessageBox()
            r = msg.question("Deseja salvar o arquivo?")
            if r == "cancelar":
                return
            elif r == "nao":
                pdf = GeraPDF()
                pdf.generatePDF(orcamento, fones, itemServicos, itemPecas)
            else:
                window = QtWidgets.QMainWindow()
                fd = QtWidgets.QFileDialog()
                path = fd.getExistingDirectory(window, "Salvar como", "./")
                if path == "":
                    return
                pdf = GeraPDF()
                pdf.generatePDF(orcamento, fones, itemServicos, itemPecas, path)

    def excluirOS(self):
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
                    r = OrcamentoController.excluirOrcamento(id)
                    if isinstance(r, Exception):
                        raise Exception(r)
                    elif not r:
                        raise Exception("Erro ao excluir")
                    else:
                        msg = QtWidgets.QMessageBox()
                        msg.setWindowTitle("Aviso")
                        msg.setWindowIcon(QtGui.QIcon("resources/logo-icon.png"))
                        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                        msg.setText(f"Ordem de Serviço excluída com sucesso!")
                        msg.exec()
                        self.listarOS()
        except Exception as e:
            msg = QtWidgets.QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("resources/logo-icon.png"))
            msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg.setWindowTitle("Erro")
            msg.setText(str(e))
            msg.exec()

    def renderBotoes(self):
        if self.comboBoxStatus.currentIndex() == 1:
            self.botaoEditar.hide()
            self.botaoFinalizar.hide()
            self.botaoExcluir.hide()
        else:
            self.botaoEditar.show()
            self.botaoFinalizar.show()
            self.botaoExcluir.show()
