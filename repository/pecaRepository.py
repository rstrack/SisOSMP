from model.modelo import Peca


class PecaRepository:
    def __init__(self) -> None:
        pass

    def save(self, peca: dict):
        return Peca.create(**peca)

    def update(self, peca: dict):
        _peca = Peca(**peca)
        _peca.save()
        return _peca

    def delete(self, id):
        return Peca.delete_by_id(id)

    def findAll(self):
        return Peca.select().order_by(Peca.descricao)

    def findByID(self, id):
        return Peca.select().where(Peca.idPeca == id).get()

    def findByDescricao(self, desc):
        _peca = Peca.select().where(Peca.descricao == desc)
        if _peca:
            return _peca.get()
        return None

    def findByInput(self, input, limit=None, orderBy=None):
        match orderBy:
            case 0:
                order_by = Peca.descricao
            case 1:
                order_by = -Peca.descricao
            case _:
                order_by = Peca.descricao
        _peca = (
            Peca.select()
            .where(Peca.descricao.contains(input))
            .order_by(order_by)
            .limit(limit)
            .distinct()
        )
        if _peca:
            return _peca
        return None
