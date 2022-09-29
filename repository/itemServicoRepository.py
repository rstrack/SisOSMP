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

    def findByOrcamento(self, orcamento):
        itemServicos = ItemServico.select().where(ItemServico.orcamento==orcamento)
        if itemServicos:
            return itemServicos
        else: return None

    def findByOrcamentoAndServico(self, orcamento, servico):
        _itemServico = ItemServico.select().where((ItemServico.orcamento==orcamento) & (ItemServico.servico==servico))
        if _itemServico:
            return _itemServico.get()
        else: return None