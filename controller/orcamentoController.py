from PyQt6 import QtWidgets, QtGui, QtCore
from datetime import datetime
from controller.clienteController import ClienteController
from controller.pecaController import PecaController
from controller.servicoController import ServicoController
from model.modelo import *

class OrcamentoController():
    def __init__(self, view):
        super(OrcamentoController, self).__init__()
        self.view = view
        self.clienteCtrl = ClienteController(self.view)
        self.clienteSelecionado = None
        self.veiculoSelecionado = None

    def atualizarCompleters(self):
        qPecas = Peca.select()
        pecas = []
        qServicos = Servico.select()
        servicos = []
        for peca in qPecas:
            pecas.append(peca.descricao)
        modelPeca = QtCore.QStringListModel()
        modelPeca.setStringList(pecas)
        for servico in qServicos:
            servicos.append(servico.descricao)
        modelServico = QtCore.QStringListModel()
        modelServico.setStringList(servicos)
        return [modelPeca, modelServico]

    def getOrcamentos(self):
        orcamentos = Orcamento.select()
        return orcamentos

    def getClienteByID(self, id):
        return Cliente.select().where(Cliente.idCliente==id).get()

    def getVeiculoByID(self, id):
        return Veiculo.select().where(Veiculo.idVeiculo==id).get()

    def getOrcamentoByID(self, id):
        return Orcamento.select().where(Orcamento.idOrcamento==id).get()

    def getMarcas(self):
        marcas = Marca.select(Marca.marca)
        return marcas

    def getVeiculosByCliente(self, cliente):
        queryVeiculo = Veiculo.select().join(Veiculo_Cliente).join(Cliente).where((Veiculo_Cliente.cliente == cliente))
        return queryVeiculo

    def getClientesByVeiculo(self, veiculo):
        queryCliente = Cliente.select().join(Veiculo_Cliente).where(Veiculo_Cliente.veiculo==veiculo)
        return queryCliente

    def getClientes(self):
        queryCliente = Cliente.select()
        return queryCliente

    def getVeiculos(self):
        queryVeiculo = Veiculo.select()
        return queryVeiculo

    def getMarcaByID(self, id):
        querymarca = Marca.select().join(Veiculo).where(Marca.idMarca==id)
        return querymarca

    def setClienteSelecionado(self, id):
        if id == None:
            self.clienteSelecionado = None
        else:
            self.clienteSelecionado = Cliente.select().where(Cliente.idCliente==id)[0]

    def setVeiculoSelecionado(self, id):
        if id == None:
            self.veiculoSelecionado = None
        else:
            self.veiculoSelecionado = Veiculo.select().where(Veiculo.idVeiculo==id)[0]

    def getDadosCliente(self, id):
        queryCliente = Cliente.select().where(Cliente.idCliente==int(id))[0]
        if(queryCliente.cpf):
            cpf=queryCliente.cpf
            cnpj=None
        else: 
            cnpj=queryCliente.cnpj
            cpf=None
        queryCidade = Cidade.select().join(Cliente).where(queryCliente.cidade_id==Cidade.idCidade)
        if queryCidade:
            cidade=queryCidade[0].nome
            queryEstado = Estado.select().join(Cidade).where(queryCidade[0].estado_id==Estado.UF)
            if queryEstado:
                uf = queryEstado[0].UF
        else: 
            cidade = None
            uf = None
        qTel = Fone.select().where(Fone.cliente==queryCliente)
        tel=[None, None]
        for i in range(len(qTel)):
            tel[i] = qTel[i].fone
        return [queryCliente.nome, cpf, cnpj, queryCliente.cep, queryCliente.endereco, queryCliente.numero,
            queryCliente.bairro, cidade, uf, tel[0], tel[1]]

    def getValorTotal(self):
        valorTotal=0
        for _,qtde,_,valor in self.view.linhasPeca:
            if valor.text():
                if qtde.text():
                    valorTotal+=float(valor.text().replace(',','.',1))*float(qtde.text().replace(',','.',1))
                else: valorTotal+=float(valor.text().replace(',','.',1))
        for _,qtde,valor in self.view.linhasServico:
            if valor.text():
                if qtde.text():
                    valorTotal+=float(valor.text().replace(',','.',1))*float(qtde.text().replace(',','.',1))
                else: valorTotal+=float(valor.text().replace(',','.',1))
        return valorTotal

    def getDadosVeiculo(self, id):
        queryVeiculo = Veiculo.select().where(Veiculo.idVeiculo==int(id))[0]
        queryMarca = Marca.select().join(Veiculo).where(queryVeiculo.marca_id==Marca.idMarca)[0]
        return [queryMarca.marca, queryVeiculo.modelo, queryVeiculo.placa, queryVeiculo.ano]

    def buscarPeca(self, lePeca, cbUn, leValor):
        qPeca = Peca.select().where(Peca.descricao==lePeca.text())
        if qPeca:
            cbUn.setCurrentText(qPeca[0].un)
            leValor.setText(str(qPeca[0].valor).replace('.',',',1))
        self.view.setValor()

    def buscarServico(self, leServico, leValor):
        qServico = Servico.select().where(Servico.descricao==leServico.text())
        if qServico:
            leValor.setText(str(qServico[0].valor).replace('.',',',1))
        self.view.setValor()

    def salvarItemPecas(self, orcamento):
        for desc, qtde, un, valor in self.view.linhasPeca:
            if desc.text() and valor.text():
                qPeca = Peca.select().where(Peca.descricao==desc)
                if not qPeca:
                    peca = PecaController.salvarPeca(desc=desc, un=un, valor=valor)
                else: peca = qPeca[0]
                if not qtde.text():
                    _qtde = 1
                else: _qtde = qtde.text()
                ItemPeca.create(peca=peca, orcamento=orcamento, qtde=_qtde, un=un.currentText())
            elif desc.text() or valor.text():
                raise Exception("Preencha todos os campos!")

    def salvarItemServicos(self, orcamento):
        for desc, qtde, valor in self.view.linhasServico:
            if desc.text() and valor.text():
                qPeca = Peca.select().where(Peca.descricao==desc)
                if not qPeca:
                    peca = ServicoController.salvarServico(desc=desc, valor=valor)
                else: peca = qPeca[0]
                if not qtde.text():
                    _qtde = 1
                else: _qtde = qtde.text()
                ItemPeca.create(peca=peca, orcamento=orcamento, qtde=_qtde)
            elif desc.text() or valor.text():
                raise Exception("Preencha todos os campos!")

    def salvarOrcamento(self):
        with db.atomic() as transaction:
            try:
                if self.view.checkboxNovoCliente.isChecked():
                    cliente = self.clienteCtrl.salvarCliente()
                elif self.clienteSelecionado == None:
                    raise Exception("Erro: nenhum cliente selecionado! Habilite o campo 'Novo Cliente' ou selecione um cliente existente")
                else:
                    cliente = self.clienteSelecionado
                    self.clienteCtrl.editarCliente(self.clienteSelecionado)

                if self.view.checkboxNovoVeiculo.isChecked():
                    veiculo = self.clienteCtrl.salvarVeiculo()
                elif self.veiculoSelecionado == None:
                    raise Exception("Erro: nenhum veículo selecionado! Habilite o campo 'Novo Veículo' ou selecione um veículo existente")
                else:
                    veiculo = self.veiculoSelecionado
                    self.clienteCtrl.editarVeiculo(self.veiculoSelecionado)

                query = Veiculo_Cliente.select().where(Veiculo_Cliente.cliente==cliente and  Veiculo_Cliente.veiculo==veiculo)
                if not query:
                    Veiculo_Cliente.create(cliente=cliente, veiculo=veiculo)

                valorTotal = self.getValorTotal()

                data = datetime.strptime(self.view.lineEditData.text(), "%d/%m/%Y")
                data = data.strftime("%Y-%m-%d")
                orcamento = Orcamento.create(dataOrcamento=data, cliente=cliente, veiculo=veiculo,
                                km = self.view.lineEditKm.text(), valorTotal=valorTotal,
                                observacoes=self.view.textEdit.toPlainText())
                
                self.salvarItemPecas(orcamento)
                self.salvarItemServicos(orcamento)

                msg =  QtWidgets.QMessageBox()
                msg.setWindowTitle("Aviso")
                msg.setText("Dados inseridos ")
                msg.exec()
                self.getMarcas()
        
            except Exception as e:
                transaction.rollback()
                msg =  QtWidgets.QMessageBox()
                msg.setWindowTitle("Erro")
                msg.setText(str(e))
                msg.exec()
                return False

    @db.atomic
    def salvareImprimir(self):
        pass

if __name__ == "__main__":
    c = OrcamentoController()
    c.run()

