from decimal import Decimal
from PyQt6 import QtCore, QtWidgets, QtGui
from ui.hoverButton import HoverButton
from util.container import handleDeps
from ui.telaCadastroOrcamento import UNIDADES


class TelaEditarPeca(QtWidgets.QMainWindow):
    paraTelaConsulta = QtCore.pyqtSignal(int)
    def __init__(self):
        super(TelaEditarPeca, self).__init__()
        self.pecaCtrl = handleDeps.getDep('PECACTRL')
        self.pecaID = None
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
        self.vlayout.addWidget(self.framedados)
        self.gridLayout = QtWidgets.QGridLayout(self.framedados)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setHorizontalSpacing(9)
        self.labelDescricao = QtWidgets.QLabel(self.framedados)
        self.gridLayout.addWidget(self.labelDescricao, 0, 0, 1, 1)
        self.labelUn = QtWidgets.QLabel(self.framedados)
        self.gridLayout.addWidget(self.labelUn, 0, 1, 1, 1)
        self.labelvalor = QtWidgets.QLabel(self.framedados)
        self.gridLayout.addWidget(self.labelvalor, 0, 2, 1, 1)
        self.lineEditDescricao = QtWidgets.QLineEdit(self.framedados)
        self.lineEditDescricao.setMaxLength(80)
        self.lineEditDescricao.setMaximumWidth(200)
        self.lineEditDescricao.setMaximumWidth(600)
        self.gridLayout.addWidget(self.lineEditDescricao, 1, 0, 1, 1)
        self.comboboxun = QtWidgets.QComboBox(self.framedados)
        self.comboboxun.addItems(UNIDADES)
        self.comboboxun.setCurrentIndex(15)
        self.gridLayout.addWidget(self.comboboxun, 1, 1, 1, 1)
        self.lineEditValorPeca = QtWidgets.QLineEdit(self.framedados)
        self.lineEditValorPeca.setFixedWidth(80)
        self.gridLayout.addWidget(self.lineEditValorPeca, 1, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 6)
        self.gridLayout.setColumnStretch(2, 2)
        self.gridLayout.setColumnStretch(4, 1)
        self.spacer = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(self.spacer, 2, 0, 1, 1)
        self.framebotoes = QtWidgets.QFrame(self.main_frame)
        self.hlayout2 = QtWidgets.QHBoxLayout(self.framebotoes)
        self.labelLegenda = QtWidgets.QLabel(self.framebotoes)
        self.hlayout2.addWidget(self.labelLegenda)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.hlayout2.addItem(spacerItem3)
        self.botaoSalvar = QtWidgets.QPushButton(self.framebotoes)
        self.botaoSalvar.setMinimumSize(100, 35)
        self.botaoSalvar.setObjectName('botaoprincipal')
        self.hlayout2.addWidget(self.botaoSalvar)
        self.botaoCancelar = QtWidgets.QPushButton(self.framebotoes)
        self.botaoCancelar.setMinimumSize(100, 35)
        self.hlayout2.addWidget(self.botaoCancelar)
        self.vlayout.addWidget(self.framebotoes)
        self.setCentralWidget(self.main_frame)
        self.retranslateUi()
        # conexoes
        self.botaoCancelar.clicked.connect(self.cancelarEdicao)
        self.botaoSalvar.clicked.connect(self.editarPeca)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.labelTitulo.setText(_translate("MainWindow", "Editar Peça"))
        self.labelDescricao.setText(_translate("MainWindow", "Descrição da peça*"))
        self.labelUn.setText(_translate("MainWindow", "Un"))
        self.labelvalor.setText(_translate("MainWindow", "Valor Un.*"))
        self.labelLegenda.setText(_translate("MainWindow", "* Campos Obrigatórios"))
        self.botaoCancelar.setText(_translate("MainWindow", "Cancelar"))
        self.botaoSalvar.setText(_translate("MainWindow", "Salvar"))

    def resetarTela(self):
        self.limparCampos()
        
    def getPeca(self):
        if not self.lineEditDescricao.text() or not self.lineEditValorPeca.text():
            raise Exception("Preencha todos os campos!")
        dict = {}
        dict['descricao'] = self.lineEditDescricao.text()
        dict['un'] = self.comboboxun.currentText()
        if not (self.lineEditValorPeca.text().replace(',','',1).isnumeric() or self.lineEditValorPeca.text().replace('.','',1).isnumeric()):
            raise Exception('Campo "valor" inválido!')
        if -Decimal(self.lineEditValorPeca.text().replace(',','.',1)).as_tuple().exponent > 2:
            raise Exception("Valores devem possuir no máximo duas casas decimais!")
        if float(self.lineEditValorPeca.text().replace(',','.',1)) <= 0:
            raise Exception('Campo "valor" deve ser maior que zero!')
        dict['valor'] = self.lineEditValorPeca.text().replace(',','.',1)
        return dict

    def editarPeca(self):
        try:
            peca = self.getPeca()
            r = self.pecaCtrl.editarPeca(self.pecaID, peca)
            if isinstance(r, Exception):
                raise Exception(r)
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Aviso")
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setText(f"Peça editada com sucesso!")
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
            self.paraTelaConsulta.emit(1)

    def renderEditar(self, id):
        self.pecaID = id
        peca = self.pecaCtrl.getPeca(id)
        self.lineEditDescricao.setText(peca['descricao'])
        self.lineEditValorPeca.setText('{:.2f}'.format(peca['valor']).replace('.',',',1))

    def limparCampos(self):
        for lineedit in self.framedados.findChildren(QtWidgets.QLineEdit):
            lineedit.clear()
