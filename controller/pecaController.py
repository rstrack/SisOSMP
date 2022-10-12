from model.modelo import db
from playhouse.shortcuts import model_to_dict
from repository.itemPecaRepository import ItemPecaRepository
from repository.pecaRepository import PecaRepository

class PecaController():
    def __init__(self):
        self.pecaRep = PecaRepository()
        self.itemPecaRep = ItemPecaRepository()

    def salvarPeca(self, peca:dict):
        with db.atomic() as transaction:
            try:
                qPeca = self.pecaRep.findByDescricao(peca['descricao'])
                if qPeca:
                    raise Exception(f'A peça {qPeca.descricao} já está cadastrada!')
                else: return self.pecaRep.save(peca)
            except Exception as e:
                transaction.rollback()
                return e

    def salvarPecas(self, pecas:list):
        with db.atomic() as transaction:
            try:
                for peca in pecas:
                    _peca = self.pecaRep.findByDescricao(peca['descricao'])
                    if _peca:
                        raise Exception(f'A peça {_peca.descricao} já está cadastrada!')
                    self.pecaRep.save(peca)
                return True
            except Exception as e:
                transaction.rollback()
                return e

    def editarPeca(self, id, peca:dict):
        with db.atomic() as transaction:
            try:
                _peca = self.pecaRep.findByDescricao(peca['descricao'])
                if _peca:
                    raise Exception(f"A peça {peca['descricao']} já está cadastrada!")
                peca['idPeca'] = id
                _peca = self.pecaRep.update(peca)
                return _peca
            except Exception as e:
                transaction.rollback()
                return e

    def listarPecas(self):
        with db.atomic() as transaction:
            try:
                pecas = self.pecaRep.findAll()
                if pecas:
                    return pecas.dicts()
                else: return None
            except Exception as e:
                transaction.rollback()
                return e

    def getPeca(self, id):
        with db.atomic() as transaction:
            try:
                peca = self.pecaRep.findByID(id)
                if peca:
                    return model_to_dict(peca)
                else: return None
            except Exception as e:
                transaction.rollback()
                return e

    def getPecaByDescricao(self, desc):
        with db.atomic() as transaction:
            try:
                peca = self.pecaRep.findByDescricao(desc)
                if peca:
                    return model_to_dict(peca)
                else: return None
            except Exception as e:
                transaction.rollback()
                return e

    def buscarPeca(self, input, limit=None):
        with db.atomic() as transaction:
            try:
                pecas = self.pecaRep.findByInput(input, limit)
                if pecas:
                    return pecas.dicts()
                else: return None
            except Exception as e:
                transaction.rollback()
                return e

    def excluirPeca(self, id):
        with db.atomic() as transaction:
            try:
                _itemPeca = self.itemPecaRep.findByPeca(id)
                if _itemPeca:
                    raise Exception('Não é possível excluir esta peça, ela está vinculada à orçamento(s).')
                linesAffected = self.pecaRep.delete(id)
                if linesAffected != 0:
                    return True
                else: return False
            except Exception as e:
                transaction.rollback()
                return e
