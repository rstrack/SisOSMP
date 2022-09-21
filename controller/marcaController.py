from repository.marcaRepository import MarcaRepository

class MarcaController():
    def __init__(self) -> None:
        self.marcaRep = MarcaRepository()

    def listarMarcas(self):
        return self.marcaRep.findAll().dicts()