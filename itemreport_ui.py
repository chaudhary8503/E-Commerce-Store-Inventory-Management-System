# Form implementation generated from reading ui file 'f:\Habib University\Database Systems\Project\Project Code\supplier code\itemreport.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(765, 330)
        MainWindow.setStyleSheet("QMainWindow{\n"
"    background-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QMenuBar{\n"
"background-color: rgb(0,0,0);\n"
"}\n"
"QLabel{\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 10px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 30, 471, 261))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    margin-top: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    color: white; /* Change this to the color you want */\n"
"}\n"
"")
        self.groupBox.setObjectName("groupBox")
        self.lowStockList = QtWidgets.QTableWidget(parent=self.groupBox)
        self.lowStockList.setGeometry(QtCore.QRect(10, 50, 441, 201))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lowStockList.setFont(font)
        self.lowStockList.setStyleSheet("QTableWidget{\n"
"    background-color: rgb(0,0,0);\n"
"    gridline-color: rgb(255, 255, 255);\n"
"    color: rgb(255,255,255);\n"
"    border-radius: 10px;\n"
"    border: 2px solid rgb(255,255,255);\n"
"    selection-background-color: rgb(46, 46, 62);\n"
"}")
        self.lowStockList.setObjectName("lowStockList")
        self.lowStockList.setColumnCount(4)
        self.lowStockList.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        item.setFont(font)
        self.lowStockList.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.lowStockList.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.lowStockList.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        item.setFont(font)
        self.lowStockList.setHorizontalHeaderItem(3, item)
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(50, 20, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(490, 30, 261, 261))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    margin-top: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    color: white; /* Change this to the color you want */\n"
"}\n"
"")
        self.groupBox_2.setObjectName("groupBox_2")
        self.topSellingList = QtWidgets.QTableWidget(parent=self.groupBox_2)
        self.topSellingList.setGeometry(QtCore.QRect(10, 40, 241, 211))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.topSellingList.setFont(font)
        self.topSellingList.setStyleSheet("QTableWidget{\n"
"    background-color: rgb(0,0,0);\n"
"    gridline-color: rgb(255, 255, 255);\n"
"    color: rgb(255,255,255);\n"
"    border-radius: 10px;\n"
"    border: 2px solid rgb(255,255,255);\n"
"    selection-background-color: rgb(46, 46, 62);\n"
"}")
        self.topSellingList.setObjectName("topSellingList")
        self.topSellingList.setColumnCount(2)
        self.topSellingList.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.topSellingList.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.topSellingList.setHorizontalHeaderItem(1, item)
        self.exitButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(20, 10, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.exitButton.setFont(font)
        self.exitButton.setStyleSheet("QPushButton{\n"
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
        self.exitButton.setObjectName("exitButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 765, 21))
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
        self.groupBox.setTitle(_translate("MainWindow", "Low Stock Items"))
        item = self.lowStockList.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ItemID"))
        item = self.lowStockList.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Item Name"))
        item = self.lowStockList.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Item Colour"))
        item = self.lowStockList.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Item Quantity Left"))
        self.label.setText(_translate("MainWindow", "These items are low in stock. Place a Purchase Order for them"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Top Selling Items"))
        item = self.topSellingList.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ItemID"))
        item = self.topSellingList.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Ttl Quantity Sold"))
        self.exitButton.setText(_translate("MainWindow", "<--"))
