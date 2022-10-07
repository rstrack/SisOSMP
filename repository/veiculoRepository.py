from model.modelo import Veiculo

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
        return Veiculo.select()

    def findByID(self, id):
        return Veiculo.select().where(Veiculo.idVeiculo==id).get()

    def findByPlaca(self, placa):
        veiculo = Veiculo.select().where(Veiculo.placa==placa)
        if veiculo:
            return veiculo.get()
        else: return None

    
