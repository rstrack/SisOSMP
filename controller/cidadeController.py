from model.modelo import Cidade, db
from repository.cidadeRepository import CidadeRepository

from playhouse.shortcuts import model_to_dict

class CidadeController():
    def __init__(self):
        self.cidadeRep = CidadeRepository()

    def salvarCidade(self, cidade:dict):
        with db.atomic() as transaction:
            try:
                if not 'nome' in cidade:
                    raise Exception("Nome da cidade não inserido")
                cidade['estado'] = self.estadoCtrl.salvarEstado(cidade['estado'])
                return Cidade.create(**cidade)
            except Exception as e:
                transaction.rollback()
                return e

    def editarCidade(self, dados:dict):
        with db.atomic() as transaction:
            try:
                cidade = self.cidadeRep.findByID(id)
                if not cidade:
                    raise Exception("Cidade não cadastrada")
                cidade = self.cidadeRep.update(dados)
                return cidade
            except Exception as e:
                transaction.rollback()
                return e

    def listarCidades(self):
        with db.atomic() as transaction:
            try:
                _listaCidades = []
                listaCidades = self.cidadeRep.findAll()
                if listaCidades: 
                    for cidade in listaCidades:
                        _listaCidades.append(model_to_dict(cidade))
                    return _listaCidades
                else: return None
            except Exception as e:
                transaction.rollback()
                return e

    def getCidade(self, id):
        with db.atomic() as transaction:
            try:
                cidade = self.cidadeRep.findByID(id)
                if cidade: return model_to_dict(cidade)
                else: return None
            except Exception as e:
                transaction.rollback()
                return e

    def deletarCidade(self, id):
        with db.atomic() as transaction:  # Opens new transaction.
            try:
                return Cidade.delete_by_id(id)
            except Exception as e:
                transaction.rollback()
                return e
