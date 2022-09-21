from model.modelo import Orcamento

class OrcamentoRepository():
    def __init__(self):
        pass

    def save(self, orcamento:dict):
        return Orcamento.create(**orcamento)

    def update(self, orcamento:dict):
        _orcamento = Orcamento(**orcamento)
        _orcamento.save()
        return _orcamento

    def delete(self, id):
        return Orcamento.delete_by_id(id)

    def findAll(self):
        return Orcamento.select()

    def findByID(self, id):
        return Orcamento.select().where(Orcamento.idOrcamento==id).get()
