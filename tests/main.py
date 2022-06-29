from menu_copy import *
from control import *
import sys

driver = sql.connect(user='root', password='admin', host='localhost', port=3306)
cursor = driver.cursor()

# VERIFICA SE O BANCO DE DADOS EXISTE
if cursor.execute(f"SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '{NOMEBANCODEDADOS}'") == 0:
    cursor.execute(f"CREATE DATABASE {NOMEBANCODEDADOS}")
    create_tables()

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
ui.stackedWidget.setCurrentIndex(0)
MainWindow.show()
sys.exit(app.exec())