from model.modelo import Cidade


class CidadeRepository:
    def __init__(self):
        pass

    @staticmethod
    def save(cidade: dict):
        return Cidade.create(**cidade)

    @staticmethod
    def update(cidade: dict):
        _cidade = Cidade(**cidade)
        _cidade.save()
        return _cidade

    @staticmethod
    def delete(id):
        return Cidade.delete_by_id(id)

    @staticmethod
    def findAll():
        return Cidade.select()

    @staticmethod
    def findByID(id):
        return Cidade.select().where(Cidade.idCidade == id).get()

    @staticmethod
    def findCidadeByNomeAndUF(nome, uf):
        cidade = Cidade.select().where((Cidade.nome == nome) & (Cidade.uf == uf))
        if cidade:
            return cidade.get()
        return None