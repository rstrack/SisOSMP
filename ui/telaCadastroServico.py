from decimal import Decimal

from PyQt6 import QtCore, QtGui, QtWidgets

from controller.servicoController import ServicoController

from ui.help import HELPCADASTROSERVICO, help
from ui.hoverButton import HoverButton


class TelaCadastroServico(QtWidgets.QMainWindow):
    def __init__(self):
        super(TelaCadastroServico, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(1280, 760)
        self.main_frame = QtWidgets.QFrame(self)
        self.main_frame.setObjectName("main_frame")
        self.vlayout = QtWidgets.QVBoxLayout(self.main_frame)
        self.vlayout.setContentsMargins(0, 0, 0, 0)
        self.vlayout.setSpacing(0)
        self.frameTitulo = QtWidgets.QFrame(self.main_frame)
        self.vlayout.addWidget(self.frameTitulo)
        self.hlayouttitulo = QtWidgets.QHBoxLayout(self.frameTitulo)
        self.hlayouttitulo.setContentsMargins(0, 0, 0, 0)
        self.hlayouttitulo.setSpacing(0)
        self.hlayouttitulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.labelTitulo = QtWidgets.QLabel(self.frameTitulo)
        self.labelTitulo.setFixedHeight(120)
        self.labelTitulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelTitulo.setObjectName("titulo")
        self.hlayouttitulo.addWidget(self.labelTitulo)
        self.botaoHelp = HoverButton(
            "",
            "./resources/help-icon1.png",
            "./resources/help-icon2.png",
            self.frameTitulo,
        )
        self.botaoHelp.setToolTip("Ajuda sobre veículo")
        self.botaoHelp.setObjectName("botaohelp")
        self.botaoHelp.setHelpIconSize(20, 20)
        self.hlayouttitulo.addWidget(self.botaoHelp)
        self.scrollarea = QtWidgets.QScrollArea(self.main_frame)
        self.scrollarea.setWidgetResizable(True)
        self.vlayout.addWidget(self.scrollarea)
        self.framegeral = QtWidgets.QFrame(self.main_frame)
        self.scrollarea.setWidget(self.framegeral)
        self.hlayout1 = QtWidgets.QHBoxLayout(self.framegeral)
        spacer = QtWidgets.QSpacerItem(
            20,
            10,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        self.hlayout1.addItem(spacer)
        self.framedados = QtWidgets.QFrame(self.scrollarea)
        self.framedados.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        self.framedados.setMaximumWidth(
            int(QtGui.QGuiApplication.primaryScreen().size().width() * 0.65)
            if QtGui.QGuiApplication.primaryScreen().size().width() > 1280
            else QtGui.QGuiApplication.primaryScreen().size().width()
        )
        self.hlayout1.addWidget(self.framedados)
        spacer = QtWidgets.QSpacerItem(
            20,
            10,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        self.hlayout1.addItem(spacer)
        self.gridLayout = QtWidgets.QGridLayout(self.framedados)
        self.labelDescricao = QtWidgets.QLabel(self.framedados)
        self.gridLayout.addWidget(self.labelDescricao, 0, 0, 1, 1)
        self.labelvalor = QtWidgets.QLabel(self.framedados)
        self.gridLayout.addWidget(self.labelvalor, 0, 1, 1, 1)
        self.lineEditDescricao = QtWidgets.QLineEdit(self.framedados)
        self.lineEditDescricao.setMaxLength(80)
        self.lineEditDescricao.setMaximumWidth(200)
        self.lineEditDescricao.setMaximumWidth(600)
        self.gridLayout.addWidget(self.lineEditDescricao, 1, 0, 1, 1)
        self.lineEditvalor = QtWidgets.QLineEdit(self.framedados)
        self.lineEditvalor.setFixedWidth(80)
        self.gridLayout.addWidget(self.lineEditvalor, 1, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 6)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(3, 1)
        self.botaoadd = QtWidgets.QPushButton(self.framedados)
        self.botaoadd.setToolTip("Adicionar linha")
        self.botaoadd.setFixedSize(QtCore.QSize(26, 26))
        self.linhasServico = [[self.lineEditDescricao, self.lineEditvalor]]
        self.gridLayout.addWidget(self.botaoadd, 1, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.gridLayout.addItem(spacerItem2, 0, 2, 1, 1)
        self.spacer = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.gridLayout.addItem(self.spacer, 2, 0, 1, 1)
        self.frameBotoesExt = QtWidgets.QFrame(self.main_frame)
        self.vlayout.addWidget(self.frameBotoesExt)
        self.hlayout2 = QtWidgets.QHBoxLayout(self.frameBotoesExt)
        spacer = QtWidgets.QSpacerItem(
            20,
            10,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        self.hlayout2.addItem(spacer)
        self.frameBotoes = QtWidgets.QFrame(self.main_frame)
        self.frameBotoes.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        self.frameBotoes.setMaximumWidth(
            int(QtGui.QGuiApplication.primaryScreen().size().width() * 0.65)
            if QtGui.QGuiApplication.primaryScreen().size().width() > 1280
            else QtGui.QGuiApplication.primaryScreen().size().width()
        )
        self.hlayout2.addWidget(self.frameBotoes)
        spacer = QtWidgets.QSpacerItem(
            20,
            10,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        self.hlayout2.addItem(spacer)
        self.hlayout3 = QtWidgets.QHBoxLayout(self.frameBotoes)
        self.labelLegenda = QtWidgets.QLabel(self.frameBotoes)
        self.hlayout3.addWidget(self.labelLegenda)
        spacerItem3 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.hlayout3.addItem(spacerItem3)
        self.botaoSalvar = QtWidgets.QPushButton(self.frameBotoes)
        self.botaoSalvar.setMinimumSize(100, 35)
        self.botaoSalvar.setObjectName("botaoprincipal")
        self.hlayout3.addWidget(self.botaoSalvar)
        self.botaoLimpar = QtWidgets.QPushButton(self.frameBotoes)
        self.botaoLimpar.setMinimumSize(100, 35)
        self.hlayout3.addWidget(self.botaoLimpar)
        self.setCentralWidget(self.main_frame)
        self.retranslateUi()
        # conexões
        self.botaoadd.clicked.connect(self.addlinhaservico)
        self.botaoLimpar.clicked.connect(self.resetarTela)
        self.botaoSalvar.clicked.connect(self.salvarServicos)
        self.botaoHelp.clicked.connect(
            lambda: help("Ajuda - Cadastro de Serviços", HELPCADASTROSERVICO)
        )

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelTitulo.setText(_translate("MainWindow", "Cadastro de serviços "))
        self.labelDescricao.setText(_translate("MainWindow", "Descrição do serviço*"))
        self.labelvalor.setText(_translate("MainWindow", "Valor un*"))
        self.botaoadd.setText(_translate("MainWindow", "+"))
        self.labelLegenda.setText(_translate("MainWindow", "* Campos Obrigatórios"))
        self.botaoLimpar.setText(_translate("MainWindow", "Limpar"))
        self.botaoSalvar.setText(_translate("MainWindow", "Salvar"))

    def addlinhaservico(self):
        lineedit1 = QtWidgets.QLineEdit()
        lineedit1.setMaxLength(80)
        lineedit1.setMaximumWidth(200)
        lineedit1.setMaximumWidth(600)
        lineedit2 = QtWidgets.QLineEdit()
        lineedit2.setFixedWidth(80)
        botaoRemoverLinha = QtWidgets.QPushButton()
        botaoRemoverLinha.setToolTip("Adicionar linha")
        botaoRemoverLinha.setFixedSize(QtCore.QSize(26, 26))
        botaoRemoverLinha.setText("-")
        botaoRemoverLinha.setObjectName("excluir")
        botaoRemoverLinha.clicked.connect(
            lambda: self.removerLinha(
                self.gridLayout.getItemPosition(
                    self.gridLayout.indexOf(botaoRemoverLinha)
                )[0]
            )
        )
        self.gridLayout.addWidget(lineedit1, len(self.linhasServico) + 1, 0, 1, 1)
        self.gridLayout.addWidget(lineedit2, len(self.linhasServico) + 1, 1, 1, 1)
        self.gridLayout.addWidget(
            botaoRemoverLinha, len(self.linhasServico) + 1, 2, 1, 1
        )
        self.linhasServico.append([lineedit1, lineedit2])
        self.gridLayout.removeItem(self.spacer)
        self.gridLayout.addItem(self.spacer, len(self.linhasServico) + 1, 0, 1, 1)

    def removerLinha(self, linha):
        for x in range(3):
            w = self.gridLayout.itemAtPosition(linha, x).widget()
            w.hide()
            w.setParent(None)
            w.deleteLater()
        for x in range(self.gridLayout.rowCount()):
            if x > linha:
                for y in range(3):
                    if (
                        not isinstance(
                            self.gridLayout.itemAtPosition(x, y), QtWidgets.QSpacerItem
                        )
                        and self.gridLayout.itemAtPosition(x, y) is not None
                    ):
                        self.gridLayout.addWidget(
                            self.gridLayout.itemAtPosition(x, y).widget(),
                            x - 1,
                            y,
                            1,
                            1,
                        )

        del self.linhasServico[linha - 1]
        self.gridLayout.removeItem(self.spacer)
        self.gridLayout.addItem(self.spacer, len(self.linhasServico) + 1, 0, 1, 1)

    def resetarTela(self):
        while len(self.linhasServico) > 1:
            self.removerLinha(2)
        self.limparCampos()

    def getServicos(self):
        servicos = []
        cont = 0
        for desc, valor in self.linhasServico:
            if desc.text() and valor.text():
                dict = {}
                dict["descricao"] = desc.text()
                if not (
                    valor.text().replace(",", "", 1).isnumeric()
                    or valor.text().replace(".", "", 1).isnumeric()
                ):
                    raise Exception('Campo "valor" inválido!')
                if -Decimal(valor.text().replace(",", ".", 1)).as_tuple().exponent > 2:
                    raise Exception(
                        "Valores devem possuir no máximo duas casas decimais!"
                    )
                dict["valor"] = valor.text().replace(",", ".", 1)
                servicos.append(dict)
                cont += 1
            elif desc.text() or valor.text():
                raise Exception("Preencha todos os campos de cada serviço!")
        if cont == 0:
            raise Exception("Campos vazios!")
        return servicos

    def salvarServicos(self):
        try:
            servicos = self.getServicos()
            r = ServicoController.salvarServicos(servicos)
            if isinstance(r, Exception):
                raise Exception(r)
            msg = QtWidgets.QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("resources/logo-icon.png"))
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setWindowTitle("Aviso")
            s = "s" if len(servicos) > 1 else ""
            msg.setText(f"Serviço{s} cadastrado{s} com sucesso!")
            msg.exec()
            self.resetarTela()
        except Exception as e:
            msg = QtWidgets.QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("resources/logo-icon.png"))
            msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg.setWindowTitle("Erro")
            msg.setText(str(e))
            msg.exec()

    def limparCampos(self):
        for lineedit in self.framedados.findChildren(QtWidgets.QLineEdit):
            lineedit.clear()
