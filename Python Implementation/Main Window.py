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
        self.resize(900,800)
        self.icon = QIcon(QPixmap("/icon.jpg"))
        self.setWindowIcon(self.icon)

        #Actions
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

        #Add menu to bar        
        self.menu = QMenuBar()
        self.file_toolbar = QToolBar()
        self.file_menu = self.menu.addMenu("File")
        self.data_menu = self.menu.addMenu("View")

        #add actions to menu
        self.file_menu.addAction(self.open_database)
        self.file_menu.addAction(self.close_database)

        self.file_toolbar.addAction(self.open_database)
        self.file_toolbar.addAction(self.close_database)

        self.data_menu.addAction(self.view_ClassUnits)
        self.data_menu.addAction(self.view_Units)
        self.data_menu.addAction(self.view_UnitAssignments)
        self.data_menu.addAction(self.view_Assignments)
        self.data_menu.addAction(self.view_Teachers)
        self.data_menu.addAction(self.view_ClassStudents)
        self.data_menu.addAction(self.view_Students)
        self.data_menu.addAction(self.view_Classes)      

        self.addToolBar(self.file_toolbar)
        self.setMenuBar(self.menu)

        #triggers
        self.open_database.triggered.connect(self.open_connection)

    def open_connection(self):
        path = QFileDialog.getOpenFileName()
        self.connection = SQLConnection(path)
        self.connection.open_database()

    def close_connection(self):
            

class SQLConnection:
    """An SQL Connection class"""

    def __init__(self,path):
        self.path = path
        self.db = None

    def open_database(self):
        if self.db:
            self.close_database()

        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(self.path)
        opened_ok = self.db.open()
        return opened_ok
    
    def close_database(self):
        self.db.close()
        QSqlDatabase.removeDatabase("Conn")

    def closeEvent(self,event):
        self.close_database()

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = Window()
    window.show()
    window.raise_()
    application.exec_()    
