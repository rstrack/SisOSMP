from playhouse.shortcuts import model_to_dict

from model.modelo import db
from repository.cidadeRepository import CidadeRepository


class CidadeController:
    def __init__(self):
        self.cidadeRep = CidadeRepository()

    def listarCidades(self):
        with db.atomic() as transaction:
            try:
                _listaCidades = []
                listaCidades = self.cidadeRep.findAll()
                if listaCidades:
                    for cidade in listaCidades:
                        _listaCidades.append(model_to_dict(cidade))
                    return _listaCidades
                return None
            except Exception as e:
                transaction.rollback()
                return e

    def getCidade(self, id):
        with db.atomic() as transaction:
            try:
                cidade = self.cidadeRep.findByID(id)
                if cidade:
                    return model_to_dict(cidade)
                return None
            except Exception as e:
                transaction.rollback()
                return e
