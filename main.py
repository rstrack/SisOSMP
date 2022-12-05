import sys
import warnings
import pymysql as sql
from PyQt6 import QtWidgets, QtGui
from app import APP
from model.modelo import DATABASE_NAME, USER, PASSWORD, PORT, create_tables

############################################################
#      ARQUIVO MAIN: INICIALIZA O BANCO E A APLICAÇÃO      #
############################################################

driver = sql.connect(user=USER, password=PASSWORD, host='localhost', port=PORT)
cursor = driver.cursor()

# VERIFICA SE O BANCO DE DADOS EXISTE
if cursor.execute(f"SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '{DATABASE_NAME}'") == 0:
    cursor.execute(f"CREATE DATABASE {DATABASE_NAME}")
    cursor.execute(f"use {DATABASE_NAME}")
    create_tables(cursor)

# IGNORA WARNING DA LIB DATEPARSER
warnings.filterwarnings(
    "ignore",
    message="The localize method is no longer necessary, as this time zone supports the fold attribute",
)

# CAPTURA ERROS SEM FECHAR O APP
def excepthook(type_, value, traceback_):
    sys.__excepthook__(type_, value, traceback_)
    msg = QtWidgets.QMessageBox()
    msg.setWindowIcon(QtGui.QIcon('resources/logo-icon.png'))
    msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
    msg.setWindowTitle("Erro")
    msg.setText('Ocorreu um erro.\nEntre em contato com o desenvolvedor')
    msg.exec()
sys.excepthook = excepthook

if __name__ == '__main__':
    c = APP()
    c.run()

