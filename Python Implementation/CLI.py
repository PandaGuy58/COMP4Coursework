import sqlite3

def create_table(table_name,db_name,sql):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("select name from sqlite_master where name=?",(table_name,))
        result = cursor.fetchall()
        keep_table = True
        if len(result) != 1:
            cursor.execute(sql)
            db.commit()
        else:
            userInput = input('{0} already exists, press 1 to overwrite it and 0 to keep it: '.format(table_name))
            if userInput == "1":
                
                cursor.execute("drop table if exists {0}".format(table_name))
                #this deletes the actual table
                
                cursor.execute(sql)
                db.commit()
            elif userInput == "0":
                print("{0} was kept!".format(table_name))
            else:
                print("Invalid input!")

def create_Class_table(db_name):
    sql = """create table Class
             (ClassID integer,
             ClassName String,
             TeacherID integer,
             primary key(ClassID),
             foreign key(TeacherID) references Teacher(TeacherID))"""
    create_table("Class",db_name,sql)

    
def create_ClassUnits_table(db_name):
    sql = """create table ClassUnits
             (ClassID integer,
             ClassName string,
             primary key(ClassID))"""
    create_table(table_name,db_name,sql)
    
def create_Unit_table(db_name):
    sql = """create table Unit
          (UnitID integer,
          UnitName string,
          primary key(UnitID))"""
    create_table("ClassUnits",db_name,sql)
    
    
def create_UnitAssigments_table(db_name):
    sql = """create table UnitAssignments
          (UnitID integer,
          AssignmentID integer,
          primary key(UnitID),
          foreign key(AssignmentID) references Assignment(AssignmentID))"""
    create_table("UnitAssignments",db_name,sql)
    
def create_Assignment_table(db_name):
    sql = """create table Assignments
          (AssignmentID integer,
          AssignmentName string,
          AssignmentMark integer,
          AssignmentMaxMark integer,
          primary key(AssignmentID))"""
    create_table("Assignments",db_name,sql)
    
def create_Teacher_table(db_name):
    sql = """create table Teacher
          (TeacherID integer,
          TeacherName string,
          TeacherSurname string,
          primary key(TeacherID))"""
    create_table("Teacher",db_name,sql)
    
def create_ClassStudents_table(db_name):
    sql = """create table ClassStudents
          (ClassID integer,
          StudentID integer,
          primary key(ClassID)
          foreign key(StudentID) references Student (StudentID))"""
    create_table("ClassStudents",db_name,sql)
    
def create_Student_table(db_name):
    sql = """create table Student
          (StudentID integer,
          StudentName string,
          StudentSurname string,
          primary key (StudentID))"""
    create_table("Student",db_name,sql)

def insert_data(sql,values,db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute(sql,values)
        db.commit()



def insert_Class_data(db_name):
    Continue = True
    while Continue:
        

    ClassName = input("Insert ClassName: ")   
    
def userInput1():
    ContinueTwo = True
    while ContinueTwo == True:
        print("Choose one of the following options: ")
        print("1. create_Class_table")
        print("2. create_ClassUnits_table")
        print("3. create_Unit_table")
        print("4. create_UnitAssigments_table")
        print("5. create_Assignment_table")
        print("6. create_Teacher_table")
        print("7. create_ClassStudents_table")
        print("8. create_Student_table")
        print("Q. Exit")
        print()

        userInput = input()
        try:
            userInput = userInput.upper()
        except:
            pass
        if userInput == "Q":
            ContinueTwo = False
        elif userInput == "1":
            create_Class_table(db_name)
        elif userInput == "2":
            create_ClassUnits_table(db_name)
        elif userInput == "3":
            create_Unit_table(db_name)
        elif userInput == "4":
            create_UnitAssigments_table(db_name)
        elif userInput == "5":
            create_Assignment_table(db_name)
        elif userInput == "6":
            create_Teacher_table(db_name)
        elif userInput == "7":
            create_ClassStudents_table(db_name)
        elif userInput == "8":
            create_Student_table(db_name)

def userInput2():
    pass

def main(db_name):
    print("Welcome to CLI for electronic markbook system")
    Continue = True
    while Continue:
        print()
        print("Choose one of the following options: ")
        print("1. (Re)create a table")
        print("Q. Exit")
        print()
        userInput = input()
        try:
            userInput = userInput.upper()
        except:
            pass
        
        if userInput == "Q":
            Continue = False
            
        elif userInput == "1":
            userInput1()

if __name__ == "__main__":
    db_name = "database_testing.db"
    main(db_name)
                    

            








    
    
        
