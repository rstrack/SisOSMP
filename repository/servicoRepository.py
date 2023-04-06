from model.modelo import Servico


class ServicoRepository:
    @staticmethod
    def save(servico: dict):
        return Servico.create(**servico)

    @staticmethod
    def update(servico: dict):
        _servico = Servico(**servico)
        _servico.save()
        return _servico

    @staticmethod
    def delete(id):
        return Servico.delete_by_id(id)

    @staticmethod
    def findAll():
        return Servico.select().order_by(Servico.descricao)

    @staticmethod
    def findByID(id):
        return Servico.select().where(Servico.idServico == id).get()

    @staticmethod
    def findByDescricao(desc):
        servico = Servico.select().where(Servico.descricao == desc)
        if servico:
            return servico.get()
        return None

    @staticmethod
    def findByInput(input, limit=None, orderBy=None):
        match orderBy:
            case 0:
                order_by = Servico.descricao
            case 1:
                order_by = -Servico.descricao
            case _:
                order_by = Servico.descricao
        _servico = (
            Servico.select()
            .where(Servico.descricao.contains(input))
            .order_by(order_by)
            .limit(limit)
            .distinct()
        )
        if _servico:
            return _servico
        return None
