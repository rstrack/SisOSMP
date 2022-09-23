from model.modelo import Servico

class ServicoRepository():
    def __init__(self) -> None:
        pass

    def save(self, servico: dict):
        return Servico.create(**servico)

    def update(self, servico:dict):
        _servico = Servico(**servico)
        _servico.save()
        return _servico

    def delete(self, id):
        return Servico.delete_by_id(id)

    def findAll(self):
        return Servico.select()

    def findByID(self, id):
        return Servico.select().where(Servico.idServico==id).get()

    def findByDescricao(self, desc):
        servico = Servico.select().where(Servico.descricao==desc)
        if servico:
            return servico.get()
        else: return None