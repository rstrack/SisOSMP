from PyQt6 import QtWidgets, QtCore, QtGui
from util.container import handleDeps
from ui.telaEditarMarca import TelaEditarMarca


class TelaMarcas(QtWidgets.QMainWindow):
    janelaFechada = QtCore.pyqtSignal(int)
    def __init__(self):
        super(TelaMarcas, self).__init__()
        self.marcaCtrl = handleDeps.getDep('MARCACTRL')
        self.setupUi()

    def setupUi(self):
        self.resize(400, 400)
        self.main_frame = QtWidgets.QFrame(self)
        self.main_frame.setObjectName("main_frame")
        self.vlayout = QtWidgets.QVBoxLayout(self.main_frame)
        self.framedados = QtWidgets.QFrame(self.main_frame)
        self.vlayout.addWidget(self.framedados)
        self.gridLayout = QtWidgets.QGridLayout(self.framedados)
        self.labelDetalhes = QtWidgets.QLabel(self.framedados)
        self.labelDetalhes.setObjectName('boldText')
        self.gridLayout.addWidget(self.labelDetalhes)
        self.tabela = QtWidgets.QTableWidget(self.framedados)
        self.gridLayout.addWidget(self.tabela)
        self.tabela.verticalHeader().setVisible(False)
        self.tabela.setEditTriggers(
            QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tabela.setSelectionMode(
            QtWidgets.QAbstractItemView.SelectionMode.NoSelection)
        self.tabela.horizontalHeader().setHighlightSections(False)
        self.framebotoes = QtWidgets.QFrame(self.main_frame)
        self.vlayout.addWidget(self.framebotoes)
        self.hlayout = QtWidgets.QHBoxLayout(self.framebotoes)
        spacer = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.hlayout.addItem(spacer)
        self.botaoConcluir = QtWidgets.QPushButton(self.framebotoes)
        self.botaoConcluir.setFixedWidth(100)
        self.hlayout.addWidget(self.botaoConcluir)

        self.setCentralWidget(self.main_frame)
        self.retranslateUi()
        self.botaoConcluir.clicked.connect(self.close)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Marcas"))
        self.labelDetalhes.setText(_translate("MainWindow", "Marcas"))
        self.botaoConcluir.setText(_translate("MainWindow", "Concluir"))

    def render(self):
        marcas = self.marcaCtrl.listarMarcas()
        if not marcas:
            try:
                self.close()
            except:
                return
        self.tabela.setColumnCount(4)
        self.tabela.setRowCount(len(marcas))
        header = ['ID', 'Marca', '', '']
        self.tabela.setHorizontalHeaderLabels(header)
        header = self.tabela.horizontalHeader()
        header.setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2,
            QtWidgets.QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(3,
            QtWidgets.QHeaderView.ResizeMode.Stretch)
        header.setDefaultAlignment(QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        i = 0
        for marca in marcas:
            item1 = QtWidgets.QTableWidgetItem(str(marca['idMarca']))
            self.tabela.setItem(i, 0, item1)
            item2 = QtWidgets.QTableWidgetItem(marca['nome'])
            self.tabela.setItem(i, 1, item2)
            botao1 = QtWidgets.QPushButton(self.framedados, text='Editar')
            botao1.setFixedWidth(100)
            botao1.clicked.connect(self.editarMarca)
            self.tabela.setCellWidget(i, 2, botao1)
            botao2 = QtWidgets.QPushButton(self.framedados, text='Excluir')
            botao2.setObjectName('excluir')
            botao2.setFixedWidth(100)
            botao2.clicked.connect(self.excluirMarca)
            self.tabela.setCellWidget(i, 3, botao2)
            i+=1
        self.tabela.hideColumn(0)
        self.show()

    def editarMarca(self):
        button = QtWidgets.QApplication.focusWidget()
        index = self.tabela.indexAt(button.pos())
        if index.isValid():
            linha = index.row()
            id = self.tabela.model().index(linha, 0).data()
            self.telaEditarMarca = TelaEditarMarca()
            self.telaEditarMarca.edicaoCompleta.connect(self.render)
            self.telaEditarMarca.render(id)

    def excluirMarca(self):
        try:
            button = QtWidgets.QApplication.focusWidget()
            index = self.tabela.indexAt(button.pos())
            if index.isValid():
                linha = index.row()
            id = self.tabela.model().index(linha, 0).data()
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Aviso")
            msgBox.setText('Tem certeza?')
            y = msgBox.addButton("Sim", QtWidgets.QMessageBox.ButtonRole.YesRole)
            n = msgBox.addButton("Não", QtWidgets.QMessageBox.ButtonRole.NoRole)
            y.setFixedWidth(60)
            n.setFixedWidth(60)
            msgBox.exec()
            if msgBox.clickedButton() == y:
                r = self.marcaCtrl.excluirMarca(id)
                if isinstance(r, Exception):
                    raise Exception(r)
            msg = QtWidgets.QMessageBox()
            msg.setWindowIcon(QtGui.QIcon('resources/logo-icon.png'))
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setWindowTitle("Aviso")
            msg.setText('Marca excluída com sucesso')
            msg.exec()
            self.render()
        except Exception as e:
            msg = QtWidgets.QMessageBox()
            msg.setWindowIcon(QtGui.QIcon('resources/logo-icon.png'))
            msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg.setWindowTitle("Erro")
            msg.setText(str(e))
            msg.exec()

    def closeEvent(self, event):
        self.janelaFechada.emit(1)
        event.accept()

