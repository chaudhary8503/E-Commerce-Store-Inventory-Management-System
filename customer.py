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
        uic.loadUi('Customers.ui',self)
        self.show()
        self.tableWidget.setColumnWidth(0,100)
        self.tableWidget.setColumnWidth(1,100)
        self.tableWidget.setColumnWidth(2,100)
        self.tableWidget.setColumnWidth(3,100)
        self.tableWidget.setColumnWidth(4,155)
        self.tableWidget.setMinimumWidth(600) 

        self.BackButton.clicked.connect(self.close_window)
        self.InsertButton.clicked.connect(self.add_customer)
        self.DeleteButton.clicked.connect(self.delete_customer)
        self.UpdateButton.clicked.connect(self.update_table)  
        self.tableWidget.itemDoubleClicked.connect(self.on_item_double_clicked)
        self.SearchButton.clicked.connect(self.search_customer)
        self.modified_data = {}  #Dictionary for storing modified data
        self.reportButton.clicked.connect(self.open_report)

        self.populate_table()

    def open_report(self):
        self.open_report_window = reports()
        self.open_report_window.show() 

    def close_window(self):
        self.close()
        
    def populate_table(self):
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        #sql query to fetch data
        selectCustomerQuery = "select * from CustomerDetails"
        cursor.execute(selectCustomerQuery)
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.tableWidget.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.tableWidget.setItem(row_index, col_index, item)

        connection.close() 
    
    def add_customer(self):
        #making connection
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        #reading the inputs from the line edits
        address = self.customerAddAddress.text()
        phone = self.customerAddPhone.text()
        email = self.customerAddEmail.text()
        name = self.customerAddName.text()
        
        #writing inserting into table using query
        insertcustomerQuery = """
        INSERT INTO customerDetails ([customerName], [customerPhoneNumber], [customerAddress], [customerEmail])
        VALUES (?,?,?,?)
        """

        #executing the query
        cursor.execute(insertcustomerQuery,(name,phone,address,email))

        #commiting the query to database
        connection.commit()

        # Clear the line edits
        self.customerAddAddress.clear()
        self.customerAddPhone.clear()
        self.customerAddEmail.clear()
        self.customerAddName.clear()

        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)  # Reset row count

        QtWidgets.QMessageBox.information(self, 'Supplier Added', 'Customer has been successfully added.', QtWidgets.QMessageBox.StandardButton.Ok)

        # Repopulate the table with the updated data
        self.populate_table()

        connection.close() 
    
    def delete_customer(self):
        # making connection
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        selected_row = self.tableWidget.currentRow() 

        if selected_row >= 0:
            confirmation = QtWidgets.QMessageBox.question(
                self, 'Confirmation', 'Are you sure you want to delete this row?', QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
            if confirmation == QtWidgets.QMessageBox.StandardButton.Yes:
                customer_id = self.tableWidget.item(selected_row, 0).text()

                # Delete associated orders first
                delete_orders_query = "DELETE FROM orders WHERE customerID = ?"
                cursor.execute(delete_orders_query, (customer_id,))
                connection.commit()

                # Now delete the customer
                delete_query = "DELETE FROM customerDetails WHERE customerID = ?"
                cursor.execute(delete_query, (customer_id,))
                connection.commit()

                # Clear the table before repopulating with updated data
                self.tableWidget.clearContents()
                self.tableWidget.setRowCount(0)  # Reset row count
                QtWidgets.QMessageBox.information(self, 'Confirmation', 'Customer has been deleted', QtWidgets.QMessageBox.StandardButton.Ok)
                # Repopulate the table with the updated data
                self.populate_table()

        else:
            QtWidgets.QMessageBox.warning(
                self, 'Warning', 'Please select a row to delete.', QtWidgets.QMessageBox.StandardButton.Ok)

        connection.close()

    def on_item_double_clicked(self, item):
        row = item.row()  # Get the row index of the double-clicked item
        column = item.column()  # Get the column index of the double-clicked item

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
                    QtWidgets.QMessageBox.warning(self, 'Warning', 'You cannot update CustomerID.', QtWidgets.QMessageBox.StandardButton.Ok)
                    return

                if column == 1:
                    customer_id = self.tableWidget.item(row, 0).text()  
                    update_query = f"UPDATE customerDetails SET [customerName] = ? WHERE [customerID] = ?"  
                    
                elif column == 2:
                    customer_id = self.tableWidget.item(row, 0).text()
                    update_query = f"UPDATE customerDetails SET [customerPhoneNumber] = ? WHERE [customerID] = ?"  
                    
                elif column == 3:
                    customer_id = self.tableWidget.item(row, 0).text() 
                    update_query = f"UPDATE customerDetails SET [customerAddress] = ? WHERE [customerID] = ?"  
                    
                elif column == 4:
                    customer_id = self.tableWidget.item(row, 0).text()  
                    update_query = f"UPDATE customerDetails SET [customerEmail] = ? WHERE [customerID] = ?" 

                modified_value = self.tableWidget.item(row, column).text()
                cursor.execute(update_query, (modified_value, customer_id))
                connection.commit()

        # Clear the modified_data dictionary after updating the database
        self.modified_data = {}

        # Clear the existing table data before repopulating it
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)

        # Refresh the table to reflect the updated data
        self.populate_table()
   
    def search_customer(self):
        search_criteria = self.customerSearchCombo.currentText()  # Get selected search criteria (Name or customerID)
        search_text = self.customerSearchLine.text()  # Get text entered in the line edit for search input

        # Clear the existing table data before populating it with search results
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)

        if search_criteria == 'Name':
            # Perform a search based on the customer name
            search_query = "SELECT * FROM customerDetails WHERE [customerName] LIKE ?"
            cursor.execute(search_query, ('%' + search_text + '%',))
        elif search_criteria == 'CustomerID':
            # Perform a search based on the customer ID
            search_query = "SELECT * FROM customerDetails WHERE [customerID] = ?"
            cursor.execute(search_query, (search_text,))

        # Fetch the search results and update the table
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.tableWidget.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.tableWidget.setItem(row_index, col_index, item)

class reports(QtWidgets.QMainWindow):
    def __init__(self):
        super(reports,self).__init__()
        uic.loadUi('customerreports.ui',self)
        self.show()
        self.populate_table() 
        self.topCustomers.setColumnWidth(1,140)
        self.exitBtn.clicked.connect(self.closeWindow)

    def closeWindow(self):
        self.close()

    def populate_table(self):
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        # Clear existing content in orderList
        self.topCustomers.clearContents()
        self.topCustomers.setRowCount(0)

        # SQL query to fetch data
        selectOrderQuery = """
        select C.customerID,C.customerName,count(orderNumber),sum(orderAmount) from orders O join customerDetails C
        on O.customerID=C.customerID
        group by C.customerID,C.customerName
        order by count(orderNumber) DESC
        """
        cursor.execute(selectOrderQuery)
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.topCustomers.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.topCustomers.setItem(row_index, col_index, item)

        connection.close()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()