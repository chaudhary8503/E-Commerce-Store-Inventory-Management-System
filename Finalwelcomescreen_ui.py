# Form implementation generated from reading ui file 'f:\Habib University\Database Systems\Project\Project Code\supplier code\Finalwelcomescreen.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(886, 500)
        MainWindow.setStyleSheet("QMainWindow{\n"
"    background-color: rgb(20,20,20);\n"
"}\n"
"\n"
"QMenuBar{\n"
"background-color: rgb(20,20,20);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.exitButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(550, 340, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.exitButton.setFont(font)
        self.exitButton.setStyleSheet("QPushButton{\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 100px;\n"
"    color: #FFF;\n"
"    background-color: rgb(30, 30, 40);\n"
"    padding-left: 18px;\n"
"    padding-right: 20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border: 2px solid rgb(53, 53, 71)\n"
"}")
        self.exitButton.setObjectName("exitButton")
        self.itemButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.itemButton.setGeometry(QtCore.QRect(150, 160, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.itemButton.setFont(font)
        self.itemButton.setStyleSheet("QPushButton{\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 100px;\n"
"    color: #FFF;\n"
"    background-color: rgb(30, 30, 40);\n"
"    padding-left: 18px;\n"
"    padding-right: 20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border: 2px solid rgb(53, 53, 71)\n"
"}")
        self.itemButton.setObjectName("itemButton")
        self.suppliersButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.suppliersButton.setGeometry(QtCore.QRect(150, 250, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.suppliersButton.setFont(font)
        self.suppliersButton.setStyleSheet("QPushButton{\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 100px;\n"
"    color: #FFF;\n"
"    background-color: rgb(30, 30, 40);\n"
"    padding-left: 18px;\n"
"    padding-right: 20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border: 2px solid rgb(53, 53, 71)\n"
"}")
        self.suppliersButton.setObjectName("suppliersButton")
        self.customersButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.customersButton.setGeometry(QtCore.QRect(550, 160, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.customersButton.setFont(font)
        self.customersButton.setStyleSheet("QPushButton{\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 100px;\n"
"    color: #FFF;\n"
"    background-color: rgb(30, 30, 40);\n"
"    padding-left: 18px;\n"
"    padding-right: 20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border: 2px solid rgb(53, 53, 71)\n"
"}")
        self.customersButton.setObjectName("customersButton")
        self.orderButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.orderButton.setGeometry(QtCore.QRect(150, 340, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.orderButton.setFont(font)
        self.orderButton.setStyleSheet("QPushButton{\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 100px;\n"
"    color: #FFF;\n"
"    background-color: rgb(30, 30, 40);\n"
"    padding-left: 18px;\n"
"    padding-right: 20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border: 2px solid rgb(53, 53, 71)\n"
"}")
        self.orderButton.setObjectName("orderButton")
        self.poButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.poButton.setGeometry(QtCore.QRect(550, 250, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.poButton.setFont(font)
        self.poButton.setStyleSheet("QPushButton{\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 100px;\n"
"    color: #FFF;\n"
"    background-color: rgb(30, 30, 40);\n"
"    padding-left: 18px;\n"
"    padding-right: 20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border: 2px solid rgb(53, 53, 71)\n"
"}")
        self.poButton.setObjectName("poButton")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 70, 641, 51))
        font = QtGui.QFont()
        font.setFamily("Goudy Stout")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 10px;\n"
"}")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, -20, 811, 491))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/Pictures/qtdesignerpic.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setGeometry(QtCore.QRect(100, 310, 711, 16))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(100, 210, 711, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(450, 130, 16, 291))
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_2.raise_()
        self.exitButton.raise_()
        self.itemButton.raise_()
        self.suppliersButton.raise_()
        self.customersButton.raise_()
        self.orderButton.raise_()
        self.poButton.raise_()
        self.label.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 886, 18))
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
        self.exitButton.setText(_translate("MainWindow", "Exit"))
        self.itemButton.setText(_translate("MainWindow", "Items"))
        self.suppliersButton.setText(_translate("MainWindow", "Suppliers"))
        self.customersButton.setText(_translate("MainWindow", "Customers"))
        self.orderButton.setText(_translate("MainWindow", "Orders"))
        self.poButton.setText(_translate("MainWindow", "Purchase Orders"))
        self.label.setText(_translate("MainWindow", "Welcome to Solasta"))
