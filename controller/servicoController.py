from ast import Not
from operator import xor
from PyQt6 import QtWidgets

from model.modelo import *

from ui.telaCadastroServico import TelaCadastroServico

class ServicoController():
    def __init__(self):
        self.viewCadastro = TelaCadastroServico()
        self.linhasservico = [[self.viewCadastro.lineEditnome, self.viewCadastro.lineEditvalor]]

    def salvarServicos(self):
        with db.atomic() as transaction:
            try:
                if len(self.viewCadastro.linhasservico) == 1 and not (self.viewCadastro.lineEditnome.text() and self.viewCadastro.lineEditvalor.text()):
                    raise Exception("Erro: campos vazios!")
                for desc, valor in self.viewCadastro.linhasservico:
                    if desc.text() and valor.text():
                        aux = valor.text().replace(',','',1)
                        if aux.isdigit():
                            Servico.create(descricao=desc.text(), valor=valor.text().replace(',','.',1))
                        else: raise Exception("Erro: digite apenas números no valor!")
                    elif desc.text() or valor.text():
                        raise Exception("Preencha todos os campos!")
                msg =  QtWidgets.QMessageBox()
                msg.setWindowTitle("Aviso")
                msg.setText("Dados inseridos!")
                msg.exec()

            except Exception as e:
                transaction.rollback()
                msg =  QtWidgets.QMessageBox()
                msg.setWindowTitle("Erro")
                msg.setText(str(e))
                msg.exec()