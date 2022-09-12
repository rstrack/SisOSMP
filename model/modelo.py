import sys
from typing import Text
from peewee import *

import os
sys.path.insert(0, os.getcwd())

from util import trigger

NOMEBANCODEDADOS="dbpasetto"

SIGLAESTADOS = "'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'"

db = MySQLDatabase(NOMEBANCODEDADOS, user='root', password='admin', host='localhost', port=3306)


class BaseModel(Model):
    class Meta:
        database = db


class Estado(BaseModel):
    UF = CharField(max_length=2, constraints=[Check(f"UF in ({SIGLAESTADOS})")], primary_key=True)


class Cidade(BaseModel):
    idCidade = AutoField()
    nome = CharField(max_length=50)
    estado = ForeignKeyField(Estado, backref='estados')
    

class Marca(BaseModel):
    idMarca = AutoField()
    marca = CharField(max_length=50,null=False)


class Veiculo(BaseModel):
    idVeiculo = AutoField()
    modelo = CharField(max_length=30,null=False)
    ano = CharField(max_length=4, constraints=[Check('ano > 1900')],null=False)
    placa = CharField(max_length=7,unique=True, constraints=[Check('CHAR_LENGTH(placa)=7')],null=False)
    marca = ForeignKeyField(Marca, backref='marcas',null=False)


class Cliente(BaseModel):
    idCliente = AutoField()
    nome = CharField(max_length=80,null=False)
    cpf = CharField(max_length=11, null=True,unique=True, constraints=[Check('CHAR_LENGTH(cpf)=11')])
    cnpj = CharField(max_length=14, null=True,unique=True, constraints=[Check('CHAR_LENGTH(cnpj)=14')])
    cep = CharField(max_length=8, null=True,constraints=[Check('CHAR_LENGTH(cep)=8')])
    endereco = CharField(max_length=80,null=True)
    numero = CharField(max_length=6, null=True, constraints=[Check('numero>=0')])
    bairro = CharField(max_length=50, null=True)
    cidade = ForeignKeyField(Cidade, backref='cidades', null=True)


class Veiculo_Cliente(BaseModel):
    veiculo = ForeignKeyField(Veiculo, backref='Veiculos',null=False)
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
    veiculo = ForeignKeyField(Veiculo, backref='Veiculos',null=False)
    km = CharField(max_length=6,null=False)
    valorTotal = DoubleField(constraints=[Check('valorTotal>=0')],null=False)
    aprovado = BooleanField(constraints=[SQL('DEFAULT FALSE')])
    dataAprovacao = DateField(null=True)
    observacoes = CharField(max_length=200, null=True)


class ItemPeca(BaseModel):
    peca = ForeignKeyField(Peca, backref='pecas')
    orcamento = ForeignKeyField(Orcamento, backref='Orcamentos')
    qtde = IntegerField()
    valor = DoubleField(constraints=[Check('valor>=0')],null=False)
    class Meta:
        primary_key = CompositeKey('peca', 'orcamento')


class ItemServico(BaseModel):
    servico = ForeignKeyField(Servico, backref='servicos',null=False)
    orcamento = ForeignKeyField(Orcamento, backref='Orcamentos',null=False)
    qtde = IntegerField()
    valor = DoubleField(constraints=[Check('valor>=0')], null=False)
    class Meta:
        primary_key = CompositeKey('servico', 'orcamento')


class Fone(BaseModel):
    cliente = ForeignKeyField(Cliente, backref='clientes',null=False)
    fone = CharField(max_length=14,null=False)
    class Meta:
        primary_key = CompositeKey('cliente', 'fone')


def create_tables(cursor):
    models = BaseModel.__subclasses__()
    db.create_tables(models)
    tr1 = trigger.Trigger('orcamento', 'tr_set_data_aprovacao', 'before', 'update', 'new.aprovado=1', 'new.dataAprovacao=curdate()')
    tr1.create_trigger(cursor)
    
