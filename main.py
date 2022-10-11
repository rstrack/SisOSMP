import pymysql as sql
from controller.mainController import MainController
from model.modelo import *
import sys
from PyQt6 import QtWidgets, QtGui

driver = sql.connect(user='root', password='admin', host='localhost', port=3306)
cursor = driver.cursor()

# VERIFICA SE O BANCO DE DADOS EXISTE
if cursor.execute(f"SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '{NOMEBANCODEDADOS}'") == 0:
    cursor.execute(f"CREATE DATABASE {NOMEBANCODEDADOS}")
    cursor.execute(f"use {NOMEBANCODEDADOS}")
    create_tables(cursor)

def excepthook(type_, value, traceback_):
    sys.__excepthook__(type_, value, traceback_)
    msg = QtWidgets.QMessageBox()
    msg.setWindowIcon(QtGui.QIcon('./resources/logo-icon.png'))
    msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
    msg.setWindowTitle("Erro")
    msg.setText('Ocorreu um erro.\nEntre em contato com o desenvolvedor')
    msg.exec()
sys.excepthook = excepthook

c = MainController()
c.run()
