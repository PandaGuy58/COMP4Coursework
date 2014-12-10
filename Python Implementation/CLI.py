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
             (ClassUnitID integer,
             ClassID integer,
             UnitID integer,
             primary key(ClassUnitID),
             foreign key(UnitID) references Units(UnitID),
             foreign key(ClassID) references Classes(ClassID))"""
    create_table("ClassUnits",db_name,sql)
    
def create_Units_table(db_name):
    sql = """create table Units
          (UnitID integer,
          UnitName string,
          primary key(UnitID))"""
    create_table("Units",db_name,sql)
    
    
def create_UnitAssigments_table(db_name):
    sql = """create table UnitAssignments
          (UnitAssignmentID integer,
          UnitID integer,
          AssignmentID integer,
          primary key(UnitAssignmentID),
          foreign key(AssignmentID) references Assignments(AssignmentID)
          foreign key(UnitID) references Units(UnitID))"""
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
          (ClassStudentID integer,
          ClassID integer,
          StudentID integer,
          primary key(ClassStudentID)
          foreign key(StudentID) references Students(StudentID)
          foreign key(ClassID) references Classes(ClassID))"""
    create_table("ClassStudents",db_name,sql)
    
def create_Students_table(db_name):
    sql = """create table Students
          (StudentID integer,
          StudentName string,
          StudentSurname string,
          primary key(StudentID))"""
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
            else:
                print("Invalid input")                

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
        try:
            return IDs[0][0]
        except IndexError:
            print("No IDs in the selected table: ")

def insert_Classes_data(db_name):
    select = "select TeacherID from Teachers"
    sql = "insert into Classes(ClassName,TeacherID) values (?,?)"
    TeacherIDs = []
    TeacherIDs.append(inspectID(db_name,select))
    Continue = True
    if len(TeacherIDs) != 0:
        print("TeacherIDs in the Teachers:")
        for each in TeacherIDs:
            print(each)
    else:
        print("No TeacherIDs in Teachers")
        Continue = False
    while Continue:
        userInput = input("Enter a valid TeacherID or Q to exit: ")
        try:
            userInput = int(userInput)
            if userInput in TeacherIDs:
                ClassName = input("Insert ClassName: ")
                values = (ClassName,userInput)
                insert_data(sql,values,db_name)
                Continue = False
            else:
                print("TeacherID not valid")
        except:
            userInput = userInput.upper()
            if userInput == "Q":
                Continue = False

def insert_ClassUnits_data(db_name):
    select = "select ClassID from Classes"
    selectTwo = "select UnitID from Units"
    ClassIDs = []
    ClassIDs.append(inspectID(db_name,select))
    UnitIDs = []
    UnitIDs.append(inspectID(db_name,selectTwo))
    sql = "insert into ClassUnits(ClassID,UnitID) values (?,?)"
    print("ClassIDs in the Classes table: ")
    Continue = True
    ContinueTwo = False
    if len(ClassIDs) == 0:
        print("No ClassIDs in Classes")
        Continue = False
    else:
        print("ClassIDs in Classes: ")
        for each in ClassIDs:
            print(each)
    while Continue:
        userInputOne = input("Enter a valid classID or Q to exit: ")
        try:
            userInputOne = int(userInputOne)
            if userInputOne in ClassIDs:
                Continue = False
                ContinueTwo = True
            else:
                print("ClassID not valid")
        except:
            userInputOne = userInputOne.upper()
            if userInputOne == "Q":
                Continue = False
                
    if ContinueTwo:
        if len(UnitIDs) != 0:
            print("UnitIDs in Units: ")
            for each in UnitIDs:
                print(each)
        else:
            print("No UnitIDs in Units")
            
            
    while ContinueTwo:
        userInputTwo = input("Enter a valid unitID or Q to exit: ")
        try:
            userInputTwo = int(userInputTwo)
            if userInputTwo in UnitIDs:
                ContinueTwo = False
                values = (userInputOne,userInputTwo)
                insert_data(sql,values,db_name)
            else:
                print("UnitID not valid")
        except:
            userInputTwo = userInputTwo.upper()
            if userInput == "Q":
                ContinueTwo = False       
              
def insert_Units_data(db_name):
    sql = "insert into Units(UnitName) values (?)"
    userInput = input("Enter the name of unit or Q to exit: ")
    if userInput != "q" and userInput != "Q":
        values = (userInput,)
        insert_data(sql,values,db_name)

