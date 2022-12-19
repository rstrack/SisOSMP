from model.modelo import Cliente, Veiculo, Veiculo_Cliente


class VeiculoClienteRepository:
    def __init__(self) -> None:
        pass

    # Salva a relação many to many a partir dos modelos
    def save(self, veiculo: Veiculo, cliente: Cliente):
        return Veiculo_Cliente.create(veiculo=veiculo, cliente=cliente)

    def delete(self, veiculo, cliente):
        return Veiculo_Cliente.delete_by_id((veiculo, cliente))

    def findByVeiculoAndCliente(self, veiculo, cliente):
        veiculoCliente = Veiculo_Cliente.select().where(
            (Veiculo_Cliente.veiculo == veiculo) & (Veiculo_Cliente.cliente == cliente)
        )
        if veiculoCliente:
            return veiculoCliente.get()
        return None

    def findVeiculosByClienteID(self, idCliente):
        return (
            Veiculo.select()
            .join(Veiculo_Cliente)
            .where(Veiculo_Cliente.cliente == idCliente)
        )

    def findClientesByVeiculoID(self, idVeiculo):
        return (
            Cliente.select()
            .join(Veiculo_Cliente)
            .where(Veiculo_Cliente.veiculo == idVeiculo)
        )
