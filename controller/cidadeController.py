from playhouse.shortcuts import model_to_dict

from model.modelo import db
from repository.cidadeRepository import CidadeRepository


class CidadeController:
    @staticmethod
    def listarCidades():
        with db.atomic() as transaction:
            try:
                _listaCidades = []
                listaCidades = CidadeRepository.findAll()
                if listaCidades:
                    for cidade in listaCidades:
                        _listaCidades.append(model_to_dict(cidade))
                    return _listaCidades
                return None
            except Exception as e:
                transaction.rollback()
                return e

    @staticmethod
    def getCidade(id):
        with db.atomic() as transaction:
            try:
                cidade = CidadeRepository.findByID(id)
                if cidade:
                    return model_to_dict(cidade)
                return None
            except Exception as e:
                transaction.rollback()
                return e

