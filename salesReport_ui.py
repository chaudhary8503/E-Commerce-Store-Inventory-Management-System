# Form implementation generated from reading ui file 'f:\Habib University\Database Systems\Project\Project Code\supplier code\salesReport.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(763, 241)
        MainWindow.setStyleSheet("QMainWindow{\n"
"    background-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QMenuBar{\n"
"background-color: rgb(0,0,0);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 40, 741, 161))
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
"\n"
"QLabel{\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 10px;\n"
"}")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 101, 16))
        self.label.setObjectName("label")
        self.yearEdit = QtWidgets.QLineEdit(parent=self.groupBox)
        self.yearEdit.setGeometry(QtCore.QRect(110, 30, 131, 20))
        self.yearEdit.setStyleSheet("QLineEdit{\n"
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
        self.yearEdit.setObjectName("yearEdit")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(260, 30, 121, 16))
        self.label_2.setObjectName("label_2")
        self.monthEdit = QtWidgets.QLineEdit(parent=self.groupBox)
        self.monthEdit.setGeometry(QtCore.QRect(390, 30, 131, 20))
        self.monthEdit.setStyleSheet("QLineEdit{\n"
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
        self.monthEdit.setObjectName("monthEdit")
        self.generateButton = QtWidgets.QPushButton(parent=self.groupBox)
        self.generateButton.setGeometry(QtCore.QRect(630, 120, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.generateButton.setFont(font)
        self.generateButton.setStyleSheet("QPushButton{\n"
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
        self.generateButton.setObjectName("generateButton")
        self.ordersEdit = QtWidgets.QLineEdit(parent=self.groupBox)
        self.ordersEdit.setGeometry(QtCore.QRect(110, 80, 131, 20))
        self.ordersEdit.setStyleSheet("QLineEdit{\n"
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
        self.ordersEdit.setObjectName("ordersEdit")
        self.revenueEdit = QtWidgets.QLineEdit(parent=self.groupBox)
        self.revenueEdit.setGeometry(QtCore.QRect(110, 130, 131, 20))
        self.revenueEdit.setStyleSheet("QLineEdit{\n"
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
        self.revenueEdit.setObjectName("revenueEdit")
        self.poEdit = QtWidgets.QLineEdit(parent=self.groupBox)
        self.poEdit.setGeometry(QtCore.QRect(390, 80, 131, 20))
        self.poEdit.setStyleSheet("QLineEdit{\n"
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
        self.poEdit.setObjectName("poEdit")
        self.expensesEdit = QtWidgets.QLineEdit(parent=self.groupBox)
        self.expensesEdit.setGeometry(QtCore.QRect(390, 130, 131, 20))
        self.expensesEdit.setStyleSheet("QLineEdit{\n"
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
        self.expensesEdit.setObjectName("expensesEdit")
        self.netProfitEdit = QtWidgets.QLineEdit(parent=self.groupBox)
        self.netProfitEdit.setGeometry(QtCore.QRect(620, 30, 113, 20))
        self.netProfitEdit.setStyleSheet("QLineEdit{\n"
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
        self.netProfitEdit.setObjectName("netProfitEdit")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 111, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 130, 111, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(260, 80, 111, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(260, 130, 111, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(540, 30, 101, 16))
        self.label_7.setObjectName("label_7")
        self.exitButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(10, 10, 71, 21))
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 763, 21))
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
        self.groupBox.setTitle(_translate("MainWindow", "Sales Report"))
        self.label.setText(_translate("MainWindow", "Enter Year:"))
        self.label_2.setText(_translate("MainWindow", "Enter Month:"))
        self.generateButton.setText(_translate("MainWindow", "Generate"))
        self.label_3.setText(_translate("MainWindow", "Total Orders"))
        self.label_4.setText(_translate("MainWindow", "Total Revenue"))
        self.label_5.setText(_translate("MainWindow", "Total PO"))
        self.label_6.setText(_translate("MainWindow", "Total Expenses"))
        self.label_7.setText(_translate("MainWindow", "Net Profit"))
        self.exitButton.setText(_translate("MainWindow", "<--"))