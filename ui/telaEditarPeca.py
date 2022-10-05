from PyQt6 import QtCore, QtWidgets, QtGui
from routes import handleRoutes
from ui.telaCadastroOrcamento import UNIDADES


class TelaEditarPeca(QtWidgets.QMainWindow):
    retornarParaConsulta = QtCore.pyqtSignal(int)
    def __init__(self):
        super(TelaEditarPeca, self).__init__()
        self.pecaCtrl = handleRoutes.getRoute('PECACTRL')
        self.setupUi()

    def setupUi(self):
        self.resize(1280, 760)
        self.main_frame = QtWidgets.QFrame(self)
        self.main_frame.setObjectName("main_frame")
        self.vlayout6 = QtWidgets.QVBoxLayout(self.main_frame)
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
        self.labelUn = QtWidgets.QLabel(self.framedados)
        self.gridLayout.addWidget(self.labelUn, 0, 1, 1, 1)
        self.labelvalor = QtWidgets.QLabel(self.framedados)
        self.gridLayout.addWidget(self.labelvalor, 0, 2, 1, 1)
        self.lineEditNomePeca = QtWidgets.QLineEdit(self.framedados)
        self.lineEditNomePeca.setMaximumWidth(200)
        self.lineEditNomePeca.setMaximumWidth(600)
        self.gridLayout.addWidget(self.lineEditNomePeca, 1, 0, 1, 1)
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
        self.linhasPeca.append(
            [self.lineEditNomePeca, self.comboboxun, self.lineEditValorPeca])
        self.botaoadd = QtWidgets.QPushButton(self.framedados)
        self.botaoadd.setFixedSize(QtCore.QSize(26, 26))
        self.gridLayout.addWidget(self.botaoadd, 1, 3, 1, 1)
        self.spacer = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(self.spacer, 2, 0, 1, 1)
        self.frameBotoes1 = QtWidgets.QFrame(self.main_frame)
        self.hlayout2 = QtWidgets.QHBoxLayout(self.frameBotoes1)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.hlayout2.addItem(spacerItem3)
        self.botaoEditar = QtWidgets.QPushButton(self.frameBotoes1)
        self.botaoEditar.setMinimumSize(QtCore.QSize(100, 30))
        self.hlayout2.addWidget(self.botaoEditar)
        self.botaoCancelar = QtWidgets.QPushButton(self.frameBotoes1)
        self.botaoCancelar.setMinimumSize(QtCore.QSize(100, 30))
        self.hlayout2.addWidget(self.botaoCancelar)
        self.vlayout6.addWidget(self.frameBotoes1)
        self.setCentralWidget(self.main_frame)
        self.retranslateUi()
        # conexoes
        self.botaoCancelar.clicked.connect(self.cancelar)
        self.botaoEditar.clicked.connect(self.editarPeca)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.labelTitulo.setText(_translate("MainWindow", "Editar Peça"))
        self.labelnome.setText(_translate("MainWindow", "Descrição da peça*"))
        self.labelUn.setText(_translate("MainWindow", "Un"))
        self.labelvalor.setText(_translate("MainWindow", "Valor Un.*"))
        self.botaoadd.setText(_translate("MainWindow", "+"))
        self.botaoCancelar.setText(_translate("MainWindow", "Cancelar"))
        self.botaoEditar.setText(_translate("MainWindow", "Editar"))

    def resetarTela(self):
        self.limparCampos()
        
    def getPeca(self):
        if not self.lineEditNomePeca.text() or not self.lineEditValorPeca.text():
            raise Exception("Preencha todos os campos!")
        dict = {}
        dict['descricao'] = self.lineEditNomePeca.text()
        dict['un'] = self.comboboxun.currentText()
        if not self.lineEditValorPeca.text().replace(',','',1).replace('.','',1).isdigit():
            raise Exception("Campo 'valor' deve possuir apenas números!")
        dict['valor'] = self.lineEditValorPeca.text().replace(',','.',1)
        return dict

    def editarPeca(self):
        try:
            peca = self.getPeca()
            r = self.pecaCtrl.salvarPeca(peca)
            if isinstance(r, Exception):
                raise Exception(r)
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Aviso")
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setText(f"Peça editada com sucesso!")
            msg.exec()
            self.retornarParaConsulta.emit(1)
        except Exception as e:
            msg = QtWidgets.QMessageBox()
            msg.setWindowIcon(QtGui.QIcon('./resources/logo-icon.png'))
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
            self.retornarParaConsulta.emit(1)

    def renderEditar(self, id):
        peca = self.pecaCtrl.getPeca(id)
        self.lineEditNomePeca.setText(peca['descricao'])

        self.lineEditValorPeca.setText(peca['valor'].replace('.',',',1))

    def limparCampos(self):
        for lineedit in self.framedados.findChildren(QtWidgets.QLineEdit):
            lineedit.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = TelaEditarPeca()
    ui.show()
    style = open('./ui/styles.qss').read()
    app.setStyleSheet(style)
    sys.exit(app.exec())
