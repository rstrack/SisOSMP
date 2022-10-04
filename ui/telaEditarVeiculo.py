from PyQt6 import QtCore, QtWidgets
from model.modelo import Veiculo
from routes import handleRoutes

SIGLAESTADOS = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS',
                'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']


class TelaEditarVeiculo(QtWidgets.QMainWindow):
    retornarConsulta = QtCore.pyqtSignal(int)
    def __init__(self):
        super(TelaEditarVeiculo, self).__init__()
        self.clienteCtrl = handleRoutes.getRoute('CLIENTECTRL')
        self.marcaCtrl = handleRoutes.getRoute('MARCACTRL')
        self.VeiculoID = None
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
        self.vlayout6.setContentsMargins(36, 18, 36, 18)
        self.vlayout6.setSpacing(36)
        self.vlayout6.addWidget(self.labelTitulo)
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
        self.gridLayout4.addWidget(self.comboBoxMarca, 1, 0, 1, 1)
        self.lineEditModelo = QtWidgets.QLineEdit(self.groupBoxVeiculo)
        self.gridLayout4.addWidget(self.lineEditModelo, 1, 1, 1, 1)
        self.lineEditPlaca = QtWidgets.QLineEdit(self.groupBoxVeiculo)
        self.gridLayout4.addWidget(self.lineEditPlaca, 1, 2, 1, 1)
        self.labelAno = QtWidgets.QLabel(self.groupBoxVeiculo)
        self.gridLayout4.addWidget(self.labelAno, 2, 0, 1, 1)
        self.lineEditAno = QtWidgets.QLineEdit(self.groupBoxVeiculo)
        self.gridLayout4.addWidget(self.lineEditAno, 3, 0, 1, 1)
        self.gridLayout4.setColumnStretch(0, 1)
        self.gridLayout4.setColumnStretch(1, 2)
        self.gridLayout4.setColumnStretch(2, 1)
        self.glayoutp.addWidget(self.groupBoxVeiculo, 0, 0, 1, -1)
        spacerItem4 = QtWidgets.QSpacerItem(
            20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        self.glayoutp.addItem(spacerItem4)
        self.vlayout6.addWidget(self.framedados)
        # botoes
        self.framebotoes = QtWidgets.QFrame(self.main_frame)
        self.hlayout4 = QtWidgets.QHBoxLayout(self.framebotoes)
        spacerItem5 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.hlayout4.addItem(spacerItem5)
        self.botaoEditar = QtWidgets.QPushButton(self.framebotoes)
        self.botaoEditar.setMinimumSize(QtCore.QSize(120, 35))
        self.botaoEditar.setObjectName('botaoprincipal')
        self.hlayout4.addWidget(self.botaoEditar)
        self.botaoCancelar = QtWidgets.QPushButton(self.framebotoes)
        self.botaoCancelar.setMinimumSize(QtCore.QSize(100, 30))
        self.hlayout4.addWidget(self.botaoCancelar)
        self.vlayout6.addWidget(self.framebotoes)
        spacerItem6 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.glayoutp.addItem(spacerItem6)
        self.setCentralWidget(self.main_frame)

        self.retranslateUi()

        self.botaoCancelar.clicked.connect(self.cancelarEdicao)
        self.botaoEditar.clicked.connect(self.editar)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Mecânica Pasetto"))
        self.labelAno.setText(_translate("MainWindow", "Ano"))
        self.labelPlaca.setText(_translate("MainWindow", "Placa"))
        self.labelModelo.setText(_translate("MainWindow", "Modelo"))
        self.labelMarca.setText(_translate("MainWindow", "Marca"))
        self.labelTitulo.setText(_translate("MainWindow", "Editar Veículo"))
        self.botaoCancelar.setText(_translate("MainWindow", "Cancelar"))
        self.botaoEditar.setText(_translate("MainWindow", "Editar"))

    def getDadosVeiculo(self):
        if len(list(filter(lambda dados: dados.text(), self.groupBoxVeiculo.findChildren(QtWidgets.QLineEdit)))) == 0:
            return None
        dict = {}
        dict['marca'] = self.comboBoxMarca.currentText().upper()
        if dict['marca'] == '':
            raise Exception('Marca obrigatória!')
        if (self.lineEditModelo.text()):
            dict['modelo'] = self.lineEditModelo.text().title()
        else:
            raise Exception('Modelo obrigatório!')
        if (self.lineEditPlaca.text()):
            if not self.lineEditPlaca.text().isalnum():
                raise Exception('Insira apenas letras e números na placa!')
            dict['placa'] = self.lineEditPlaca.text().upper()
        else:
            raise Exception('Placa obrigatória')
        
        if (self.lineEditAno.text()):
            dict['ano'] = self.lineEditAno.text()
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
        self.comboBoxMarca.clear()
        marcas = self.marcaCtrl.listarMarcas()
        for marca in marcas:
            self.comboBoxMarca.addItem(marca['nome'])
        self.comboBoxMarca.setCurrentIndex(-1)
    
    def editar(self):
        try:
            veiculo = self.getDadosVeiculo()
            r = self.clienteCtrl.editarVeiculo(self.VeiculoID, veiculo)
            if isinstance(r, Exception):
                raise Exception(r)
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Aviso")
            msg.setText('Veiculo editado com sucesso!')
            msg.exec()
            self.retornarConsulta.emit(1)
        except Exception as e:
            msg = QtWidgets.QMessageBox()
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
            self.retornarConsulta.emit(1)
    
    def limparCampos(self):
        for lineedit in self.framedados.findChildren(QtWidgets.QLineEdit):
            lineedit.clear()

    def renderEditar(self, id):
        self.limparCampos()
        self.setMarcas()
        self.VeiculoID = id
        veiculo = self.clienteCtrl.getVeiculo(id)
        self.setVeiculo(veiculo['marca']['nome'], veiculo['modelo'], veiculo['placa'], veiculo['ano'])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = TelaEditarVeiculo()

    ui.show()

    style = open('./ui/styles.qss').read()
    app.setStyleSheet(style)

    sys.exit(app.exec())