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


class Login (QWidget , login): ################## Login Class #########
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)




class MainApp (QMainWindow, ui):################## Main Class #########
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)


def main ():
    app = QApplication (sys.argv)
    window = Login()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()