def insert_UnitAssignments_data(db_name):
    select = "select UnitID from Units"
    selectTwo = "select AssignmentID from Assignments"
    UnitIDs = []
    UnitIDs.append(inspectID(db_name,select))
    AssignmentIDs = []
    AssignmentIDs.append(inspectID(db_name,selectTwo))
    sql = "insert into UnitAssignments(UnitID,AssignmentID) values (?,?)"
    print("UnitIDs in Units table: ")
    Continue = True
    ContinueTwo = False
    if len(UnitIDs) == 0:
        print("No UnitIDs in Units")
        Continue = False
    else:
        for each in UnitIDs:
            print(each)
    while Continue:
        userInputOne = input("Enter a valid UnitID or Q to exit: ")
        try:
            userInputOne = int(userInputOne)
            if userInputOne in UnitIDs:
                Continue = False
                ContinueTwo = True
            else:
                print("UnitID not found")
        except:
            userInputOne = userInputOne.upper()
            if userInputOne == "Q":
                Continue = False
                
    if ContinueTwo:
        if len(AssignmentIDs) == 0:
            print("No AssignmentIDs in Assignments")
            ContinueTwo = False
        else:
            print("AssignmentIDs in Assignments: ")
            for each in AssignmentIDs:
                print(each)

    while ContinueTwo:
        userInputTwo = input("Enter a valid AssignmenID or Q to exit: ")
        try:
            userInputTwo = int(userInputTwo)
            if userInputTwo in AssignmentIDs:
                ContinueTwo = False
                values = (userInputOne,userInputTwo)
                insert_data(sql,values,db_name)
            else:
                print("AssignmentID not valid")
        except:
            userInputTwo = userInputTwo.upper()
            if userInput == "Q":
                ContinueTwo = False

def insert_Assignments_data(db_name):
    sql = "insert into Assignments(AssignmentName,AssignmentMark,AssignmentMaxMark) values (?,?,?)"
    array = []
    messages = ["Enter the AssignmentName or Q to exit: ","Enter the AssignmentMark or Q to exit: ","Enter the AssignmentMaxMark or Q to exit: "]
    Continue = True
    counter = 0 
    while Continue:
        array.append(input(messages[counter]))
        if array[counter] != "Q":
            counter += 1
        else:
            Continue = False
        if counter == 3:
            Continue = False
            values = (array[0],array[1],array[2])
            insert_data(sql,values,db_name)

def insert_Teachers_data(db_name):
    sql = "insert into Teachers(TeacherName,TeacherSurname) values (?,?)"
    TeacherName = input("Enter the TeacherName or Q to exit: ")
    Continue = True
    if TeacherName == "Q" or TeacherName == "q":
        Continue = False
    if Continue:
        TeacherSurname = input("Enter the TeacherSurname or Q to exit: ")
        if TeacherName != "Q" and TeacherName != "q":
            values = (TeacherName,TeacherSurname)
            insert_data(sql,values,db_name)

def insert_ClassStudents_data(db_name):
    sql = "insert into ClassStudents(ClassID,StudentID) values(?,?)"
    select = "select ClassID from Classes"
    selectTwo = "select StudentID from Students"
    ClassIDs = []
    ClassIDs.append(inspectID(db_name,select))
    StudentIDs = []
    StudentIDs.append(inspectID(db_name,selectTwo))
    print("ClassIDs in Classes: ")
    Continue = True
    ContinueTwo = False
    if len(StudentIDs) == 0:
        print("No ClassIDs in Classes")
        Continue = False
    else:
        for each in StudentIDs:
            print(each)
    while Continue:
        userInputOne = input("Enter a valid ClassID or Q to exit: ")
        try:
            userInputOne = int(userInputOne)
            if userInputOne in ClassIDs:
                Continue = False
                ContinueTwo = True
            else:
                print("StudentID not valid")
        except:
            userInputOne = userInputOne.upper()
            if userInputOne == "Q":
                Continue = False

    if ContinueTwo:
        print("StudentIDs in Students: ")
        if len(StudentIDs) == 0:
            print("No StudentIDs in Students")
            ContinueTwo = False
        else:
            for each in StudentIDs:
                print(each)
    while ContinueTwo:
        userInputTwo = input("Enter a valid StudentID or Q to exit: ")
        try:
            userInputTwo = int(userInputTwo)
            if userInputTwo in StudentIDs:
                ContinueTwo = False
                values = (userInputOne,userInputTwo)
                insert_data(sql,values,db_name)
            else:
                print("StudentID not valid")
        except:
            userInputTwo = userInputTwo.upper()
            if userInputTwo == "Q":
                ContinueTwo = False          

