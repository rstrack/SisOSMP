import datetime

import pymysql as sql
from peewee import *

# NOME DO BANCO DE DADOS EM QUESTÃO
NOMEBANCODEDADOS = "teste2"

db = MySQLDatabase(NOMEBANCODEDADOS, user='root', password='admin', host='localhost', port=3306)


class BaseModel(Model):
    class Meta:
        database = db


class Estado(BaseModel):
    nome = CharField(max_length=30)


class Cidade(BaseModel):
    estado = ForeignKeyField(Estado, backref='estados')
    nome = CharField(max_length=50)


class Bairro(BaseModel):
    cidade = ForeignKeyField(Cidade, backref='cidades')
    nome = CharField(max_length=50)


class Carro(BaseModel):
    marca = CharField(max_length=20)
    modelo = CharField(max_length=30)
    ano = CharField(max_length=4)
    placa = CharField(max_length=7)


class Cliente(BaseModel):
    nome = CharField(max_length=50)
    cpfj = CharField(max_length=14, null=True)
    endereco = CharField(null=True)
    bairro = ForeignKeyField(Bairro, backref='bairros', null=True)


class Carro_Cliente(BaseModel):
    carro = ForeignKeyField(Carro, backref='carros')
    cliente = ForeignKeyField(Cliente, backref='clientes')
    dataAdd = DateField(default=datetime.date)


class Peca(BaseModel):
    descricao = CharField(max_length=80)
    valor = DoubleField()


class Servico(BaseModel):
    descricao = CharField(max_length=80)
    valor = DoubleField()


class OrdemServico(BaseModel):
    data = DateField(default=datetime.date)
    aprovado = BooleanField(default=False)
    dataAprovacao = DateField()
    cliente = ForeignKeyField(Cliente, backref='clientes')
    carro = ForeignKeyField(Carro, backref='carros')


class ItemPeca(BaseModel):
    peca = ForeignKeyField(Peca, backref='pecas')
    OS = ForeignKeyField(OrdemServico, backref='ordemservicos')
    valor = DoubleField()


class ItemServico(BaseModel):
    servico = ForeignKeyField(Servico, backref='servicos')
    OS = ForeignKeyField(OrdemServico, backref='ordemservicos')
    valor = DoubleField()


class Fone(BaseModel):
    cliente = ForeignKeyField(Cliente, backref='clientes')
    fone = CharField(max_length=14)


def create_tables():
    models = BaseModel.__subclasses__()
    db.create_tables(models)


