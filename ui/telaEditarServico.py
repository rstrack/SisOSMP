from PyQt6 import QtCore, QtWidgets, QtGui
from container import handleDeps

class TelaEditarServico(QtWidgets.QMainWindow):
    retornarParaConsulta = QtCore.pyqtSignal(int)
    def __init__(self):
        super(TelaEditarServico, self).__init__()
        self.servicoCtrl = handleDeps.getDep('SERVICOCTRL')
        self.servicoID = None
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
        self.labelvalor = QtWidgets.QLabel(self.framedados)
        self.gridLayout.addWidget(self.labelvalor, 0, 1, 1, 1)
        self.lineEditNomeServico = QtWidgets.QLineEdit(self.framedados)
        self.lineEditNomeServico.setMaximumWidth(200)
        self.lineEditNomeServico.setMaximumWidth(600)
        self.gridLayout.addWidget(self.lineEditNomeServico, 1, 0, 1, 1)
        self.lineEditValorServico = QtWidgets.QLineEdit(self.framedados)
        self.lineEditValorServico.setFixedWidth(80)
        self.gridLayout.addWidget(self.lineEditValorServico, 1, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 6)
        self.gridLayout.setColumnStretch(4, 1)
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
        self.botaoCancelar.clicked.connect(self.cancelarEdicao)
        self.botaoEditar.clicked.connect(self.editarServico)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.labelTitulo.setText(_translate("MainWindow", "Editar Serviço"))
        self.labelnome.setText(_translate("MainWindow", "Descrição do serviço*"))
        self.labelvalor.setText(_translate("MainWindow", "Valor Un.*"))
        self.botaoCancelar.setText(_translate("MainWindow", "Cancelar"))
        self.botaoEditar.setText(_translate("MainWindow", "Editar"))

    def resetarTela(self):
        self.limparCampos()
        
    def getServico(self):
        if not self.lineEditNomeServico.text() or not self.lineEditValorServico.text():
            raise Exception("Preencha todos os campos!")
        dict = {}
        dict['descricao'] = self.lineEditNomeServico.text()
        if not self.lineEditValorServico.text().replace(',','',1).replace('.','',1).isdigit():
            raise Exception("Campo 'valor' deve possuir apenas números!")
        dict['valor'] = self.lineEditValorServico.text().replace(',','.',1)
        return dict

    def editarServico(self):
        try:
            servico = self.getServico()
            r = self.servicoCtrl.editarServico(self.servicoID, servico)
            if isinstance(r, Exception):
                raise Exception(r)
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Aviso")
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setText(f"Serviço editado com sucesso!")
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
        self.servicoID = id
        servico = self.servicoCtrl.getServico(id)
        self.lineEditNomeServico.setText(servico['descricao'])
        self.lineEditValorServico.setText(str(servico['valor']).replace('.',',',1))

    def limparCampos(self):
        for lineedit in self.framedados.findChildren(QtWidgets.QLineEdit):
            lineedit.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = TelaEditarServico()
    ui.show()
    style = open('./ui/styles.qss').read()
    app.setStyleSheet(style)
    sys.exit(app.exec())