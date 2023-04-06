from model.modelo import Marca


class MarcaRepository:
    @staticmethod
    def save(marca):
        return Marca.create(**marca)
    
    @staticmethod
    def update(marca):
        _marca = Marca(**marca)
        _marca.save()
        return _marca

    @staticmethod
    def delete(id):
        return Marca.delete_by_id(id)

    @staticmethod
    def findAll():
        return Marca.select().order_by(Marca.nome)

    @staticmethod
    def findByID(id):
        return Marca.select().where(Marca.idMarca == id).get()

    @staticmethod
    def findByNome(nome):
        marca = Marca.select().where(Marca.nome == nome)
        if marca:
            return marca.get()
        return None
