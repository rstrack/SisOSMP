import pymysql as sql

from model.modelo import *
from orcamentoController import OrcamentoController

"""
mysql://ba92f7c1b49b96:96ccbd2f@us-cdbr-east-05.cleardb.net/heroku_9dc20ebb2063eae?reconnect=true
USERNAME = 'ba92f7c1b49b96'  # Replace with your master username
PASSWORD = '96ccbd2f'  # Replace with your RDS instance password
ENDPOINT = 'us-cdbr-east-05.cleardb.net'  # Replace with your RDS endpoint
PORT = 3306   # Replace with instance port
CURSORCLASS = pymysql.cursors.DictCursor  # NO NEED to modify this
"""

'''TEMPLATE BASICO DE CRIAÇÃO COM A TABELA AUXILIAR
cliente = Cliente.create(nome='Rafael Strack', cpfj=11816405981, fone=42984089591)
marca = Marca.create(marca='Chevrolet')
carro = Veiculo.create(marca = marca, modelo='Prisma', ano=2018, km=45000, placa='BBW6969')
Veiculo_Cliente.create(veiculo=carro, cliente=cliente)
'''

driver = sql.connect(user='root', password='admin', host='localhost', port=3306)
cursor = driver.cursor()

# VERIFICA SE O BANCO DE DADOS EXISTE
if cursor.execute(f"SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '{NOMEBANCODEDADOS}'") == 0:
    cursor.execute(f"CREATE DATABASE {NOMEBANCODEDADOS}")
    cursor.execute(f"use {NOMEBANCODEDADOS}")
    create_tables(cursor)

c = OrcamentoController()
c.run()



