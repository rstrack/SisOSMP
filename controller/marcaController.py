from playhouse.shortcuts import model_to_dict

from model.modelo import db
from repository.marcaRepository import MarcaRepository
from repository.veiculoRepository import VeiculoRepository


class MarcaController:
    def __init__(self) -> None:
        self.marcaRep = MarcaRepository()
        self.veiculoRep = VeiculoRepository()

    def listarMarcas(self):
        return self.marcaRep.findAll().dicts()

    def getMarca(self, id):
        marca = self.marcaRep.findByID(id)
        if marca:
            return model_to_dict(marca)
        return None

    def editarMarca(self, id, marca):
        with db.atomic() as transaction:
            try:
                marca["idMarca"] = id
                _marca = self.marcaRep.update(marca)
                return _marca
            except Exception as e:
                transaction.rollback()
                return e

    def excluirMarca(self, id):
        with db.atomic() as transaction:
            try:
                veiculos = self.veiculoRep.findByMarca(id)
                if veiculos:
                    raise Exception(
                        "Não é possível excluir esta marca, ela está vinculada à veículo(s)."
                    )
                linesAffected = self.marcaRep.delete(id)
                return linesAffected
            except Exception as e:
                transaction.rollback()
                return e
