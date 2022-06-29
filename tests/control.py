from PyQt6 import QtWidgets

from modelo import *

#função pra uma só linha, implementar para varias linhas
def salvarPecas(descricao, valor):
    Peca.create(descricao=descricao,valor=valor)
    msg =  QtWidgets.QMessageBox()
    msg.setWindowTitle("Aviso")
    msg.setText("Dados inseridos com sucesso!")
    msg.exec()
