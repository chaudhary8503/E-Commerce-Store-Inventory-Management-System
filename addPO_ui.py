# Form implementation generated from reading ui file 'f:\Habib University\Database Systems\Project\Project Code\supplier code\addPO.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(819, 568)
        MainWindow.setStyleSheet("QMainWindow{\n"
"    background-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QMenuBar{\n"
"background-color: rgb(0,0,0);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 230, 791, 291))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("QGroupBox {\n"
"    background-color: rgb(0,0,0);\n"
"    border: 1px solid black;\n"
"    color: white; \n"
"}")
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 20, 481, 51))
        self.groupBox_3.setObjectName("groupBox_3")
        self.customerSearchCombo = QtWidgets.QComboBox(parent=self.groupBox_3)
        self.customerSearchCombo.setGeometry(QtCore.QRect(10, 20, 101, 22))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.customerSearchCombo.setFont(font)
        self.customerSearchCombo.setStyleSheet("QComboBox QAbstractItemView {\n"
"    background-color: rgb(30, 30, 40);\n"
"    color: #FFF;\n"
"    selection-background-color: rgb(53, 53, 71);\n"
"    selection-color: #FFF;\n"
"}\n"
"\n"
"\n"
"QComboBox{\n"
"    background-color: rgb(30, 30, 40);\n"
"    color: rgb(255,255,255);\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"    border: 2px solid rgb(53, 53, 71);\n"
"    \n"
"    background-color: rgb(40, 40, 54);\n"
"}")
        self.customerSearchCombo.setObjectName("customerSearchCombo")
        self.customerSearchCombo.addItem("")
        self.customerSearchCombo.addItem("")
        self.customerSearchLine = QtWidgets.QLineEdit(parent=self.groupBox_3)
        self.customerSearchLine.setGeometry(QtCore.QRect(120, 20, 251, 21))
        self.customerSearchLine.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 100px;\n"
"    color: #FFF;\n"
"    background-color: rgb(30, 30, 40);\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(53, 53, 71)\n"
"}\n"
"\n"
"QLineEdit: focus{\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"}")
        self.customerSearchLine.setObjectName("customerSearchLine")
        self.customerSearchButton = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.customerSearchButton.setGeometry(QtCore.QRect(390, 20, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.customerSearchButton.setFont(font)
        self.customerSearchButton.setObjectName("customerSearchButton")
        self.groupBox_4 = QtWidgets.QGroupBox(parent=self.groupBox_2)
        self.groupBox_4.setGeometry(QtCore.QRect(520, 30, 251, 171))
        self.groupBox_4.setStyleSheet("QGroupBox {\n"
"    background-color: rgb(0,0,0);\n"
"    border: 1px solid black;\n"
"    color: white; \n"
"}")
        self.groupBox_4.setObjectName("groupBox_4")
        self.label = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label.setGeometry(QtCore.QRect(10, 20, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"    color: #FFF;\n"
"}")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
"    color: #FFF;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{\n"
"    color: #FFF;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel{\n"
"    color: #FFF;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.customerNameLine = QtWidgets.QLineEdit(parent=self.groupBox_4)
        self.customerNameLine.setGeometry(QtCore.QRect(90, 20, 141, 20))
        self.customerNameLine.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 100px;\n"
"    color: #FFF;\n"
"    background-color: rgb(30, 30, 40);\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(53, 53, 71)\n"
"}\n"
"\n"
"QLineEdit: focus{\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"}")
        self.customerNameLine.setObjectName("customerNameLine")
        self.customerContactLine = QtWidgets.QLineEdit(parent=self.groupBox_4)
        self.customerContactLine.setGeometry(QtCore.QRect(90, 50, 141, 20))
        self.customerContactLine.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 100px;\n"
"    color: #FFF;\n"
"    background-color: rgb(30, 30, 40);\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(53, 53, 71)\n"
"}\n"
"\n"
"QLineEdit: focus{\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"}")
        self.customerContactLine.setObjectName("customerContactLine")
        self.customerAddressLine = QtWidgets.QLineEdit(parent=self.groupBox_4)
        self.customerAddressLine.setGeometry(QtCore.QRect(90, 80, 141, 20))
        self.customerAddressLine.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 100px;\n"
"    color: #FFF;\n"
"    background-color: rgb(30, 30, 40);\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(53, 53, 71)\n"
"}\n"
"\n"
"QLineEdit: focus{\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"}")
        self.customerAddressLine.setObjectName("customerAddressLine")
        self.customerEmailLine = QtWidgets.QLineEdit(parent=self.groupBox_4)
        self.customerEmailLine.setGeometry(QtCore.QRect(90, 110, 141, 20))
        self.customerEmailLine.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 100px;\n"
