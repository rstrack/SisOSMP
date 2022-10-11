from model.modelo import  db
from playhouse.shortcuts import model_to_dict
from repository.cidadeRepository import CidadeRepository
from repository.foneRepository import FoneRepository
from repository.itemPecaRepository import ItemPecaRepository
from repository.itemServicoRepository import ItemServicoRepository
from repository.orcamentoRepository import OrcamentoRepository
from repository.clienteRepository import ClienteRepository
from repository.pecaRepository import PecaRepository
from repository.servicoRepository import ServicoRepository
from repository.veiculoRepository import VeiculoRepository
from repository.veiculoClienteRepository import VeiculoClienteRepository
from repository.marcaRepository import MarcaRepository

class OrcamentoController():
    def __init__(self):
        super(OrcamentoController, self).__init__()
        self.orcamentoRep = OrcamentoRepository()
        self.cidadeRep = CidadeRepository()
        self.clienteRep = ClienteRepository()
        self.foneRep = FoneRepository()
        self.marcaRep = MarcaRepository()
        self.veiculoRep = VeiculoRepository()
        self.veiculoClienteRep = VeiculoClienteRepository()
        self.pecaRep = PecaRepository()
        self.itemPecaRep = ItemPecaRepository()
        self.servicoRep = ServicoRepository()
        self.itemServicoRep = ItemServicoRepository()

    #salva um orçamento e dependencias caso necessário. Para maior praticidade, também atualiza campos de clientes e veiculos selecionados
    def salvarOrcamento(self, cliente:dict, fonesTela:list, clienteSel, veiculo:dict, veiculoSel, orcamento:dict, pecas:list, servicos:list):
        with db.atomic() as transaction:
            try:
                #cliente
                if cliente['cidade'] != None:
                    cidade = self.cidadeRep.findCidadeByNomeAndUF(cliente['cidade'], cliente['uf'])
                    if cidade: cliente['cidade'] = cidade
                    else: cliente['cidade'] = self.cidadeRep.save({'nome':cliente['cidade'], 'uf':cliente['uf']})
                if clienteSel:
                    cliente['idCliente'] = clienteSel
                    _cliente = self.clienteRep.update(cliente)
                else: _cliente = self.clienteRep.save(cliente)
                #fone(s)
                fonesBanco = self.foneRep.findByClienteID(_cliente)
                if fonesBanco != None:
                    fonesBanco = list(fonesBanco.dicts())
                    for fone in fonesBanco:
                        if not fone['fone'] in fonesTela:
                            self.foneRep.delete(_cliente, fone['fone'])
                    for fone in fonesTela:
                        if fone != None and next((False for item in fonesBanco if item['fone']==fone), True):
                            self.foneRep.save(_cliente, fone)
                else:
                    for fone in fonesTela:
                        self.foneRep.save(_cliente, fone)
                #marca
                marca = self.marcaRep.findByNome(veiculo['marca'])
                if marca:
                    veiculo['marca'] = marca
                else: veiculo['marca'] = self.marcaRep.save({'nome':veiculo['marca']})
                #veiculo
                if veiculoSel:
                    veiculo['idVeiculo'] = veiculoSel
                    _veiculo = self.veiculoRep.update(veiculo)
                else: 
                    _veiculo = self.veiculoRep.save(veiculo)
                veiculoCliente = self.veiculoClienteRep.findByVeiculoAndCliente(_veiculo, _cliente)
                if veiculoCliente == None:
                    self.veiculoClienteRep.save(_veiculo, _cliente)
                #orçamento
                orcamento['cliente'] = _cliente
                orcamento['veiculo'] = _veiculo
                _orcamento = self.orcamentoRep.save(orcamento)
                #itemPeça
                for peca in pecas:
                    if peca['descricao'] != None:
                        qtde = peca.pop('qtde')
                        _peca = self.pecaRep.findByDescricao(peca['descricao'])
                        _itemPeca = self.itemPecaRep.findByOrcamentoAndPeca(_orcamento, _peca)
                        if _itemPeca:
                            raise Exception('Use apenas uma linha para cada peça e aumente a quantidade')
                        if not _peca:
                            _peca = self.pecaRep.save(peca)
                        peca['qtde'] = qtde
                        peca['peca'] = _peca
                        peca['orcamento'] = _orcamento
                        self.itemPecaRep.save(peca)
                #itemServiço
                for servico in servicos:
                    if servico['descricao'] != None:
                        qtde = servico.pop('qtde')
                        _servico = self.servicoRep.findByDescricao(servico['descricao'])
                        _itemServico = self.itemServicoRep.findByOrcamentoAndServico(_orcamento, _servico)
                        if _itemServico:
                            raise Exception('Use apenas uma linha para cada serviço e aumente a quantidade')
                        if not _servico:
                            _servico = self.servicoRep.save(servico)
                        servico['qtde'] = qtde
                        servico['servico'] = _servico
                        servico['orcamento'] = _orcamento
                        self.itemServicoRep.save(servico)
                return model_to_dict(_orcamento)
            except Exception as e:
                transaction.rollback()
                return e
            
    #editar orçamento -> edições como data, valor das peças e servicos e valor total, adição e remoção de peças e servicos
    #edições em cliente e veículo deverão ser feitas no cadastro do orçamento ao selecionar dados ja existentes ou em telas de edição
    def editarOrcamento(self, id, orcamento:dict, pecas:list, servicos:list):
        with db.atomic() as transaction:
            try:
                #teste de linhas duplicadas TENTAR MELHORAR LÓGICA
                for peca in pecas:
                    for _peca in pecas:
                        if peca['descricao']==_peca['descricao'] and pecas.index(peca) != pecas.index(_peca):
                            raise Exception('Use apenas uma linha para cada peça e aumente a quantidade')
                for servico in servicos:
                    for _servico in servicos:
                        if servico['descricao']==_servico['descricao'] and servicos.index(servico) != servicos.index(_servico):
                            raise Exception('Use apenas uma linha para cada serviço e aumente a quantidade')
                orcamento['idOrcamento'] = id
                _orcamento = self.orcamentoRep.update(orcamento)
                itemPecaBanco = self.itemPecaRep.findByOrcamento(id)
                if itemPecaBanco:
                    for itemBanco in itemPecaBanco:
                        if next((False for item in pecas if item['descricao']==self.pecaRep.findByID(itemBanco.peca).descricao), True):
                            self.itemPecaRep.delete((itemBanco.peca, _orcamento))
                for peca in pecas:
                    if peca['descricao'] != None:
                        _peca = self.pecaRep.findByDescricao(peca['descricao'])
                        if _peca:
                            _itemPeca = self.itemPecaRep.findByOrcamentoAndPeca(_orcamento, _peca)
                            if _itemPeca:
                                self.itemPecaRep.update({'orcamento':_orcamento, 'peca': _peca, 'qtde':peca['qtde'], 'valor': peca['valor']})
                            else:
                                self.itemPecaRep.save({'orcamento':_orcamento, 'peca': _peca, 'qtde':peca['qtde'], 'valor': peca['valor']})
                        else:
                            _peca = self.pecaRep.save({'descricao': peca['descricao'], 'un': peca['un'], 'valor':peca['valor']})
                            self.itemPecaRep.save({'orcamento':_orcamento, 'peca': _peca, 'qtde':peca['qtde'], 'valor': peca['valor']})
                
                itemServicoBanco = self.itemServicoRep.findByOrcamento(id)
                if itemServicoBanco:
                    for itemBanco in itemServicoBanco:
                        if next((False for item in servicos if item['descricao']==self.servicoRep.findByID(itemBanco.servico).descricao), True):
                            self.itemServicoRep.delete((itemBanco.servico, _orcamento))
                for servico in servicos:
                    if servico['descricao'] != None:
                        _servico = self.servicoRep.findByDescricao(servico['descricao'])
                        if _servico:
                            _itemServico = self.itemServicoRep.findByOrcamentoAndServico(_orcamento, _servico)
                            if _itemServico:
                                self.itemServicoRep.update({'orcamento':_orcamento, 'servico': _servico, 'qtde':servico['qtde'], 'valor': servico['valor']})
                            else:
                                self.itemServicoRep.save({'orcamento':_orcamento, 'servico': _servico, 'qtde':servico['qtde'], 'valor': servico['valor']})
                        else:
                            _servico = self.servicoRep.save({'descricao': servico['descricao'], 'valor':servico['valor']})
                            self.itemServicoRep.save({'orcamento':_orcamento, 'servico': _servico, 'qtde':servico['qtde'], 'valor': servico['valor']})
            
            except Exception as e:
                transaction.rollback()
                return e
    
    def aprovarOrcamento(self, idOrcamento):
        with db.atomic() as transaction:
            try:
                r = self.orcamentoRep.update({'idOrcamento':idOrcamento, 'aprovado': True})
                return r
            except Exception as e:
                transaction.rollback()
                return e

    def listarOrcamentos(self, aprovado, limit=None):
        _orcamentos = []
        orcamentos = self.orcamentoRep.findByAprovado(aprovado, limit)
        if orcamentos:
            for orcamento in orcamentos:
                _orcamentos.append(model_to_dict(orcamento))
            return _orcamentos
        else: return None

    def getOrcamento(self, idOrcamento):
        orcamento = self.orcamentoRep.findByID(idOrcamento)
        if orcamento:
            return model_to_dict(orcamento)
        else: return None

    def listarItemPecas(self, idOrcamento):
        itemPecas = self.itemPecaRep.findByOrcamento(idOrcamento)
        if itemPecas: return itemPecas.dicts()
        else: return None

    def listarItemServicos(self, idOrcamento):
        itemServicos = self.itemServicoRep.findByOrcamento(idOrcamento)
        if itemServicos: return itemServicos.dicts()
        else: return None

    def excluirOrcamento(self, idOrcamento):
        with db.atomic() as transaction:
            try:
                linesAffected = self.orcamentoRep.delete(idOrcamento)
                if linesAffected != 0:
                    return True
                else: return False
            except Exception as e:
                transaction.rollback()
                return e
