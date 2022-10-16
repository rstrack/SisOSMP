from model.modelo import Cliente, Marca, Veiculo, Veiculo_Cliente

class VeiculoRepository():
    def __init__(self):
        pass

    def save(self, veiculo:dict):
        return Veiculo.create(**veiculo)

    def update(self, veiculo:dict):
        _veiculo = Veiculo(**veiculo)
        _veiculo.save()
        return _veiculo

    def delete(self, id):
        return Veiculo.delete_by_id(id)

    def findAll(self):
        return Veiculo.select().join(Marca).order_by(Marca.nome, Veiculo.modelo)

    def findByID(self, id):
        return Veiculo.select().where(Veiculo.idVeiculo==id).get()

    def findByMarca(self, idMarca):
        veiculo = Veiculo.select().where(Veiculo.marca==idMarca)
        if veiculo:
            return veiculo
        else: return None

    def findByPlaca(self, placa):
        veiculo = Veiculo.select().where(Veiculo.placa==placa)
        if veiculo:
            return veiculo.get()
        else: return None

    def findByInput(self, input, limit=None):
        veiculo = Veiculo.select().join(Marca).switch(Veiculo).join(Veiculo_Cliente).join(Cliente).where(
            (Veiculo.modelo.contains(input))
            |(Veiculo.ano.contains(input))
            |(Veiculo.placa.contains(input))
            |((Veiculo.marca==Marca.idMarca)&(Marca.nome.contains(input)))
            |((Veiculo.idVeiculo==Veiculo_Cliente.veiculo)&(Veiculo_Cliente.cliente==Cliente.idCliente)&(Cliente.nome.contains(input)))
            ).order_by(Marca.nome, Veiculo.modelo)\
            .limit(limit)\
            .distinct()
        if veiculo:
            return veiculo
        else: 
            return None