"    color: #FFF;\n"
"    background-color: rgb(30, 30, 40);\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(53, 53, 71)\n"
"}\n"
"\n"
"QLineEdit: focus{\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"}")
        self.customerEmailLine.setObjectName("customerEmailLine")
        self.addCustomerButton = QtWidgets.QPushButton(parent=self.groupBox_4)
        self.addCustomerButton.setGeometry(QtCore.QRect(140, 140, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.addCustomerButton.setFont(font)
        self.addCustomerButton.setStyleSheet("QPushButton{\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 100px;\n"
"    color: #FFF;\n"
"    background-color: rgb(30, 30, 40);\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border: 2px solid rgb(53, 53, 71)\n"
"}")
        self.addCustomerButton.setObjectName("addCustomerButton")
        self.selectCustomerButton = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.selectCustomerButton.setGeometry(QtCore.QRect(520, 210, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.selectCustomerButton.setFont(font)
        self.selectCustomerButton.setStyleSheet("QPushButton{\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 100px;\n"
"    color: #FFF;\n"
"    background-color: rgb(30, 30, 40);\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border: 2px solid rgb(53, 53, 71)\n"
"}")
        self.selectCustomerButton.setObjectName("selectCustomerButton")
        self.doneButton = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.doneButton.setGeometry(QtCore.QRect(690, 210, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.doneButton.setFont(font)
        self.doneButton.setStyleSheet("QPushButton{\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 100px;\n"
"    color: #FFF;\n"
"    background-color: rgb(30, 30, 40);\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border: 2px solid rgb(53, 53, 71)\n"
"}")
        self.doneButton.setObjectName("doneButton")
        self.supplierList = QtWidgets.QTableWidget(parent=self.groupBox_2)
        self.supplierList.setGeometry(QtCore.QRect(20, 80, 401, 171))
        self.supplierList.setMaximumSize(QtCore.QSize(401, 16777215))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.supplierList.setFont(font)
        self.supplierList.setStyleSheet("QTableWidget{\n"
"    background-color: rgb(0,0,0);\n"
"    gridline-color: rgb(255, 255, 255);\n"
"    color: rgb(255,255,255);\n"
"    border-radius: 10px;\n"
"    border: 2px solid rgb(255,255,255);\n"
"    selection-background-color: rgb(46, 46, 62);\n"
"}")
        self.supplierList.setWordWrap(True)
        self.supplierList.setObjectName("supplierList")
        self.supplierList.setColumnCount(6)
        self.supplierList.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.supplierList.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.supplierList.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.supplierList.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.supplierList.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.supplierList.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.supplierList.setHorizontalHeaderItem(5, item)
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel{\n"
"    color: #FFF;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.orderDateEdit = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.orderDateEdit.setGeometry(QtCore.QRect(70, 10, 110, 22))
        self.orderDateEdit.setObjectName("orderDateEdit")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(540, 20, 271, 201))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("QGroupBox {\n"
"    background-color: rgb(0,0,0);\n"
"    border: 1px solid black;\n"
"    color: white; \n"
"}")
        self.groupBox.setObjectName("groupBox")
        self.itemIDCombo = QtWidgets.QComboBox(parent=self.groupBox)
        self.itemIDCombo.setGeometry(QtCore.QRect(110, 30, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.itemIDCombo.setFont(font)
        self.itemIDCombo.setStyleSheet("QComboBox QAbstractItemView {\n"
"    background-color: rgb(30, 30, 40);\n"
"    color: #FFF;\n"
"    selection-background-color: rgb(53, 53, 71);\n"
"    selection-color: #FFF;\n"
"}\n"
"\n"
"\n"
"QComboBox{\n"
"    background-color: rgb(30, 30, 40);\n"
"    color: rgb(255,255,255);\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"    border: 2px solid rgb(53, 53, 71);\n"
"    \n"
"    background-color: rgb(40, 40, 54);\n"
"}")
        self.itemIDCombo.setObjectName("itemIDCombo")
        self.itemIDCombo.addItem("")
        self.itemIDCombo.setItemText(0, "")
        self.itemIDCombo.addItem("")
        self.itemIDCombo.addItem("")
        self.itemIDCombo.addItem("")
        self.itemIDCombo.addItem("")
        self.itemIDCombo.addItem("")
        self.itemIDCombo.addItem("")
        self.itemIDCombo.addItem("")
        self.itemIDCombo.addItem("")
        self.itemIDCombo.addItem("")
        self.itemIDCombo.addItem("")
        self.itemIDCombo.addItem("")
        self.itemIDCombo.addItem("")
        self.itemIDCombo.addItem("")
        self.itemIDCombo.addItem("")
        self.itemIDCombo.addItem("")
        self.itemNameCombo = QtWidgets.QComboBox(parent=self.groupBox)
        self.itemNameCombo.setGeometry(QtCore.QRect(110, 60, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.itemNameCombo.setFont(font)
        self.itemNameCombo.setStyleSheet("QComboBox QAbstractItemView {\n"
"    background-color: rgb(30, 30, 40);\n"
"    color: #FFF;\n"
"    selection-background-color: rgb(53, 53, 71);\n"
"    selection-color: #FFF;\n"
"}\n"
"\n"
"\n"
"QComboBox{\n"
"    background-color: rgb(30, 30, 40);\n"
"    color: rgb(255,255,255);\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"    border: 2px solid rgb(53, 53, 71);\n"
"    \n"
"    background-color: rgb(40, 40, 54);\n"
"}")
        self.itemNameCombo.setObjectName("itemNameCombo")
        self.itemNameCombo.addItem("")
        self.itemNameCombo.setItemText(0, "")
        self.itemNameCombo.addItem("")
        self.itemNameCombo.addItem("")
        self.itemNameCombo.addItem("")
        self.itemNameCombo.addItem("")
        self.itemNameCombo.addItem("")
        self.unitPriceLine = QtWidgets.QLineEdit(parent=self.groupBox)
        self.unitPriceLine.setGeometry(QtCore.QRect(110, 150, 113, 20))
        self.unitPriceLine.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 100px;\n"
"    color: #FFF;\n"
"    background-color: rgb(30, 30, 40);\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(53, 53, 71)\n"
"}\n"
"\n"
"QLineEdit: focus{\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"}")
        self.unitPriceLine.setObjectName("unitPriceLine")
        self.addItemsButton = QtWidgets.QPushButton(parent=self.groupBox)
        self.addItemsButton.setGeometry(QtCore.QRect(110, 180, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.addItemsButton.setFont(font)
        self.addItemsButton.setStyleSheet("QPushButton{\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 100px;\n"
"    color: #FFF;\n"
"    background-color: rgb(30, 30, 40);\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border: 2px solid rgb(53, 53, 71)\n"
"}")
        self.addItemsButton.setObjectName("addItemsButton")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(20, 30, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel{\n"
"    color: #FFF;\n"
"}")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(20, 60, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("QLabel{\n"
"    color: #FFF;\n"
"}")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(20, 90, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("QLabel{\n"
"    color: #FFF;\n"
"}")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(20, 120, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("QLabel{\n"
"    color: #FFF;\n"
"}")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(20, 150, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("QLabel{\n"
"    color: #FFF;\n"
"}")
        self.label_10.setObjectName("label_10")
        self.quantityLine = QtWidgets.QLineEdit(parent=self.groupBox)
        self.quantityLine.setGeometry(QtCore.QRect(110, 90, 113, 20))
        self.quantityLine.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 100px;\n"
"    color: #FFF;\n"
"    background-color: rgb(30, 30, 40);\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(53, 53, 71)\n"
"}\n"
"\n"
"QLineEdit: focus{\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"}")
        self.quantityLine.setObjectName("quantityLine")
        self.colourLine = QtWidgets.QLineEdit(parent=self.groupBox)
        self.colourLine.setGeometry(QtCore.QRect(110, 120, 113, 20))
        self.colourLine.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 100px;\n"
"    color: #FFF;\n"
"    background-color: rgb(30, 30, 40);\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(53, 53, 71)\n"
"}\n"
"\n"
"QLineEdit: focus{\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"}")
        self.colourLine.setObjectName("colourLine")
        self.itemDetailsTable = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.itemDetailsTable.setGeometry(QtCore.QRect(20, 40, 501, 171))
        self.itemDetailsTable.setStyleSheet("QTableWidget{\n"
"    background-color: rgb(0,0,0);\n"
"    gridline-color: rgb(255, 255, 255);\n"
"    color: rgb(255,255,255);\n"
"    border-radius: 10px;\n"
"    border: 2px solid rgb(255,255,255);\n"
"    selection-background-color: rgb(46, 46, 62);\n"
"}")
        self.itemDetailsTable.setObjectName("itemDetailsTable")
        self.itemDetailsTable.setColumnCount(5)
        self.itemDetailsTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.itemDetailsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.itemDetailsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.itemDetailsTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.itemDetailsTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.itemDetailsTable.setHorizontalHeaderItem(4, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 819, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Customer list"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Search Suppliers"))
        self.customerSearchCombo.setItemText(0, _translate("MainWindow", "Name"))
        self.customerSearchCombo.setItemText(1, _translate("MainWindow", "SupplierID"))
        self.customerSearchButton.setText(_translate("MainWindow", "Search"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Add Supplier"))
        self.label.setText(_translate("MainWindow", "Name:"))
        self.label_2.setText(_translate("MainWindow", "Contact:"))
        self.label_3.setText(_translate("MainWindow", "City:"))
        self.label_4.setText(_translate("MainWindow", "Email:"))
        self.addCustomerButton.setText(_translate("MainWindow", "Add Supplier"))
        self.selectCustomerButton.setText(_translate("MainWindow", "Select Supplier"))
        self.doneButton.setText(_translate("MainWindow", "Done"))
        item = self.supplierList.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "SupplierID"))
        item = self.supplierList.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Supplier Name"))
        item = self.supplierList.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "City"))
        item = self.supplierList.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Country"))
        item = self.supplierList.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Email"))
        item = self.supplierList.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Contact. No"))
        self.label_5.setText(_translate("MainWindow", "Date:"))
        self.groupBox.setTitle(_translate("MainWindow", "Add Items to PO"))
        self.itemIDCombo.setItemText(1, _translate("MainWindow", "101"))
        self.itemIDCombo.setItemText(2, _translate("MainWindow", "102"))
        self.itemIDCombo.setItemText(3, _translate("MainWindow", "103"))
        self.itemIDCombo.setItemText(4, _translate("MainWindow", "104"))
        self.itemIDCombo.setItemText(5, _translate("MainWindow", "201"))
        self.itemIDCombo.setItemText(6, _translate("MainWindow", "202"))
        self.itemIDCombo.setItemText(7, _translate("MainWindow", "203"))
        self.itemIDCombo.setItemText(8, _translate("MainWindow", "204"))
        self.itemIDCombo.setItemText(9, _translate("MainWindow", "301"))
        self.itemIDCombo.setItemText(10, _translate("MainWindow", "302"))
        self.itemIDCombo.setItemText(11, _translate("MainWindow", "303"))
        self.itemIDCombo.setItemText(12, _translate("MainWindow", "304"))
        self.itemIDCombo.setItemText(13, _translate("MainWindow", "401"))
        self.itemIDCombo.setItemText(14, _translate("MainWindow", "402"))
        self.itemIDCombo.setItemText(15, _translate("MainWindow", "501"))
        self.itemNameCombo.setItemText(1, _translate("MainWindow", "Tumbler"))
        self.itemNameCombo.setItemText(2, _translate("MainWindow", "Metallic Bottle"))
        self.itemNameCombo.setItemText(3, _translate("MainWindow", "Metallic Straw"))
        self.itemNameCombo.setItemText(4, _translate("MainWindow", "Tote Bags"))
        self.itemNameCombo.setItemText(5, _translate("MainWindow", "Glass Tumbler"))
        self.addItemsButton.setText(_translate("MainWindow", "Add Item to PO"))
        self.label_6.setText(_translate("MainWindow", "ItemID:"))
        self.label_7.setText(_translate("MainWindow", "Item Name:"))
        self.label_8.setText(_translate("MainWindow", "Quantity:"))
        self.label_9.setText(_translate("MainWindow", "Color:"))
        self.label_10.setText(_translate("MainWindow", "Unit Price:"))
        item = self.itemDetailsTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "PO Number"))
        item = self.itemDetailsTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Item ID"))
        item = self.itemDetailsTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Qty"))
        item = self.itemDetailsTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Colour"))
        item = self.itemDetailsTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Price Per Unit"))
