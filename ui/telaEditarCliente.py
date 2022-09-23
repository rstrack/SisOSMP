from PyQt6 import QtCore, QtWidgets
from routes import handleRoutes

SIGLAESTADOS = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS',
                'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']


class TelaEditarCliente(QtWidgets.QMainWindow):

    def __init__(self):
        super(TelaEditarCliente, self).__init__()
        self.clienteCtrl = handleRoutes.getRoute('CLIENTE')
        self.marcaCtrl = handleRoutes.getRoute('MARCA')
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
        self.gridLayout.addWidget(self.lineEditNomeCliente, 1, 1, 1, 1)
        self.lineEditDocumento = QtWidgets.QLineEdit(self.groupBoxCliente)
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
        self.gridLayout2.addWidget(self.lineEditCEP, 1, 0, 1, 1)
        self.lineEditEnder = QtWidgets.QLineEdit(self.groupBoxEnder)
        self.gridLayout2.addWidget(self.lineEditEnder, 1, 1, 1, 2)
        self.lineEditNumero = QtWidgets.QLineEdit(self.groupBoxEnder)
        self.gridLayout2.addWidget(self.lineEditNumero, 1, 3, 1, 1)
        self.labelBairro = QtWidgets.QLabel(self.groupBoxEnder)
        self.gridLayout2.addWidget(self.labelBairro, 2, 0, 1, 2)
        self.labelCidade = QtWidgets.QLabel(self.groupBoxEnder)
        self.gridLayout2.addWidget(self.labelCidade, 2, 2, 1, 1)
        self.labelUF = QtWidgets.QLabel(self.groupBoxEnder)
        self.gridLayout2.addWidget(self.labelUF, 2, 3, 1, 1)
        self.lineEditBairro = QtWidgets.QLineEdit(self.groupBoxEnder)
        self.gridLayout2.addWidget(self.lineEditBairro, 3, 0, 1, 2)
        self.lineEditCidade = QtWidgets.QLineEdit(self.groupBoxEnder)
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
        self.lineEditTel1 = QtWidgets.QLineEdit(self.groupBoxTel)
        self.vlayout7.addWidget(self.lineEditTel1)
        self.labelTel2 = QtWidgets.QLabel(self.groupBoxTel)
        self.vlayout7.addWidget(self.labelTel2)
        self.lineEditTel2 = QtWidgets.QLineEdit(self.groupBoxTel)
        self.vlayout7.addWidget(self.lineEditTel2)
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
        self.glayoutp.addWidget(self.groupBoxVeiculo, 2, 0, 1, -1)
        spacerItem4 = QtWidgets.QSpacerItem(
            20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        self.glayoutp.addItem(spacerItem4)
        self.vlayout6.addWidget(self.framedados)
        self.glayoutp.setColumnStretch(0, 3)
        self.glayoutp.setColumnStretch(1, 1)
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
        self.botaolimpar = QtWidgets.QPushButton(self.framebotoes)
        self.botaolimpar.setMinimumSize(QtCore.QSize(100, 30))
        self.hlayout4.addWidget(self.botaolimpar)
        self.vlayout6.addWidget(self.framebotoes)
        spacerItem6 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.glayoutp.addItem(spacerItem6)
        self.setCentralWidget(self.main_frame)

        self.retranslateUi()
        self.setMarcas()

        self.botaolimpar.clicked.connect(self.limparCampos)
        self.botaoEditar.clicked.connect(self.salvar)
        self.comboBoxPessoa.currentIndexChanged.connect(self.escolherTipoPessoa)

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
        self.labelTel1.setText(_translate("MainWindow", "Fone 1"))
        self.labelTel2.setText(_translate("MainWindow", "Fone 2"))
        self.labelAno.setText(_translate("MainWindow", "Ano"))
        self.labelPlaca.setText(_translate("MainWindow", "Placa"))
        self.labelModelo.setText(_translate("MainWindow", "Modelo"))
        self.labelMarca.setText(_translate("MainWindow", "Marca"))
        self.botaolimpar.setText(_translate("MainWindow", "Cancelar"))
        self.botaoEditar.setText(_translate("MainWindow", "Editar"))

    #################### REFORMULAR TODA A FUNÇÃO! ########################
    
    def editar(self):
        try:
            cliente = self.getDadosCliente()
            veiculo = self.getDadosVeiculo()
            
            #se tem valores escritos nos campos de cliente e veiculo, tenta editar os dois
            if cliente and veiculo:
                fones = self.getFones()
                r = self.clienteCtrl.salvarClienteVeiculo(cliente, fones, veiculo)
                string = 'Cliente e Veiculo inseridos com sucesso!'
            #se somente possuem dados sobre cliente:
            elif cliente:
                fones = self.getFones()
                r = self.clienteCtrl.salvarCliente(cliente, fones)
                string = 'Cliente inserido com sucesso!'
            #se somente possuem dados sobre veiculo:
            elif veiculo: 
                r = self.clienteCtrl.salvarVeiculo(veiculo)
                string = 'Veiculo inserido com sucesso!'
            else: raise Exception('Campos vazios!')

            if isinstance(r, Exception):
                raise Exception(r)

            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Aviso")
            msg.setText(string)
            msg.exec()
        except Exception as e:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Aviso")
            msg.setText(str(e))
            msg.exec()

    def limparCampos(self):
        for lineedit in self.framedados.findChildren(QtWidgets.QLineEdit):
            lineedit.clear()

    def getDadosCliente(self):
        lista = list()
        lista.extend(self.groupBoxCliente.findChildren(QtWidgets.QLineEdit))
        lista.extend(self.groupBoxEnder.findChildren(QtWidgets.QLineEdit))
        if len(list(filter(lambda dados: dados.text(), lista))) == 0:
            return None
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
        if (self.lineEditTel1.text()):
            if not self.lineEditTel1.text().isnumeric():
                raise Exception('Fone 1 inválido')
            fones.append(self.lineEditTel1.text())
            cont += 1
        else:
            fones.append(None)
        if (self.lineEditTel2.text()):
            if not self.lineEditTel2.text().isnumeric():
                raise Exception('Fone 2 inválido')
            fones.append(self.lineEditTel2.text())
            cont += 1
        else:
            fones.append(None)
        if cont == 0:
            raise Exception('Fone obrigatório')
        return fones

    def getDadosVeiculo(self):
        if len(list(filter(lambda dados: dados.text(), self.groupBoxVeiculo.findChildren(QtWidgets.QLineEdit)))) == 0:
            return None
        dict = {}
        dict['marca'] = self.comboBoxMarca.currentText().upper()
        if dict['marca'] == '':
            raise Exception('Marca obrigatória')
        if (self.lineEditModelo.text()):
            dict['modelo'] = self.lineEditModelo.text().title()
        else:
            raise Exception('Modelo obrigatório')
        if (self.lineEditPlaca.text()):
            if not self.lineEditPlaca.text().isalnum():
                raise Exception('Insira apenas letras e números na placa')
            dict['placa'] = self.lineEditPlaca.text().upper()
        else:
            raise Exception('Placa obrigatória')
        
        if (self.lineEditAno.text()):
            dict['ano'] = self.lineEditAno.text()
        else:
            dict['ano'] = None
        return dict

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

    def setMarcas(self):
        marcas = self.marcaCtrl.listarMarcas()
        for marca in marcas:
            self.comboBoxMarca.addItem(marca['nome'])
        self.comboBoxMarca.setCurrentIndex(-1)

    def renderEditar(self, id):
        self.labelTitulo.setText('Editar Cliente')
        cliente = self.clienteCtrl.getCliente(id)
        self.comboBoxPessoa.setCurrentIndex(int(cliente['tipo']))
        self.lineEditNomeCliente.setText(cliente['nome'])
        self.lineEditDocumento.setText(cliente['documento'])
        #...continuar

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = TelaEditarCliente()

    ui.show()

    style = open('./ui/styles.qss').read()
    app.setStyleSheet(style)

    sys.exit(app.exec())
