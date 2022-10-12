from model.modelo import ItemPeca

class ItemPecaRepository():
    def __init__(self) -> None:
        pass

    def save(self, itemPeca: dict):
        return ItemPeca.create(**itemPeca)

    def update(self, itemPeca:dict):
        _itemPeca = ItemPeca(**itemPeca)
        _itemPeca.save()
        return _itemPeca

    def delete(self, id):
        return ItemPeca.delete_by_id(id)

    def findAll(self):
        return ItemPeca.select()
    
    def findByOrcamento(self, orcamento):
        itemPecas = ItemPeca.select().where(ItemPeca.orcamento==orcamento)
        if itemPecas:
            return itemPecas
        else: return None

    def findByPeca(self, peca):
        itemPecas = ItemPeca.select().where(ItemPeca.peca==peca)
        if itemPecas:
            return itemPecas
        else: return None

    def findByOrcamentoAndPeca(self, orcamento, peca):
        itemPeca = ItemPeca.select().where((ItemPeca.orcamento==orcamento) & (ItemPeca.peca==peca))
        if itemPeca:
            return itemPeca.get()    
        else: return None

    