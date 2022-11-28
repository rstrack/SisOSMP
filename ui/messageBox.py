from PyQt6 import QtWidgets

class MessageBox():
    def __init__(self) -> None:
        pass

    def question(self, string):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Aviso")
        msgBox.setText(string)
        y = msgBox.addButton("Sim", QtWidgets.QMessageBox.ButtonRole.YesRole)
        n = msgBox.addButton("Não", QtWidgets.QMessageBox.ButtonRole.NoRole)
        c = msgBox.addButton(
            "Cancelar", QtWidgets.QMessageBox.ButtonRole.RejectRole)
        y.setFixedWidth(60)
        n.setFixedWidth(60)
        c.setFixedWidth(100)
        msgBox.exec()
        if msgBox.clickedButton() == y:
            return 'sim'
        if msgBox.clickedButton() == n:
            return 'nao'
        if msgBox.clickedButton() == c:
            return 'cancelar'