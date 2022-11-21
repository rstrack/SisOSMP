import os
from PyQt6 import QtCore, QtGui, QtWidgets

class TelaInicial(QtWidgets.QMainWindow):

    def __init__(self):
        super(TelaInicial, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(1280, 900)
        self.mainwidget = QtWidgets.QWidget(self)
        self.hlayout1 = QtWidgets.QHBoxLayout(self.mainwidget)
        self.hlayout1.setContentsMargins(0, 0, 0, 0)
        self.hlayout1.setSpacing(0)
        # frame lateral
        self.framelateral = QtWidgets.QFrame(self.mainwidget)
        self.framelateral.setMaximumWidth(250)
        self.framelateral.setObjectName("framelateral")
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setXOffset(1)
        shadow.setYOffset(0)
        self.framelateral.setGraphicsEffect(shadow)
        self.vlayout1 = QtWidgets.QVBoxLayout(self.framelateral)
        self.vlayout1.setContentsMargins(0, 0, 0, 0)
        self.vlayout1.setSpacing(0)
        # frame da logo(dentro do frame lateral)
        self.logo_frame = QtWidgets.QFrame(self.framelateral)
        self.logo_frame.setObjectName('framelogo')
        self.vlayout2 = QtWidgets.QVBoxLayout(self.logo_frame)
        self.vlayout2.setContentsMargins(9, 0, 9, 0)
        self.vlayout2.setSpacing(0)
        # logo
        self.logo_label = QtWidgets.QLabel(self.logo_frame)
        self.logo_label.setMaximumHeight(180)
        self.logo_label.setPixmap(QtGui.QPixmap("resources/logo-icon.png"))
        self.logo_label.setScaledContents(True)
        self.vlayout2.addWidget(self.logo_label)
        self.vlayout1.addWidget(self.logo_frame)
        # frame do menu(dentro do frame lateral)
        self.framemenu = QtWidgets.QFrame(self.framelateral)
        self.framemenu.setObjectName('framemenu')
        self.vlayout3 = QtWidgets.QVBoxLayout(self.framemenu)
        self.vlayout3.setContentsMargins(0, 0, 0, 0)
        # frames do menu
        self.framemenu1 = QtWidgets.QFrame(self.framemenu)
        self.vlayout3.addWidget(self.framemenu1)
        self.framemenu2 = QtWidgets.QFrame(self.framemenu)
        self.vlayout3.addWidget(self.framemenu2)
        self.framemenu3 = QtWidgets.QFrame(self.framemenu)
        self.vlayout3.addWidget(self.framemenu3)
        self.framemenu4 = QtWidgets.QFrame(self.framemenu)
        self.vlayout3.addWidget(self.framemenu4)
        # aba "cadastro"
        self.labelcadastro = QtWidgets.QLabel(self.framemenu1)
        self.labelcadastro.setObjectName('labelmenu')
        self.labelcadastro.setText("CADASTRO")
        self.labelcadastro.setFixedHeight(40)
        self.hline1 = QtWidgets.QFrame(self.framemenu3)
        self.hline1.setObjectName("hline")
        self.hline1.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.hline1.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        '''self.vlayoutlabel1 = QtWidgets.QVBoxLayout(self.framemenu1)
        self.vlayoutlabel1.setSizeConstraint(
            QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.vlayoutlabel1.setSpacing(0)
        self.vlayoutlabel1.setContentsMargins(0,0,0,0)
        self.vlayoutlabel1.addWidget(self.labelcadastro)'''
        self.vlayout4 = QtWidgets.QVBoxLayout(self.framemenu2)
        self.vlayout4.setContentsMargins(0,0,0,0)
        self.vlayout4.setSpacing(0)
        self.vlayout4.setSizeConstraint(
            QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.vlayout4.addWidget(self.labelcadastro)
        #self.vlayout4.addWidget(self.hline1)
        # opçoes da aba
        self.botao_pecas = QtWidgets.QPushButton(self.framemenu2)
        self.vlayout4.addWidget(self.botao_pecas)
        self.botao_servicos = QtWidgets.QPushButton(self.framemenu2)
        self.vlayout4.addWidget(self.botao_servicos)
        self.botao_clientes = QtWidgets.QPushButton(self.framemenu2)
        self.vlayout4.addWidget(self.botao_clientes)
        self.botao_orcamentos = QtWidgets.QPushButton(self.framemenu2)
        self.vlayout4.addWidget(self.botao_orcamentos)
        # aba "consulta"
        self.labelconsulta = QtWidgets.QLabel(self.framemenu3)
        self.labelconsulta.setObjectName('labelmenu')
        self.labelconsulta.setText("CONSULTA")
        self.labelconsulta.setFixedHeight(40)
        self.hline2 = QtWidgets.QFrame(self.framemenu3)
        self.hline2.setObjectName("hline")
        self.hline2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.hline2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        '''self.vlayoutlabel2 = QtWidgets.QVBoxLayout(self.framemenu3)
        self.vlayoutlabel2.setSizeConstraint(
            QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.vlayoutlabel2.setSpacing(0)
        self.vlayoutlabel2.setContentsMargins(0,0,0,0)
        self.vlayoutlabel2.addWidget(self.labelconsulta)'''
        self.vlayout5 = QtWidgets.QVBoxLayout(self.framemenu4)
        self.vlayout5.setContentsMargins(0,0,0,0)
        self.vlayout5.setSpacing(0)
        self.vlayout5.addWidget(self.labelconsulta)
        #self.vlayout5.addWidget(self.hline2)
        # opçoes da aba
        self.botao_pecas_2 = QtWidgets.QPushButton(self.framemenu4)
        self.vlayout5.addWidget(self.botao_pecas_2)
        self.botao_servicos_2 = QtWidgets.QPushButton(self.framemenu4)
        self.vlayout5.addWidget(self.botao_servicos_2)
        self.botao_clientes_2 = QtWidgets.QPushButton(self.framemenu4)
        self.vlayout5.addWidget(self.botao_clientes_2)
        self.botao_veiculos = QtWidgets.QPushButton(self.framemenu4)
        self.vlayout5.addWidget(self.botao_veiculos)
        self.botao_orcamentos_2 = QtWidgets.QPushButton(self.framemenu4)
        self.vlayout5.addWidget(self.botao_orcamentos_2)
        self.botao_os = QtWidgets.QPushButton(self.framemenu4)
        self.vlayout5.addWidget(self.botao_os)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.vlayout3.addItem(spacerItem1)
        self.vlayout1.addWidget(self.framemenu)
        self.hlayout1.addWidget(self.framelateral)
        self.main_frame = QtWidgets.QFrame(self.mainwidget)
        self.main_frame.setObjectName("main_frame")
        self.hlayout1.addWidget(self.main_frame)
        self.vlayout6 = QtWidgets.QVBoxLayout(self.main_frame)
        self.vlayout6.setContentsMargins(0, 0, 0, 0)
        self.vlayout6.setSpacing(0)
        self.stackedWidget = QtWidgets.QStackedWidget(self.main_frame)
        self.vlayout6.addWidget(self.stackedWidget)
        # página inicial
        self.label_inicio = QtWidgets.QLabel(self.stackedWidget)
        self.label_inicio.setObjectName("bemvindo")
        self.label_inicio.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.stackedWidget.addWidget(self.label_inicio)
        self.setCentralWidget(self.mainwidget)
        # barra de menu
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 948, 21))
        self.menubar.setDefaultUp(False)
        self.menuFerramentas = QtWidgets.QMenu(self.menubar)
        self.setMenuBar(self.menubar)
        self.actionImportar_dados = QtGui.QAction(self)
        self.actionExportar_dados = QtGui.QAction(self)
        self.menuFerramentas.addAction(self.actionImportar_dados)
        self.menuFerramentas.addAction(self.actionExportar_dados)
        self.menubar.addAction(self.menuFerramentas.menuAction())
        self.actionImportar_dados.triggered.connect(self.importar)
        self.actionExportar_dados.triggered.connect(self.exportar)
        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Mecânica Pasetto"))
        self.botao_pecas.setText(_translate("MainWindow", "PEÇAS"))
        self.botao_servicos.setText(_translate("MainWindow", "SERVIÇOS"))
        self.botao_clientes.setText(_translate("MainWindow", "CLIENTES / VEÍCULOS"))
        self.botao_orcamentos.setText(_translate("MainWindow", "ORÇAMENTOS"))
        self.botao_pecas_2.setText(_translate("MainWindow", "PEÇAS"))
        self.botao_servicos_2.setText(_translate("MainWindow", "SERVIÇOS"))
        self.botao_clientes_2.setText(_translate("MainWindow", "CLIENTES"))
        self.botao_veiculos.setText(_translate("MainWindow", "VEICULOS"))
        self.botao_orcamentos_2.setText(_translate("MainWindow", "ORÇAMENTOS"))
        self.botao_os.setText(_translate("MainWindow", "ORDENS DE SERVIÇO"))
        self.label_inicio.setText(_translate("MainWindow", "Bem Vindo!"))
        self.menuFerramentas.setTitle(_translate("MainWindow", "Ferramentas"))
        self.actionImportar_dados.setText(
            _translate("MainWindow", "Importar dados"))
        self.actionExportar_dados.setText(
            _translate("MainWindow", "Exportar dados"))

    def importar(self):
        try:
            window = QtWidgets.QMainWindow()
            fd = QtWidgets.QFileDialog()
            path = fd.getOpenFileName(window, 'Importar', './')
            if path[0] == '':
                return
            if os.path.exists("C:/Program Files/MySQL/MySQL Server 8.0/bin"):
                mysqldump_path = "C:/Program Files/MySQL/MySQL Server 8.0/bin"
            else: mysqldump_path = "bin/"
            os.popen('"%s/mysql" -u %s -p%s %s < "%s"' % (mysqldump_path, "root", "admin", "dbpasetto", path[0]))
        except Exception as e:
            msg = QtWidgets.QMessageBox()
            msg.setWindowIcon(QtGui.QIcon('resources/logo-icon.png'))
            msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg.setWindowTitle("Erro")
            msg.setText(str(e))
            msg.exec()

    def exportar(self):
        try:
            window = QtWidgets.QMainWindow()
            fd = QtWidgets.QFileDialog()
            path = fd.getSaveFileName(window, 'Exportar como', './', "Arquivos SQL (*.sql)")
            if path[0] == '':
                return
            if os.path.exists("C:/Program Files/MySQL/MySQL Server 8.0/bin"):
                mysqldump_path = "C:/Program Files/MySQL/MySQL Server 8.0/bin"
            else: mysqldump_path = "bin/"
            os.popen('"%s/mysqldump" -u %s -p%s %s > "%s"' % (mysqldump_path, "root", "admin", "dbpasetto", path[0]))
        except Exception as e:
            msg = QtWidgets.QMessageBox()
            msg.setWindowIcon(QtGui.QIcon('resources/logo-icon.png'))
            msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg.setWindowTitle("Erro")
            msg.setText(str(e))
            msg.exec()
