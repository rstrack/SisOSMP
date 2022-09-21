from model.modelo import db
from controller.mainController import MainController
from model.modelo import *


# VERIFICA SE O BANCO DE DADOS EXISTE
if db.execute_sql(f"SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '{NOMEBANCODEDADOS}'") == 0:
    db.execute_sql(f"CREATE DATABASE {NOMEBANCODEDADOS}")
    db.execute_sql(f"use {NOMEBANCODEDADOS}")
    create_tables(db)

c = MainController()
c.run()
