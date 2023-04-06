from playhouse.shortcuts import model_to_dict

from model.modelo import db
from repository.cidadeRepository import CidadeRepository
from repository.clienteRepository import ClienteRepository
from repository.foneRepository import FoneRepository
from repository.itemPecaRepository import ItemPecaRepository
from repository.itemServicoRepository import ItemServicoRepository
from repository.marcaRepository import MarcaRepository
from repository.orcamentoRepository import OrcamentoRepository
from repository.pecaRepository import PecaRepository
from repository.servicoRepository import ServicoRepository
from repository.veiculoClienteRepository import VeiculoClienteRepository
from repository.veiculoRepository import VeiculoRepository


class OrcamentoController:
    # salva um orçamento e dependencias caso necessário. Para maior praticidade, também atualiza campos de clientes e veiculos selecionados
    @staticmethod
    def salvarOrcamento(
                cliente: dict,
        fonesTela: list,
        clienteSel,
        veiculo: dict,
        veiculoSel,
        orcamento: dict,
        pecas: list,
        servicos: list,
    ):
        with db.atomic() as transaction:
            try:
                # cliente
                if cliente["cidade"] is not None:
                    cidade = CidadeRepository.findCidadeByNomeAndUF(
                        cliente["cidade"], cliente["uf"]
                    )
                    if cidade:
                        cliente["cidade"] = cidade
                    else:
                        cliente["cidade"] = CidadeRepository.save(
                            {"nome": cliente["cidade"], "uf": cliente["uf"]}
                        )
                if clienteSel:
                    cliente["idCliente"] = clienteSel
                    _cliente = ClienteRepository.update(cliente)
                else:
                    _cliente = ClienteRepository.save(cliente)
                # fone(s)
                fonesBanco = FoneRepository.findByClienteID(_cliente)
                if fonesBanco is not None:
                    fonesBanco = list(fonesBanco.dicts())
                    for fone in fonesBanco:
                        if not fone["fone"] in fonesTela:
                            FoneRepository.delete(_cliente, fone["fone"])
                    for fone in fonesTela:
                        if fone is not None and next(
                            (False for item in fonesBanco if item["fone"] == fone), True
                        ):
                            FoneRepository.save(_cliente, fone)
                else:
                    for fone in fonesTela:
                        FoneRepository.save(_cliente, fone)
                # marca
                marca = MarcaRepository.findByNome(veiculo["marca"])
                if marca:
                    veiculo["marca"] = marca
                else:
                    veiculo["marca"] = MarcaRepository.save({"nome": veiculo["marca"]})
                # veiculo
                if veiculoSel:
                    veiculo["idVeiculo"] = veiculoSel
                    _veiculo = VeiculoRepository.update(veiculo)
                else:
                    _veiculo = VeiculoRepository.save(veiculo)
                veiculoCliente = VeiculoClienteRepository.findByVeiculoAndCliente(
                    _veiculo, _cliente
                )
                if veiculoCliente is None:
                    VeiculoClienteRepository.save(_veiculo, _cliente)
                # orçamento
                orcamento["cliente"] = _cliente
                orcamento["veiculo"] = _veiculo
                _orcamento = OrcamentoRepository.save(orcamento)
                # itemPeça
                for peca in pecas:
                    if peca["descricao"] is not None:
                        qtde = peca.pop("qtde")
                        _peca = PecaRepository.findByDescricao(peca["descricao"])
                        _itemPeca = ItemPecaRepository.findByOrcamentoAndPeca(
                            _orcamento, _peca
                        )
                        if _itemPeca:
                            raise Exception(
                                "Use apenas uma linha para cada peça e aumente a quantidade"
                            )
                        if not _peca:
                            _peca = PecaRepository.save(peca)
                        peca["qtde"] = qtde
                        peca["peca"] = _peca
                        peca["orcamento"] = _orcamento
                        ItemPecaRepository.save(peca)
                # itemServiço
                for servico in servicos:
                    if servico["descricao"] is not None:
                        qtde = servico.pop("qtde")
                        _servico = ServicoRepository.findByDescricao(servico["descricao"])
                        _itemServico = ItemServicoRepository.findByOrcamentoAndServico(
                            _orcamento, _servico
                        )
                        if _itemServico:
                            raise Exception(
                                "Use apenas uma linha para cada serviço e aumente a quantidade"
                            )
                        if not _servico:
                            _servico = ServicoRepository.save(servico)
                        servico["qtde"] = qtde
                        servico["servico"] = _servico
                        servico["orcamento"] = _orcamento
                        ItemServicoRepository.save(servico)
                return model_to_dict(_orcamento)
            except Exception as e:
                transaction.rollback()
                return e

    # editar orçamento -> edições como data, valor das peças e servicos e valor total, adição e remoção de peças e servicos
    # edições em cliente e veículo deverão ser feitas no cadastro do orçamento ao selecionar dados ja existentes ou em telas de edição
    @staticmethod
    def editarOrcamento(id, orcamento: dict, pecas: list, servicos: list):
        with db.atomic() as transaction:
            try:
                # teste de linhas duplicadas TENTAR MELHORAR LÓGICA
                for peca in pecas:
                    for _peca in pecas:
                        if peca["descricao"] == _peca["descricao"] and pecas.index(
                            peca
                        ) != pecas.index(_peca):
                            raise Exception(
                                "Use apenas uma linha para cada peça e aumente a quantidade"
                            )
                for servico in servicos:
                    for _servico in servicos:
                        if servico["descricao"] == _servico[
                            "descricao"
                        ] and servicos.index(servico) != servicos.index(_servico):
                            raise Exception(
                                "Use apenas uma linha para cada serviço e aumente a quantidade"
                            )
                orcamento["idOrcamento"] = id
                _orcamento = OrcamentoRepository.update(orcamento)
                itemPecaBanco = ItemPecaRepository.findByOrcamento(id)
                if itemPecaBanco:
                    for itemBanco in itemPecaBanco:
                        if next(
                            (
                                False
                                for item in pecas
                                if item["descricao"]
                                == PecaRepository.findByID(itemBanco.peca).descricao
                            ),
                            True,
                        ):
                            ItemPecaRepository.delete((itemBanco.peca, _orcamento))
                for peca in pecas:
                    if peca["descricao"] is not None:
                        _peca = PecaRepository.findByDescricao(peca["descricao"])
                        if _peca:
                            _itemPeca = ItemPecaRepository.findByOrcamentoAndPeca(
                                _orcamento, _peca
                            )
                            if _itemPeca:
                                ItemPecaRepository.update(
                                    {
                                        "orcamento": _orcamento,
                                        "peca": _peca,
                                        "qtde": peca["qtde"],
                                        "valor": peca["valor"],
                                    }
                                )
                            else:
                                ItemPecaRepository.save(
                                    {
                                        "orcamento": _orcamento,
                                        "peca": _peca,
                                        "qtde": peca["qtde"],
                                        "valor": peca["valor"],
                                    }
                                )
                        else:
                            _peca = PecaRepository.save(
                                {
                                    "descricao": peca["descricao"],
                                    "un": peca["un"],
                                    "valor": peca["valor"],
                                }
                            )
                            ItemPecaRepository.save(
                                {
                                    "orcamento": _orcamento,
                                    "peca": _peca,
                                    "qtde": peca["qtde"],
                                    "valor": peca["valor"],
                                }
                            )

                itemServicoBanco = ItemServicoRepository.findByOrcamento(id)
                if itemServicoBanco:
                    for itemBanco in itemServicoBanco:
                        if next(
                            (
                                False
                                for item in servicos
                                if item["descricao"]
                                == ServicoRepository.findByID(itemBanco.servico).descricao
                            ),
                            True,
                        ):
                            ItemServicoRepository.delete((itemBanco.servico, _orcamento))
                for servico in servicos:
                    if servico["descricao"] is not None:
                        _servico = ServicoRepository.findByDescricao(servico["descricao"])
                        if _servico:
                            _itemServico = (
                                ItemServicoRepository.findByOrcamentoAndServico(
                                    _orcamento, _servico
                                )
                            )
                            if _itemServico:
                                ItemServicoRepository.update(
                                    {
                                        "orcamento": _orcamento,
                                        "servico": _servico,
                                        "qtde": servico["qtde"],
                                        "valor": servico["valor"],
                                    }
                                )
                            else:
                                ItemServicoRepository.save(
                                    {
                                        "orcamento": _orcamento,
                                        "servico": _servico,
                                        "qtde": servico["qtde"],
                                        "valor": servico["valor"],
                                    }
                                )
                        else:
                            _servico = ServicoRepository.save(
                                {
                                    "descricao": servico["descricao"],
                                    "valor": servico["valor"],
                                }
                            )
                            ItemServicoRepository.save(
                                {
                                    "orcamento": _orcamento,
                                    "servico": _servico,
                                    "qtde": servico["qtde"],
                                    "valor": servico["valor"],
                                }
                            )
                return model_to_dict(_orcamento)
            except Exception as e:
                transaction.rollback()
                return e

    @staticmethod
    def reprovarOrcamento(idOrcamento):
        with db.atomic() as transaction:
            try:
                r = OrcamentoRepository.update(
                    {"idOrcamento": idOrcamento, "status": "1"}
                )
                return r
            except Exception as e:
                transaction.rollback()
                return e

    @staticmethod
    def aprovarOrcamento(idOrcamento):
        with db.atomic() as transaction:
            try:
                r = OrcamentoRepository.update(
                    {"idOrcamento": idOrcamento, "status": "2"}
                )
                return r
            except Exception as e:
                transaction.rollback()
                return e

    @staticmethod
    def finalizarOrcamento(idOrcamento):
        with db.atomic() as transaction:
            try:
                r = OrcamentoRepository.update(
                    {"idOrcamento": idOrcamento, "status": "3"}
                )
                return r
            except Exception as e:
                transaction.rollback()
                return e

    @staticmethod
    def listarOrcamentos(status, limit=None):
        _orcamentos = []
        orcamentos = OrcamentoRepository.findByStatus(status, limit)
        if orcamentos:
            for orcamento in orcamentos:
                _orcamentos.append(model_to_dict(orcamento))
            return _orcamentos
        return None

    @staticmethod
    def getOrcamento(idOrcamento):
        orcamento = OrcamentoRepository.findByID(idOrcamento)
        if orcamento:
            return model_to_dict(orcamento)
        return None

    @staticmethod
    def listarItemPecas(idOrcamento):
        itemPecas = ItemPecaRepository.findByOrcamento(idOrcamento)
        if itemPecas:
            return itemPecas.dicts()
        return None

    @staticmethod
    def listarItemServicos(idOrcamento):
        itemServicos = ItemServicoRepository.findByOrcamento(idOrcamento)
        if itemServicos:
            return itemServicos.dicts()
        return None

    @staticmethod
    def buscarOrcamento(status, input, limit=None, orderBy: int = None):
        with db.atomic() as transaction:
            try:
                _orcamentos = []
                orcamentos = OrcamentoRepository.findByInput(
                    status, input, limit, orderBy
                )
                if orcamentos:
                    for orcamento in orcamentos:
                        _orcamentos.append(model_to_dict(orcamento))
                    return _orcamentos
                return None
            except Exception as e:
                transaction.rollback()
                return e

    @staticmethod
    def excluirOrcamento(idOrcamento):
        with db.atomic() as transaction:
            try:
                linesAffected = OrcamentoRepository.delete(idOrcamento)
                return linesAffected
            except Exception as e:
                transaction.rollback()
                return e
