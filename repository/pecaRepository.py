from model.modelo import Peca

class PecaRepository():
    def __init__(self) -> None:
        pass

    def save(self, peca: dict):
        return Peca.create(**peca)

    def update(self, peca:dict):
        _peca = Peca(**peca)
        _peca.save()
        return _peca

    def delete(self, id):
        return Peca.delete_by_id(id)

    def findAll(self):
        return Peca.select().order_by(Peca.descricao)

    def findByID(self, id):
        return Peca.select().where(Peca.idPeca==id).get()

    def findByDescricao(self, desc):
        _peca =  Peca.select().where(Peca.descricao==desc)
        if _peca:
            return _peca.get()
        else: return None
