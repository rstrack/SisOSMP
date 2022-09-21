from model.modelo import ItemServico, Orcamento, Servico

class ItemServicoRepository():
    def __init__(self) -> None:
        pass

    def save(self, itemServico: dict):
        return ItemServico.create(**itemServico)

    def update(self, itemServico:dict):
        _itemServico = ItemServico(**itemServico)
        _itemServico.save()
        return _itemServico

    def delete(self, id):
        return ItemServico.delete_by_id(id)

    def findAll(self):
        return ItemServico.select()


    #Analisar finds necessarios
    def findByOrcamentoID(self, id):
        return ItemServico.select().where()