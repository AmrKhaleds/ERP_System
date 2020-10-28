from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import MySQLdb
from PyQt5.uic import loadUiType
import datetime
from xlrd import *
from xlsxwriter import *

login,_ = loadUiType('Login.ui') ######## Login Window ###########

ui,_ = loadUiType ('Main_Window.ui') ########## Main Window ##########


'''class Login (QWidget , login): ################## Login Class #########
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.UI_Changes()


    def UI_Changes(self):
        ## Ui Changes in Login
        self.setFixedSize(573, 362)'''




class MainApp (QMainWindow, ui):################## Main Class #########
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.UI_Changes()
        self.handel_Bottons()

    def UI_Changes(self):
        ## Ui Changes in Login
        self.tabWidget.tabBar().setVisible(False)
        self.tabWidget.setCurrentIndex(0)
        print("in ui changes")


    def handel_Bottons (self):
        self.pushButton.clicked.connect(self.Open_File_Page)
        self.pushButton_2.clicked.connect(self.Open_Lists_Page)
        self.pushButton_3.clicked.connect(self.Open_Sales_Page)
        self.pushButton_4.clicked.connect(self.Open_Purchases_Page)
        self.pushButton_5.clicked.connect(self.Open_Items_Page)
        self.pushButton_6.clicked.connect(self.Open_Account_Page)
        self.pushButton_7.clicked.connect(self.Open_Custmers_and_vendors_Page)
        self.pushButton_8.clicked.connect(self.Open_Employees_Page)
        self.pushButton_9.clicked.connect(self.open_Reports_Page)


##########################################################################
    def Open_File_Page (self):
        self.tabWidget.setCurrentIndex(0)
        print("Page 1")
    def Open_Lists_Page(self):
        self.tabWidget.setCurrentIndex(1)
        print("Page 2")
    def Open_Sales_Page(self):
        self.tabWidget.setCurrentIndex(2)
        print("Page 3")
    def Open_Purchases_Page(self):
        self.tabWidget.setCurrentIndex(3)
        print("Page 4")
    def Open_Items_Page(self):
        self.tabWidget.setCurrentIndex(4)
        print("Page 5")
    def Open_Account_Page(self):
        self.tabWidget.setCurrentIndex(5)
        print("Page 6")
    def Open_Custmers_and_vendors_Page(self):
        self.tabWidget.setCurrentIndex(6)
        print("Page 7")
    def Open_Employees_Page(self):
        self.tabWidget.setCurrentIndex(7)
        print("Page 8")
    def open_Reports_Page(self):
        self.tabWidget.setCurrentIndex(8)
        print("Page 9")


def main ():
    app = QApplication (sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()



