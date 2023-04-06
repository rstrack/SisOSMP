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
    @staticmethod
    def salvarCliente(dados: dict, fones: list):
        with db.atomic() as transaction:
            try:
                if dados["nome"] is None:
                    raise Exception('Campo "Nome" obrigatório')
                if dados["documento"]:
                    cliente = ClienteRepository.findByDocumento(dados["documento"])
                    if cliente:
                        raise Exception(
                            f"Documento já registrado para o cliente {cliente.nome}"
                        )
                if dados["cidade"] is not None:
                    cidade = {}
                    cidade["nome"] = dados.pop("cidade")
                    cidade["uf"] = dados.pop("uf")
                    qCidade = CidadeRepository.findCidadeByNomeAndUF(
                        cidade["nome"], cidade["uf"]
                    )
                    if qCidade:
                        dados["cidade"] = qCidade
                    else:
                        dados["cidade"] = CidadeRepository.save(cidade)
                _cliente = ClienteRepository.save(dados)
                for fone in fones:
                    if fone is not None:
                        _fone = FoneRepository.findByFone(fone)
                        if _fone:
                            if str(_fone.cliente) == str(_cliente.idCliente):
                                raise Exception("Fones duplicados!")
                            raise Exception(
                                f"Fone {_fone.fone} já cadastrado por outro cliente"
                            )
                        FoneRepository.save(_cliente, fone)
                return _cliente
            except Exception as e:
                transaction.rollback()
                return e

    # salva dados do cliente, telefones, veiculo e vincula-os
    @staticmethod
    def salvarClienteVeiculo(
        dadosCliente: dict, dadosFone: list, dadosVeiculo: dict
    ):
        with db.atomic() as transaction:
            try:
                cliente = ClienteController.salvarCliente(dadosCliente, dadosFone)
                if isinstance(cliente, Exception):
                    raise Exception(cliente)
                qVeiculo = VeiculoRepository.findByPlaca(dadosVeiculo["placa"])
                if qVeiculo:
                    question = MessageBox.question(
                        MessageBox(),
                        f"Veiculo {qVeiculo.modelo} placa {qVeiculo.placa} já registrado. "
                        + f"Deseja utilizá-lo para o cliente {cliente.nome}? ",
                    )
                    if question == "sim":
                        VeiculoClienteRepository.save(qVeiculo, cliente)
                    else:
                        raise Exception("Cadastro cancelado")
                else:
                    veiculo = ClienteController.salvarVeiculo(dadosVeiculo)
                    if isinstance(veiculo, Exception):
                        raise Exception(veiculo)
                    VeiculoClienteRepository.save(veiculo, cliente)
                return True
            except Exception as e:
                transaction.rollback()
                return e

    @staticmethod
    def editarCliente(idCliente, cliente: dict, fonesTela: list):
        with db.atomic() as transaction:
            try:
                cliente["idCliente"] = idCliente
                if cliente["documento"]:
                    qCliente = ClienteRepository.findByDocumento(cliente["documento"])
                    if qCliente:
                        if str(qCliente.idCliente) != str(idCliente):
                            raise Exception(
                                f"Documento já registrado para o cliente {qCliente.nome}"
                            )
                if cliente["cidade"] is not None:
                    cidade = {}
                    cidade["nome"] = cliente.pop("cidade")
                    cidade["uf"] = cliente.pop("uf")
                    qCidade = CidadeRepository.findCidadeByNomeAndUF(
                        cidade["nome"], cidade["uf"]
                    )
                    if qCidade:
                        cliente["cidade"] = qCidade
                    else:
                        cliente["cidade"] = CidadeRepository.save(cidade)
                _cliente = ClienteRepository.update(cliente)
                fonesBanco = FoneRepository.findByClienteID(_cliente)
                if fonesBanco is not None:
                    fonesBanco = list(fonesBanco.dicts())
                    for fone in fonesBanco:
                        if not fone["fone"] in fonesTela:
                            FoneRepository.delete(_cliente, fone["fone"])
                    for fone in fonesTela:
                        if fone is not None:
                            _fone = FoneRepository.findByFone(fone)
                            if _fone:
                                if str(_fone.cliente) != str(_cliente.idCliente):
                                    raise Exception(
                                        f"Fone {_fone.fone} já cadastrado por outro cliente!"
                                    )
                        if fone is not None and next(
                            (False for item in fonesBanco if item["fone"] == fone), True
                        ):
                            FoneRepository.save(_cliente, fone)
                else:
                    for fone in fonesTela:
                        FoneRepository.save(_cliente, fone)
                return _cliente
            except Exception as e:
                transaction.rollback()
                return e

    # listar todos os clientes ou clientes vinculados a um veiculo
    @staticmethod
    def listarClientes(idVeiculo=None, qtde=None):
        _clientes = []
        if idVeiculo:
            clientes = VeiculoClienteRepository.findClientesByVeiculoID(idVeiculo)
            if clientes:
                for cliente in clientes:
                    _clientes.append(model_to_dict(cliente))
                return _clientes
            return None
        else:
            clientes = ClienteRepository.findAll(qtde)
            if clientes:
                for cliente in clientes:
                    _clientes.append(model_to_dict(cliente))
                return _clientes
            return None

    # buscar clientes por uma string de alguma coluna (Ex.: nome, documento, telefone)
    @staticmethod
    def buscarCliente(input, limit=None, orderBy=None):
        with db.atomic() as transaction:
            try:
                _clientes = []
                clientes = ClienteRepository.findByInput(input, limit, orderBy)
                if clientes:
                    for cliente in clientes:
                        _clientes.append(model_to_dict(cliente))
                    return _clientes
                return None
            except Exception as e:
                transaction.rollback()
                return e

    # listar cliente pelo id
    @staticmethod
    def getCliente(id):
        cliente = ClienteRepository.findByID(id)
        if cliente:
            return model_to_dict(cliente)
        return None

    # listar fones dado um cliente
    @staticmethod
    def listarFones(idCliente):
        fones = FoneRepository.findByClienteID(idCliente)
        if fones:
            return fones.dicts()
        return None

    # salva somente um veiculo
    @staticmethod
    def salvarVeiculo(veiculo):
        with db.atomic() as transaction:
            try:
                qVeiculo = VeiculoRepository.findByPlaca(veiculo["placa"])
                if qVeiculo:
                    raise Exception(
                        f"Placa {qVeiculo.placa} já registrada para o veículo "
                        + f"{MarcaRepository.findByID(qVeiculo.marca).nome} {qVeiculo.modelo}"
                    )
                marca = MarcaRepository.findByNome(veiculo["marca"])
                if not marca:
                    marca = MarcaRepository.save({"nome": veiculo["marca"]})
                veiculo["marca"] = marca
                return VeiculoRepository.save(veiculo)

            except Exception as e:
                transaction.rollback()
                return e

    @staticmethod
    def editarVeiculo(idVeiculo, veiculo):
        with db.atomic() as transaction:
            try:
                qVeiculo = VeiculoRepository.findByPlaca(veiculo["placa"])
                if qVeiculo:
                    if str(qVeiculo.idVeiculo) != str(idVeiculo):
                        raise Exception(
                            f"Placa {qVeiculo.placa} já registrada para o veículo "
                            + f"{MarcaRepository.findByID(qVeiculo.marca).nome} {qVeiculo.modelo}"
                        )
                veiculo["idVeiculo"] = idVeiculo
                marca = MarcaRepository.findByNome(veiculo["marca"])
                if not marca:
                    marca = MarcaRepository.save({"nome": veiculo["marca"]})
                veiculo["marca"] = marca
                _veiculo = VeiculoRepository.update(veiculo)
                return _veiculo
            except Exception as e:
                transaction.rollback()
                return e

    # listar todos os veiculos ou veiculos vinculados a um cliente
    @staticmethod
    def listarVeiculos(idCliente=None):
        with db.atomic() as transaction:
            try:
                _veiculos = []
                if idCliente:
                    veiculos = VeiculoClienteRepository.findVeiculosByClienteID(idCliente)
                    if veiculos:
                        for veiculo in veiculos:
                            _veiculos.append(model_to_dict(veiculo))
                        return _veiculos
                    return None
                else:
                    veiculos = VeiculoRepository.findAll()
                    if veiculos:
                        for veiculo in veiculos:
                            _veiculos.append(model_to_dict(veiculo))
                        return _veiculos
                    return None
            except Exception as e:
                transaction.rollback()
                return e

    @staticmethod
    def getVeiculo(id):
        veiculo = VeiculoRepository.findByID(id)
        if veiculo:
            return model_to_dict(veiculo)
        return None

    # buscar veiculos por uma string de alguma coluna (Ex.: marca, modelo, placa)
    @staticmethod
    def buscarVeiculo(input, limit=None, orderBy=None):
        with db.atomic() as transaction:
            try:
                _veiculos = []
                veiculos = VeiculoRepository.findByInput(input, limit, orderBy)
                if veiculos:
                    for veiculo in veiculos:
                        _veiculos.append(model_to_dict(veiculo))
                    return _veiculos
                return None
            except Exception as e:
                transaction.rollback()
                return e

    @staticmethod
    def excluirCliente(id):
        with db.atomic() as transaction:
            try:
                orcamento = OrcamentoRepository.findByClienteID(id)
                if orcamento:
                    raise Exception(
                        "Não é possível excluir este cliente, ele está vinculado à orçamento(s)."
                    )
                linesAffected = ClienteRepository.delete(id)
                return linesAffected
            except Exception as e:
                transaction.rollback()
                return e

    @staticmethod
    def excluirVeiculo(id):
        with db.atomic() as transaction:
            try:
                orcamento = OrcamentoRepository.findByVeiculoID(id)
                if orcamento:
                    raise Exception(
                        "Não é possível excluir este veículo, ele está vinculado à orçamento(s)."
                    )
                linesAffected = VeiculoRepository.delete(id)
                return linesAffected
            except Exception as e:
                transaction.rollback()
                return e

    @staticmethod
    def excluirVeiculoCliente(veiculo, cliente):
        with db.atomic() as transaction:
            try:
                veiculoCliente = VeiculoClienteRepository.findByVeiculoAndCliente(
                    veiculo, cliente
                )
                linesAffected = VeiculoClienteRepository.delete(
                    veiculoCliente.veiculo, veiculoCliente.cliente
                )
                if linesAffected != 0:
                    return True
                return False
            except Exception as e:
                transaction.rollback()
                return e
