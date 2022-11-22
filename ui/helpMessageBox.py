from PyQt6 import QtWidgets, QtGui, QtCore
import sys

class HelpMessageBox(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setObjectName('helpMessageBox')
        self.setWindowTitle("Ajuda")
        self.setWindowIcon(QtGui.QIcon('./resources/logo-icon.png'))
        QBtn = QtWidgets.QDialogButtonBox.StandardButton.Ok
        self.buttonBox = QtWidgets.QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)

        self.layout = QtWidgets.QVBoxLayout()
        self.message =  "<p style= ' line-height:150% ' >\n"
        self.label = QtWidgets.QLabel()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
        # self.setFixedSize(400,400)

    def setMessage(self, str: str):
        self.message += f"{str} </p>"
        self.label.setText(str)
        print(self.message)

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    msg = HelpMessageBox()
    msg.setMessage('Teste\nTeste2')
    msg.exec()
    app.exec(sys.exit())
