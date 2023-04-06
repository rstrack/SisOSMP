from peewee import JOIN

from model.modelo import Cliente, Marca, Veiculo, Veiculo_Cliente


class VeiculoRepository:
    @staticmethod
    def save(veiculo: dict):
        return Veiculo.create(**veiculo)

    @staticmethod
    def update(veiculo: dict):
        _veiculo = Veiculo(**veiculo)
        _veiculo.save()
        return _veiculo

    @staticmethod
    def delete(id):
        return Veiculo.delete_by_id(id)

    @staticmethod
    def findAll():
        return Veiculo.select().join(Marca).order_by(Marca.nome, Veiculo.modelo)

    @staticmethod
    def findByID(id):
        return Veiculo.select().where(Veiculo.idVeiculo == id).get()

    @staticmethod
    def findByMarca(idMarca):
        veiculo = Veiculo.select().where(Veiculo.marca == idMarca)
        if veiculo:
            return veiculo
        return None

    @staticmethod
    def findByPlaca(placa):
        veiculo = Veiculo.select().where(Veiculo.placa == placa)
        if veiculo:
            return veiculo.get()
        return None

    @staticmethod
    def findByInput(input, limit=None, orderBy=None):
        match orderBy:
            case 0:
                order_by1 = Marca.nome
                order_by2 = Veiculo.modelo
            case 1:
                order_by1 = -Marca.nome
                order_by2 = -Veiculo.modelo
            case 2:
                order_by2 = Marca.nome
                order_by1 = Veiculo.modelo
            case 3:
                order_by2 = -Marca.nome
                order_by1 = -Veiculo.modelo
            case _:
                order_by1 = Marca.nome
                order_by2 = Veiculo.modelo
        veiculo = (
            Veiculo.select()
            .join(Marca, JOIN.LEFT_OUTER)
            .switch(Veiculo)
            .join(Veiculo_Cliente, JOIN.LEFT_OUTER)
            .join(Cliente, JOIN.LEFT_OUTER)
            .where(
                (Veiculo.modelo.contains(input))
                | (Veiculo.ano.contains(input))
                | (Veiculo.placa.contains(input))
                | ((Veiculo.marca == Marca.idMarca) & (Marca.nome.contains(input)))
                | (
                    (Veiculo.idVeiculo == Veiculo_Cliente.veiculo)
                    & (Veiculo_Cliente.cliente == Cliente.idCliente)
                    & (Cliente.nome.contains(input))
                )
            )
            .order_by(order_by1, order_by2)
            .limit(limit)
            .distinct()
        )
        if veiculo:
            return veiculo
        return None
