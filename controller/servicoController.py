from playhouse.shortcuts import model_to_dict

from model.modelo import db
from repository.itemServicoRepository import ItemServicoRepository
from repository.servicoRepository import ServicoRepository


class ServicoController:
    @staticmethod
    def salvarServico(servico: dict):
        with db.atomic() as transaction:
            try:
                qServico = ServicoRepository.findByDescricao(servico["descricao"])
                if qServico:
                    raise Exception(
                        f"O serviço {servico['descricao']} já está cadastrado!"
                    )
                return ServicoRepository.save(servico)
            except Exception as e:
                transaction.rollback()
                return e

    @staticmethod
    def salvarServicos(servicos: list):
        with db.atomic() as transaction:
            try:
                for servico in servicos:
                    _servico = ServicoRepository.findByDescricao(servico["descricao"])
                    if _servico:
                        raise Exception(
                            f"O serviço {servico['descricao']} já está cadastrado!"
                        )
                    ServicoRepository.save(servico)
                return True
            except Exception as e:
                transaction.rollback()
                return e

    @staticmethod
    def editarServico(id, servico: dict):
        with db.atomic() as transaction:
            try:
                qServico = ServicoRepository.findByDescricao(servico["descricao"])
                if qServico:
                    if str(qServico.idServico) != str(id):
                        raise Exception(
                            f"O serviço {servico['descricao']} já está cadastrado!"
                        )
                servico["idServico"] = id
                _servico = ServicoRepository.update(servico)
                return _servico
            except Exception as e:
                transaction.rollback()
                return e

    @staticmethod
    def listarServicos():
        servicos = ServicoRepository.findAll()
        if servicos:
            return servicos.dicts()
        return None

    @staticmethod
    def getServico(id):
        servico = ServicoRepository.findByID(id)
        if servico:
            return model_to_dict(servico)
        return None

    @staticmethod
    def getServicoByDescricao(desc):
        servico = ServicoRepository.findByDescricao(desc)
        if servico:
            return model_to_dict(servico)
        return None

    @staticmethod
    def buscarServico(input, limit=None, orderBy=None):
        with db.atomic() as transaction:
            try:
                servicos = ServicoRepository.findByInput(input, limit, orderBy)
                if servicos:
                    _servicos = []
                    for servico in servicos:
                        _servicos.append(model_to_dict(servico))
                    return _servicos
                return None
            except Exception as e:
                transaction.rollback()
                return e

    @staticmethod
    def excluirServico(id):
        with db.atomic() as transaction:
            try:
                _itemServico = ItemServicoRepository.findByServico(id)
                if _itemServico:
                    raise Exception(
                        "Não é possível excluir este serviço, ela está vinculado à orçamento(s)."
                    )
                linesAffected = ServicoRepository.delete(id)
                return linesAffected
            except Exception as e:
                transaction.rollback()
                return e
