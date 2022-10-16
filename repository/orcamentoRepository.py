from dateparser import parse
from model.modelo import Cliente, Fone, Marca, Orcamento, Veiculo

class OrcamentoRepository():
    def __init__(self):
        pass

    def save(self, orcamento:dict):
        return Orcamento.create(**orcamento)

    def update(self, orcamento:dict):
        _orcamento = Orcamento(**orcamento)
        _orcamento.save()
        return _orcamento

    def delete(self, id):
        return Orcamento.delete_by_id(id)

    def findAll(self, limit):
        return Orcamento.select().order_by(-Orcamento.dataOrcamento).limit(limit)

    def findByID(self, id):
        return Orcamento.select().where(Orcamento.idOrcamento==id).get()
    
    def findByClienteID(self, id):
        return Orcamento.select().where(Orcamento.cliente==id)

    def findByVeiculoID(self, id):
        return Orcamento.select().where(Orcamento.veiculo==id)

    def findByAprovado(self, aprovado, limit):
        return Orcamento.select().where(Orcamento.aprovado==aprovado).order_by(-Orcamento.dataOrcamento).limit(limit)
    
    def findByInput(self, aprovado, input:str, limit=None):
        data = parse(input, date_formats=['%d/%m/%Y', '%d/%m/%y', '%d','%d/', '%d/%m', '%d/%m/'], locales=['pt-PT'])
        if data: 
            orcamentos = Orcamento.select()\
                        .join(Cliente)\
                        .join(Fone)\
                        .switch(Orcamento)\
                        .join(Veiculo)\
                        .join(Marca)\
                        .where((Orcamento.aprovado==aprovado)
                            &((Orcamento.dataOrcamento==data.date())
                            |(Orcamento.dataAprovacao==data.date())
                            |(Cliente.nome.contains(input))
                            |(Cliente.documento.contains(input))
                            |(Cliente.documento.contains(input))
                            |((Cliente.idCliente==Fone.cliente) & (Fone.fone.contains(input)))
                            |((Veiculo.marca==Marca.idMarca) & (Marca.nome.contains(input)))
                            |(Veiculo.modelo.contains(input))
                            |(Veiculo.placa.contains(input)))
                        ).order_by(-Orcamento.dataOrcamento)\
                        .limit(limit)\
                        .distinct()
            if orcamentos:
                return orcamentos
            else: return None
        else:
            orcamentos = Orcamento.select()\
                        .join(Cliente)\
                        .join(Fone)\
                        .switch(Orcamento)\
                        .join(Veiculo)\
                        .join(Marca)\
                        .where((Orcamento.aprovado==aprovado)
                            &((Cliente.nome.contains(input))
                            |(Cliente.documento.contains(input))
                            |(Cliente.documento.contains(input))
                            |((Cliente.idCliente==Fone.cliente) & (Fone.fone.contains(input)))
                            |((Veiculo.marca==Marca.idMarca) & (Marca.nome.contains(input)))
                            |(Veiculo.modelo.contains(input))
                            |(Veiculo.placa.contains(input)))
                        ).order_by(-Orcamento.dataOrcamento)\
                        .limit(limit)\
                        .distinct()
            if orcamentos:
                return orcamentos
            else: return None
    