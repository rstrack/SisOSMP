from model.modelo import ItemPeca


class ItemPecaRepository:
    @staticmethod
    def save( itemPeca: dict):
        return ItemPeca.create(**itemPeca)
    
    @staticmethod
    def update( itemPeca: dict):
        _itemPeca = ItemPeca(**itemPeca)
        _itemPeca.save()
        return _itemPeca

    @staticmethod
    def delete( id):
        return ItemPeca.delete_by_id(id)

    @staticmethod
    def findAll():
        return ItemPeca.select()

    @staticmethod
    def findByOrcamento( orcamento):
        itemPecas = ItemPeca.select().where(ItemPeca.orcamento == orcamento)
        if itemPecas:
            return itemPecas
        return None

    @staticmethod
    def findByPeca( peca):
        itemPecas = ItemPeca.select().where(ItemPeca.peca == peca)
        if itemPecas:
            return itemPecas
        return None

    @staticmethod
    def findByOrcamentoAndPeca( orcamento, peca):
        itemPeca = ItemPeca.select().where(
            (ItemPeca.orcamento == orcamento) & (ItemPeca.peca == peca)
        )
        if itemPeca:
            return itemPeca.get()
        return None
