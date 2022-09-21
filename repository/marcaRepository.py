from model.modelo import Marca

class MarcaRepository():
    def __init__(self):
        pass

    def save(self, marca):
        return Marca.create(**marca)

    def update(self, marca):
        _marca = Marca(**marca)
        _marca.save()
        return _marca

    def delete(self, id):
        return Marca.delete_by_id(id)
        

    def findAll(self):
        return Marca.select()

    def findByID(self, id):
        return Marca.select().where(Marca.idMarca==id).get()

    def findByNome(self, nome):
        marca = Marca.select().where(Marca.nome==nome)
        if marca:
            return marca.get()
        else: return None