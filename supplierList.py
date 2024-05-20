from PyQt6 import QtWidgets, uic, QtCore
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QHeaderView
import sys
import pyodbc

server = ' ANSABCHAUDHARY1'
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
        uic.loadUi('newSupplierList.ui',self)
        self.show() 
        self.supplierList.setColumnWidth(0,100)
        self.supplierList.setColumnWidth(1,150)
        self.supplierList.setColumnWidth(2,80)
        self.supplierList.setColumnWidth(3,80)
        self.supplierList.setColumnWidth(4,150)
        self.supplierList.setMinimumWidth(720)

        self.supplierInsertButton.clicked.connect(self.add_supplier)
        self.supplierDeleteButton.clicked.connect(self.delete_supplier)
        self.supplierUpdateButton.clicked.connect(self.update_table)  
        self.supplierList.itemDoubleClicked.connect(self.on_item_double_clicked)
        self.supplierSearchButton.clicked.connect(self.search_supplier)
        self.exitButton.clicked.connect(self.close_window)
        self.modified_data = {}  #Dictionary to store modified data

        self.populate_table()
        
    def close_window(self):
        self.close()
        
    def populate_table(self):
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        #sql query to fetch data
        selectSupplierQuery = "select * from supplierDetails"
        cursor.execute(selectSupplierQuery)
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.supplierList.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.supplierList.setItem(row_index, col_index, item)

        connection.close()
    
    def add_supplier(self):
        #making connection
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        #reading the inputs from the line edits
        country = self.supplierAddCountry.text()
        city = self.supplierAddCity.text()
        phone = self.supplierAddContact.text()
        email = self.supplierAddEmail.text()
        name = self.supplierAddName.text()

        #writing inserting into table using query
        insertSupplierQuery = """
        INSERT INTO supplierDetails ([supplierName], [supplierCity], [supplierCountry], [supplierEmail], [supplierNumber])
        VALUES (?,?,?,?,?)
        """

        #executing the query
        cursor.execute(insertSupplierQuery,(name,city,country,email,phone))

        #commiting the query to database
        connection.commit()

        # Clear the line edits
        self.supplierAddCountry.clear()
        self.supplierAddCity.clear()
        self.supplierAddContact.clear()
        self.supplierAddEmail.clear()
        self.supplierAddName.clear()

        self.supplierList.clearContents()
        self.supplierList.setRowCount(0)  
        QtWidgets.QMessageBox.information(self, 'Supplier Added', 'Supplier has been successfully added.', QtWidgets.QMessageBox.StandardButton.Ok)

        # Repopulate the table with the updated data
        self.populate_table()

        connection.close() 
    
    def delete_supplier(self):
        #making connection
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        selected_row = self.supplierList.currentRow() 

        if selected_row >= 0:  
            confirmation = QtWidgets.QMessageBox.question(self, 'Confirmation', 'Are you sure you want to delete this supplier?', QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
            
            if confirmation == QtWidgets.QMessageBox.StandardButton.Yes:
                supplier_id = self.supplierList.item(selected_row, 0).text()  

                delete_query = "DELETE FROM supplierDetails WHERE supplierID = ?"  

                cursor.execute(delete_query, (supplier_id,))
                connection.commit()

                self.supplierList.clearContents()
                self.supplierList.setRowCount(0) 
                QtWidgets.QMessageBox.information(self, 'Confirmation', 'Supplier has been deleted', QtWidgets.QMessageBox.StandardButton.Ok)
                self.populate_table()

        else:
            QtWidgets.QMessageBox.warning(self, 'Warning', 'Please select a row to delete.', QtWidgets.QMessageBox.StandardButton.Ok)

        connection.close() 

    def on_item_double_clicked(self, item):
        row = item.row()  
        column = item.column() 

        # Store the original value before editing for reference
        original_value = item.text()

        # Allow editing by setting the item as editable
        item.setFlags(item.flags() | QtCore.Qt.ItemFlag.ItemIsEditable)

        # Update the modified_data dictionary with the modified value
        self.modified_data.setdefault(row, {})[column] = original_value

    def update_table(self):
        for row, columns in self.modified_data.items():
            for column, value in columns.items():
                if column==0:
                    QtWidgets.QMessageBox.warning(self, 'Warning', 'You cannot update supplier ID.', QtWidgets.QMessageBox.StandardButton.Ok)
                    return
                elif column==1:
                    supplier_id = self.supplierList.item(row, 0).text()  
                    update_query = f"UPDATE supplierDetails SET [supplierName] = ? WHERE [supplierID] = ?"
                    
                elif column==2:
                    supplier_id = self.supplierList.item(row, 0).text()  
                    update_query = f"UPDATE supplierDetails SET [supplierCity] = ? WHERE [supplierID] = ?" 
                    
                elif column==3:
                    supplier_id = self.supplierList.item(row, 0).text() 
                    update_query = f"UPDATE supplierDetails SET [supplierCountry] = ? WHERE [supplierID] = ?" 
                    
                elif column==4:
                    supplier_id = self.supplierList.item(row, 0).text()  
                    update_query = f"UPDATE supplierDetails SET [supplierEmail] = ? WHERE [supplierID] = ?"  
                    
                elif column==5:
                    supplier_id = self.supplierList.item(row, 0).text()  
                    update_query = f"UPDATE supplierDetails SET [supplierNumber] = ? WHERE [supplierID] = ?"  
                
                modified_value = self.supplierList.item(row, column).text()
                cursor.execute(update_query, (modified_value, supplier_id))
                connection.commit()

        # Clear the modified_data dictionary after updating the database
        self.modified_data = {}

        # Clear the existing table data before repopulating it
        self.supplierList.clearContents()
        self.supplierList.setRowCount(0)
        QtWidgets.QMessageBox.information(self, 'Updated', 'Supplier Details have been updated', QtWidgets.QMessageBox.StandardButton.Ok)
        
        # Refresh the table to reflect the updated data
        self.populate_table()

    def search_supplier(self):
        search_criteria = self.supplierSearchCombo.currentText() 
        search_text = self.supplierSearchLine.text()  

        # Clear the existing table data before populating it with search results
        self.supplierList.clearContents()
        self.supplierList.setRowCount(0)

        if search_criteria == 'Name':
            search_query = "SELECT * FROM supplierDetails WHERE [supplierName] LIKE ?"
            cursor.execute(search_query, ('%' + search_text + '%',))
        elif search_criteria == 'SupplierID':
            search_query = "SELECT * FROM supplierDetails WHERE [supplierID] = ?"
            cursor.execute(search_query, (search_text,))

        for row_index, row_data in enumerate(cursor.fetchall()):
            self.supplierList.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.supplierList.setItem(row_index, col_index, item)



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()