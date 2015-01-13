from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *
import sqlite3
import sys

from SQLConnection import *

class MainWindow(QMainWindow):
    """Main Window Layout"""
    #constructor
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Markbook")
        self.resize(500,500)
        #actions
        #file
        self.new_database = QAction("New Database",self)
        self.open_a_database = QAction("Open a Databse",self)
        self.close_database = QAction("Close Database",self)
        self.exit = QAction("Exit",self)        

        #view
        self.view_Assignments = QAction("Assignments",self)
        self.view_ClassStudents = QAction("Class Students",self)
        self.view_ClassUnits = QAction("Class Units",self)
        self.view_Classes = QAction("Classes",self)
        self.view_Students = QAction("Students",self)
        self.view_Teachers = QAction("Teachers",self)
        self.view_UnitAssignments = QAction("Unit Assignments",self)
        self.view_Units = QAction("Units",self)        

        #add menu the application
        self.menu = QMenuBar()
        self.file_menu = self.menu.addMenu("File")
        self.view_menu = self.menu.addMenu("View")

        #add actions to menu
        self.file_menu.addAction(self.new_database)
        self.file_menu.addAction(self.open_a_database)
        self.file_menu.addAction(self.close_database)
        self.file_menu.addAction(self.exit)

        self.view_menu.addAction(self.view_Assignments)
        self.view_menu.addAction(self.view_ClassStudents)
        self.view_menu.addAction(self.view_ClassUnits)
        self.view_menu.addAction(self.view_Classes)
        self.view_menu.addAction(self.view_Students)
        self.view_menu.addAction(self.view_Teachers)
        self.view_menu.addAction(self.view_UnitAssignments)
        self.view_menu.addAction(self.view_Units)

        #initalize menu bar
        self.setMenuBar(self.menu)

        #initialize application
        self.dbNotConnected()
        
    def dbConnected(self):
        self.view_menu.setEnabled(True)
        self.close_database.setEnabled(True)

    def dbNotConnected(self):
        self.view_menu.setEnabled(False)
        self.close_database.setEnabled(False)

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    application.exec_()    
