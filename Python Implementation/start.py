import sqlite3

def create_table(db_name,sql):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        
def create_Class_table(db_name):
    sql = """create table Class
             (ClassID integer,
             ClassName String,
             TeacherID integer,
             primary key(ClassID),
             foreign key(TeacherID) references Teacher(TeacherID))"""  
    create_table(db_name,sql)

def create_ClassUnits_table(db_name):
    sql = """create table ClassUnits
             (ClassID integer,
             ClassName string,
             primary key(ClassID))"""
    create_table(db_name,sql)

def create_Unit_table(db_name):
    sql = """create table Unit
          (UnitID integer,
          UnitName string,
          primary key(UnitID))"""
    create_table(db_name,sql)

def create_UnitAssigments_table(db_name):
    sql = """create table UnitAssignments
          (UnitID integer,
          AssignmentID integer,
          primary key(UnitID),
          foreign key(AssignmentID) references Assignment(AssignmentID))"""
    create_table(db_name,sql)

def create_Assignment_table(db_name):
    sql = """create table Assignments
          (AssignmentID integer,
          AssignmentName string,
          AssignmentMark integer,
          AssignmentMaxMark integer,
          primary key(AssignmentID))"""
    
def create_Teacher_table(db_name):
    sql = """create table Teacher
          (TeacherID integer,
          TeacherName string,
          TeacherSurname string,
          primary key(TeacherID))"""
    create_table(db_name,sql)

def create_ClassStudents_table(db_name):
    sql = """create table ClassStudents
          (ClassID integer,
          StudentID integer,
          primary key(ClassID)
          foreign key(StudentID) references Student (StudentID))"""
    create_table(db_name,sql)

def create_Student_table(db_name):
    sql = """create table Student
          (StudentID integer,
          StudentName string,
          StudentSurname string,
          primary key (StudentID))"""
    create_table(db_name,sql)

if __name__ == "__main__":
    db_name = "database_testing"
    create_Class_table(db_name)
    create_ClassUnits_table(db_name)
    create_Unit_table(db_name)
    create_UnitAssigments_table(db_name)
    create_Assignment_table(db_name)
    create_Teacher_table(db_name)
    create_ClassStudents_table(db_name)
    create_Student_table(db_name)
