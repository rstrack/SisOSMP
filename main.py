import pymysql as sql
from controller.mainController import MainController
from model.modelo import *

driver = sql.connect(user='root', password='admin', host='localhost', port=3306)
cursor = driver.cursor()

# VERIFICA SE O BANCO DE DADOS EXISTE
if cursor.execute(f"SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '{NOMEBANCODEDADOS}'") == 0:
    cursor.execute(f"CREATE DATABASE {NOMEBANCODEDADOS}")
    cursor.execute(f"use {NOMEBANCODEDADOS}")
    create_tables(cursor)

c = MainController()
c.run()
