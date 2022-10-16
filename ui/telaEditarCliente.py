from PyQt6 import QtCore, QtWidgets, QtGui
from container import handleDeps

SIGLAESTADOS = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS',
                'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']


class TelaEditarCliente(QtWidgets.QMainWindow):
    paraTelaConsulta = QtCore.pyqtSignal(int)
    def __init__(self):
        super(TelaEditarCliente, self).__init__()
        self.clienteCtrl = handleDeps.getDep('CLIENTECTRL')
        self.cidadeCtrl = handleDeps.getDep('CIDADECTRL')
        self.marcaCtrl = handleDeps.getDep('MARCACTRL')
        self.buscaCEP = handleDeps.getDep('CEP')
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
        self.framegeral.setMaximumWidth(int(QtGui.QGuiApplication.primaryScreen().size().width()*0.6) 
            if QtGui.QGuiApplication.primaryScreen().size().width()> 1280 else QtGui.QGuiApplication.primaryScreen().size().width())
        self.hlayout.addWidget(self.framegeral)
        spacer = QtWidgets.QSpacerItem(
            20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.hlayout.addItem(spacer)
        self.vlayout = QtWidgets.QVBoxLayout(self.framegeral)
        self.vlayout.setContentsMargins(0,0,0,0)
        self.vlayout.setSpacing(0)
        # titulo
        self.labelTitulo = QtWidgets.QLabel(self.framegeral)
        self.labelTitulo.setFixedHeight(100)
        self.labelTitulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelTitulo.setObjectName("titulo")
        self.vlayout.addWidget(self.labelTitulo)
        self.framedados = QtWidgets.QFrame(self.main_frame)
        self.glayoutp = QtWidgets.QGridLayout(self.framedados)
        # dados do cliente
        self.groupBoxCliente = QtWidgets.QGroupBox(self.framedados)
        self.groupBoxCliente.setTitle("Dados de Identificação")
        self.glayoutp.addWidget(self.groupBoxCliente, 0, 0, 1, -1)
        self.gridLayout = QtWidgets.QGridLayout(self.groupBoxCliente)
        self.labelTipo = QtWidgets.QLabel(self.groupBoxCliente)
        self.gridLayout.addWidget(self.labelTipo, 0, 0, 1, 1)
        self.labelNomeCliente = QtWidgets.QLabel(self.groupBoxCliente)
        self.gridLayout.addWidget(self.labelNomeCliente, 0, 1, 1, 1)
        self.labelDocumento = QtWidgets.QLabel(self.groupBoxCliente)
        self.gridLayout.addWidget(self.labelDocumento, 0, 2, 1, 1)
        self.comboBoxPessoa = QtWidgets.QComboBox(self.groupBoxCliente)
        self.comboBoxPessoa.addItems(["PESSOA FÍSICA", "PESSOA JURÍDICA", "ESTRANGEIRO"])
        self.gridLayout.addWidget(self.comboBoxPessoa, 1, 0, 1, 1)
        self.lineEditNomeCliente = QtWidgets.QLineEdit(self.groupBoxCliente)
        self.lineEditNomeCliente.setMaxLength(80)
        self.gridLayout.addWidget(self.lineEditNomeCliente, 1, 1, 1, 1)
        self.lineEditDocumento = QtWidgets.QLineEdit(self.groupBoxCliente)
        self.lineEditDocumento.setMaxLength(14)
        self.gridLayout.addWidget(self.lineEditDocumento, 1, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 5)
        self.gridLayout.setColumnStretch(2, 1)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        self.glayoutp.addItem(spacerItem2)
        # dados de endereço
        self.groupBoxEnder = QtWidgets.QGroupBox(self.framedados)
        self.groupBoxEnder.setTitle("Endereço")
        self.glayoutp.addWidget(self.groupBoxEnder, 1, 0)
        self.gridLayout2 = QtWidgets.QGridLayout(self.groupBoxEnder)
        self.groupBoxEnder.setLayout(self.gridLayout2)
        self.labelcep = QtWidgets.QLabel(self.groupBoxEnder)
        self.gridLayout2.addWidget(self.labelcep, 0, 0, 1, 1)
        self.labelender = QtWidgets.QLabel(self.groupBoxEnder)
        self.gridLayout2.addWidget(self.labelender, 0, 1, 1, 2)
        self.labelnumero = QtWidgets.QLabel(self.groupBoxEnder)
        self.gridLayout2.addWidget(self.labelnumero, 0, 3, 1, 1)
        self.lineEditCEP = QtWidgets.QLineEdit(self.groupBoxEnder)
        self.lineEditCEP.setMaxLength(8)
        self.gridLayout2.addWidget(self.lineEditCEP, 1, 0, 1, 1)
        self.lineEditEnder = QtWidgets.QLineEdit(self.groupBoxEnder)
        self.lineEditEnder.setMaxLength(80)
        self.gridLayout2.addWidget(self.lineEditEnder, 1, 1, 1, 2)
        self.lineEditNumero = QtWidgets.QLineEdit(self.groupBoxEnder)
        self.lineEditNumero.setMaxLength(6)
        self.gridLayout2.addWidget(self.lineEditNumero, 1, 3, 1, 1)
        self.labelBairro = QtWidgets.QLabel(self.groupBoxEnder)
        self.gridLayout2.addWidget(self.labelBairro, 2, 0, 1, 2)
        self.labelCidade = QtWidgets.QLabel(self.groupBoxEnder)
        self.gridLayout2.addWidget(self.labelCidade, 2, 2, 1, 1)
        self.labelUF = QtWidgets.QLabel(self.groupBoxEnder)
        self.gridLayout2.addWidget(self.labelUF, 2, 3, 1, 1)
        self.lineEditBairro = QtWidgets.QLineEdit(self.groupBoxEnder)
        self.lineEditBairro.setMaxLength(50)
        self.gridLayout2.addWidget(self.lineEditBairro, 3, 0, 1, 2)
        self.lineEditCidade = QtWidgets.QLineEdit(self.groupBoxEnder)
        self.lineEditCidade.setMaxLength(50)
        self.gridLayout2.addWidget(self.lineEditCidade, 3, 2, 1, 1)
        self.comboBoxuf = QtWidgets.QComboBox(self.groupBoxEnder)
        self.comboBoxuf.addItems(SIGLAESTADOS)
        self.comboBoxuf.setCurrentText('PR')
        self.gridLayout2.addWidget(self.comboBoxuf, 3, 3, 1, 1)
        self.gridLayout2.setColumnStretch(1, 2)
        self.gridLayout2.setColumnStretch(2, 5)
        self.gridLayout2.setColumnStretch(3, 1)
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        self.glayoutp.addItem(spacerItem3)
        # telefone
        self.groupBoxTel = QtWidgets.QGroupBox(self.framedados)
        self.groupBoxTel.setTitle("Contato")
        self.glayoutp.addWidget(self.groupBoxTel, 1, 1)
        self.vlayout7 = QtWidgets.QVBoxLayout(self.groupBoxTel)
        self.labelTel1 = QtWidgets.QLabel(self.groupBoxTel)
        self.vlayout7.addWidget(self.labelTel1)
        self.lineEditFone1 = QtWidgets.QLineEdit(self.groupBoxTel)
        self.lineEditFone1.setMaxLength(14)
        self.vlayout7.addWidget(self.lineEditFone1)
        self.labelTel2 = QtWidgets.QLabel(self.groupBoxTel)
        self.vlayout7.addWidget(self.labelTel2)
        self.lineEditFone2 = QtWidgets.QLineEdit(self.groupBoxTel)
        self.lineEditFone2.setMaxLength(14)
        self.vlayout7.addWidget(self.lineEditFone2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        self.glayoutp.addItem(spacerItem4)
        self.vlayout.addWidget(self.framedados)
        self.glayoutp.setColumnStretch(0, 3)
        self.glayoutp.setColumnStretch(1, 1)
        # botoes
        self.framebotoes = QtWidgets.QFrame(self.main_frame)
        self.hlayout4 = QtWidgets.QHBoxLayout(self.framebotoes)
        self.labelLegenda = QtWidgets.QLabel(self.framebotoes)
        self.hlayout4.addWidget(self.labelLegenda)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.hlayout4.addItem(spacerItem5)
        self.botaoSalvar = QtWidgets.QPushButton(self.framebotoes)
        self.botaoSalvar.setMinimumSize(QtCore.QSize(100, 35))
        self.botaoSalvar.setObjectName('botaoprincipal')
        self.hlayout4.addWidget(self.botaoSalvar)
        self.botaoCancelar = QtWidgets.QPushButton(self.framebotoes)
        self.botaoCancelar.setMinimumSize(QtCore.QSize(100, 35))
        self.hlayout4.addWidget(self.botaoCancelar)
        self.vlayout.addWidget(self.framebotoes)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.glayoutp.addItem(spacerItem6)
        self.setCentralWidget(self.main_frame)
        self.completerCidade = QtWidgets.QCompleter([])
        self.completerCidade.setMaxVisibleItems(5)
        self.completerCidade.setCaseSensitivity(
            QtCore.Qt.CaseSensitivity.CaseInsensitive)
        self.completerCidade.setCompletionMode(
            QtWidgets.QCompleter.CompletionMode.PopupCompletion)
        self.lineEditCidade.setCompleter(self.completerCidade)
        self.retranslateUi()
        self.botaoCancelar.clicked.connect(self.cancelarEdicao)
        self.botaoSalvar.clicked.connect(self.editar)
        self.comboBoxPessoa.currentIndexChanged.connect(self.escolherTipoPessoa)
        self.lineEditCEP.textChanged.connect(self.buscarDadosCEP)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Mecânica Pasetto"))
        self.labelTitulo.setText(_translate("MainWindow", "Editar Cliente"))
        self.labelTipo.setText(_translate("MainWindow", "Tipo"))
        self.labelNomeCliente.setText(_translate("MainWindow", "Nome*"))
        self.labelDocumento.setText(_translate("MainWindow", "CPF"))
        self.labelCidade.setText(_translate("MainWindow", "Cidade"))
        self.labelcep.setText(_translate("MainWindow", "CEP"))
        self.labelBairro.setText(_translate("MainWindow", "Bairro"))
        self.labelender.setText(_translate("MainWindow", "Endereço"))
        self.labelnumero.setText(_translate("MainWindow", "Nº"))
        self.labelUF.setText(_translate("MainWindow", "UF"))
        self.labelTel1.setText(_translate("MainWindow", "Fone 1*"))
        self.labelTel2.setText(_translate("MainWindow", "Fone 2"))
        self.labelLegenda.setText(_translate("MainWindow", "* Campos Obrigatórios"))
        self.botaoCancelar.setText(_translate("MainWindow", "Cancelar"))
        self.botaoSalvar.setText(_translate("MainWindow", "Salvar"))
    
    def editar(self):
        try:
            cliente = self.getDadosCliente()
            fones = self.getFones()
            r = self.clienteCtrl.editarCliente(self.clienteID, cliente, fones)
            if isinstance(r, Exception):
                raise Exception(r)
            msg = QtWidgets.QMessageBox()
            msg.setWindowIcon(QtGui.QIcon('./resources/logo-icon.png'))
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setWindowTitle("Aviso")
            msg.setText('Cliente editado com sucesso!')
            msg.exec()
            self.paraTelaConsulta.emit(1)
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
            self.paraTelaConsulta.emit(1)

    def limparCampos(self):
        for lineedit in self.framedados.findChildren(QtWidgets.QLineEdit):
            lineedit.clear()

    def getDadosCliente(self):
        lista = list()
        lista.extend(self.groupBoxCliente.findChildren(QtWidgets.QLineEdit))
        lista.extend(self.groupBoxEnder.findChildren(QtWidgets.QLineEdit))
        lista.extend(self.groupBoxTel.findChildren(QtWidgets.QLineEdit))
        if len(list(filter(lambda dados: dados.text(), lista))) == 0:
            raise Exception('Campos vazios!')
        dict = {}
        dict['tipo'] = self.comboBoxPessoa.currentIndex()
        if (self.lineEditDocumento.text()):
            if dict['tipo'] == 0:
                documento = 'CPF'
                if len(self.lineEditDocumento.text()) != 11:
                    raise Exception('CPF inválido')
            elif dict['tipo'] == 1:
                documento = 'CNPJ'
                if len(self.lineEditDocumento.text()) != 14:
                    raise Exception('CNPJ inválido')
            else: documento = 'Documento'
            if not self.lineEditDocumento.text().isnumeric():
                raise Exception(f'Digite apenas números no campo {documento}')
            dict['documento'] = self.lineEditDocumento.text()
        else:
            dict['documento'] = None
        if (self.lineEditNomeCliente.text()):
            dict['nome'] = self.lineEditNomeCliente.text().title()
        else:
            raise Exception("Nome do cliente obrigatório")
        if (self.lineEditCEP.text()):
            if len(self.lineEditCEP.text()) != 8:
                raise Exception("CEP inválido")
            dict['cep'] = self.lineEditCEP.text()
        else:
            dict['cep'] = None
        if (self.lineEditEnder.text()):
            dict['endereco'] = self.lineEditEnder.text()
        else:
            dict['endereco'] = None
        if (self.lineEditNumero.text()):
            dict['numero'] = self.lineEditNumero.text()
        else:
            dict['numero'] = None
        if (self.lineEditBairro.text()):
            dict['bairro'] = self.lineEditBairro.text()
        else:
            dict['bairro'] = None
        if (self.lineEditCidade.text()):
            dict['cidade'] = self.lineEditCidade.text().title()
        else:
            dict['cidade'] = None
        dict['uf'] = self.comboBoxuf.currentText()
        return dict

    def getFones(self):
        fones = []
        cont = 0
        if (self.lineEditFone1.text()):
            if not self.lineEditFone1.text().isnumeric() or len(self.lineEditFone1.text())<8:
                raise Exception('Fone 1 inválido')
            fones.append(self.lineEditFone1.text())
            cont += 1
        else:
            fones.append(None)
        if (self.lineEditFone2.text()):
            if not self.lineEditFone2.text().isnumeric() or len(self.lineEditFone2.text())<8:
                raise Exception('Fone 2 inválido')
            fones.append(self.lineEditFone2.text())
            cont += 1
        else:
            fones.append(None)
        if cont == 0:
            raise Exception('Fone obrigatório')
        return fones

    def setCliente(self, tipo, nome, documento=None, tel1=None, tel2=None):
        self.lineEditNomeCliente.setText(nome)
        if documento:
            self.lineEditDocumento.setText(documento)
            if tipo == '0':
                self.labelDocumento.setText("CPF")
            elif tipo == '1':
                self.labelDocumento.setText("CNPJ")
            elif tipo == '2':
                self.labelDocumento.setText("Documento")
        self.comboBoxPessoa.setCurrentIndex(int(tipo))
        self.lineEditFone1.setText(tel1)
        self.lineEditFone2.setText(tel2)

    def setEndereco(self, cep=None, ender=None, numero=None, bairro=None, cidade=None, uf=None):
        if cep:
            self.lineEditCEP.setText(cep)
        if ender:
            self.lineEditEnder.setText(ender)
        if numero:
            self.lineEditNumero.setText(numero)
        if bairro:
            self.lineEditBairro.setText(bairro)
        if cidade:
            self.lineEditCidade.setText(cidade)
        if uf:
            self.comboBoxuf.setCurrentIndex(
                self.comboBoxuf.findText(uf, QtCore.Qt.MatchFlag.MatchExactly))

    def escolherTipoPessoa(self):
        if (self.comboBoxPessoa.currentIndex() == 0):
            self.labelDocumento.setText('CPF')
        elif (self.comboBoxPessoa.currentIndex() == 1):
            self.labelDocumento.setText('CNPJ')
        else: self.labelDocumento.setText('Documento')

    def setCompleters(self):
        cidades = self.cidadeCtrl.listarCidades()
        listaCidades = []
        if cidades:
            for cidade in cidades:
                listaCidades.append(cidade['nome'])
        modelCidades = QtCore.QStringListModel()
        modelCidades.setStringList(listaCidades)
        self.completerCidade.setModel(modelCidades)

    def renderEditar(self, id):
        self.limparCampos()
        self.setCompleters()
        self.clienteID = id
        cliente = self.clienteCtrl.getCliente(id)
        fones = self.clienteCtrl.listarFones(cliente['idCliente'])
        listaFones = [None, None]
        if fones:
            for x in range(len(fones)):
                listaFones[x] = fones[x]['fone']
        self.setCliente(cliente['tipo'], cliente['nome'], cliente['documento'], listaFones[0], listaFones[1])
        if cliente['cidade'] != None:
            cidade = cliente['cidade']['nome']
            uf = cliente['cidade']['uf']
        else: 
            cidade = None
            uf = None
        self.setEndereco(cliente['cep'], cliente['endereco'], cliente['numero'], cliente['bairro'], cidade, uf)

    def buscarDadosCEP(self):
        cep = self.lineEditCEP.text()
        if len(cep) !=8:
            return
        dados = self.buscaCEP.buscarCEP(cep)
        if dados == None:
            return
        if 'erro' in dados:
            return
        self.lineEditEnder.setText(dados['logradouro'])
        self.lineEditBairro.setText(dados['bairro'])
        self.lineEditCidade.setText(dados['localidade'])
        self.comboBoxuf.setCurrentIndex(self.comboBoxuf.findText(dados['uf'], QtCore.Qt.MatchFlag.MatchExactly))
        return
