from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *
import sqlite3
import sys

class Window(QMainWindow):
    """Main Windows Layout"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Markbook")

        self.teacher_login = QAction("Login as a teacher",self)
        self.admin_login = QAction("Log in as an administrator",self)
        
        self.open_database = QAction("Open Database",self)
        self.close_database = QAction("Close Database",self)
        
        self.view_ClassUnits = QAction("View ClassUnits",self)
        self.view_Units = QAction("View Units",self)
        self.view_UnitAssignments = QAction("View UnitAssignments",self)
        self.view_Assignments = QAction("View Assignments",self)
        self.view_Teachers = QAction("View Teachers",self)
        self.view_ClassStudents = QAction("View ClassStudents",self)
        self.view_Students = QAction("View Students",self)
        self.view_Classes = QAction("View Classes",self)
        
        self.menu = QMenuBar()
        
        
        self.database_toolbar = QToolBar()
        self.database_menu = self.menu.addMenu("Database")
        self.data_menu = self.menu.addMenu("Data")

        self.database_menu.addAction(self.open_database)
        self.database_menu.addAction(self.close_database)

        self.data_menu.addAction(self.view_data)

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = Window()
    window.show()
    window.raise_()
    application.exec_()    
