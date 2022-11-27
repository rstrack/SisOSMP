from PyQt6 import QtWidgets, QtGui, QtCore
import sys

class HelpMessageBox(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setObjectName('helpMessageBox')
        self.setWindowTitle("Ajuda")
        self.setWindowIcon(QtGui.QIcon('./resources/logo-icon.png'))
        # self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        QBtn = QtWidgets.QDialogButtonBox.StandardButton.Ok
        self.buttonBox = QtWidgets.QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.layout = QtWidgets.QVBoxLayout()
        self.label = QtWidgets.QLabel()
        self.label.setWordWrap(True)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignJustify | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.setModal(True)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
        self.setFixedWidth(350)

    def setMessage(self, str: str):
        self.label.setText(str)


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    msg = HelpMessageBox()
    msg.setMessage('''Neque porro quisquam est qui dolorem ipsum
quia dolor sit amet, consectetur, adipisci velit''')
    msg.exec()
    app.exec(sys.exit())
