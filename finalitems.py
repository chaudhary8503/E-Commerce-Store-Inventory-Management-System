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
        uic.loadUi('finalitems.ui',self)
        self.show()
        self.tableWidget.setColumnWidth(0,100)
        self.tableWidget.setColumnWidth(1,100)
        self.tableWidget.setColumnWidth(2,100)
        self.tableWidget.setColumnWidth(3,80)
        self.tableWidget.setColumnWidth(4,155)
        self.tableWidget.setMinimumWidth(600)

        self.BackButton.clicked.connect(self.close_window)
        self.InsertButton.clicked.connect(self.add_item)
        self.DeleteButton.clicked.connect(self.delete_item)
        self.UpdateButton.clicked.connect(self.update_table)  
        self.tableWidget.itemDoubleClicked.connect(self.on_item_double_clicked)
        self.SearchButton.clicked.connect(self.search_item)
        self.modified_data = {}  #Dictionary to store modified data
        self.reportsButton.clicked.connect(self.openReport)

        self.populate_table()

    def openReport(self):
        self.openReportWindow = viewReport()
        self.openReportWindow.show()

    def close_window(self):
        self.close()
        
    def populate_table(self):
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        #sql query to fetch data
        selectitemQuery = "select * from items"
        cursor.execute(selectitemQuery)
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.tableWidget.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.tableWidget.setItem(row_index, col_index, item)

        connection.close() 
    
    def add_item(self):
        #making connection
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        #reading the inputs from the line edits
        id = self.itemAddID.text()
        name = self.itemAddName.text()
        colour =  self.itemAddColour.text()
        qtyavailable = self.itemqtyAvailable.text() 
        price = self.itemAddPrice.text()
       
        #writing inserting into table using query
        insertitemQuery = """
        INSERT INTO items ([itemID],[itemName], [itemColour], [itemQtyAvailable], [pricePerUnit])
        VALUES (?,?,?,?,?)
        """

        #executing the query
        cursor.execute(insertitemQuery,(id,name,colour,qtyavailable,price))

        #commiting the query to database
        connection.commit()

        # Clear the line edits
        self.itemqtyAvailable.clear()
        self.itemAddColour.clear()
        self.itemAddPrice.clear()
        self.itemAddName.clear()
        self.itemAddID.clear()

        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)  # Reset row count
        QtWidgets.QMessageBox.information(self, 'Item Added', 'Item has been successfully added.', QtWidgets.QMessageBox.StandardButton.Ok)
        # Repopulate the table with the updated data
        self.populate_table()

        connection.close() 
    
    def delete_item(self):
    # making connection
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        selected_row = self.tableWidget.currentRow()  # Get the index of the selected row

        if selected_row >= 0:  
            confirmation = QtWidgets.QMessageBox.question(self, 'Confirmation', 'Are you sure you want to delete this row?', QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
           
            if confirmation == QtWidgets.QMessageBox.StandardButton.Yes:
                item_id = self.tableWidget.item(selected_row, 0).text()  

                delete_orders_query = "DELETE FROM itemorder WHERE itemID = ?"
                cursor.execute(delete_orders_query, (item_id,))
                connection.commit()

                delete_orders_query = "DELETE FROM purchaseItem WHERE itemID = ?"
                cursor.execute(delete_orders_query, (item_id,))
                connection.commit()

                delete_query = "DELETE FROM items WHERE itemID = ?"  

                cursor.execute(delete_query, (item_id,))
                connection.commit()

                self.tableWidget.clearContents()
                self.tableWidget.setRowCount(0)  
                QtWidgets.QMessageBox.information(self, 'Confirmation', 'Item has been deleted', QtWidgets.QMessageBox.StandardButton.Ok)

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
        selected_row = self.tableWidget.currentRow()  

        if selected_row >= 0:  
            confirmation = QtWidgets.QMessageBox.question(self, 'Confirmation', 'Are you sure you want to update this row?', QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
           
            if confirmation == QtWidgets.QMessageBox.StandardButton.Yes:
                for row, columns in self.modified_data.items():
                    for column, value in columns.items():
                        if column==0:
                            QtWidgets.QMessageBox.warning(self, 'Warning', 'You cannot update itemID.', QtWidgets.QMessageBox.StandardButton.Ok)
                            return

                        if column == 1:
                            item_id = self.tableWidget.item(row, 0).text() 
                            update_query = f"UPDATE items SET [itemName] = ? WHERE [itemID] = ?" 
                            
                        elif column == 2:
                            item_id = self.tableWidget.item(row, 0).text()  
                            update_query = f"UPDATE items SET [itemColour] = ? WHERE [itemID] = ?"  
                            
                        elif column == 3:
                            item_id = self.tableWidget.item(row, 0).text()  
                            update_query = f"UPDATE items SET [itemQtyAvailable] = ? WHERE [itemID] = ?"  
                            
                        elif column == 4:
                            item_id = self.tableWidget.item(row, 0).text()  
                            update_query = f"UPDATE items SET [pricePerUnit] = ? WHERE [itemID] = ?" 

                        modified_value = self.tableWidget.item(row, column).text()
                        cursor.execute(update_query, (modified_value, item_id))
                        connection.commit()

                # Clear the modified_data dictionary after updating the database
                self.modified_data = {}

                # Clear the existing table data before repopulating it
                self.tableWidget.clearContents()
                self.tableWidget.setRowCount(0)
                QtWidgets.QMessageBox.information(self, 'Confirmation', 'Item has been updated', QtWidgets.QMessageBox.StandardButton.Ok)
                # Refresh the table to reflect the updated data
                self.populate_table()
        else:
            QtWidgets.QMessageBox.warning(self, 'Warning', 'Please select a row to update.', QtWidgets.QMessageBox.StandardButton.Ok)

    def search_item(self):

        # Create the connection string based on the au
        search_criteria = self.comboBox.currentText() 
        search_text = self.itemSearchLine.text()  

        # Clear the existing table data before populating it with search results
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)

        if search_criteria == 'Name':
            # Perform a search based on the item name
            search_query = "SELECT * FROM Items WHERE [itemName] LIKE ?"
            cursor.execute(search_query, ('%' + search_text + '%',))
        elif search_criteria == 'ItemID':
            # Perform a search based on the item ID
            search_query = "SELECT * FROM Items WHERE [itemID] = ?"
            cursor.execute(search_query, (search_text,))

        # Fetch the search results and update the table
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.tableWidget.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.tableWidget.setItem(row_index, col_index, item)

class viewReport(QtWidgets.QMainWindow):
    def __init__(self):
        super(viewReport,self).__init__()
        uic.loadUi('itemreport.ui',self)
        self.show()
        self.openLowStock() 
        self.openTopList() 
        self.lowStockList.setColumnWidth(0,100)
        self.lowStockList.setColumnWidth(3,120)
        self.exitButton.clicked.connect(self.closeWindow)

    def closeWindow(self):
        self.close() 

    def openTopList(self):
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        # Clear existing content in orderList
        self.topSellingList.clearContents()
        self.topSellingList.setRowCount(0)

        # SQL query to fetch data
        selectOrderQuery = """
        select itemID,sum(itemQtyBought) from itemOrder group by itemID order by sum(itemQtyBought) desc
        """

        cursor.execute(selectOrderQuery)
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.topSellingList.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.topSellingList.setItem(row_index, col_index, item)

        connection.close()
 
    def openLowStock(self):
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        # Clear existing content in orderList
        self.lowStockList.clearContents()
        self.lowStockList.setRowCount(0)

        # SQL query to fetch data
        selectOrderQuery = """
        select itemID,itemName,itemColour,itemQtyAvailable from items where itemQtyAvailable<5
        """
        cursor.execute(selectOrderQuery)
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.lowStockList.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.lowStockList.setItem(row_index, col_index, item)

        connection.close()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main() 