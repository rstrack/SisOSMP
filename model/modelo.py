import sys
from peewee import *
from util import trigger
import os
sys.path.insert(0, os.getcwd())

NOMEBANCODEDADOS="dbpasetto"

SIGLAESTADOS = "'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'"

db = MySQLDatabase(NOMEBANCODEDADOS, user='root', password='admin', host='localhost', port=3306)


class BaseModel(Model):
    class Meta:
        database = db


class Cidade(BaseModel):
    idCidade = AutoField()
    nome = CharField(max_length=50, null=False)
    uf = CharField(max_length=2, null=False, constraints=[Check(f"UF in ({SIGLAESTADOS})")])
    

class Marca(BaseModel):
    idMarca = AutoField()
    nome = CharField(max_length=50,null=False)


class Veiculo(BaseModel):
    idVeiculo = AutoField()
    modelo = CharField(max_length=30,null=False)
    ano = CharField(max_length=4, constraints=[Check('ano > 1900')],null=True)
    placa = CharField(max_length=7,unique=True, constraints=[Check('CHAR_LENGTH(placa)=7')],null=False)
    marca = ForeignKeyField(Marca, backref='marcas',null=False)


class Cliente(BaseModel):
    idCliente = AutoField()
    nome = CharField(max_length=80,null=False)
    tipo = CharField(max_length=1, null=False, constraints=[Check("tipo in ('0','1','2')")])
    documento = CharField(max_length=14, null=True,unique=True)
    cep = CharField(max_length=8, null=True,constraints=[Check('CHAR_LENGTH(cep)=8')])
    endereco = CharField(max_length=80,null=True)
    numero = CharField(max_length=6, null=True, constraints=[Check('numero>=0')])
    bairro = CharField(max_length=50, null=True)
    cidade = ForeignKeyField(Cidade, backref='cidades', null=True)
    class Meta:
        constraints = \
        [Check("CHAR_LENGTH(documento)=11 and tipo='0' or CHAR_LENGTH(documento)=14 and tipo='1' or tipo='2'")]


class Veiculo_Cliente(BaseModel):
    veiculo = ForeignKeyField(Veiculo, backref='veiculos',null=False)
    cliente = ForeignKeyField(Cliente, backref='clientes',null=False)
    habilitado = BooleanField(constraints=[SQL('DEFAULT TRUE')])
    class Meta:
        primary_key = CompositeKey('veiculo', 'cliente')


class Peca(BaseModel):
    idPeca = AutoField()
    descricao = CharField(max_length=80,null=False)
    un = CharField(max_length=5,null=False)
    valor = DoubleField(constraints=[Check('valor>=0')],null=False)


class Servico(BaseModel):
    idServico = AutoField()
    descricao = CharField(max_length=80,null=False)
    valor = DoubleField(constraints=[Check('valor>=0')],null=False)


class Orcamento(BaseModel):
    idOrcamento = AutoField()
    dataOrcamento = DateField(constraints=[SQL('DEFAULT (CURRENT_DATE)')], null=False)
    cliente = ForeignKeyField(Cliente, backref='clientes',null=False)
    veiculo = ForeignKeyField(Veiculo, backref='veiculos',null=False)
    km = CharField(max_length=6,null=False)
    valorTotal = DoubleField(constraints=[Check('valorTotal>=0')],null=False)
    aprovado = BooleanField(constraints=[SQL('DEFAULT FALSE')])
    dataAprovacao = DateField(null=True)
    observacoes = CharField(max_length=200, null=True)


class ItemPeca(BaseModel):
    peca = ForeignKeyField(Peca, backref='pecas')
    orcamento = ForeignKeyField(Orcamento, backref='orcamentos')
    qtde = IntegerField()
    valor = DoubleField(constraints=[Check('valor>=0')],null=False)
    class Meta:
        primary_key = CompositeKey('peca', 'orcamento')


class ItemServico(BaseModel):
    servico = ForeignKeyField(Servico, backref='servicos',null=False)
    orcamento = ForeignKeyField(Orcamento, backref='orcamentos',null=False)
    qtde = IntegerField()
    valor = DoubleField(constraints=[Check('valor>=0')], null=False)
    class Meta:
        primary_key = CompositeKey('servico', 'orcamento')


class Fone(BaseModel):
    cliente = ForeignKeyField(Cliente, backref='clientes',null=False)
    fone = CharField(max_length=14,null=False, unique=True)
    class Meta:
        primary_key = CompositeKey('cliente', 'fone')


def create_tables(cursor):
    models = BaseModel.__subclasses__()
    db.create_tables(models)
    tr1 = trigger.Trigger('orcamento', 'tr_set_data_aprovacao', 'before', 'update', 'new.aprovado=1', 'new.dataAprovacao=curdate()')
    tr1.create_trigger(cursor)
    
