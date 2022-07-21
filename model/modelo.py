from codecs import charmap_build
import datetime
from email.policy import default
from operator import truediv
from pickle import TRUE

import pymysql as sql
from peewee import *

# NOME DO BANCO DE DADOS EM QUESTÃO
NOMEBANCODEDADOS = "teste"

db = MySQLDatabase(NOMEBANCODEDADOS, user='root', password='admin', host='localhost', port=3306)


class BaseModel(Model):
    class Meta:
        database = db


class Estado(BaseModel):
    UF = CharField(max_length=2)


class Cidade(BaseModel):
    nome = CharField(max_length=50)
    estado = ForeignKeyField(Estado, backref='estados')
    

class Marca(BaseModel):
    marca = CharField(max_length=50)


class Veiculo(BaseModel):
    modelo = CharField(max_length=30)
    ano = CharField(max_length=4)
    placa = CharField(max_length=7)
    marca = ForeignKeyField(Marca, backref='marcas')


class Cliente(BaseModel):
    nome = CharField(max_length=50)
    cpf = CharField(max_length=11, null=True)
    cnpj = CharField(max_length=14, null=True)
    endereco = CharField(max_length=80,null=True)
    numero = CharField(max_length=6, null=True)
    bairro = CharField(max_length=50, null=True)
    cidade = ForeignKeyField(Cidade, backref='cidades', null=True)


class Veiculo_Cliente(BaseModel):
    Veiculo = ForeignKeyField(Veiculo, backref='Veiculos')
    cliente = ForeignKeyField(Cliente, backref='clientes')
    habilitado = BooleanField(default=False)


class Peca(BaseModel):
    descricao = CharField(max_length=80)
    un = CharField(max_length=5)
    valor = DoubleField()


class Servico(BaseModel):
    descricao = CharField(max_length=80)
    valor = DoubleField()


class OrdemServico(BaseModel):
    data = DateField(default=datetime.date)
    cliente = ForeignKeyField(Cliente, backref='clientes')
    Veiculo = ForeignKeyField(Veiculo, backref='Veiculos')
    km = CharField(max_length=6)
    valorTotal = DoubleField()
    aprovado = BooleanField(default=False)
    dataAprovacao = DateField(null=True)
    dataPrevista = DateField()


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


