from PyQt6 import QtCore, QtGui, QtWidgets
from container import handleDeps

class TelaCadastroServico(QtWidgets.QMainWindow):

    def __init__(self):
        super(TelaCadastroServico, self).__init__()
        self.servicoCtrl = handleDeps.getDep('SERVICOCTRL')
        self.setupUi()

    def setupUi(self):
        self.resize(1280, 760)
        self.main_frame = QtWidgets.QFrame(self)
        self.main_frame.setObjectName("main_frame")
        self.vlayout6 = QtWidgets.QVBoxLayout(self.main_frame)
        # frame titulo
        self.frame_titulo = QtWidgets.QFrame(self.main_frame)
        self.vlayout6.addWidget(self.frame_titulo)
        self.labelTitulo = QtWidgets.QLabel(self.frame_titulo)
        self.labelTitulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelTitulo.setObjectName("titulo")
        self.vlayout6.setContentsMargins(18, 18, 18, 18)
        self.vlayout6.setSpacing(36)
        self.vlayout6.addWidget(self.labelTitulo)
        self.scrollarea = QtWidgets.QScrollArea(self.main_frame)
        self.scrollarea.setWidgetResizable(True)
        self.scrollarea.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.vlayout6.addWidget(self.scrollarea)
        self.framedados = QtWidgets.QFrame(self.scrollarea)
        self.scrollarea.setWidget(self.framedados)
        self.gridLayout = QtWidgets.QGridLayout(self.framedados)

        self.labelnome = QtWidgets.QLabel(self.framedados)
        self.gridLayout.addWidget(self.labelnome, 0, 0, 1, 1)
        self.labelvalor = QtWidgets.QLabel(self.framedados)
        self.gridLayout.addWidget(self.labelvalor, 0, 1, 1, 1)
        self.lineEditnome = QtWidgets.QLineEdit(self.framedados)
        self.lineEditnome.setMaximumWidth(200)
        self.lineEditnome.setMaximumWidth(600)
        self.gridLayout.addWidget(self.lineEditnome, 1, 0, 1, 1)
        self.lineEditvalor = QtWidgets.QLineEdit(self.framedados)
        self.lineEditvalor.setFixedWidth(80)
        self.gridLayout.addWidget(self.lineEditvalor, 1, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 6)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(3, 1)
        self.botaoadd = QtWidgets.QPushButton(self.framedados)
        self.botaoadd.setToolTip('Adicionar linha')
        self.botaoadd.setFixedSize(QtCore.QSize(26, 26))
        self.linhasServico = [[self.lineEditnome, self.lineEditvalor]]
        self.gridLayout.addWidget(self.botaoadd, 1, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 2, 1, 1)
        self.spacer = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(self.spacer, 2, 0, 1, 1)
        self.frameBotoes1 = QtWidgets.QFrame(self.main_frame)
        self.hlayout2 = QtWidgets.QHBoxLayout(self.frameBotoes1)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.hlayout2.addItem(spacerItem3)
        self.botaoSalvar = QtWidgets.QPushButton(self.frameBotoes1)
        self.botaoSalvar.setMinimumSize(QtCore.QSize(100, 35))
        self.botaoSalvar.setObjectName('botaoprincipal')
        self.hlayout2.addWidget(self.botaoSalvar)
        self.botaoLimpar = QtWidgets.QPushButton(self.frameBotoes1)
        self.botaoLimpar.setMinimumSize(QtCore.QSize(100, 35))
        self.hlayout2.addWidget(self.botaoLimpar)
        self.vlayout6.addWidget(self.frameBotoes1)
        self.setCentralWidget(self.main_frame)
        self.retranslateUi()
        # conexões
        self.botaoadd.clicked.connect(self.addlinhaservico)
        self.botaoLimpar.clicked.connect(self.resetarTela)
        self.botaoSalvar.clicked.connect(self.salvarServicos)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelTitulo.setText(_translate(
            "MainWindow", "Cadastro de serviços"))
        self.labelnome.setText(_translate(
            "MainWindow", "Descrição do serviço*"))
        self.labelvalor.setText(_translate("MainWindow", "Valor un*"))
        self.botaoadd.setText(_translate("MainWindow", "+"))
        self.botaoLimpar.setText(_translate("MainWindow", "Limpar"))
        self.botaoSalvar.setText(_translate("MainWindow", "Salvar"))

    def addlinhaservico(self):
        label1 = QtWidgets.QLabel(text="Descrição do serviço*")
        label2 = QtWidgets.QLabel(text="Valor un*")
        lineedit1 = QtWidgets.QLineEdit()
        lineedit1.setMaximumWidth(200)
        lineedit1.setMaximumWidth(600)
        lineedit2 = QtWidgets.QLineEdit()
        lineedit2.setFixedWidth(80)
        botaoRemoverLinha = QtWidgets.QPushButton()
        botaoRemoverLinha.setToolTip('Adicionar linha')
        botaoRemoverLinha.setFixedSize(QtCore.QSize(26, 26))
        botaoRemoverLinha.setText("-")
        botaoRemoverLinha.setObjectName('excluir')
        botaoRemoverLinha.clicked.connect(lambda: self.removerLinha(self.gridLayout.getItemPosition(self.gridLayout.indexOf(botaoRemoverLinha))[0]))
        self.gridLayout.addWidget(label1, len(self.linhasServico)*2, 0, 1, 1)
        self.gridLayout.addWidget(label2, len(self.linhasServico)*2, 1, 1, 1)
        self.gridLayout.addWidget(lineedit1, len(
            self.linhasServico)*2+1, 0, 1, 1)
        self.gridLayout.addWidget(lineedit2, len(
            self.linhasServico)*2+1, 1, 1, 1)
        self.gridLayout.addWidget(botaoRemoverLinha, len(
            self.linhasServico)*2+1, 2, 1, 1)
        self.linhasServico.append([lineedit1, lineedit2])
        self.gridLayout.removeItem(self.spacer)
        self.gridLayout.addItem(self.spacer, len(
            self.linhasServico)*2, 0, 1, 1)

    def removerLinha(self, linha):
        for x in range(2):
            w1 = self.gridLayout.itemAtPosition(linha-1, x).widget()
            w1.hide()
            w1.setParent(None)
            w1.deleteLater()
            w2 = self.gridLayout.itemAtPosition(linha, x).widget()
            w2.hide()
            w2.setParent(None)
            w2.deleteLater()
        w = self.gridLayout.itemAtPosition(linha, 2).widget()
        w.hide()
        w.setParent(None)
        w.deleteLater()
        for x in range(self.gridLayout.rowCount()):
            if x > linha:
                for y in range(3):
                    if not isinstance(self.gridLayout.itemAtPosition(x, y), QtWidgets.QSpacerItem) and self.gridLayout.itemAtPosition(x, y) != None:
                        self.gridLayout.addWidget(self.gridLayout.itemAtPosition(x, y).widget(), x-2, y, 1, 1)
        
        del self.linhasServico[int((linha-1)/2)]
        self.gridLayout.removeItem(self.spacer)
        self.gridLayout.addItem(self.spacer, len(self.linhasServico)*2, 0, 1, 1)

    def resetarTela(self):
        while len(self.linhasServico)>1:
            self.removerLinha(3)
        self.limparCampos()

    def getServicos(self):
        servicos = []
        for desc, valor in self.linhasServico:
            if desc.text() and valor.text():
                dict = {}
                dict['descricao'] = desc.text()
                if not valor.text().replace(',','').replace('.','').isdigit():
                    raise Exception("Campo 'valor' inválido!")
                dict['valor'] = valor.text().replace(',','.',1)
                servicos.append(dict)
            elif desc.text() or valor.text():
                raise Exception('Preencha todos os campos de cada serviço!')
        return servicos

    def salvarServicos(self):
        try:
            servicos = self.getServicos()
            r = self.servicoCtrl.salvarServicos(servicos)
            if isinstance(r, Exception):
                raise Exception(r)
            msg = QtWidgets.QMessageBox()
            msg.setWindowIcon(QtGui.QIcon('./resources/logo-icon.png'))
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setWindowTitle("Aviso")
            s = 's' if len(servicos)>1 else ''
            msg.setText(f"Serviço{s} cadastrado{s} com sucesso!")
            msg.exec()
            self.resetarTela()
        except Exception as e:
            msg = QtWidgets.QMessageBox()
            msg.setWindowIcon(QtGui.QIcon('./resources/logo-icon.png'))
            msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg.setWindowTitle("Erro")
            msg.setText(str(e))
            msg.exec()

    def limparCampos(self):
        for lineedit in self.framedados.findChildren(QtWidgets.QLineEdit):
            lineedit.clear()
