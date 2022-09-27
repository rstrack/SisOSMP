from model.modelo import ItemPeca, Orcamento, Peca

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

    def findByOrcamentoAndPeca(self, orcamento, peca):
        return ItemPeca.select().where((ItemPeca.orcamento==orcamento) & (ItemPeca.peca==peca)).get()

    