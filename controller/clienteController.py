from PyQt6 import QtWidgets, QtGui, QtCore
from controller.veiculoController import VeiculoController
from model.modelo import *

class ClienteController():
    def __init__(self, view):
        super(ClienteController, self).__init__()
        self.view = view

    def getMarcas(self):
        marcas = Marca.select(Marca.marca)
        return marcas

    def salvarCliente(self):
        cliente = self.view.getDadosCliente()
        estado = cliente.pop('estado')
        if not 'nome' in cliente:
            raise Exception("Campo 'Nome' obrigatório")
        if 'cidade' in cliente:
            cidade = cliente.pop('cidade')
            qEstado = Estado.select().where(Estado.UF==estado)
            if not qEstado:
                cEstado = Estado.create(UF=estado) #SALVA ESTADO
            else: cEstado = qEstado[0]
            qCidade = Cidade.select().where(Cidade.nome==cidade)
            if not qCidade:
                cCidade = Cidade.create(nome=cidade, estado=cEstado) #SALVA CIDADE
            else: cCidade = qCidade[0]
            cliente['cidade'] = cCidade
        cCliente = Cliente.create(**cliente) #SALVA CLIENTE
        fones = self.view.getFones()
        for fone in fones:
            Fone.create(cliente=cCliente, fone=fone) #SALVA TELEFONE
        return cCliente

    def salvarVeiculo(self):
        veiculo = self.view.getDadosVeiculo()
        marca = veiculo.pop('marca')
        if not 'marca':
            raise Exception("Erro: Campo 'Marca' vazio!")
        if not'modelo' in veiculo:
            raise Exception("Erro: Campo 'Modelo' vazio!")
        if not 'placa' in veiculo:
            raise Exception("Erro: Campo 'Placa' vazio!")
        qMarca = Marca.select().where(Marca.marca==marca)
        if not qMarca:
            cMarca = Marca.create(marca=marca)
        else: cMarca = qMarca[0]
        veiculo['marca'] = cMarca
        qVeiculo = Veiculo.select().where(Veiculo.placa==veiculo['placa'])
        if qVeiculo:
            raise Exception(f"Erro: placa {veiculo['placa']} já utilizada pelo veículo {cMarca.marca}{qVeiculo[0].modelo}")
        cVeiculo = Veiculo.create(**veiculo) #SALVA VEICULO
        return cVeiculo

    def salvarClienteVeiculo(self):
        with db.atomic() as transaction:
            try:
                cliente = self.view.getDadosCliente()
                estado = cliente.pop('estado')
                veiculo = self.view.getDadosVeiculo()
                marca = veiculo.pop('marca')
                if not cliente and not veiculo:
                    raise Exception("Erro: Campos Vazios!")
                if cliente:
                    if not 'nome' in cliente:
                        raise Exception("Campo 'Nome' obrigatório")
                    if 'cidade' in cliente:
                        cidade = cliente.pop('cidade')
                        qEstado = Estado.select().where(Estado.UF==estado)
                        if not qEstado:
                            cEstado = Estado.create(UF=estado) #SALVA ESTADO
                        else: cEstado = qEstado[0]
                        qCidade = Cidade.select().where(Cidade.nome==cidade)
                        if not qCidade:
                            cCidade = Cidade.create(nome=cidade, estado=cEstado) #SALVA CIDADE
                        else: cCidade = qCidade[0]
                        cliente['cidade'] = cCidade
                    cCliente = Cliente.create(**cliente) #SALVA CLIENTE
                    fones = self.view.getFones()
                    for fone in fones:
                        Fone.create(cliente=cCliente, fone=fone) #SALVA TELEFONE
                if veiculo:
                    if not 'marca' or not ('modelo' or 'placa') in veiculo:
                        raise Exception("Erro: Campo(s) Vazio(s)!")
                    qMarca = Marca.select().where(Marca.marca==marca)
                    if not qMarca:
                        cMarca = Marca.create(marca=marca)
                    else: cMarca = qMarca[0]
                    veiculo['marca'] = cMarca
                    qVeiculo = Veiculo.select().where(Veiculo.placa==veiculo['placa'])
                    if not qVeiculo:
                        cVeiculo = Veiculo.create(**veiculo) #SALVA VEICULO
                        if cliente:
                            Veiculo_Cliente.create(cliente=cCliente, veiculo=cVeiculo) #SALVA VEICULO_CLIENTE
                    elif cliente:
                        msgBox = QtWidgets.QMessageBox()
                        msgBox.setWindowTitle("Aviso")
                        msgBox.setText(f"Veículo {qVeiculo[0].modelo} placa {qVeiculo[0].placa} já está cadastrado. Deseja vincular ao cliente {cliente['nome']}?")
                        y = msgBox.addButton("Sim", QtWidgets.QMessageBox.ButtonRole.YesRole)
                        n = msgBox.addButton("Não", QtWidgets.QMessageBox.ButtonRole.NoRole)
                        c = msgBox.addButton("Cancelar", QtWidgets.QMessageBox.ButtonRole.RejectRole)
                        y.setFixedWidth(60)
                        n.setFixedWidth(60)
                        c.setFixedWidth(100)
                        msgBox.exec()
                        if msgBox.clickedButton()==y:
                            Veiculo_Cliente.create(cliente=cCliente, veiculo=qVeiculo[0]) #SALVA VEICULO_CLIENTE
                        if msgBox.clickedButton()==c:
                            raise Exception("Cadastro cancelado")

                    else: raise Exception(f"Veículo {qVeiculo[0].modelo} placa {qVeiculo[0].placa} já cadastrado!")
                msg =  QtWidgets.QMessageBox()
                msg.setWindowTitle("Aviso")
                msg.setText("Dados inseridos!")
                msg.exec()
            except Exception as e:
                transaction.rollback()
                msg =  QtWidgets.QMessageBox()
                msg.setWindowTitle("Erro")
                msg.setText(str(e))
                msg.exec()
                return False

    def editarCliente(self, _cliente):
        clienteOld = Cliente.select().where(Cliente.idCliente==_cliente.idCliente).get()
        cliente = self.view.getDadosCliente()
        estado = cliente.pop('estado')
        if not 'nome' in cliente:
            raise Exception("Campo 'Nome' obrigatório")
        if 'cidade' in cliente:
            cidade = cliente.pop('cidade')
            qEstado = Estado.select().where(Estado.UF==estado)
            if not qEstado:
                cEstado = Estado.create(UF=estado) #SALVA ESTADO
            else: cEstado = qEstado[0]
            qCidade = Cidade.select().where(Cidade.nome==cidade)
            if not qCidade:
                cCidade = Cidade.create(nome=cidade, estado=cEstado) #SALVA CIDADE
            else: cCidade = qCidade[0]
            cliente['cidade'] = cCidade
        if 'nome' in cliente: clienteOld.nome = cliente['nome']
        if 'cep' in cliente: clienteOld.cep = cliente['cep']
        if 'endereco' in cliente: clienteOld.endereco = cliente['endereco']
        if 'numero' in cliente: clienteOld.numero = cliente['numero']
        if 'bairro' in cliente: clienteOld.bairro = cliente['bairro']
        if 'cidade' in cliente: clienteOld.cidade = cliente['cidade']
        if 'cpf' in cliente: clienteOld.cpf = cliente['cpf']
        if 'cnpj' in cliente: clienteOld.cnpj = cliente['cnpj']
        clienteOld.save()
        ############### LIDAR COM TELEFONE


    def editarVeiculo(self, _veiculo):
        veiculo = self.view.getDadosVeiculo()
        marca = veiculo.pop('marca')
        qMarca = Marca.select().where(Marca.marca==marca)
        if not qMarca:
            cMarca = Marca.create(marca=marca)
        else: cMarca = qMarca[0]
        veiculo['marca'] = cMarca
        Veiculo.update(**veiculo).where(Veiculo.idVeiculo==_veiculo.idVeiculo).execute() #SALVA VEICULO

    def listarClientes(self):
        pass


    def deletarCliente(self):
        pass

    def editarveiculo(self, ):
        pass

    def _salvarCliente(self):
        with db.atomic() as transaction:
            try:
                cliente = self.salvarCliente()
                veiculo = self.controlVeiculo.salvarVeiculo()
                query = Veiculo_Cliente.select().where(cliente==cliente and veiculo==veiculo)
                if not query:
                    Veiculo_Cliente.create(cliente=cliente, veiculo=veiculo)
                msg =  QtWidgets.QMessageBox()
                msg.setWindowTitle("Aviso")
                msg.setText("Dados inseridos ")
                msg.exec()
                self.limparCampos()

            except Exception as e:
                transaction.rollback()
                msg =  QtWidgets.QMessageBox()
                msg.setWindowTitle("Erro")
                msg.setText(str(e))
                msg.exec()

    def limparCampos(self):
        pass