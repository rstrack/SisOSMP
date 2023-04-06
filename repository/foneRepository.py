from model.modelo import Fone


class FoneRepository:
    @staticmethod
    def save(cliente, fone):
        return Fone.create(cliente=cliente, fone=fone)

    @staticmethod
    def findByClienteID(id):
        return Fone.select().where(Fone.cliente == id)

    @staticmethod
    def delete(cliente, fone):
        return (
            Fone.delete()
            .where((Fone.cliente == cliente) & (Fone.fone == fone))
            .execute()
        )

    @staticmethod
    def findByFone(fone):
        _fone = Fone.select().where(Fone.fone == fone)
        if _fone:
            return _fone.get()
        return None
