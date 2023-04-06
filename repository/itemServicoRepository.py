from model.modelo import ItemServico


class ItemServicoRepository:
    @staticmethod
    def save(itemServico: dict):
        return ItemServico.create(**itemServico)

    @staticmethod
    def update(itemServico: dict):
        _itemServico = ItemServico(**itemServico)
        _itemServico.save()
        return _itemServico

    @staticmethod
    def delete(id):
        return ItemServico.delete_by_id(id)

    @staticmethod
    def findAll():
        return ItemServico.select()

    @staticmethod
    def findByOrcamento(orcamento):
        itemServicos = ItemServico.select().where(ItemServico.orcamento == orcamento)
        if itemServicos:
            return itemServicos
        return None

    @staticmethod
    def findByServico(servico):
        itemServicos = ItemServico.select().where(ItemServico.servico == servico)
        if itemServicos:
            return itemServicos
        return None

    @staticmethod
    def findByOrcamentoAndServico(orcamento, servico):
        _itemServico = ItemServico.select().where(
            (ItemServico.orcamento == orcamento) & (ItemServico.servico == servico)
        )
        if _itemServico:
            return _itemServico.get()
        return None
