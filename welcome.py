from PyQt6 import QtWidgets, uic, QtCore
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QHeaderView
import sys
import pyodbc

server = 'ANSABCHAUDHARY1'
database = 'NEW_SOLASTA'  
use_windows_authentication = True
username = "sa"
password = "Fall2022.dbms"

if use_windows_authentication:
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
else:
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
connection = pyodbc.connect(connection_string)

cursor = connection.cursor() 

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        uic.loadUi('Finalwelcomescreen.ui',self)
        self.show() 
        self.suppliersButton.clicked.connect(self.openSupplier)
        self.customersButton.clicked.connect(self.openCustomer)
        self.exitButton.clicked.connect(self.exitWindow)
        self.orderButton.clicked.connect(self.openOrders)
        self.itemButton.clicked.connect(self.openItems)
        self.poButton.clicked.connect(self.openPO)
       
    def openPO(self):
        import subprocess
        subprocess.Popen(['python','purchaseorder.py']) 
        
    def openSupplier(self):
        import subprocess
        subprocess.Popen(['python', 'supplierList.py']) 
    
    def openCustomer(self):
        import subprocess
        subprocess.Popen(['python', 'customer.py'])

    def exitWindow(self):
        self.close()

    def openOrders(self):
        import subprocess
        subprocess.Popen(['python','orders.py'])

    def openItems(self):
        import subprocess
        subprocess.Popen(['python','finalitems.py'])

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main() 