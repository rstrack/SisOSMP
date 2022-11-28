from PyQt6 import QtWidgets, QtGui, QtCore
import sys

class HelpMessageBox(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setObjectName('helpMessageBox')
        self.setWindowTitle("Ajuda")
        self.setWindowIcon(QtGui.QIcon('./resources/help-icon1.png'))
        self.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        QBtn = QtWidgets.QDialogButtonBox.StandardButton.Ok
        self.buttonBox = QtWidgets.QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.layout1 = QtWidgets.QVBoxLayout()
        self.layout1.setSpacing(9)
        self.layout1.setContentsMargins(16,16,16,0)
        self.setLayout(self.layout1)
        self.setFixedWidth(350)

    def setMessage(self, str: str):
        labels = str.split('\n')
        for label in labels:
            l = QtWidgets.QLabel()
            l.setWordWrap(True)
            l.setAlignment(QtCore.Qt.AlignmentFlag.AlignJustify | QtCore.Qt.AlignmentFlag.AlignVCenter)
            l.setSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
            l.setText('<p style="text-indent:30px;line-height:20px;">'+label+'</p>')
            self.layout1.addWidget(l)
        self.layout1.addWidget(self.buttonBox)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.layout1.addItem(spacerItem)
        self.setFixedHeight(self.sizeHint().height()-150)

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    style = open('resources/styles.qss').read()
    app.setStyleSheet(style)
    msg = HelpMessageBox()
    msg.setMessage('''Cadastro de orçamento de manutenção de veículos. Cadastre um novo cliente e/ou veículo ou selecione um já existente. Ao selecionar, é possível editar seus dados.
Se estiver com acesso à internet, campos de endereço são completados automaticamente ao inserir o CEP.
Adicione peças e serviços ao orçamento. Necessário pelo menos um serviço. Para adicionar mais peças ou serviços, clique no botão "+" disponível em suas respectivas seções.
Após concluir, selecione a opção de salvar somente ou salvar e gerar o arquivo PDF para visualização do orçamento.''')
    msg.exec()
    app.exec(sys.exit())
