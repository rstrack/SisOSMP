import re
import threading

from PyQt6 import QtCore, QtGui, QtWidgets

from controller.cidadeController import CidadeController
from controller.clienteController import ClienteController
from controller.marcaController import MarcaController

from ui.help import HELPCADASTROCLIENTE, help
from ui.hoverButton import HoverButton

from util.buscaCEP import BuscaCEP

SIGLAESTADOS = [
    "AC",
    "AL",
    "AP",
    "AM",
    "BA",
    "CE",
    "DF",
    "ES",
    "GO",
    "MA",
    "MT",
    "MS",
    "MG",
    "PA",
    "PB",
    "PR",
    "PE",
    "PI",
    "RJ",
    "RN",
    "RS",
    "RO",
    "RR",
    "SC",
    "SP",
    "SE",
    "TO",
]

REGEXPLACA = "([A-Za-z]{2}[A-Za-z0-9][0-9][A-Za-z0-9]{3})|([A-Za-z]{3}-?[0-9]{4})"


class TelaCadastroCliente(QtWidgets.QMainWindow):
    def __init__(self):
        super(TelaCadastroCliente, self).__init__()
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
        # titulo
        self.frameTitulo = QtWidgets.QFrame(self.framegeral)
        self.vlayout.addWidget(self.frameTitulo)
        self.hlayouttitulo = QtWidgets.QHBoxLayout(self.frameTitulo)
        self.hlayouttitulo.setContentsMargins(0, 0, 0, 0)
        self.hlayouttitulo.setSpacing(0)
        self.hlayouttitulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.labelTitulo = QtWidgets.QLabel(self.frameTitulo)
        self.labelTitulo.setFixedHeight(100)
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
        # dados do cliente
        self.framedados = QtWidgets.QFrame(self.main_frame)
        self.vlayout2 = QtWidgets.QVBoxLayout(self.framedados)
        self.vlayout2.setSpacing(9)
        self.groupBoxCliente = QtWidgets.QGroupBox(self.framedados)
        self.groupBoxCliente.setTitle("Dados do Cliente")
        self.groupBoxCliente.setCheckable(True)
        self.vlayout2.addWidget(self.groupBoxCliente)
        self.glayoutp = QtWidgets.QGridLayout(self.groupBoxCliente)
        self.frameDadosCliente = QtWidgets.QFrame(self.groupBoxCliente)
        self.glayoutp.addWidget(self.frameDadosCliente, 0, 0, 1, -1)
        self.gridLayoutCliente = QtWidgets.QGridLayout(self.frameDadosCliente)
        self.labelTipo = QtWidgets.QLabel(self.frameDadosCliente)
        self.gridLayoutCliente.addWidget(self.labelTipo, 0, 0, 1, 1)
        self.labelNomeCliente = QtWidgets.QLabel(self.frameDadosCliente)
        self.gridLayoutCliente.addWidget(self.labelNomeCliente, 0, 1, 1, 1)
        self.labelDocumento = QtWidgets.QLabel(self.frameDadosCliente)
        self.gridLayoutCliente.addWidget(self.labelDocumento, 0, 2, 1, 1)
        self.comboBoxPessoa = QtWidgets.QComboBox(self.frameDadosCliente)
        self.comboBoxPessoa.addItems(
            ["PESSOA FÍSICA", "PESSOA JURÍDICA", "ESTRANGEIRO"]
        )
        self.gridLayoutCliente.addWidget(self.comboBoxPessoa, 1, 0, 1, 1)
        self.lineEditNomeCliente = QtWidgets.QLineEdit(self.frameDadosCliente)
        self.lineEditNomeCliente.setMaxLength(80)
        self.gridLayoutCliente.addWidget(self.lineEditNomeCliente, 1, 1, 1, 1)
        self.lineEditDocumento = QtWidgets.QLineEdit(self.frameDadosCliente)
        self.lineEditDocumento.setMaxLength(14)
        self.gridLayoutCliente.addWidget(self.lineEditDocumento, 1, 2, 1, 1)
        self.gridLayoutCliente.setColumnStretch(0, 1)
        self.gridLayoutCliente.setColumnStretch(1, 5)
        self.gridLayoutCliente.setColumnStretch(2, 1)
        self.frameEnder = QtWidgets.QFrame(self.groupBoxCliente)
        self.glayoutp.addWidget(self.frameEnder, 1, 0)
        self.gridLayout2 = QtWidgets.QGridLayout(self.frameEnder)
        self.frameEnder.setLayout(self.gridLayout2)
        self.labelcep = QtWidgets.QLabel(self.frameEnder)
        self.gridLayout2.addWidget(self.labelcep, 0, 0, 1, 1)
        self.labelender = QtWidgets.QLabel(self.frameEnder)
        self.gridLayout2.addWidget(self.labelender, 0, 1, 1, 2)
        self.labelnumero = QtWidgets.QLabel(self.frameEnder)
        self.gridLayout2.addWidget(self.labelnumero, 0, 3, 1, 1)
        self.lineEditCEP = QtWidgets.QLineEdit(self.frameEnder)
        self.lineEditCEP.setMaxLength(8)
        self.gridLayout2.addWidget(self.lineEditCEP, 1, 0, 1, 1)
        self.lineEditEnder = QtWidgets.QLineEdit(self.frameEnder)
        self.lineEditEnder.setMaxLength(80)
        self.gridLayout2.addWidget(self.lineEditEnder, 1, 1, 1, 2)
        self.lineEditNumero = QtWidgets.QLineEdit(self.frameEnder)
        self.lineEditNumero.setMaxLength(6)
        self.gridLayout2.addWidget(self.lineEditNumero, 1, 3, 1, 1)
        self.labelBairro = QtWidgets.QLabel(self.frameEnder)
        self.gridLayout2.addWidget(self.labelBairro, 2, 0, 1, 2)
        self.labelCidade = QtWidgets.QLabel(self.frameEnder)
        self.gridLayout2.addWidget(self.labelCidade, 2, 2, 1, 1)
        self.labelUF = QtWidgets.QLabel(self.frameEnder)
        self.gridLayout2.addWidget(self.labelUF, 2, 3, 1, 1)
        self.lineEditBairro = QtWidgets.QLineEdit(self.frameEnder)
        self.lineEditBairro.setMaxLength(50)
        self.gridLayout2.addWidget(self.lineEditBairro, 3, 0, 1, 2)
        self.lineEditCidade = QtWidgets.QLineEdit(self.frameEnder)
        self.lineEditCidade.setMaxLength(50)
        self.gridLayout2.addWidget(self.lineEditCidade, 3, 2, 1, 1)
        self.comboBoxuf = QtWidgets.QComboBox(self.frameEnder)
        self.comboBoxuf.addItems(SIGLAESTADOS)
        self.comboBoxuf.setCurrentText("PR")
        self.gridLayout2.addWidget(self.comboBoxuf, 3, 3, 1, 1)
        self.gridLayout2.setColumnStretch(1, 2)
        self.gridLayout2.setColumnStretch(2, 5)
        self.gridLayout2.setColumnStretch(3, 1)
        self.frameTel = QtWidgets.QFrame(self.groupBoxCliente)
        self.glayoutp.addWidget(self.frameTel, 1, 1)
        self.vlayout7 = QtWidgets.QVBoxLayout(self.frameTel)
        self.labelTel1 = QtWidgets.QLabel(self.frameTel)
        self.vlayout7.addWidget(self.labelTel1)
        self.lineEditFone1 = QtWidgets.QLineEdit(self.frameTel)
        self.lineEditFone1.setMaxLength(14)
        self.vlayout7.addWidget(self.lineEditFone1)
        self.labelTel2 = QtWidgets.QLabel(self.frameTel)
        self.vlayout7.addWidget(self.labelTel2)
        self.lineEditFone2 = QtWidgets.QLineEdit(self.frameTel)
        self.lineEditFone2.setMaxLength(14)
        self.vlayout7.addWidget(self.lineEditFone2)
        # DIVISÃO
        self.hline = QtWidgets.QFrame(self.framedados)
        self.hline.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.hline.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        # self.hline.setStyleSheet('border:none;background-color: gray')
        self.hline.setStyleSheet("color: gray")
        self.vlayout2.addWidget(self.hline)
        # dados do veiculo
        self.groupBoxVeiculo = QtWidgets.QGroupBox(self.framedados)
        self.groupBoxVeiculo.setTitle("Dados do Veículo")
        self.groupBoxVeiculo.setCheckable(True)
        self.gridLayout4 = QtWidgets.QGridLayout(self.groupBoxVeiculo)
        self.labelMarca = QtWidgets.QLabel(self.groupBoxVeiculo)
        self.gridLayout4.addWidget(self.labelMarca, 0, 0, 1, 1)
        self.labelModelo = QtWidgets.QLabel(self.groupBoxVeiculo)
        self.gridLayout4.addWidget(self.labelModelo, 0, 1, 1, 1)
        self.labelPlaca = QtWidgets.QLabel(self.groupBoxVeiculo)
        self.gridLayout4.addWidget(self.labelPlaca, 0, 2, 1, 1)
        self.comboBoxMarca = QtWidgets.QComboBox(self.groupBoxVeiculo)
        self.comboBoxMarca.setEditable(True)
        self.comboBoxMarca.lineEdit().setMaxLength(50)
        self.gridLayout4.addWidget(self.comboBoxMarca, 1, 0, 1, 1)
        self.lineEditModelo = QtWidgets.QLineEdit(self.groupBoxVeiculo)
        self.lineEditModelo.setMaxLength(30)
        self.gridLayout4.addWidget(self.lineEditModelo, 1, 1, 1, 1)
        self.lineEditPlaca = QtWidgets.QLineEdit(self.groupBoxVeiculo)
        self.lineEditPlaca.setMaxLength(8)
        self.gridLayout4.addWidget(self.lineEditPlaca, 1, 2, 1, 1)
        self.labelAno = QtWidgets.QLabel(self.groupBoxVeiculo)
        self.gridLayout4.addWidget(self.labelAno, 2, 0, 1, 1)
        self.lineEditAno = QtWidgets.QLineEdit(self.groupBoxVeiculo)
        self.lineEditAno.setMaxLength(4)
        self.gridLayout4.addWidget(self.lineEditAno, 3, 0, 1, 1)
        self.gridLayout4.setColumnStretch(0, 1)
        self.gridLayout4.setColumnStretch(1, 2)
        self.gridLayout4.setColumnStretch(2, 1)
        self.vlayout2.addWidget(self.groupBoxVeiculo)
        self.vlayout.addWidget(self.framedados)
        spacerItem4 = QtWidgets.QSpacerItem(
            20,
            10,
            QtWidgets.QSizePolicy.Policy.Maximum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.vlayout.addItem(spacerItem4)
        self.glayoutp.setColumnStretch(0, 3)
        self.glayoutp.setColumnStretch(1, 1)
        # botoes
        self.framebotoes = QtWidgets.QFrame(self.main_frame)
        self.hlayout4 = QtWidgets.QHBoxLayout(self.framebotoes)
        self.labelLegenda = QtWidgets.QLabel(self.framebotoes)
        self.hlayout4.addWidget(self.labelLegenda)
        spacerItem5 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.hlayout4.addItem(spacerItem5)
        self.botaoSalvar = QtWidgets.QPushButton(self.framebotoes)
        self.botaoSalvar.setMinimumSize(100, 35)
        self.botaoSalvar.setObjectName("botaoprincipal")
        self.hlayout4.addWidget(self.botaoSalvar)
        self.botaolimpar = QtWidgets.QPushButton(self.framebotoes)
        self.botaolimpar.setMinimumSize(100, 35)
        self.hlayout4.addWidget(self.botaolimpar)
        self.vlayout.addWidget(self.framebotoes)
        """spacerItem6 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.glayoutp.addItem(spacerItem6)"""
        self.setCentralWidget(self.main_frame)
        self.completerCidade = QtWidgets.QCompleter([])
        self.completerCidade.setMaxVisibleItems(5)
        self.completerCidade.setCaseSensitivity(
            QtCore.Qt.CaseSensitivity.CaseInsensitive
        )
        self.completerCidade.setCompletionMode(
            QtWidgets.QCompleter.CompletionMode.PopupCompletion
        )
        self.lineEditCidade.setCompleter(self.completerCidade)

        self.retranslateUi()
        self.setMarcas()

        self.botaolimpar.clicked.connect(self.resetarTela)
        self.botaoSalvar.clicked.connect(self.salvar)
        self.comboBoxPessoa.currentIndexChanged.connect(self.escolherTipoPessoa)
        self.lineEditCEP.textChanged.connect(self.buscarDadosCEP)
        self.groupBoxCliente.clicked.connect(self.checkBoxes)
        self.groupBoxVeiculo.clicked.connect(self.checkBoxes)
        self.botaoHelp.clicked.connect(
            lambda: help("Ajuda - Cadastro de Clientes", HELPCADASTROCLIENTE, 450)
        )

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Mecânica Pasetto"))
        self.labelTitulo.setText(
            _translate("MainWindow", "Cadastro de Clientes e/ou Veículos")
        )
        self.labelTipo.setText(_translate("MainWindow", "Tipo"))
        self.labelNomeCliente.setText(_translate("MainWindow", "Nome*"))
        self.labelDocumento.setText(_translate("MainWindow", "CPF"))
        self.labelCidade.setText(_translate("MainWindow", "Cidade"))
        self.labelcep.setText(_translate("MainWindow", "CEP"))
        self.labelBairro.setText(_translate("MainWindow", "Bairro"))
        self.labelender.setText(_translate("MainWindow", "Logradouro"))
        self.labelnumero.setText(_translate("MainWindow", "Nº"))
        self.labelUF.setText(_translate("MainWindow", "UF"))
        self.labelTel1.setText(_translate("MainWindow", "Fone 1*"))
        self.labelTel2.setText(_translate("MainWindow", "Fone 2"))
        self.labelAno.setText(_translate("MainWindow", "Ano"))
        self.labelPlaca.setText(_translate("MainWindow", "Placa*"))
        self.labelModelo.setText(_translate("MainWindow", "Modelo*"))
        self.labelMarca.setText(_translate("MainWindow", "Marca*"))
        self.labelLegenda.setText(_translate("MainWindow", "* Campos Obrigatórios"))
        self.botaolimpar.setText(_translate("MainWindow", "Limpar"))
        self.botaoSalvar.setText(_translate("MainWindow", "Salvar"))

    def salvar(self):
        try:
            cliente = self.getDadosCliente()
            veiculo = self.getDadosVeiculo()
            # se tem valores escritos nos campos de cliente e veiculo, tenta salvar os dois
            if cliente and veiculo:
                fones = self.getFones()
                r = ClienteController.salvarClienteVeiculo(cliente, fones, veiculo)
                string = "Cliente e Veiculo cadastrados com sucesso!"
            # se somente possuem dados sobre cliente:
            elif cliente:
                fones = self.getFones()
                r = ClienteController.salvarCliente(cliente, fones)
                string = "Cliente cadastrado com sucesso!"
            # se somente possuem dados sobre veiculo:
            elif veiculo:
                r = ClienteController.salvarVeiculo(veiculo)
                string = "Veiculo cadastrado com sucesso!"
            else:
                raise Exception("Campos vazios!")
            if isinstance(r, Exception):
                raise Exception(r)
            msg = QtWidgets.QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("resources/logo-icon.png"))
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setWindowTitle("Aviso")
            msg.setText(string)
            msg.exec()
            self.resetarTela()
        except Exception as e:
            msg = QtWidgets.QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("resources/logo-icon.png"))
            msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg.setWindowTitle("Erro")
            msg.setText(str(e))
            msg.exec()

    def limparCliente(self):
        for lineedit in self.groupBoxCliente.findChildren(QtWidgets.QLineEdit):
            lineedit.clear()

    def limparVeiculo(self):
        for lineedit in self.groupBoxVeiculo.findChildren(QtWidgets.QLineEdit):
            lineedit.clear()

    def resetarTela(self):
        self.limparCliente()
        self.limparVeiculo()
        self.setMarcas()

    def checkBoxes(self):
        if self.groupBoxCliente.isChecked() == False:
            self.limparCliente()
        if self.groupBoxVeiculo.isChecked() == False:
            self.limparVeiculo()

    def getDadosCliente(self):
        if self.groupBoxCliente.isChecked() == False:
            return None
        dict = {}
        dict["tipo"] = self.comboBoxPessoa.currentIndex()
        if self.lineEditDocumento.text():
            if dict["tipo"] == 0:
                documento = "CPF"
                if len(self.lineEditDocumento.text()) != 11:
                    raise Exception("CPF inválido!")
            elif dict["tipo"] == 1:
                documento = "CNPJ"
                if len(self.lineEditDocumento.text()) != 14:
                    raise Exception("CNPJ inválido!")
            else:
                documento = "Documento"
            if not self.lineEditDocumento.text().isnumeric():
                raise Exception(f'Digite apenas números no campo "{documento}"!')
            dict["documento"] = self.lineEditDocumento.text()
        else:
            dict["documento"] = None
        if self.lineEditNomeCliente.text():
            dict["nome"] = self.lineEditNomeCliente.text().title()
        else:
            raise Exception("Nome do cliente obrigatório!")
        if self.lineEditCEP.text():
            if not self.lineEditCEP.text().isnumeric():
                raise Exception('Digite apenas números no campo "CEP"!')
            if len(self.lineEditCEP.text()) != 8:
                raise Exception("CEP inválido!")
            dict["cep"] = self.lineEditCEP.text()
        else:
            dict["cep"] = None
        if self.lineEditEnder.text():
            dict["endereco"] = self.lineEditEnder.text()
        else:
            dict["endereco"] = None
        if self.lineEditNumero.text():
            dict["numero"] = self.lineEditNumero.text()
        else:
            dict["numero"] = None
        if self.lineEditBairro.text():
            dict["bairro"] = self.lineEditBairro.text()
        else:
            dict["bairro"] = None
        if self.lineEditCidade.text():
            dict["cidade"] = self.lineEditCidade.text().title()
        else:
            dict["cidade"] = None
        dict["uf"] = self.comboBoxuf.currentText()
        return dict

    def getFones(self):
        fones = []
        cont = 0
        if self.lineEditFone1.text():
            if (
                not self.lineEditFone1.text().isnumeric()
                or len(self.lineEditFone1.text()) < 8
            ):
                raise Exception("Fone 1 inválido!")
            fones.append(self.lineEditFone1.text())
            cont += 1
        else:
            fones.append(None)
        if self.lineEditFone2.text():
            if (
                not self.lineEditFone2.text().isnumeric()
                or len(self.lineEditFone2.text()) < 8
            ):
                raise Exception("Fone 2 inválido!")
            fones.append(self.lineEditFone2.text())
            cont += 1
        else:
            fones.append(None)
        if cont == 0:
            raise Exception("Fone obrigatório!")
        return fones

    def getDadosVeiculo(self):
        if self.groupBoxVeiculo.isChecked() == False:
            return None
        dict = {}
        if self.comboBoxMarca.currentText():
            dict["marca"] = self.comboBoxMarca.currentText().title()
        else:
            raise Exception("Marca obrigatória!")
        if self.lineEditModelo.text():
            dict["modelo"] = (
                self.lineEditModelo.text()[0].upper() + self.lineEditModelo.text()[1:]
            )
        else:
            raise Exception("Modelo obrigatório!")
        if self.lineEditPlaca.text():
            if not re.match(REGEXPLACA, self.lineEditPlaca.text()):
                raise Exception("Placa inválida!")
            dict["placa"] = self.lineEditPlaca.text().upper()
        else:
            raise Exception("Placa obrigatória!")
        if self.lineEditAno.text():
            if self.lineEditAno.text().isnumeric():
                if int(self.lineEditAno.text()) > 1900:
                    dict["ano"] = self.lineEditAno.text()
                else:
                    raise Exception("Ano do veículo inválido!")
            else:
                raise Exception("Ano do veículo inválido!")
        else:
            dict["ano"] = None
        return dict

    def setEndereco(
        self, cep=None, ender=None, numero=None, bairro=None, cidade=None, uf=None
    ):
        if cep:
            self.lineEditCEP.setText(cep)
        if ender:
            self.lineEditEnder.setText(ender)
        if numero:
            self.lineEditNumero.setText(numero)
        if bairro:
            self.lineEditBairro.setText(bairro)
        if cidade:
            self.lineEditCidade.setText(cidade)
        if uf:
            self.comboBoxuf.setCurrentIndex(
                self.comboBoxuf.findText(uf, QtCore.Qt.MatchFlag.MatchExactly)
            )

    def escolherTipoPessoa(self):
        if self.comboBoxPessoa.currentIndex() == 0:
            self.labelDocumento.setText("CPF")
        elif self.comboBoxPessoa.currentIndex() == 1:
            self.labelDocumento.setText("CNPJ")
        else:
            self.labelDocumento.setText("Documento")

    def setMarcas(self):
        currentText = self.comboBoxMarca.currentText()
        self.comboBoxMarca.clear()
        marcas = MarcaController.listarMarcas()
        for marca in marcas:
            self.comboBoxMarca.addItem(marca["nome"])
        self.comboBoxMarca.setCurrentIndex(
            self.comboBoxMarca.findText(currentText, QtCore.Qt.MatchFlag.MatchExactly)
        )

    def setCompleters(self):
        cidades = CidadeController.listarCidades()
        listaCidades = []
        if cidades:
            for cidade in cidades:
                listaCidades.append(cidade["nome"])
        modelCidades = QtCore.QStringListModel()
        modelCidades.setStringList(listaCidades)
        self.completerCidade.setModel(modelCidades)

    def buscarDadosCEP(self):
        cep = self.lineEditCEP.text()
        if len(cep) != 8:
            return
        t = threading.Thread(target=self.threadCEP, args=(cep,))
        t.start()

    def threadCEP(self, cep):
        dados = BuscaCEP.buscarCEP(cep)
        if dados is None:
            return
        if "erro" in dados:
            return
        self.lineEditEnder.setText(dados["logradouro"])
        self.lineEditBairro.setText(dados["bairro"])
        self.lineEditCidade.setText(dados["localidade"])
        self.comboBoxuf.setCurrentIndex(
            self.comboBoxuf.findText(dados["uf"], QtCore.Qt.MatchFlag.MatchExactly)
        )
        return
