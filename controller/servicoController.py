from PyQt6 import QtWidgets
from playhouse.shortcuts import model_to_dict
from model.modelo import *
from repository.itemServicoRepository import ItemServicoRepository
from repository.servicoRepository import ServicoRepository

class ServicoController():
    def __init__(self):
        self.servicoRep = ServicoRepository()
        self.itemServicoRep = ItemServicoRepository()

    def salvarServico(self, servico:dict):
        with db.atomic() as transaction:
            try:
                qServico = self.servicoRep.findByDescricao(servico['descricao'])
                if qServico:
                    raise Exception(f"O serviço {servico['descricao']} já está cadastrado!")
                else: return self.servicoRep.save(servico)
            except Exception as e:
                transaction.rollback()
                return e

    def salvarServicos(self, servicos:list):
        with db.atomic() as transaction:
            try:
                for servico in servicos:
                    _servico = self.servicoRep.findByDescricao(servico['descricao'])
                    if _servico:
                        raise Exception(f"O serviço {servico['descricao']} já está cadastrado!")
                    self.servicoRep.save(servico)
                return True
            except Exception as e:
                transaction.rollback()
                return e

    def editarServico(self, id, servico:dict):
        with db.atomic() as transaction:
            try:
                qServico = self.servicoRep.findByDescricao(servico['descricao'])
                if qServico:
                    raise Exception(f"O serviço {servico['descricao']} já está cadastrado!")
                servico['idServico'] = id
                _servico = self.servicoRep.update(servico)
                return _servico
            except Exception as e:
                transaction.rollback()
                return e

    def listarServicos(self):
        servicos = self.servicoRep.findAll()
        if servicos:
            return servicos.dicts()
        else: return None

    def getServico(self, id):
        servico = self.servicoRep.findByID(id)
        if servico:
            return model_to_dict(servico)
        else: return None

    def getServicoByDescricao(self, desc):
        servico = self.servicoRep.findByDescricao(desc)
        if servico:
            return model_to_dict(servico)
        else: return None

    def excluirServico(self, id):
        with db.atomic() as transaction:
            try:
                _itemServico = self.itemServicoRep.findByServico(id)
                if _itemServico:
                    raise Exception('Não é possível excluir este serviço, ela está vinculado à orçamento(s).')
                linesAffected = self.servicoRep.delete(id)
                if linesAffected != 0:
                    return True
                else: return False
            except Exception as e:
                transaction.rollback()
                return e