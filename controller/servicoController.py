from pickle import FALSE
from PyQt6 import QtWidgets

from model.modelo import *

class ServicoController():
    def __init__(self):
        pass

    def salvarServico(self, desc, valor):
        qPeca = Peca.select().where(Peca.descricao==desc)
        if not qPeca:
            if valor.replace(',','',1).isdigit():
                servico = Peca.create(descricao=desc, valor=valor.replace(',','.',1))
            else: raise Exception("Erro: digite apenas números no valor!")
        else: 
            raise Exception(f"Peça {desc.text()} já existe!")
        return servico

    def salvarServicos(self):
        with db.atomic() as transaction:
            try:
                qtde = 0
                for desc, valor in self.view.linhasservico:
                    if desc.text() and valor.text():
                        qServico = Servico.select().where(Servico.descricao==desc.text())
                        if not qServico:
                            if valor.text().replace(',','',1).replace('.','',1).isdigit():
                                Servico.create(descricao=desc.text(), valor=valor.text().replace(',','.',1))
                                qtde=+1
                            else: raise Exception("Erro: digite apenas números no valor!")
                        else: raise Exception(f"Erro: Serviço {desc.text()} já existe!")
                    elif desc.text() or valor.text():
                        raise Exception("Erro: Preencha todos os campos!")
                if(qtde==0):
                    raise Exception("Erro: campos vazios!")
                msg =  QtWidgets.QMessageBox()
                msg.setWindowTitle("Aviso")
                msg.setText(f"{qtde} serviço(s) cadastrado(s) com sucesso!")
                msg.exec()
                return True
            except Exception as e:
                transaction.rollback()
                msg =  QtWidgets.QMessageBox()
                msg.setWindowTitle("Erro")
                msg.setText(str(e))
                msg.exec()
                return False