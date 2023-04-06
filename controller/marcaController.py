from playhouse.shortcuts import model_to_dict

from model.modelo import db
from repository.marcaRepository import MarcaRepository
from repository.veiculoRepository import VeiculoRepository


class MarcaController:
    @staticmethod
    def listarMarcas():
        return MarcaRepository.findAll().dicts()

    @staticmethod
    def getMarca(id):
        marca = MarcaRepository.findByID(id)
        if marca:
            return model_to_dict(marca)
        return None

    @staticmethod
    def editarMarca(id, marca):
        with db.atomic() as transaction:
            try:
                marca["idMarca"] = id
                _marca = MarcaRepository.update(marca)
                return _marca
            except Exception as e:
                transaction.rollback()
                return e

    @staticmethod
    def excluirMarca(id):
        with db.atomic() as transaction:
            try:
                veiculos = VeiculoRepository.findByMarca(id)
                if veiculos:
                    raise Exception(
                        "Não é possível excluir esta marca, ela está vinculada à veículo(s)."
                    )
                linesAffected = MarcaRepository.delete(id)
                return linesAffected
            except Exception as e:
                transaction.rollback()
                return e
