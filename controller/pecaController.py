from playhouse.shortcuts import model_to_dict

from model.modelo import db
from repository.itemPecaRepository import ItemPecaRepository
from repository.pecaRepository import PecaRepository


class PecaController:
    @staticmethod
    def salvarPeca(peca: dict):
        with db.atomic() as transaction:
            try:
                qPeca = PecaRepository.findByDescricao(peca["descricao"])
                if qPeca:
                    raise Exception(f"A peça {qPeca.descricao} já está cadastrada!")
                return PecaRepository.save(peca)
            except Exception as e:
                transaction.rollback()
                return e

    @staticmethod
    def salvarPecas(pecas: list):
        with db.atomic() as transaction:
            try:
                for peca in pecas:
                    _peca = PecaRepository.findByDescricao(peca["descricao"])
                    if _peca:
                        raise Exception(f"A peça {_peca.descricao} já está cadastrada!")
                    PecaRepository.save(peca)
                return True
            except Exception as e:
                transaction.rollback()
                return e

    @staticmethod
    def editarPeca(id, peca: dict):
        with db.atomic() as transaction:
            try:
                qPeca = PecaRepository.findByDescricao(peca["descricao"])
                if qPeca:
                    if str(qPeca.idPeca) != str(id):
                        raise Exception(
                            f"A peça {peca['descricao']} já está cadastrada!"
                        )
                peca["idPeca"] = id
                _peca = PecaRepository.update(peca)
                return _peca
            except Exception as e:
                transaction.rollback()
                return e

    @staticmethod
    def listarPecas():
        with db.atomic() as transaction:
            try:
                pecas = PecaRepository.findAll()
                if pecas:
                    return pecas.dicts()
                return None
            except Exception as e:
                transaction.rollback()
                return e

    @staticmethod
    def getPeca(id):
        with db.atomic() as transaction:
            try:
                peca = PecaRepository.findByID(id)
                if peca:
                    return model_to_dict(peca)
                return None
            except Exception as e:
                transaction.rollback()
                return e

    @staticmethod
    def getPecaByDescricao(desc):
        with db.atomic() as transaction:
            try:
                peca = PecaRepository.findByDescricao(desc)
                if peca:
                    return model_to_dict(peca)
                return None
            except Exception as e:
                transaction.rollback()
                return e

    @staticmethod
    def buscarPeca(input, limit=None, orderBy=None):
        with db.atomic() as transaction:
            try:
                pecas = PecaRepository.findByInput(input, limit, orderBy)
                if pecas:
                    _pecas = []
                    for peca in pecas:
                        _pecas.append(model_to_dict(peca))
                    return _pecas
                return None
            except Exception as e:
                transaction.rollback()
                return e

    @staticmethod
    def excluirPeca(id):
        with db.atomic() as transaction:
            try:
                _itemPeca = ItemPecaRepository.findByPeca(id)
                if _itemPeca:
                    raise Exception(
                        "Não é possível excluir esta peça, ela está vinculada à orçamento(s)."
                    )
                linesAffected = PecaRepository.delete(id)
                if linesAffected != 0:
                    return True
                return False
            except Exception as e:
                transaction.rollback()
                return e
