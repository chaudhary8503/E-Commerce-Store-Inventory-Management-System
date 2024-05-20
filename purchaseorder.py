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


class PurchaseOrder(QtWidgets.QMainWindow):
    def __init__(self):
        super(PurchaseOrder,self).__init__()
        uic.loadUi('purchaseOrderList.ui',self)
        self.populate_orderList()
        self.searchOrders.clicked.connect(self.search)
        self.exitButton.clicked.connect(self.abc)
        self.deleteOrder.clicked.connect(self.delete_order)
        self.addOrder.clicked.connect(self.add_Order)
        self.orderList.setColumnWidth(0,120)
        self.orderList.setColumnWidth(1,120)
        self.orderList.setColumnWidth(2,120)
        self.orderList.setColumnWidth(3,120)


        self.view_order_window = None
        self.viewOrder.clicked.connect(self.openViewOrder)

        self.open_update_window = None
        self.modifyOrder.clicked.connect(self.openUpdateOrder)
    def abc(self):
        self.close()
    def openUpdateOrder(self):
        selected_row = self.orderList.currentRow()
        if selected_row >= 0:
            row_data = []  
            for column in range(self.orderList.columnCount()):
                item = self.orderList.item(selected_row, column)
                if item is not None:
                    row_data.append(item.text())
                else:
                    row_data.append("")  
                    
            if self.open_update_window is None:
                self.open_update_window = modify(row_data)
            self.open_update_window.populate_table(row_data)
            self.open_update_window.modify_add_item(row_data)
            self.open_update_window.show()
        else:
            QtWidgets.QMessageBox.warning(self, 'Warning', 'Please select an order to view.', QtWidgets.QMessageBox.StandardButton.Ok)
            

    def openViewOrder(self):
        selected_row = self.orderList.currentRow()
        if selected_row >= 0:
            row_data = []  
            for column in range(self.orderList.columnCount()):
                item = self.orderList.item(selected_row, column)
                if item is not None:
                    row_data.append(item.text())
                else:
                    row_data.append("") 
                    
            if self.view_order_window is None:
                self.view_order_window = view_order(row_data)
            self.view_order_window.populate_viewOrderTable(row_data)
            self.view_order_window.show()
        else:
            QtWidgets.QMessageBox.warning(self, 'Warning', 'Please select an order to view.', QtWidgets.QMessageBox.StandardButton.Ok)

    def add_Order(self):
        self.master_form = add()
        self.master_form.show()
    
    def modify_Order(self):
        self.master_form = modify()
        self.master_form.show()
    
    def populate_orderList(self):
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        select_query = "SELECT * FROM purchaseOrder"
        cursor.execute( select_query)
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.orderList.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.orderList.setItem(row_index, col_index, item)

        connection.close()
    def delete_order(self):
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        selected_row = self.orderList.currentRow()  

        if selected_row >= 0:  
            confirmation = QtWidgets.QMessageBox.question(self, 'Confirmation', 'Are you sure you want to delete this order?', QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
            
            if confirmation == QtWidgets.QMessageBox.StandardButton.Yes:
                order_id = self.orderList.item(selected_row, 0).text()  
                delete_associated_query = "DELETE FROM purchaseItem WHERE purchaseOrderNumber = ?"
                cursor.execute(delete_associated_query, (order_id,))
                connection.commit()

                delete_query = "DELETE FROM purchaseOrder WHERE purchaseOrderNumber = ?"  

                cursor.execute(delete_query, (order_id,))
                connection.commit()

                QtWidgets.QMessageBox.information(self, 'Deletion', f'Order number {order_id} has been deleted.', QtWidgets.QMessageBox.StandardButton.Ok)

                self.orderList.clearContents()
                self.orderList.setRowCount(0)  

                self.populate_orderList()

        else:
            QtWidgets.QMessageBox.warning(self, 'Warning', 'Please select an order to delete.', QtWidgets.QMessageBox.StandardButton.Ok)

        connection.close() 

    
    def search(self) :
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        search_criteria = self.searchOrderCombo.currentText() 
        search_text = self.searchOrderLine.text()  

        self.orderList.clearContents()
        self.orderList.setRowCount(0)

        if search_criteria == 'PO Number':
            search_query = "SELECT * FROM purchaseOrder WHERE [purchaseOrderNumber] LIKE ?"
            cursor.execute(search_query, ('%' + search_text + '%',))
        elif search_criteria == 'SupplierID':
            search_query = "SELECT * FROM purchaseOrder WHERE [supplierID] = ?"
            cursor.execute(search_query, (search_text,))

        for row_index, row_data in enumerate(cursor.fetchall()):
            self.orderList.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.orderList.setItem(row_index, col_index, item)

class add(QtWidgets.QMainWindow):
    def __init__(self):
        super(add,self).__init__()
        uic.loadUi("addPO.ui",self)
        self.show()
        self.populate_customers_table()
        self.customerSearchButton.clicked.connect(self.search_customer)
        self.addCustomerButton.clicked.connect(self.add_customer)
        self.itemIDCombo.currentTextChanged.connect(self.update_fields)
        self.itemNameCombo.currentTextChanged.connect(self.update_fields)
        self.addItemsButton.clicked.connect(self.add_item)
        self.selectCustomerButton.clicked.connect(self.select_customer)
        self.doneButton.clicked.connect(self.order_done)
        self.orderInserted = False
        self.order_num = 0
        self.supplierInserted = False
        self.itemDetailsTable.setColumnWidth(0,70)
        self.supplierList.setColumnWidth(0,60) 
        self.supplierList.setColumnWidth(0,60)
        self.itemDetailsTable.setColumnWidth(0,100)
        self.itemDetailsTable.setColumnWidth(1,100)
        self.itemDetailsTable.setColumnWidth(2,100)
        self.itemDetailsTable.setColumnWidth(3,100)
        self.supplierList.setMaximumWidth(800) 

    def populate_customers_table(self):
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        selectCustomersQuery = "select * from supplierDetails"
        cursor.execute(selectCustomersQuery)
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.supplierList.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.supplierList.setItem(row_index, col_index, item)


        connection.close()
    
    def search_customer(self):
        search_criteria = self.customerSearchCombo.currentText()  
        search_text = self.customerSearchLine.text() 
        cursor = connection.cursor()
        self.supplierList.clearContents()
        self.supplierList.setRowCount(0)

        if search_text.strip() == '':  
            search_query = "SELECT * FROM supplierDetails"
            cursor.execute(search_query)
        else:
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

    def add_customer(self):
        #making connection
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        
        #reading the inputs from the line edits
        name = self.customerNameLine.text()
        contact = self.customerContactLine.text()
        address = self.customerAddressLine.text()
        email = self.customerEmailLine.text()

        #writing inserting into table using query
        insertSupplierQuery = """
        INSERT INTO supplierDetails ([supplierName],[supplierNumber] ,[supplierCity], [supplierEmail])
        VALUES (?,?,?,?)
        """

        #executing the query
        cursor.execute(insertSupplierQuery,(name,contact,address,email))

        #commiting the query to database
        connection.commit()

        QtWidgets.QMessageBox.information(self, 'Success', 'Supplier has been added', QtWidgets.QMessageBox.StandardButton.Ok)

        # Clear the line edits
        self.customerNameLine.clear()
        self.customerContactLine.clear()
        self.customerAddressLine.clear()
        self.customerEmailLine.clear()

        self.supplierList.clearContents()
        self.supplierList.setRowCount(0)  # Reset row count

        # Repopulate the table with the updated data
        self.populate_customers_table()

        connection.close() 
            
    def update_fields(self):
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        selected_item_id = self.itemIDCombo.currentText()
        selected_item_name = self.itemNameCombo.currentText()

        # Formulate the SQL query based on the selected item details
        query = "SELECT * FROM items WHERE itemID=?"
        cursor.execute(query, (selected_item_id))

        # Fetch the data
        data = cursor.fetchone()

        # Update other fields based on the retrieved data
        if data:
            self.itemIDCombo.setCurrentText(str(data[0]))
            self.itemNameCombo.setCurrentText(str(data[1]))
            self.colourLine.setText(str(data[2]))
            self.quantityLine.setText(str(data[3]))
            self.unitPriceLine.setText(str(data[4]))
            
        else:
            self.itemIDCombo.setCurrentIndex(-1)
            self.itemNameCombo.setCurrentIndex(-1)
            self.colourLine.clear()
            self.quantityLine.clear()
            self.unitPriceLine.clear()

        cursor.close() 
        connection.close()

    def select_customer(self):
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        self.supplierInserted=True
        selected_row = self.supplierList.currentRow()
        if selected_row >= 0:
            customer_id = self.supplierList.item(selected_row, 0).text()
            if self.orderInserted==False:
                selected_date = self.orderDateEdit.date().toString("yyyy-MM-dd")
                amount = 0
                create_order_query = """
                        insert into purchaseOrder ([supplierID],[amountPaid],[dateOfPurchase])
                        values (?,?,?)
                        """
                cursor.execute(create_order_query, (customer_id, amount,selected_date))
                connection.commit() 
                orderNumber = cursor.execute("SELECT @@IDENTITY").fetchone()[0] 
                self.order_num = orderNumber 
                return orderNumber 
        else:
            QtWidgets.QMessageBox.warning(self, 'Warning', 'Please select a customer.', QtWidgets.QMessageBox.StandardButton.Ok)
            return None


    def add_item(self,row_data):
        #making connection
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        if self.supplierInserted==False:
            QtWidgets.QMessageBox.warning(self,'Warning','Please select a supplier before generating order',QtWidgets.QMessageBox.StandardButton.Ok)
            return 
        
        self.orderInserted = True
        #reading the inputs from the line edits
        itemID = self.itemIDCombo.currentText()
        itemName = self.itemNameCombo.currentText()
        quantity = self.quantityLine.text()
        colour = self.colourLine.text() 
        price = self.unitPriceLine.text()

        self.orderInserted=True
        orderNum = self.order_num
        add_items_query = """
                    insert into purchaseItem ([purchaseOrderNumber],[itemID],[itemQtyProcured],[itemCost])
                    values (?,?,?,?)
                    """
        cursor.execute(add_items_query,(orderNum,itemID,quantity,float(price))) 

        increase_items = """
                UPDATE items
                set itemQtyAvailable = ?
                where itemID = ?
        """
        cursor.execute("select itemQtyAvailable from items where itemID=?",itemID)
        current_items = cursor.fetchone()
        qty_avail = current_items[0]
        update_qty = int(qty_avail) + int(quantity)
        cursor.execute(increase_items,update_qty,itemID)

        #populating the purchase\item list
        populate_item_query = """
                select purchaseOrderNumber,itemID,itemQtyProcured,itemCost from purchaseItem
                where purchaseOrderNumber = ?
                            """
        
        cursor.execute(populate_item_query,orderNum)
        result = cursor.fetchall()

        # Clear the contents of QLineEdit widgets
        self.quantityLine.clear()
        self.colourLine.clear()
        self.unitPriceLine.clear()
        
        # Clear the current selection in QComboBox widgets
        self.itemIDCombo.setCurrentIndex(0) 
        self.itemNameCombo.setCurrentIndex(0)  

        self.itemDetailsTable.clearContents()
        self.itemDetailsTable.setRowCount(0)

        for row_index, row_data in enumerate(result):
            self.itemDetailsTable.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.itemDetailsTable.setItem(row_index, col_index, item)
        
        connection.commit() 
        connection.close()

    def order_done(self,event):
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        update_query = """
        UPDATE purchaseOrder
        SET amountPaid = (
            select sum(itemCost*itemQtyProcured)
            from purchaseItem
            where purchaseItem.purchaseOrderNumber = purchaseOrder.purchaseOrderNumber
            )
        """


        if self.orderInserted==True and self.supplierInserted==True:
            cursor.execute(update_query)
            cursor.commit() 
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setText("Purchase Order has been added.")
            msg.setWindowTitle("Success")
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.exec()
            if msg.clickedButton() == msg.button(QtWidgets.QMessageBox.StandardButton.Ok):
                repopulate = add()
                repopulate.populate_customers_table()
                self.close()  
        elif self.supplierInserted==True and self.orderInserted==False:
            QtWidgets.QMessageBox.warning(None,'Empty PO','You are entering an empty PO. You can modify it later')
            self.close()
        else:        
            QtWidgets.QMessageBox.warning(None,'No PO','You are exiting without entering an order')
            self.close()
    
class modify(QtWidgets.QMainWindow):
    def __init__(self,row_data):
        super(modify,self).__init__()
        uic.loadUi('modifyPO.ui',self)
        self.populate_table(row_data)
        self.removeItem.clicked.connect(self.remove_item)
        self.addItemButton.clicked.connect(self.modify_add_item)
        self.itemIDCombo.currentTextChanged.connect(self.update_fields)
        self.itemNameCombo.currentTextChanged.connect(self.update_fields)
        self.doneButton.clicked.connect(self.change_done)
        self.orderDetails.itemDoubleClicked.connect(self.on_item_double_clicked)
        self.updateItem.clicked.connect(self.update_table)
        self.modified_data = {}  # Dictionary to store modified data
        self.order_number = 0

    def update_table(self):
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        new_val = (self.orderDetails.item(self.row, self.col).text())

        item_id = self.orderDetails.item(self.row, 0).text() 
        update_query = "UPDATE purchaseItem SET [itemQtyProcured] = ? WHERE [itemID] = ?"
        update_amount = """UPDATE purchaseOrder
            SET amountPaid = (
            select sum(itemCost*itemQtyProcured)
            from purchaseItem
            where purchaseOrder.purchaseOrderNumber = purchaseItem.purchaseOrderNumber
            )
        """
        print(new_val)
        # Update the database with modified value
        cursor.execute(update_query, (new_val, item_id))
        cursor.execute(update_amount) 
        connection.commit()

        # Clear the modified_data dictionary after updating the database
        self.modified_data = {}

        # Clear the existing table data before repopulating it
        self.orderDetails.clearContents()
        self.orderDetails.setRowCount(0)

        # Populate the table with updated data
        orderNum = self.order_number
        selectOrderQuery = "SELECT itemID, itemQtyProcured, itemCost FROM purchaseItem WHERE purchaseOrderNumber = ?"
        cursor.execute(selectOrderQuery, orderNum)
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.orderDetails.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.orderDetails.setItem(row_index, col_index, item)

        # Close the database connection
        connection.close()
        QtWidgets.QMessageBox.information(self, 'Updated', 'Order Details have been updated', QtWidgets.QMessageBox.StandardButton.Ok)

    def remove_item(self):
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        selected_row = self.orderDetails.currentRow()  

        if selected_row >= 0:  
            confirmation = QtWidgets.QMessageBox.question(self, 'Confirmation', 'Are you sure you want to delete this item from order?', QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
            
            if confirmation == QtWidgets.QMessageBox.StandardButton.Yes:
                item_id = self.orderDetails.item(selected_row, 0).text()  
                delete_associated_query = "DELETE FROM purchaseItem WHERE itemID = ?"
                cursor.execute(delete_associated_query, (item_id,))
                connection.commit()

                QtWidgets.QMessageBox.information(self, 'Deletion', f'Item number {item_id} has been deleted.', QtWidgets.QMessageBox.StandardButton.Ok)

                

        else:
            QtWidgets.QMessageBox.warning(self, 'Warning', 'Please select an order to delete.', QtWidgets.QMessageBox.StandardButton.Ok)

        connection.close() 

    def populate_table(self,row_data):
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        orderNum = row_data[0]
        self.order_number = orderNum

        # Clear existing content in orderList
        self.orderDetails.clearContents()
        self.orderDetails.setRowCount(0)

        # SQL query to fetch data
        selectOrderQuery = "SELECT itemID,itemQtyProcured,itemCost FROM purchaseItem where purchaseOrderNumber = ?"
        cursor.execute(selectOrderQuery,orderNum)
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.orderDetails.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.orderDetails.setItem(row_index, col_index, item)

        connection.close()

    def on_item_double_clicked(self, item):
        self.row = item.row()
        self.col = item.column()
        row = item.row()  
        column = item.column() 

        if column==1:
            # Store the original value before editing for reference
            original_value = item.text()

            # Allow editing by setting the item as editable
            item.setFlags(item.flags() | QtCore.Qt.ItemFlag.ItemIsEditable)

            # Update the modified_data dictionary with the modified value
            self.modified_data.setdefault(row, {})[column] = original_value
        else:
            QtWidgets.QMessageBox.warning(None, "Invalid Operation", "You cannot edit this information", QtWidgets.QMessageBox.StandardButton.Ok)

    def modify_add_item(self,row_data):
        #making connection
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        orderNum = self.order_number
        #reading the inputs from the line edits
        itemID = self.itemIDCombo.currentText()
        itemName = self.itemNameCombo.currentText()
        quantity = self.quantityLine.text()
        colour = self.colourLine.text() 
        price = self.unitPriceLine.text()
        if price=='':
            price = '0'
        
        add_items_query = """
                    insert into purchaseItem ([purchaseOrderNumber],[itemID],[itemQtyProcured],[itemCost])
                    values (?,?,?,?)
                    """ 
        cursor.execute(add_items_query,(orderNum,itemID,quantity,float(price))) 

        # Clear the contents of QLineEdit widgets
        self.quantityLine.clear()
        self.colourLine.clear()
        self.unitPriceLine.clear()
        
        # Clear the current selection in QComboBox widgets
        self.itemIDCombo.setCurrentIndex(0)  
        self.itemNameCombo.setCurrentIndex(0)  

        increase_items = """
                UPDATE items
                set itemQtyAvailable = ?
                where itemID = ?
        """
        cursor.execute("select itemQtyAvailable from items where itemID=?",itemID)
        current_items = cursor.fetchone()
        qty_avail = current_items[0]
        print(qty_avail)
        print(quantity)
        if quantity=='':
            quantity='0'
        update_qty = int(qty_avail) + int(quantity)
        cursor.execute(increase_items,update_qty,itemID)

        populate_item_query = """
                select itemID,itemQtyProcured,itemCost from purchaseItem
                where purchaseOrderNumber = ?
                            """
        
        cursor.execute(populate_item_query,orderNum)
        result = cursor.fetchall()

        self.orderDetails.clearContents()
        self.orderDetails.setRowCount(0)

        for row_index, row_data in enumerate(result):
            self.orderDetails.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.orderDetails.setItem(row_index, col_index, item)
        
        connection.commit() 
        connection.close()

    
    def update_fields(self):
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        selected_item_id = self.itemIDCombo.currentText()
        selected_item_name = self.itemNameCombo.currentText()

        query = "SELECT * FROM items WHERE itemID=?"
        cursor.execute(query, (selected_item_id))

        data = cursor.fetchone()

        if data:
            self.itemIDCombo.setCurrentText(str(data[0]))
            self.itemNameCombo.setCurrentText(str(data[1]))
            self.colourLine.setText(str(data[2]))
            self.quantityLine.setText(str(data[3]))
            self.unitPriceLine.setText(str(data[4]))
            
        else:
            self.itemIDCombo.setCurrentIndex(-1)
            self.itemNameCombo.setCurrentIndex(-1)
            self.colourLine.clear()
            self.quantityLine.clear()
            self.unitPriceLine.clear()

        cursor.close() 
        connection.close()
    def change_done(self):
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        update_query = """
        UPDATE purchaseOrder
        SET amountPaid = (
            select sum(itemCost*itemQtyProcured)
            from purchaseItem
            where purchaseItem.purchaseOrderNumber = purchaseOrder.purchaseOrderNumber
            )
        """
        cursor.execute(update_query)
        connection.commit()

        connection.close()

        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg.setText("Order has been modified.")
        msg.setWindowTitle("Success")
        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msg.exec()
        if msg.clickedButton() == msg.button(QtWidgets.QMessageBox.StandardButton.Ok):
            repopulate = add()
            repopulate.populate_customers_table()
            self.close()  

class view_order(QtWidgets.QMainWindow):
    def __init__(self, row_data):
        super(view_order, self).__init__()
        uic.loadUi('viewPO.ui', self)
        self.show()
        self.viewExitButton.clicked.connect(self.close_screen)

    def close_screen(self):
        self.close()

    def populate_viewOrderTable(self, row_data):
        order_id = row_data[0]  
        customer_id = row_data[1] 

        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        self.viewCustomerIDLine.setText(str(customer_id))
        self.viewCustomerIDLine.setEnabled(False) 

        self.viewOrderTable.clearContents()
        self.viewOrderTable.setRowCount(0)

        selectOrderQuery = "SELECT purchaseOrderNumber,itemID,itemCost,itemQtyProcured FROM purchaseItem WHERE purchaseOrderNumber = ?"
        cursor.execute(selectOrderQuery, (order_id,))

        for row_index, row_data in enumerate(cursor.fetchall()):
            self.viewOrderTable.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.viewOrderTable.setItem(row_index, col_index, item)

        connection.close()    

def main():
    app = QApplication(sys.argv)
    window = PurchaseOrder()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()