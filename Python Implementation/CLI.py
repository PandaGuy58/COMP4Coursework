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

def create_Classes_table(db_name):
    sql = """create table Classes
             (ClassID integer,
             ClassName String,
             TeacherID integer,
             primary key(ClassID),
             foreign key(TeacherID) references Teacher(TeacherID))"""
    create_table("Classes",db_name,sql)

    
def create_ClassUnits_table(db_name):
    sql = """create table ClassUnits
             (ClassID integer,
             UnitID integer,
             primary key(ClassID)
             foreign key(UnitID) references Unit(UnitID))"""
    create_table("ClassUnits",db_name,sql)
    
def create_Units_table(db_name):
    sql = """create table Units
          (UnitID integer,
          UnitName string,
          primary key(UnitID))"""
    create_table("Units",db_name,sql)
    
    
def create_UnitAssigments_table(db_name):
    sql = """create table UnitAssignments
          (UnitID integer,
          AssignmentID integer,
          primary key(UnitID),
          foreign key(AssignmentID) references Assignment(AssignmentID))"""
    create_table("UnitAssignments",db_name,sql)
    
def create_Assignments_table(db_name):
    sql = """create table Assignments
          (AssignmentID integer,
          AssignmentName string,
          AssignmentMark integer,
          AssignmentMaxMark integer,
          primary key(AssignmentID))"""
    create_table("Assignments",db_name,sql)
    
def create_Teachers_table(db_name):
    sql = """create table Teachers
          (TeacherID integer,
          TeacherName string,
          TeacherSurname string,
          primary key(TeacherID))"""
    create_table("Teachers",db_name,sql)
    
def create_ClassStudents_table(db_name):
    sql = """create table ClassStudents
          (ClassID integer,
          StudentID integer,
          primary key(ClassID)
          foreign key(StudentID) references Student (StudentID))"""
    create_table("ClassStudents",db_name,sql)
    
def create_Students_table(db_name):
    sql = """create table Students
          (StudentID integer,
          StudentName string,
          StudentSurname string,
          primary key (StudentID))"""
    create_table("Students",db_name,sql)
    
def userInput1(db_name):
    Continue = True
    while Continue:
        print("Choose one of the following options: ")
        print("1. create_Classes_table")
        print("2. create_ClassUnits_table")
        print("3. create_Units_table")
        print("4. create_UnitAssigments_table")
        print("5. create_Assignments_table")
        print("6. create_Teachers_table")
        print("7. create_ClassStudents_table")
        print("8. create_Students_table")
        print("Q. Exit")
        print()

        userInput = input()
        if userInput == "1":
            create_Classes_table(db_name)
        elif userInput == "2":
            create_ClassUnits_table(db_name)
        elif userInput == "3":
            create_Units_table(db_name)
        elif userInput == "4":
            create_UnitAssigments_table(db_name)
        elif userInput == "5":
            create_Assignments_table(db_name)
        elif userInput == "6":
            create_Teachers_table(db_name)
        elif userInput == "7":
            create_ClassStudents_table(db_name)
        elif userInput == "8":
            create_Students_table(db_name)
        else:
            userInput = userInput.upper()
            if userInput == "Q":
                Continue = False

def insert_data(sql,values,db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute(sql,values)
        db.commit()

def inspectID(db_name,select):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute(select)
        IDs = cursor.fetchall()
        return IDs

def insert_Classes_data(db_name):
    select = "select TeacherID from Teachers"
    sql = "insert into Classes (ClassName, TeacherID) values (?,?)"
    teacherIDs = []
    teacherIDs.append(inspectID(db_name,select))
    print("Teacher IDs in the database:")
    for each in teacherIDs:
        print(each)
    Continue = True
    while Continue:
        userInput = input("Enter a valid ID or press Q to exit: ")
        try:
            userInput = userInput.upper()
            if userInput == "Q":
                Continue = False
        except:
            userInput = int(userInput)
            if userInput in teacherIDs:
                ClassName = input("Insert ClassName: ")
                values = (ClassName,userInput)
                insert_data(sql,values,db_name)

def insert_ClassUnits_data(db_name):
    pass

def insert_Units_data(db_name):
    sql = "insert into Units (UnitName,) values (?)"
    userInput = input("Enter the name of unit or Q to exit: ")
    if userInput != "q" or userInput != "Q":
        values = (userInput,)
        insert_data(sql,values,db_name)

def insert_UnitAssignments_data(db_name):
    pass

def insert_Assignments_data(db_name):
    sql = "insert into Assignments"

def insert_Teachers_data(db_name):
    pass

def insert_ClassStudents_data(db_name):
    pass

def insert_Students_data(db_name):
    pass



def userInput2(db_name):
    Continue = True
    while Continue:
        print("Choose one of the following options: ")
        print("1. insert_Class_data")

        print("Q. Exit")
        print()
        userInput = input()
        if userInput == "1":
            insert_Classes_data(db_name)
        elif userInput == "3":
            insert_Units_data(db_name)
        else:
            userInput = userInput.upper()
            if userInput == "Q":
                Continue = False        

def main(db_name):
    print("Welcome to CLI for electronic markbook system")
    Continue = True
    while Continue:
        print()
        print("Choose one of the following options: ")
        print("1. (Re)create a table")
        print("2. Enter data")
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
            userInput1(db_name)
        elif userInput == "2":
            userInput2(db_name)

if __name__ == "__main__":
    db_name = "database_testing.db"
    main(db_name)
                    

    
    
        
