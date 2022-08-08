import sys
from PyQt6 import QtWidgets, QtGui, QtCore
from controller.veiculoController import VeiculoController
from model.modelo import *
from ui.telaCadastroCliente import TelaCadastroCliente
from util.buscaCEP import BuscaCEP

class ClienteController():
    def __init__(self):
        super(ClienteController, self).__init__()
        self.viewCadastro = TelaCadastroCliente()
        self.controlVeiculo = VeiculoController(self.viewCadastro)

    def salvarCliente(self, viewCadastro):
        cliente = viewCadastro.getDadosCliente()
        if not 'nome' in cliente:
            raise Exception("Campo 'Nome' obrigatório")
        if 'cidade' in cliente:
            cidade = cliente.pop('cidade')
            estado = cliente.pop('estado')
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
        
        fones = viewCadastro.getFones()
        for fone in fones:
            Fone.create(cliente=cCliente, fone=fone) #SALVA TELEFONE
        return cCliente
        
    def editarCliente(self):
        pass

    def listarClientes(self):
        pass


    def deletarCliente(self):
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

