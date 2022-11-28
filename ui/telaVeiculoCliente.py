from PyQt6 import QtCore, QtWidgets
from ui.hoverButton import HoverButton
from util.container import handleDeps

class TelaVeiculoCliente(QtWidgets.QMainWindow):
    janelaFechada = QtCore.pyqtSignal(int)
    def __init__(self):
        super(TelaVeiculoCliente, self).__init__()
        self.clienteCtrl = handleDeps.getDep('CLIENTECTRL')
        self.clienteID = None
        self.veiculoID = None
        self.setupUi()

    def setupUi(self):
        # self.resize(400, 400)
        self.main_frame = QtWidgets.QFrame(self)
        self.main_frame.setObjectName("main_frame")
        self.vlayout = QtWidgets.QVBoxLayout(self.main_frame)
        self.frameTitulo = QtWidgets.QFrame(self.main_frame)
        self.vlayout.addWidget(self.frameTitulo)
        self.hlayouttitulo = QtWidgets.QHBoxLayout(self.frameTitulo)
        self.hlayouttitulo.setContentsMargins(0,0,0,0)
        self.hlayouttitulo.setSpacing(0)
        self.hlayouttitulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.labelTitulo = QtWidgets.QLabel(self.frameTitulo)
        self.labelTitulo.setFixedHeight(40)
        self.labelTitulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelTitulo.setObjectName("boldText")
        self.hlayouttitulo.addWidget(self.labelTitulo)
        self.botaoHelp = HoverButton("", "./resources/help-icon1.png", "./resources/help-icon2.png", self.frameTitulo)
        self.botaoHelp.setToolTip('Ajuda')
        self.botaoHelp.setObjectName('botaohelp')
        self.botaoHelp.setHelpIconSize(18,18)
        self.hlayouttitulo.addWidget(self.botaoHelp)
        self.framedados = QtWidgets.QFrame(self.main_frame)
        self.vlayout.addWidget(self.framedados)
        # self.gridLayout = QtWidgets.QGridLayout(self.framedados)
        self.vlayout2 = QtWidgets.QVBoxLayout(self.framedados)
        self.tabela = QtWidgets.QTableWidget(self.framedados)
        self.vlayout2.addWidget(self.tabela)
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
        self.setWindowTitle(_translate("MainWindow", "Veículos/Clientes"))
        self.botaoConcluir.setText(_translate("MainWindow", "Concluir"))

    def renderVeiculos(self, idCliente):
        self.setWindowTitle("Veículos")
        self.tabela.setColumnCount(5)
        header = ['ID', 'Marca', 'Modelo', 'Placa', '']
        self.tabela.setHorizontalHeaderLabels(header)
        header = self.tabela.horizontalHeader()
        header.setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        header.setDefaultAlignment(QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        header.setStretchLastSection(True)
        self.clienteID = idCliente
        i = 0
        cliente = self.clienteCtrl.getCliente(idCliente)
        self.labelTitulo.setText(f"Veículos vinculados ao cliente\n{cliente['nome']}")
        veiculos = self.clienteCtrl.listarVeiculos(idCliente)
        if veiculos:
            self.tabela.setRowCount(len(veiculos))
            for veiculo in veiculos:
                item1 = QtWidgets.QTableWidgetItem(str(veiculo['idVeiculo']))
                self.tabela.setItem(i, 0, item1)
                item2 = QtWidgets.QTableWidgetItem(veiculo['marca']['nome'])
                self.tabela.setItem(i, 1, item2)
                item3 = QtWidgets.QTableWidgetItem(veiculo['modelo'])
                self.tabela.setItem(i, 2, item3)
                item4 = QtWidgets.QTableWidgetItem(veiculo['placa'])
                self.tabela.setItem(i, 3, item4)
                botao = QtWidgets.QPushButton(self.framedados, text='Desvincular')
                botao.setFixedWidth(150)
                botao.clicked.connect(self.desvincularVeiculo)
                self.tabela.setCellWidget(i, 4, botao)
                i+=1
            self.tabela.hideColumn(0)
            self.resize(self.tabela.sizeHintForColumn(0) + 
                self.tabela.sizeHintForColumn(1) +
                self.tabela.sizeHintForColumn(2) +
                self.tabela.sizeHintForColumn(3) +
                self.tabela.sizeHintForColumn(4) + 30,
                400)
        else:
            self.tabela.setRowCount(0)

    def desvincularVeiculo(self):
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
                veiculo = self.clienteCtrl.getVeiculo(id)
                r = self.clienteCtrl.excluirVeiculoCliente(veiculo['idVeiculo'], self.clienteID)
                if isinstance(r, Exception):
                    raise Exception(r)
            self.renderVeiculos(self.clienteID)

    def renderClientes(self, idVeiculo):
        self.setWindowTitle("Clientes")
        self.tabela.setColumnCount(5)
        header = ['ID', 'Nome', 'Documento', 'Fones', '']
        self.tabela.setHorizontalHeaderLabels(header)
        header = self.tabela.horizontalHeader()
        header.setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(3,
            QtWidgets.QHeaderView.ResizeMode.Interactive)
        header.setDefaultAlignment(QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        header.setStretchLastSection(True)
        self.veiculoID = idVeiculo
        i = 0
        veiculo = self.clienteCtrl.getVeiculo(idVeiculo)
        self.labelTitulo.setText(f"Clientes vinculados ao veículo\n{veiculo['marca']['nome']} {veiculo['modelo']}")
        clientes = self.clienteCtrl.listarClientes(idVeiculo)
        if clientes:
            self.tabela.setRowCount(len(clientes))
            for cliente in clientes:
                item1 = QtWidgets.QTableWidgetItem(str(cliente['idCliente']))
                self.tabela.setItem(i, 0, item1)
                item2 = QtWidgets.QTableWidgetItem(cliente['nome'])
                self.tabela.setItem(i, 1, item2)
                item3 = QtWidgets.QTableWidgetItem(cliente['documento'])
                self.tabela.setItem(i, 2, item3)
                queryFones = self.clienteCtrl.listarFones(cliente['idCliente'])
                if queryFones:
                    fones = []
                    for fone in queryFones:
                        fones.append(fone['fone'])
                fones = ', '.join(fones)
                item4 = QtWidgets.QTableWidgetItem(fones)
                self.tabela.setItem(i, 3, item4)
                botao = QtWidgets.QPushButton(self.framedados, text='Desvincular')
                botao.setFixedWidth(150)
                botao.clicked.connect(self.desvincularCliente)
                self.tabela.setCellWidget(i, 4, botao)
                i+=1
            self.tabela.hideColumn(0)
            self.resize(self.tabela.sizeHintForColumn(0) + 
                self.tabela.sizeHintForColumn(1) +
                self.tabela.sizeHintForColumn(2) +
                self.tabela.sizeHintForColumn(3) +
                self.tabela.sizeHintForColumn(4) + 30,
                400)
        else:
            self.tabela.setRowCount(0)

    def desvincularCliente(self):
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
                cliente = self.clienteCtrl.getCliente(id)
                r = self.clienteCtrl.excluirVeiculoCliente(self.veiculoID, cliente['idCliente'])
                if isinstance(r, Exception):
                    raise Exception(r)
            self.renderClientes(self.veiculoID)

    def closeEvent(self, event):
        self.janelaFechada.emit(1)
        event.accept()
