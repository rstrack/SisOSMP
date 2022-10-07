from model.modelo import Fone

class FoneRepository():
    def __init__(self) -> None:
        pass

    def save(self, cliente, fone):
        return Fone.create(cliente=cliente, fone=fone)

    def update(self, dados):
        pass

    def findByClienteID(self, id):
        return Fone.select().where(Fone.cliente==id)

    def delete(self, cliente, fone):
        return Fone.delete().where((Fone.cliente==cliente) & (Fone.fone==fone)).execute()

    def findByFone(self, fone):
        return Fone.select().where(Fone.fone==fone)