def insert_Students_data(db_name):
    sql = "insert into Students(StudentName,StudentSurname) values(?,?)"
    StudentName = input("Enter the StudentName or Q to exit: ")
    Continue = True
    if StudentName == "Q" or StudentName == "q":
        Continue = False
    if Continue:
        StudentSurname = input("Enter the StudentSurname: ")
        if StudentSurname != "Q" and StudentSurname != "q":
            values = (StudentName, StudentSurname)
            insert_data(sql,values,db_name)

def userInput2(db_name):
    Continue = True
    while Continue:
        print("Choose one of the following options: ")
        print("1. insert_Classes_data")
        print("2. insert_ClassUnits_data")
        print("3. insert_Units_data")
        print("4. insert_UnitAssignments_data")
        print("5. insert_Assignments_data")
        print("6. insert_Teachers_data")
        print("7. insert_ClassStudents_data")
        print("8. insert_Students_data")
        print("Q. Exit")
        print()
        userInput = input()
        if userInput == "1":
            insert_Classes_data(db_name)
        elif userInput == "2":
            insert_ClassUnits_data(db_name)
        elif userInput == "3":
            insert_Units_data(db_name)
        elif userInput == "4":
            insert_UnitAssignments_data(db_name)
        elif userInput == "5":
            insert_Assignments_data(db_name)
        elif userInput == "6":
            insert_Teachers_data(db_name)
        elif userInput == "7":
            insert_ClassStudents_data(db_name)
        elif userInput == "8":
            insert_Students_data(db_name)
        else:
            userInput = userInput.upper()
            if userInput == "Q":
                Continue = False
            else:
                print("Invalid input")

def userInput3(db_name):
    pass

def delete_Classes_data(db_name):
    pass

def delete_ClassUnits_data(db_name):
    pass

def delete_Units_data(db_name):
    pass

def delete_UnitAssignments_data(db_name):
    pass

def delete_Assignments_data(db_name):
    pass

def delete_Teachers_data(db_name):
    pass

def delete_ClassStudents_data(db_name):
    pass

def delete_Students_data(db_name):
    pass

def userInput4(db_name):
    Continue = True
    while Continue:
        print("Choose one of the following options: ")
        print("1. delete_Classes_data")
        print("2. delete_ClassUnits_data")
        print("3. delete_Units_data")
        print("4. delete_UnitAssignments_data")
        print("5. delete_Assignments_data")
        print("6. delete_Teachers_data")
        print("7. delete_ClassStudents_data")
        print("8. delete_Students_data")
        print("Q. Exit")
        print()
        userInput = input()
        if userInput == "1":
            insert_Classes_data(db_name)
        elif userInput == "2":
            insert_ClassUnits_data(db_name)
        elif userInput == "3":
            insert_Units_data(db_name)
        elif userInput == "4":
            insert_UnitAssignments_data(db_name)
        elif userInput == "5":
            insert_Assignments_data(db_name)
        elif userInput == "6":
            insert_Teachers_data(db_name)
        elif userInput == "7":
            insert_ClassStudents_data(db_name)
        elif userInput == "8":
            insert_Students_data(db_name)
        else:
            userInput = userInput.upper()
            if userInput == "Q":
                Continue = False
            else:
                print("Invalid input")

def main(db_name):
    print("Welcome to CLI for electronic markbook system")
    Continue = True
    while Continue:
        print()
        print("Choose one of the following options: ")
        print("1. (Re)create a table")
        print("2. Enter data")
        print("3. Update data")
        print("4. Delete data")
        print("Q. Exit")
        print()
        userInput = input()
        if userInput == "1":
            userInput1(db_name)
        elif userInput == "2":
            userInput2(db_name)
        else:
            userInput = userInput.upper()
            if userInput == "Q" or userInput == "q":
                Continue = False
            else:
                print("Invalid Input")

if __name__ == "__main__":
    db_name = "database_testing.db"
    main(db_name)
                    

    
    
        
