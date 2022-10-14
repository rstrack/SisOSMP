from PyQt6 import QtWidgets, QtCore, QtGui
from container import handleDeps

class TelaEditarMarca(QtWidgets.QMainWindow):
    edicaoCompleta = QtCore.pyqtSignal(int)
    def __init__(self):
        super(TelaEditarMarca, self).__init__()
        self.marcaCtrl = handleDeps.getDep('MARCACTRL')
        self.setupUi()

    def setupUi(self):
        self.resize(400, 150)
        self.main_frame = QtWidgets.QFrame(self)
        self.main_frame.setObjectName("main_frame")
        self.vlayout = QtWidgets.QVBoxLayout(self.main_frame)
        self.framedados = QtWidgets.QFrame(self.main_frame)
        self.vlayout.addWidget(self.framedados)
        self.gridLayout = QtWidgets.QGridLayout(self.framedados)  
        self.label = QtWidgets.QLabel(self.framedados)
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.framedados)
        self.lineEdit.setMaxLength(50)
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.framebotoes = QtWidgets.QFrame(self.main_frame)
        self.vlayout.addWidget(self.framebotoes)
        self.hlayout = QtWidgets.QHBoxLayout(self.framebotoes)
        spacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.hlayout.addItem(spacer)
        self.botaoEditar = QtWidgets.QPushButton(self.framebotoes)
        self.botaoEditar.setFixedWidth(100)
        self.hlayout.addWidget(self.botaoEditar)
        self.botaoCancelar = QtWidgets.QPushButton(self.framebotoes)
        self.botaoCancelar.setFixedWidth(100)
        self.hlayout.addWidget(self.botaoCancelar)
        self.setCentralWidget(self.main_frame)
        self.retranslateUi()
        self.botaoEditar.clicked.connect(self.editarMarca)
        self.botaoCancelar.clicked.connect(self.cancelarEdicao) 

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Marcas"))
        self.label.setText(_translate("MainWindow", "Marca"))
        self.botaoEditar.setText(_translate("MainWindow", "Editar"))
        self.botaoCancelar.setText(_translate("MainWindow", "Cancelar"))

    def render(self, idMarca):
        self.marcaID = idMarca
        marca = self.marcaCtrl.getMarca(idMarca)
        self.lineEdit.setText(marca['nome'])
        self.show()

    def editarMarca(self):
        try:
            if not self.lineEdit.text():
                raise Exception('Insira a marca!')
            nomeMarca = self.lineEdit.text()
            r = self.marcaCtrl.editarMarca(self.marcaID, {'nome': nomeMarca})
            if isinstance(r, Exception):
                raise Exception(r)
            msg = QtWidgets.QMessageBox()
            msg.setWindowIcon(QtGui.QIcon('./resources/logo-icon.png'))
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setWindowTitle("Aviso")
            msg.setText('Marca editada com sucesso!')
            msg.exec()
            self.edicaoCompleta.emit(1)
            self.close()
        except Exception as e:
            msg = QtWidgets.QMessageBox()
            msg.setWindowIcon(QtGui.QIcon('./resources/logo-icon.png'))
            msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg.setWindowTitle("Erro")
            msg.setText(str(e))
            msg.exec()

    def cancelarEdicao(self):
        self.close()