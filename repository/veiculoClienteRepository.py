from model.modelo import Cliente, Veiculo, Veiculo_Cliente


class VeiculoClienteRepository:
    @staticmethod
    def save(veiculo: Veiculo, cliente: Cliente):
        return Veiculo_Cliente.create(veiculo=veiculo, cliente=cliente)

    @staticmethod
    def delete(veiculo, cliente):
        return Veiculo_Cliente.delete_by_id((veiculo, cliente))

    @staticmethod
    def findByVeiculoAndCliente(veiculo, cliente):
        veiculoCliente = Veiculo_Cliente.select().where(
            (Veiculo_Cliente.veiculo == veiculo) & (Veiculo_Cliente.cliente == cliente)
        )
        if veiculoCliente:
            return veiculoCliente.get()
        return None

    @staticmethod
    def findVeiculosByClienteID(idCliente):
        return (
            Veiculo.select()
            .join(Veiculo_Cliente)
            .where(Veiculo_Cliente.cliente == idCliente)
        )

    @staticmethod
    def findClientesByVeiculoID(idVeiculo):
        return (
            Cliente.select()
            .join(Veiculo_Cliente)
            .where(Veiculo_Cliente.veiculo == idVeiculo)
        )
