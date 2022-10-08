from model.modelo import Cidade

class CidadeRepository():
    def __init__(self):
        pass

    def save(self, cidade:dict):
        return Cidade.create(**cidade)

    def update(self, cidade:dict):
        _cidade = Cidade(**cidade)
        _cidade.save()
        return _cidade

    def delete(self, id):
        return Cidade.delete_by_id(id)

    def findAll(self):
        return Cidade.select()

    def findByID(seld, id):
        return Cidade.select().where(Cidade.idCidade==id).get()

    def findCidadeByNomeAndUF(self, nome, uf):
        cidade = Cidade.select().where(Cidade.nome==nome and  Cidade.uf==uf)
        if cidade: return cidade.get()
        else: return None

