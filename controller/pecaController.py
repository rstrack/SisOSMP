from model.modelo import db
from playhouse.shortcuts import model_to_dict
from repository.pecaRepository import PecaRepository

class PecaController():
    def __init__(self):
        self.pecaRep = PecaRepository()

    def salvarPeca(self, peca:dict):
        with db.atomic() as transaction:
            try:
                qPeca = self.pecaRep.findByDescricao(peca['descricao'])
                if qPeca:
                    return qPeca
                else: return self.pecaRep.save(peca)
            except Exception as e:
                transaction.rollback()
                return e

    def editarPeca(self, peca:dict):
        with db.atomic() as transaction:
            try:
                pass


            except Exception as e:
                transaction.rollback()
                return e


    '''def salvarPecas(self):
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
                return False'''

    def getPecaByDescricao(self, desc):
        peca = self.pecaRep.findByDescricao(desc)
        if peca:
            return model_to_dict(peca)
        else: return None

    def getPeca(self, id):
        peca = self.pecaRep.findByID(id)
        if peca:
            return model_to_dict(peca)
        else: return None

    def listarPecas(self):
        pecas = self.pecaRep.findAll()
        if pecas:
            return pecas.dicts()
        else: return None