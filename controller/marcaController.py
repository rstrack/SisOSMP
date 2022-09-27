from repository.marcaRepository import MarcaRepository
from playhouse.shortcuts import model_to_dict

class MarcaController():
    def __init__(self) -> None:
        self.marcaRep = MarcaRepository()

    def listarMarcas(self):
        return self.marcaRep.findAll().dicts()

    def getMarca(self, id):
        marca = self.marcaRep.findByID(id)
        if marca:
            return model_to_dict(marca)
        else: return None