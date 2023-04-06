from dateparser import parse
from peewee import JOIN

from model.modelo import Cliente, Fone, Marca, Orcamento, Veiculo


class OrcamentoRepository:
    @staticmethod
    def save(orcamento: dict):
        return Orcamento.create(**orcamento)
    
    @staticmethod
    def update(orcamento: dict):
        _orcamento = Orcamento(**orcamento)
        _orcamento.save()
        return _orcamento

    @staticmethod
    def delete(id):
        return Orcamento.delete_by_id(id)

    @staticmethod
    def findAll(limit):
        return Orcamento.select().order_by(-Orcamento.dataOrcamento).limit(limit)

    @staticmethod
    def findByID(id):
        return Orcamento.select().where(Orcamento.idOrcamento == id).get()

    @staticmethod
    def findByClienteID(id):
        return Orcamento.select().where(Orcamento.cliente == id)

    @staticmethod
    def findByVeiculoID(id):
        return Orcamento.select().where(Orcamento.veiculo == id)

    @staticmethod
    def findByStatus(status, limit):
        return (
            Orcamento.select()
            .where(Orcamento.status == status)
            .order_by(-Orcamento.dataOrcamento)
            .limit(limit)
        )

    @staticmethod
    def findByInput(status, input: str, limit=None, orderBy=None):
        match orderBy:
            case 0:
                order_by = -Orcamento.dataOrcamento
            case 1:
                order_by = +Orcamento.dataOrcamento
            case 2:
                order_by = -Orcamento.dataAprovacao
            case 3:
                order_by = +Orcamento.dataAprovacao
            case _:
                order_by = -Orcamento.dataOrcamento
        data = parse(
            input,
            date_formats=["%d/%m/%Y", "%d/%m/%y", "%d", "%d/", "%d/%m", "%d/%m/"],
            locales=["pt-PT"],
        )
        if data:
            orcamentos = (
                Orcamento.select()
                .join(Cliente, JOIN.LEFT_OUTER)
                .join(Fone, JOIN.LEFT_OUTER)
                .switch(Orcamento)
                .join(Veiculo, JOIN.LEFT_OUTER)
                .join(Marca, JOIN.LEFT_OUTER)
                .where(
                    (Orcamento.status == status)
                    & (
                        (Orcamento.dataOrcamento == data.date())
                        | (Orcamento.dataAprovacao == data.date())
                        | (Cliente.nome.contains(input))
                        | (Cliente.documento.contains(input))
                        | (Cliente.documento.contains(input))
                        | (
                            (Cliente.idCliente == Fone.cliente)
                            & (Fone.fone.contains(input))
                        )
                        | (
                            (Veiculo.marca == Marca.idMarca)
                            & (Marca.nome.contains(input))
                        )
                        | (Veiculo.modelo.contains(input))
                        | (Veiculo.placa.contains(input))
                    )
                )
                .order_by(order_by)
                .limit(limit)
                .distinct()
            )
            if orcamentos:
                return orcamentos
            return None
        else:
            orcamentos = (
                Orcamento.select()
                .join(Cliente)
                .join(Fone)
                .switch(Orcamento)
                .join(Veiculo)
                .join(Marca)
                .where(
                    (Orcamento.status == status)
                    & (
                        (Cliente.nome.contains(input))
                        | (Cliente.documento.contains(input))
                        | (Cliente.documento.contains(input))
                        | (
                            (Cliente.idCliente == Fone.cliente)
                            & (Fone.fone.contains(input))
                        )
                        | (
                            (Veiculo.marca == Marca.idMarca)
                            & (Marca.nome.contains(input))
                        )
                        | (Veiculo.modelo.contains(input))
                        | (Veiculo.placa.contains(input))
                    )
                )
                .order_by(order_by)
                .limit(limit)
                .distinct()
            )
            if orcamentos:
                return orcamentos
            return None
