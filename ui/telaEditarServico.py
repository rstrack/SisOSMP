from decimal import Decimal
from PyQt6 import QtCore, QtWidgets, QtGui
from util.container import handleDeps

class TelaEditarServico(QtWidgets.QMainWindow):
    paraTelaConsulta = QtCore.pyqtSignal(int)
    def __init__(self):
        super(TelaEditarServico, self).__init__()
        self.servicoCtrl = handleDeps.getDep('SERVICOCTRL')
        self.servicoID = None
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
        self.labelTitulo = QtWidgets.QLabel(self.framegeral)
        self.labelTitulo.setFixedHeight(100)
        self.labelTitulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelTitulo.setObjectName("titulo")
        self.vlayout.addWidget(self.labelTitulo)
        self.framedados = QtWidgets.QFrame(self.main_frame)
        self.vlayout.addWidget(self.framedados)
        self.gridLayout = QtWidgets.QGridLayout(self.framedados)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setHorizontalSpacing(9)
        self.labelDescricao = QtWidgets.QLabel(self.framedados)
        self.gridLayout.addWidget(self.labelDescricao, 0, 0, 1, 1)
        self.labelvalor = QtWidgets.QLabel(self.framedados)
        self.gridLayout.addWidget(self.labelvalor, 0, 1, 1, 1)
        self.lineEditDescricao = QtWidgets.QLineEdit(self.framedados)
        self.lineEditDescricao.setMaxLength(80)
        self.lineEditDescricao.setMaximumWidth(200)
        self.lineEditDescricao.setMaximumWidth(600)
        self.gridLayout.addWidget(self.lineEditDescricao, 1, 0, 1, 1)
        self.lineEditValorServico = QtWidgets.QLineEdit(self.framedados)
        self.lineEditValorServico.setFixedWidth(80)
        self.gridLayout.addWidget(self.lineEditValorServico, 1, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 6)
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
        self.botaoSalvar.setMinimumSize(QtCore.QSize(100, 35))
        self.botaoSalvar.setObjectName('botaoprincipal')
        self.hlayout2.addWidget(self.botaoSalvar)
        self.botaoCancelar = QtWidgets.QPushButton(self.framebotoes)
        self.botaoCancelar.setMinimumSize(QtCore.QSize(100, 35))
        self.hlayout2.addWidget(self.botaoCancelar)
        self.vlayout.addWidget(self.framebotoes)
        self.setCentralWidget(self.main_frame)
        self.retranslateUi()
        # conexoes
        self.botaoCancelar.clicked.connect(self.cancelarEdicao)
        self.botaoSalvar.clicked.connect(self.editarServico)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.labelTitulo.setText(_translate("MainWindow", "Editar Serviço"))
        self.labelDescricao.setText(_translate("MainWindow", "Descrição do serviço*"))
        self.labelvalor.setText(_translate("MainWindow", "Valor Un.*"))
        self.labelLegenda.setText(_translate("MainWindow", "* Campos Obrigatórios"))
        self.botaoCancelar.setText(_translate("MainWindow", "Cancelar"))
        self.botaoSalvar.setText(_translate("MainWindow", "Salvar"))

    def resetarTela(self):
        self.limparCampos()
        
    def getServico(self):
        if not self.lineEditDescricao.text() or not self.lineEditValorServico.text():
            raise Exception("Preencha todos os campos!")
        dict = {}
        dict['descricao'] = self.lineEditDescricao.text()
        if not (self.lineEditValorServico.text().replace(',','',1).isnumeric() or self.lineEditValorServico.text().replace('.','',1).isnumeric()):
            raise Exception('Campo "valor" inválido!')
        if -Decimal(self.lineEditValorServico.text().replace(',','.',1)).as_tuple().exponent > 2:
            raise Exception("Valores devem possuir no máximo duas casas decimais!")
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
        self.servicoID = id
        servico = self.servicoCtrl.getServico(id)
        self.lineEditDescricao.setText(servico['descricao'])
        self.lineEditValorServico.setText('{:.2f}'.format(servico['valor']).replace('.',',',1))

    def limparCampos(self):
        for lineedit in self.framedados.findChildren(QtWidgets.QLineEdit):
            lineedit.clear()
