from decimal import Decimal
from PyQt6 import QtCore, QtWidgets, QtGui
from util.container import handleDeps
from ui.telaCadastroOrcamento import UNIDADES


class TelaCadastroPeca(QtWidgets.QMainWindow):

    def __init__(self):
        super(TelaCadastroPeca, self).__init__()
        self.pecaCtrl = handleDeps.getDep('PECACTRL')
        self.setupUi()

    def setupUi(self):
        self.resize(1280, 760)
        self.main_frame = QtWidgets.QFrame(self)
        self.main_frame.setObjectName("main_frame")
        self.vlayout = QtWidgets.QVBoxLayout(self.main_frame)
        self.vlayout.setContentsMargins(0,0,0,0)
        self.vlayout.setSpacing(0)
        self.labelTitulo = QtWidgets.QLabel(self.main_frame)
        self.labelTitulo.setFixedHeight(120)
        self.labelTitulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelTitulo.setObjectName("titulo")
        self.vlayout.addWidget(self.labelTitulo)
        self.scrollarea = QtWidgets.QScrollArea(self.main_frame)
        #self.scrollarea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollarea.setWidgetResizable(True)
        self.framegeral = QtWidgets.QFrame(self.scrollarea)
        self.vlayout.addWidget(self.scrollarea)
        self.scrollarea.setWidget(self.framegeral)
        self.hlayout1 = QtWidgets.QHBoxLayout(self.framegeral)
        spacer = QtWidgets.QSpacerItem(
            20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.hlayout1.addItem(spacer)
        self.framedados = QtWidgets.QFrame(self.scrollarea)
        self.framedados.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        self.framedados.setMaximumWidth(int(QtGui.QGuiApplication.primaryScreen().size().width()*0.65) 
            if QtGui.QGuiApplication.primaryScreen().size().width()> 1280 else QtGui.QGuiApplication.primaryScreen().size().width())
        self.hlayout1.addWidget(self.framedados)
        spacer = QtWidgets.QSpacerItem(
            20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.hlayout1.addItem(spacer)
        self.gridLayout = QtWidgets.QGridLayout(self.framedados)
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
        self.linhasPeca = [[self.lineEditDescricao, self.comboboxun, self.lineEditValorPeca]]
        self.botaoadd = QtWidgets.QPushButton(self.framedados)
        self.botaoadd.setToolTip('Adicionar linha')
        self.botaoadd.setFixedSize(QtCore.QSize(26, 26))
        self.gridLayout.addWidget(self.botaoadd, 1, 3, 1, 1)
        self.spacer = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(self.spacer, 2, 0, 1, 1)
        self.frameBotoesExt = QtWidgets.QFrame(self.main_frame)
        self.vlayout.addWidget(self.frameBotoesExt)
        self.hlayout2 = QtWidgets.QHBoxLayout(self.frameBotoesExt)
        spacer = QtWidgets.QSpacerItem(
            20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.hlayout2.addItem(spacer)
        self.frameBotoes = QtWidgets.QFrame(self.main_frame)
        self.frameBotoes.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        self.frameBotoes.setMaximumWidth(int(QtGui.QGuiApplication.primaryScreen().size().width()*0.65) 
            if QtGui.QGuiApplication.primaryScreen().size().width()> 1280 else QtGui.QGuiApplication.primaryScreen().size().width())
        self.hlayout2.addWidget(self.frameBotoes)
        spacer = QtWidgets.QSpacerItem(
            20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.hlayout2.addItem(spacer)
        self.hlayout3 = QtWidgets.QHBoxLayout(self.frameBotoes)
        self.labelLegenda = QtWidgets.QLabel(self.frameBotoes)
        self.hlayout3.addWidget(self.labelLegenda)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.hlayout3.addItem(spacerItem3)
        self.botaosalvar = QtWidgets.QPushButton(self.frameBotoes)
        self.botaosalvar.setMinimumSize(100, 35)
        self.botaosalvar.setObjectName('botaoprincipal')
        self.hlayout3.addWidget(self.botaosalvar)
        self.botaolimpar = QtWidgets.QPushButton(self.frameBotoes)
        self.botaolimpar.setMinimumSize(100, 35)
        self.hlayout3.addWidget(self.botaolimpar)
        self.setCentralWidget(self.main_frame)
        self.retranslateUi()
        # conexoes
        self.botaoadd.clicked.connect(self.addLinhaPeca)
        self.botaolimpar.clicked.connect(self.resetarTela)
        self.botaosalvar.clicked.connect(self.salvarPecas)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.labelTitulo.setText(_translate("MainWindow", "Cadastro de peças"))
        self.labelDescricao.setText(_translate("MainWindow", "Nome da peça*"))
        self.labelUn.setText(_translate("MainWindow", "Un"))
        self.labelvalor.setText(_translate("MainWindow", "Valor un*"))
        self.botaoadd.setText(_translate("MainWindow", "+"))
        self.labelLegenda.setText(_translate("MainWindow", "* Campos Obrigatórios"))
        self.botaolimpar.setText(_translate("MainWindow", "Limpar"))
        self.botaosalvar.setText(_translate("MainWindow", "Salvar"))

    def addLinhaPeca(self):
        lineedit1 = QtWidgets.QLineEdit()
        lineedit1.setMaxLength(80)
        lineedit1.setMaximumWidth(200)
        lineedit1.setMaximumWidth(600)
        comboBox = QtWidgets.QComboBox()
        comboBox.addItems(UNIDADES)
        comboBox.setCurrentIndex(15)
        lineedit2 = QtWidgets.QLineEdit()
        lineedit2.setFixedWidth(80)
        botaoRemoverLinha = QtWidgets.QPushButton()
        botaoRemoverLinha.setFixedSize(QtCore.QSize(26, 26))
        botaoRemoverLinha.setToolTip('Remover linha')
        botaoRemoverLinha.setText("-")
        botaoRemoverLinha.setObjectName('excluir')
        botaoRemoverLinha.clicked.connect(lambda: self.removerLinha(self.gridLayout.getItemPosition(self.gridLayout.indexOf(botaoRemoverLinha))[0]))
        self.gridLayout.addWidget(lineedit1, len(self.linhasPeca)+1, 0, 1, 1)
        self.gridLayout.addWidget(comboBox, len(self.linhasPeca)+1, 1, 1, 1)
        self.gridLayout.addWidget(lineedit2, len(self.linhasPeca)+1, 2, 1, 1)
        self.gridLayout.addWidget(botaoRemoverLinha, len(
            self.linhasPeca)+1, 3, 1, 1)
        self.linhasPeca.append([lineedit1, comboBox, lineedit2])
        self.gridLayout.removeItem(self.spacer)
        self.gridLayout.addItem(self.spacer, len(self.linhasPeca)+1, 0, 1, 1)

    def removerLinha(self, linha):
        for x in range(4):
            w = self.gridLayout.itemAtPosition(linha, x).widget()
            w.hide()
            w.setParent(None)
            w.deleteLater()
        for x in range(self.gridLayout.rowCount()):
            if x > linha:
                for y in range(4):
                    if not isinstance(self.gridLayout.itemAtPosition(x, y), QtWidgets.QSpacerItem) and self.gridLayout.itemAtPosition(x, y) != None:
                        self.gridLayout.addWidget(self.gridLayout.itemAtPosition(x, y).widget(), x-1, y, 1, 1)
        del self.linhasPeca[linha-1]
        self.gridLayout.removeItem(self.spacer)
        self.gridLayout.addItem(self.spacer, len(self.linhasPeca)+1, 0, 1, 1)

    def resetarTela(self):
        while len(self.linhasPeca)>1:
            self.removerLinha(3)
        self.limparCampos()
        

    def getPecas(self):
        pecas = []
        cont = 0
        for desc, un, valor in self.linhasPeca:
            if desc.text() and valor.text():
                dict = {}
                dict['descricao'] = desc.text()
                dict['un'] = un.currentText()
                if not (valor.text().replace(',','',1).isnumeric() or valor.text().replace('.','',1).isnumeric()):
                    raise Exception('Campo "valor" inválido!')
                if -Decimal(valor.text().replace(',','.',1)).as_tuple().exponent > 2:
                    raise Exception("Valores devem possuir no máximo duas casas decimais!")
                if float(valor.text().replace(',','.',1)) <= 0:
                    raise Exception('Campo "valor" deve ser maior que zero!')
                dict['valor'] = valor.text().replace(',','.',1)
                pecas.append(dict)
                cont+=1
            elif desc.text() or valor.text():
                raise Exception('Preencha todos os campos de cada peça!')
        if cont == 0:
            raise Exception('Campos vazios!')
        return pecas

    def salvarPecas(self):
        try:
            pecas = self.getPecas()
            r = self.pecaCtrl.salvarPecas(pecas)
            if isinstance(r, Exception):
                raise Exception(r)
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Aviso")
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            s = 's' if len(pecas)>1 else ''
            msg.setText(f"Peça{s} cadastrada{s} com sucesso!")
            msg.exec()
            self.resetarTela()
        except Exception as e:
            msg = QtWidgets.QMessageBox()
            msg.setWindowIcon(QtGui.QIcon('resources/logo-icon.png'))
            msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg.setWindowTitle("Erro")
            msg.setText(str(e))
            msg.exec()

    def limparCampos(self):
        for lineedit in self.framedados.findChildren(QtWidgets.QLineEdit):
            lineedit.clear()

