from PyQt6 import QtWidgets

from model.modelo import *

class PecaController():
    def __init__(self, view=None):
        self.view = view

    def salvarPeca(self, desc, un, valor):
        if valor.replace(',','',1).isdigit():
            peca = Peca.create(descricao=desc, un=un, valor=valor.replace(',','.',1))
        else: raise Exception("Erro: digite apenas números no valor!")
        return peca

    def salvarPecas(self):
        with db.atomic() as transaction:
            try:
                qtde = 0
                for desc, un, valor in self.view.linhasPeca:
                    if desc.text() and valor.text():
                        qPeca = Peca.select().where(Peca.descricao==desc.text())
                        if not qPeca:
                            if valor.text().replace(',','',1).replace('.','',1).isdigit():
                                Peca.create(descricao=desc.text(), un=un.currentText(), valor=valor.text().replace(',','.',1))
                                qtde=+1
                            else: raise Exception("Erro: digite apenas números no valor!")
                        else: 
                            raise Exception(f"Erro: s  Serviço {desc.text()} já existe!")
                    elif desc.text() or valor.text():
                        raise Exception("Erro: Preencha todos os campos!")
                if(qtde==0):
                    raise Exception("Erro: campos vazios!")
                msg =  QtWidgets.QMessageBox()
                msg.setWindowTitle("Aviso")
                msg.setText(f"{qtde} peça(s) cadastrada(s) com sucesso!")
                msg.exec()
                return True
            except Exception as e:
                transaction.rollback()
                msg =  QtWidgets.QMessageBox()
                msg.setWindowTitle("Erro")
                msg.setText(str(e))
                msg.exec()
                return False

    def listarPecas(self):
        pass