from playhouse.shortcuts import model_to_dict

from model.modelo import db
from repository.cidadeRepository import CidadeRepository
from repository.clienteRepository import ClienteRepository
from repository.foneRepository import FoneRepository
from repository.marcaRepository import MarcaRepository
from repository.orcamentoRepository import OrcamentoRepository
from repository.veiculoClienteRepository import VeiculoClienteRepository
from repository.veiculoRepository import VeiculoRepository
from ui.messageBox import MessageBox


class ClienteController:
    def __init__(self):
        self.clienteRep = ClienteRepository()
        self.orcamentoRep = OrcamentoRepository()
        self.cidadeRep = CidadeRepository()
        self.foneRep = FoneRepository()
        self.marcaRep = MarcaRepository()
        self.veiculoRep = VeiculoRepository()
        self.veiculoClienteRep = VeiculoClienteRepository()

    def salvarCliente(self, dados: dict, fones: list):
        with db.atomic() as transaction:
            try:
                if dados["nome"] is None:
                    raise Exception('Campo "Nome" obrigatório')
                if dados["documento"]:
                    cliente = self.clienteRep.findByDocumento(dados["documento"])
                    if cliente:
                        raise Exception(
                            f"Documento já registrado para o cliente {cliente.nome}"
                        )
                if dados["cidade"] is not None:
                    cidade = {}
                    cidade["nome"] = dados.pop("cidade")
                    cidade["uf"] = dados.pop("uf")
                    qCidade = self.cidadeRep.findCidadeByNomeAndUF(
                        cidade["nome"], cidade["uf"]
                    )
                    if qCidade:
                        dados["cidade"] = qCidade
                    else:
                        dados["cidade"] = self.cidadeRep.save(cidade)
                _cliente = self.clienteRep.save(dados)
                for fone in fones:
                    if fone is not None:
                        _fone = self.foneRep.findByFone(fone)
                        if _fone:
                            if str(_fone.cliente) == str(_cliente.idCliente):
                                raise Exception("Fones duplicados!")
                            raise Exception(
                                f"Fone {_fone.fone} já cadastrado por outro cliente"
                            )
                        self.foneRep.save(_cliente, fone)
                return _cliente
            except Exception as e:
                transaction.rollback()
                return e

    # salva dados do cliente, telefones, veiculo e vincula-os
    def salvarClienteVeiculo(
        self, dadosCliente: dict, dadosFone: list, dadosVeiculo: dict
    ):
        with db.atomic() as transaction:
            try:
                cliente = self.salvarCliente(dadosCliente, dadosFone)
                if isinstance(cliente, Exception):
                    raise Exception(cliente)
                qVeiculo = self.veiculoRep.findByPlaca(dadosVeiculo["placa"])
                if qVeiculo:
                    question = MessageBox.question(
                        MessageBox(),
                        f"Veiculo {qVeiculo.modelo} placa {qVeiculo.placa} já registrado. "
                        + f"Deseja utilizá-lo para o cliente {cliente.nome}? ",
                    )
                    if question == "sim":
                        self.veiculoClienteRep.save(qVeiculo, cliente)
                    else:
                        raise Exception("Cadastro cancelado")
                else:
                    veiculo = self.salvarVeiculo(dadosVeiculo)
                    if isinstance(veiculo, Exception):
                        raise Exception(veiculo)
                    self.veiculoClienteRep.save(veiculo, cliente)
                return True
            except Exception as e:
                transaction.rollback()
                return e

    def editarCliente(self, idCliente, cliente: dict, fonesTela: list):
        with db.atomic() as transaction:
            try:
                cliente["idCliente"] = idCliente
                if cliente["documento"]:
                    qCliente = self.clienteRep.findByDocumento(cliente["documento"])
                    if qCliente:
                        if str(qCliente.idCliente) != str(idCliente):
                            raise Exception(
                                f"Documento já registrado para o cliente {qCliente.nome}"
                            )
                if cliente["cidade"] is not None:
                    cidade = {}
                    cidade["nome"] = cliente.pop("cidade")
                    cidade["uf"] = cliente.pop("uf")
                    qCidade = self.cidadeRep.findCidadeByNomeAndUF(
                        cidade["nome"], cidade["uf"]
                    )
                    if qCidade:
                        cliente["cidade"] = qCidade
                    else:
                        cliente["cidade"] = self.cidadeRep.save(cidade)
                _cliente = self.clienteRep.update(cliente)
                fonesBanco = self.foneRep.findByClienteID(_cliente)
                if fonesBanco is not None:
                    fonesBanco = list(fonesBanco.dicts())
                    for fone in fonesBanco:
                        if not fone["fone"] in fonesTela:
                            self.foneRep.delete(_cliente, fone["fone"])
                    for fone in fonesTela:
                        if fone is not None:
                            _fone = self.foneRep.findByFone(fone)
                            if _fone:
                                if str(_fone.cliente) != str(_cliente.idCliente):
                                    raise Exception(
                                        f"Fone {_fone.fone} já cadastrado por outro cliente!"
                                    )
                        if fone is not None and next(
                            (False for item in fonesBanco if item["fone"] == fone), True
                        ):
                            self.foneRep.save(_cliente, fone)
                else:
                    for fone in fonesTela:
                        self.foneRep.save(_cliente, fone)
                return _cliente
            except Exception as e:
                transaction.rollback()
                return e

    # listar todos os clientes ou clientes vinculados a um veiculo
    def listarClientes(self, idVeiculo=None, qtde=None):
        _clientes = []
        if idVeiculo:
            clientes = self.veiculoClienteRep.findClientesByVeiculoID(idVeiculo)
            if clientes:
                for cliente in clientes:
                    _clientes.append(model_to_dict(cliente))
                return _clientes
            return None
        else:
            clientes = self.clienteRep.findAll(qtde)
            if clientes:
                for cliente in clientes:
                    _clientes.append(model_to_dict(cliente))
                return _clientes
            return None

    # buscar clientes por uma string de alguma coluna (Ex.: nome, documento, telefone)
    def buscarCliente(self, input, limit=None, orderBy=None):
        with db.atomic() as transaction:
            try:
                _clientes = []
                clientes = self.clienteRep.findByInput(input, limit, orderBy)
                if clientes:
                    for cliente in clientes:
                        _clientes.append(model_to_dict(cliente))
                    return _clientes
                return None
            except Exception as e:
                transaction.rollback()
                return e

    # listar cliente pelo id
    def getCliente(self, id):
        cliente = self.clienteRep.findByID(id)
        if cliente:
            return model_to_dict(cliente)
        return None

    # listar fones dado um cliente
    def listarFones(self, idCliente):
        fones = self.foneRep.findByClienteID(idCliente)
        if fones:
            return fones.dicts()
        return None

    # salva somente um veiculo
    def salvarVeiculo(self, veiculo):
        with db.atomic() as transaction:
            try:
                qVeiculo = self.veiculoRep.findByPlaca(veiculo["placa"])
                if qVeiculo:
                    raise Exception(
                        f"Placa {qVeiculo.placa} já registrada para o veículo "
                        + f"{self.marcaRep.findByID(qVeiculo.marca).nome} {qVeiculo.modelo}"
                    )
                marca = self.marcaRep.findByNome(veiculo["marca"])
                if not marca:
                    marca = self.marcaRep.save({"nome": veiculo["marca"]})
                veiculo["marca"] = marca
                return self.veiculoRep.save(veiculo)

            except Exception as e:
                transaction.rollback()
                return e

    def editarVeiculo(self, idVeiculo, veiculo):
        with db.atomic() as transaction:
            try:
                qVeiculo = self.veiculoRep.findByPlaca(veiculo["placa"])
                if qVeiculo:
                    if str(qVeiculo.idVeiculo) != str(idVeiculo):
                        raise Exception(
                            f"Placa {qVeiculo.placa} já registrada para o veículo "
                            + f"{self.marcaRep.findByID(qVeiculo.marca).nome} {qVeiculo.modelo}"
                        )
                veiculo["idVeiculo"] = idVeiculo
                marca = self.marcaRep.findByNome(veiculo["marca"])
                if not marca:
                    marca = self.marcaRep.save({"nome": veiculo["marca"]})
                veiculo["marca"] = marca
                _veiculo = self.veiculoRep.update(veiculo)
                return _veiculo
            except Exception as e:
                transaction.rollback()
                return e

    # listar todos os veiculos ou veiculos vinculados a um cliente
    def listarVeiculos(self, idCliente=None):
        with db.atomic() as transaction:
            try:
                _veiculos = []
                if idCliente:
                    veiculos = self.veiculoClienteRep.findVeiculosByClienteID(idCliente)
                    if veiculos:
                        for veiculo in veiculos:
                            _veiculos.append(model_to_dict(veiculo))
                        return _veiculos
                    return None
                else:
                    veiculos = self.veiculoRep.findAll()
                    if veiculos:
                        for veiculo in veiculos:
                            _veiculos.append(model_to_dict(veiculo))
                        return _veiculos
                    return None
            except Exception as e:
                transaction.rollback()
                return e

    def getVeiculo(self, id):
        veiculo = self.veiculoRep.findByID(id)
        if veiculo:
            return model_to_dict(veiculo)
        return None

    # buscar veiculos por uma string de alguma coluna (Ex.: marca, modelo, placa)
    def buscarVeiculo(self, input, limit=None, orderBy=None):
        with db.atomic() as transaction:
            try:
                _veiculos = []
                veiculos = self.veiculoRep.findByInput(input, limit, orderBy)
                if veiculos:
                    for veiculo in veiculos:
                        _veiculos.append(model_to_dict(veiculo))
                    return _veiculos
                return None
            except Exception as e:
                transaction.rollback()
                return e

    def excluirCliente(self, id):
        with db.atomic() as transaction:
            try:
                orcamento = self.orcamentoRep.findByClienteID(id)
                if orcamento:
                    raise Exception(
                        "Não é possível excluir este cliente, ele está vinculado à orçamento(s)."
                    )
                linesAffected = self.clienteRep.delete(id)
                return linesAffected
            except Exception as e:
                transaction.rollback()
                return e

    def excluirVeiculo(self, id):
        with db.atomic() as transaction:
            try:
                orcamento = self.orcamentoRep.findByVeiculoID(id)
                if orcamento:
                    raise Exception(
                        "Não é possível excluir este veículo, ele está vinculado à orçamento(s)."
                    )
                linesAffected = self.veiculoRep.delete(id)
                return linesAffected
            except Exception as e:
                transaction.rollback()
                return e

    def excluirVeiculoCliente(self, veiculo, cliente):
        with db.atomic() as transaction:
            try:
                veiculoCliente = self.veiculoClienteRep.findByVeiculoAndCliente(
                    veiculo, cliente
                )
                linesAffected = self.veiculoClienteRep.delete(
                    veiculoCliente.veiculo, veiculoCliente.cliente
                )
                if linesAffected != 0:
                    return True
                return False
            except Exception as e:
                transaction.rollback()
                return e
