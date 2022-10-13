from model.modelo import Cliente, Fone

class ClienteRepository():
    def __init__(self):
        pass

    def save(self, cliente):
        return Cliente.create(**cliente)

    def update(self, cliente:dict):
        _cliente = Cliente(**cliente)
        _cliente.save()
        return _cliente

    def delete(self, id):
        return Cliente.delete_by_id(id)

    def findAll(self, limit=None):
        return Cliente.select().order_by(Cliente.nome).limit(limit)
    
    def findByID(self, id):
        return Cliente.select().where(Cliente.idCliente==id).get()

    def findByDocumento(self, documento):
        cliente = Cliente.select().where(Cliente.documento==documento)
        if cliente:
            return cliente.get()
        else: return None

    def findByInput(self, input, limit=None):
        return Cliente.select().join(Fone).where(Cliente.nome.contains(input) | 
            (Cliente.documento.contains(input)) | (Cliente.idCliente==Fone.cliente) & 
            (Fone.fone==input)).order_by(Cliente.nome).limit(limit).distinct()

