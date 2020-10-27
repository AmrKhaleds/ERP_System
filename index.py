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
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.UI_Changes()

    def UI_Changes(self):
        ## Ui Changes in Login
        
        grid= QGridLayout()
        grid.setSpacing(10)


def main ():
    app = QApplication (sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()



