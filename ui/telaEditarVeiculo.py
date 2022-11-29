import re
from PyQt6 import QtCore, QtWidgets, QtGui
from ui.help import HELPEDITARVEICULO, help
from ui.telaCadastroCliente import REGEXPLACA
from ui.hoverButton import HoverButton
from util.container import handleDeps

SIGLAESTADOS = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS',
                'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']


class TelaEditarVeiculo(QtWidgets.QMainWindow):
    paraTelaConsulta = QtCore.pyqtSignal(int)
    def __init__(self):
        super(TelaEditarVeiculo, self).__init__()
        self.clienteCtrl = handleDeps.getDep('CLIENTECTRL')
        self.marcaCtrl = handleDeps.getDep('MARCACTRL')
        self.VeiculoID = None
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
        self.framegeral.setMaximumWidth(int(QtGui.QGuiApplication.primaryScreen().size().width()*0.65) 
            if QtGui.QGuiApplication.primaryScreen().size().width()> 1280 else QtGui.QGuiApplication.primaryScreen().size().width())
        self.hlayout.addWidget(self.framegeral)
        spacer = QtWidgets.QSpacerItem(
            20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.hlayout.addItem(spacer)
        self.vlayout = QtWidgets.QVBoxLayout(self.framegeral)
        self.vlayout.setContentsMargins(0,0,0,0)
        self.vlayout.setSpacing(0)
        # titulo
        self.frameTitulo = QtWidgets.QFrame(self.framegeral)
        self.vlayout.addWidget(self.frameTitulo)
        self.hlayouttitulo = QtWidgets.QHBoxLayout(self.frameTitulo)
        self.hlayouttitulo.setContentsMargins(0,0,0,0)
        self.hlayouttitulo.setSpacing(0)
        self.hlayouttitulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.labelTitulo = QtWidgets.QLabel(self.frameTitulo)
        self.labelTitulo.setFixedHeight(100)
        self.labelTitulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelTitulo.setObjectName("titulo")
        self.hlayouttitulo.addWidget(self.labelTitulo)
        self.botaoHelp = HoverButton("", "./resources/help-icon1.png", "./resources/help-icon2.png", self.frameTitulo)
        self.botaoHelp.setToolTip('Ajuda')
        self.botaoHelp.setObjectName('botaohelp')
        self.botaoHelp.setHelpIconSize(20,20)
        self.hlayouttitulo.addWidget(self.botaoHelp)
        self.framedados = QtWidgets.QFrame(self.main_frame)
        self.glayoutp = QtWidgets.QGridLayout(self.framedados)
        # dados do veiculo
        self.groupBoxVeiculo = QtWidgets.QGroupBox(self.framedados)
        self.groupBoxVeiculo.setTitle("Dados do Veículo")
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
        self.lineEditPlaca.setMaxLength(7)
        self.gridLayout4.addWidget(self.lineEditPlaca, 1, 2, 1, 1)
        self.labelAno = QtWidgets.QLabel(self.groupBoxVeiculo)
        self.gridLayout4.addWidget(self.labelAno, 2, 0, 1, 1)
        self.lineEditAno = QtWidgets.QLineEdit(self.groupBoxVeiculo)
        self.lineEditAno.setMaxLength(4)
        self.gridLayout4.addWidget(self.lineEditAno, 3, 0, 1, 1)
        self.gridLayout4.setColumnStretch(0, 1)
        self.gridLayout4.setColumnStretch(1, 2)
        self.gridLayout4.setColumnStretch(2, 1)
        self.glayoutp.addWidget(self.groupBoxVeiculo, 0, 0, 1, -1)
        spacerItem4 = QtWidgets.QSpacerItem(
            20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        self.glayoutp.addItem(spacerItem4)
        self.vlayout.addWidget(self.framedados)
        # botoes
        self.framebotoes = QtWidgets.QFrame(self.main_frame)
        self.hlayout4 = QtWidgets.QHBoxLayout(self.framebotoes)
        self.labelLegenda = QtWidgets.QLabel(self.framebotoes)
        self.hlayout4.addWidget(self.labelLegenda)
        spacerItem5 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.hlayout4.addItem(spacerItem5)
        self.botaoSalvar = QtWidgets.QPushButton(self.framebotoes)
        self.botaoSalvar.setMinimumSize(100, 35)
        self.botaoSalvar.setObjectName('botaoprincipal')
        self.hlayout4.addWidget(self.botaoSalvar)
        self.botaoCancelar = QtWidgets.QPushButton(self.framebotoes)
        self.botaoCancelar.setMinimumSize(100, 35)
        self.hlayout4.addWidget(self.botaoCancelar)
        self.vlayout.addWidget(self.framebotoes)
        spacerItem6 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.glayoutp.addItem(spacerItem6)
        self.setCentralWidget(self.main_frame)

        self.retranslateUi()

        self.botaoCancelar.clicked.connect(self.cancelarEdicao)
        self.botaoSalvar.clicked.connect(self.editar)
        self.botaoHelp.clicked.connect(lambda: help('Ajuda - Editar Serviço', HELPEDITARVEICULO))

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Mecânica Pasetto"))
        self.labelAno.setText(_translate("MainWindow", "Ano"))
        self.labelPlaca.setText(_translate("MainWindow", "Placa*"))
        self.labelModelo.setText(_translate("MainWindow", "Modelo*"))
        self.labelMarca.setText(_translate("MainWindow", "Marca*"))
        self.labelTitulo.setText(_translate("MainWindow", "Editar Veículo"))
        self.labelLegenda.setText(_translate("MainWindow", "* Campos Obrigatórios"))
        self.botaoCancelar.setText(_translate("MainWindow", "Cancelar"))
        self.botaoSalvar.setText(_translate("MainWindow", "Salvar"))

    def getDadosVeiculo(self):
        if len(list(filter(lambda dados: dados.text(), self.groupBoxVeiculo.findChildren(QtWidgets.QLineEdit)))) == 0:
            return None
        dict = {}
        if self.comboBoxMarca.currentText():
            dict['marca'] = self.comboBoxMarca.currentText().title()
        else:
            raise Exception('Marca obrigatória!')
        if self.lineEditModelo.text():
            dict['modelo'] = self.lineEditModelo.text()[0].upper() + self.lineEditModelo.text()[1:]
        else:
            raise Exception('Modelo obrigatório!')
        if self.lineEditPlaca.text():
            if not re.match(REGEXPLACA, self.lineEditPlaca.text()):
                raise Exception('Placa inválida!')
            dict['placa'] = self.lineEditPlaca.text().upper()
        else:
            raise Exception('Placa obrigatória!')
        if self.lineEditAno.text():
            if self.lineEditAno.text().isnumeric():
                if int(self.lineEditAno.text()) > 1900:
                    dict['ano'] = self.lineEditAno.text()
                else: raise Exception('Ano do veículo inválido!')
            else: raise Exception('Ano do veículo inválido!')
        else:
            dict['ano'] = None
        return dict

    def setVeiculo(self, marca, modelo, placa, ano=None):
        self.lineEditModelo.setText(modelo)
        self.lineEditAno.setText(ano)
        self.lineEditPlaca.setText(placa)
        self.comboBoxMarca.setCurrentIndex(
            self.comboBoxMarca.findText(marca, QtCore.Qt.MatchFlag.MatchExactly))

    def setMarcas(self):
        currentText = self.comboBoxMarca.currentText()
        self.comboBoxMarca.clear()
        marcas = self.marcaCtrl.listarMarcas()
        for marca in marcas:
            self.comboBoxMarca.addItem(marca['nome'])
        self.comboBoxMarca.setCurrentIndex(
            self.comboBoxMarca.findText(currentText, QtCore.Qt.MatchFlag.MatchExactly))
    
    def editar(self):
        try:
            veiculo = self.getDadosVeiculo()
            r = self.clienteCtrl.editarVeiculo(self.VeiculoID, veiculo)
            if isinstance(r, Exception):
                raise Exception(r)
            msg = QtWidgets.QMessageBox()
            msg.setWindowIcon(QtGui.QIcon('resources/logo-icon.png'))
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setWindowTitle("Aviso")
            msg.setText('Veiculo editado com sucesso!')
            msg.exec()
            self.paraTelaConsulta.emit(1)
        except Exception as e:
            msg = QtWidgets.QMessageBox()
            msg.setWindowIcon(QtGui.QIcon('resources/logo-icon.png'))
            msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg.setWindowTitle("Erro")
            msg.setText(str(e))
            msg.exec()

    def cancelarEdicao(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Aviso")
        msgBox.setText('Deseja cancelar a edição? Alterações serão perdidas')
        y = msgBox.addButton("Sim", QtWidgets.QMessageBox.ButtonRole.YesRole)
        n = msgBox.addButton("Não", QtWidgets.QMessageBox.ButtonRole.NoRole)
        y.setFixedWidth(60)
        n.setFixedWidth(60)
        msgBox.exec()
        if msgBox.clickedButton() == y:
            self.VeiculoID = None
            self.paraTelaConsulta.emit(1)
    
    def limparCampos(self):
        for lineedit in self.framedados.findChildren(QtWidgets.QLineEdit):
            lineedit.clear()

    def renderEditar(self, id):
        self.limparCampos()
        self.setMarcas()
        self.VeiculoID = id
        veiculo = self.clienteCtrl.getVeiculo(id)
        self.setVeiculo(veiculo['marca']['nome'], veiculo['modelo'], veiculo['placa'], veiculo['ano'])
