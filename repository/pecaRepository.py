from model.modelo import Peca


class PecaRepository:
    @staticmethod
    def save(peca: dict):
        return Peca.create(**peca)

    @staticmethod
    def update(peca: dict):
        _peca = Peca(**peca)
        _peca.save()
        return _peca

    @staticmethod
    def delete(id):
        return Peca.delete_by_id(id)

    @staticmethod
    def findAll():
        return Peca.select().order_by(Peca.descricao)

    @staticmethod
    def findByID(id):
        return Peca.select().where(Peca.idPeca == id).get()

    @staticmethod
    def findByDescricao(desc):
        _peca = Peca.select().where(Peca.descricao == desc)
        if _peca:
            return _peca.get()
        return None

    @staticmethod
    def findByInput(input, limit=None, orderBy=None):
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
