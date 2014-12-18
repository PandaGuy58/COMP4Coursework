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
        List = []
        try:
            for each in IDs:
                List.append(each[0])
            return List
        except IndexError:
            print("No IDs in the selected table: ")

def insert_Classes_data(db_name):
    select = "select TeacherID from Teachers"
    sql = "insert into Classes(ClassName,TeacherID) values (?,?)"
    TeacherIDs = []
    TeacherIDs = inspectID(db_name,select)
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
    ClassIDs = inspectID(db_name,select)
    UnitIDs = []
    UnitIDs = inspectID(db_name,selectTwo)
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
    UnitIDs = inspectID(db_name,select)
    AssignmentIDs = []
    AssignmentIDs = inspectID(db_name,selectTwo)
    sql = "insert into UnitAssignments(UnitID,AssignmentID) values (?,?)"
    print("UnitIDs in Units: ")
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
    List = []
    messages = ["Enter the AssignmentName or Q to exit: ","Enter the AssignmentMark or Q to exit: ","Enter the AssignmentMaxMark or Q to exit: "]
    Continue = True
    ContinueTwo = True
    userInput = input(messages[0])
    if userInput.upper() != "Q":
        List.append(userInput)
        while  Continue:
            userInput = input(messages[1])
            if userInput.upper() == "Q":
                Continue = False
            else:
                try:
                    List.append(int(userInput))
                    Continue = False
                    while ContinueTwo:
                        userInput = input(messages[2])
                        if userInput.upper() == "Q":
                            Continue = False
                        else:
                            try:
                                List.append(int(userInput))
                                ContinueTwo = False
                                values = (List[0],List[1],List[2])
                                insert_data(sql,values,db_name)
                            except:
                                print("You must enter an integer")
                except:
                    print("You must enter an integer")


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
    ClassIDs = inspectID(db_name,select)
    StudentIDs = []
    StudentIDs = inspectID(db_name,selectTwo)
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

def amend_data(db_name,sql,values):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute(sql,values)
        db.commit()

def amend_Classes_data(db_name):
    select = "select ClassID from Classes"
    IDs = inspectID(db_name,select)
    sql = "update Classes set ClassName=?, TeacherID=? where ClassID=?"
    Continue = True
    ContinueTwo = False
    if len(IDs) != 0:
        print("ClassIDs in Classes:")
        for each in IDs:
            print(each)
        while Continue:
            validID = input("Enter a valid ID or Q to exit: ")
            if validID.upper() == "Q":
                Continue = False
            else:
                try:
                    if int(validID) in IDs:
                        Continue = False
                        select = "select TeacherID from Teachers"
                        IDs = inspectID(db_name,select)
                        try:
                            if len(IDs) != 0:
                                print("TeacherIDs in Teachers:")
                                for each in IDs:
                                    print(each)
                                ContinueTwo = True
                        except:
                            print("No TeacherIDs in Teachers")
                    else:
                        print("Invalid ID")
                except:
                    print("Invalid input")

    while ContinueTwo:
        teacherID = input("Enter a valid ID or Q to exit: ")
        if int(teacherID) in IDs:
            ClassName = input("Enter ClassName or Q to exit: ")
            values = (ClassName,int(teacherID),int(validID))
            amend_data(db_name,sql,values)
            ContinueTwo = False
        else:
            print("Invalid ID")


def amend_ClassUnits_data(db_name):
    select = "select ClassUnitID from ClassUnits"
    IDs = inspectID(db_name,select)
    sql = "update ClassUnits set ClassID=?, UnitID=? where ClassUnitID=?"
    Continue = True
    ContinueTwo = False
    ContinueThree = False
    try:
        if len(IDs) != 0:
            print("ClassUnitIDs in ClassUnits: ")
            for each in IDs:
                print(each)
            while Continue:
                classUnitID = input("Enter a valid ID or Q to exit: ")
                if classUnitID.upper() == "Q":
                    Continue = False
                else:
                    try:
                        if int(classUnitID) in IDs:
                            Continue = False
                            select = "select ClassID from Classes"
                            IDs = inspectID(db_name,select)
                            try:
                                if len(IDs) != 0:
                                    print("ClassIDs from Classes:")
                                    for each in IDs:
                                        print(each)
                                    ContinueTwo = True
                            except:
                                print("No ClassIDs in Classes")
                        else:
                            print("Invalid ID")
                    except:
                        print("Invalid input")
    except:
        print("No ClassIDs in Classes")

    while ContinueTwo:
        classID = input("Enter a valid ID or Q to exit: ")
        if classID.upper() == "Q":
            ContinueTwo = False
        else:
            try:
                if int(classID) in IDs:
                    ContinueTwo = False
                    select = "select UnitID from Units"
                    IDs = inspectID(db_name,select)
                    try:
                        if len(IDs) != 0:
                            print("UnitIDs in Units")
                            for each in IDs:
                                print(each)
                            ContinueThree = True
                    except:
                        print("No UnitIDs in Units")
                else:
                    print("Invalid ID")
            except:
                print("Invalid input")
                
    while ContinueThree:
        validID3 = input("Enter a valid ID or Q to exit: ")
        if validID3.upper() == "Q":
            ContinueThree = False
        else:
            if int(validID3) in IDs:
                ContinueThree = False
                values = (int(classID),int(validID3),int(classUnitID))
                amend_data(db_name,sql,values)
            else:
                print("Invalid ID")

def amend_Units_data(db_name):
    select = "select UnitID from Units"
    IDs = inspectID(db_name,select)
    sql = "update Units set UnitName=? where UnitID=?"
    Continue = True
    print("UnitIDs in Units: ")
    for each in IDs:
        print(each)
    while Continue:
        validID = input("Enter a valid ID or Q to exit")
        if validID.upper() == "Q":
            Continue = False
        else:
            try:
                if int(validID) in IDs:
                    Continue = False
                    UnitName = input("Enter unit name: ")
                    values = (UnitName,int(validID))
                    amend_data(db_name,sql,values)
                else:
                    print("Invalid ID")
            except:
                print("Invalid input")

def amend_UnitAssignments_data(db_name):
    select = "select UnitAssignmentID from UnitAssignments"
    IDs = inspectID(db_name,select)
    sql = "update UnitAssignments set UnitID=?, AssignmentID=? where UnitAssignmentID=?"
    Continue = True
    ContinueTwo = False
    ContinueThree = False
    if len(IDs) != 0:
        print("UnitAssignmentIDs in UnitAssignments: ")
        for each in IDs:
            print(each)
        while Continue:
            unitAssignmentID = input("Enter a valid ID or Q to exit: ")
            if unitAssignmentID.upper() == "Q":
                Continue = False
            else:
                    if int(unitAssignmentID) in IDs:
                        Continue = False
                        select = "select UnitID from Units"
                        IDs = inspectID(db_name,select)
                        try:
                            if len(IDs) != 0:
                                print("UnitIDs in Units")
                                for each in IDs:
                                    print(each)
                                ContinueTwo = True
                        except:
                            print("No UnitIDs in Units")
                    else:
                        print("Invalid ID")


    while ContinueTwo:
        UnitID = input("Enter a valid ID or Q to exit: ")
        if UnitID.upper() == "Q":
            ContinueTwo = False
        else:
            try:
                if int(UnitID) in IDs:
                    ContinueTwo = False
                    select = "select AssignmentID from Assignments"
                    IDs = inspectID(db_name,select)
                    try:
                        if len(IDs) != 0:
                            print("AssignmentIDs in Assignments:")
                            for each in IDs:
                                print(each)
                            ContinueThree = True
                    except:
                        print("No AssignmentIDs in Assignments")
                else:
                    print("Invalid ID")
            except:
                print("Invalid input")
                
    while ContinueThree:
        AssignmentID = input("Enter a valid ID or Q to exit: ")
        if AssignmentID.upper() == "Q":
            ContinueThree = False
        else:
            if int(AssignmentID) in IDs:
                ContinueThree = False
                values = (int(UnitID),int(AssignmentID),int(unitAssignmentID))
                amend_data(db_name,sql,values)
            else:
                print("Invalid ID")
        

def amend_Assignments_data(db_name):
    select = "select AssignmentID from Assignments"
    IDs = inspectID(db_name,select)
    sql = "update Assignments set AssignmentName=?, AssignmentMark=?, AssignmentMaxMark=? where AssignmentID=?"
    messages = ["Enter the AssignmentName or Q to exit: ","Enter the AssignmentMark or Q to exit: ","Enter the AssignmentMaxMark or Q to exit: "]
    ContinueZero = True
    Continue = False
    ContinueTwo = True
    List = []
    try:
        if len(IDs) != 0:
            print("AssignmentID in Assignments: ")
            for each in IDs:
                print(each)
            while ContinueZero:
                AssignmentID = input("Insert valid AssignmentID or Q to exit: ")
                if AssignmentID.upper() == "Q":
                    ContinueZero = False
                else:
                    try:
                        if int(AssignmentID) in IDs:
                            Continue = True
                            ContinueZero = False
                        else:
                            print("Invalid ID")
                    except:
                        print("You must enter an integer")
    except:
        print("No AssignmentIDs in Assignments")
    if Continue:
        userInput = input(messages[0])
        if userInput.upper() != "Q":
            List.append(userInput)
            while  Continue:
                userInput = input(messages[1])
                if userInput.upper() == "Q":
                    Continue = False
                else:
                    try:
                        List.append(int(userInput))
                        Continue = False
                        while ContinueTwo:
                            userInput = input(messages[2])
                            if userInput.upper() == "Q":
                                Continue = False
                            else:
                                try:
                                    List.append(int(userInput))
                                    ContinueTwo = False
                                    values = (List[0],List[1],List[2],int(AssignmentID))
                                    insert_data(sql,values,db_name)
                                except:
                                    print("You must enter an integer")
                    except:
                        print("You must enter an integer")
        

def amend_Teachers_data(db_name):
    select = "select TeacherID from Teachers"
    IDs = inspectID(db_name,select)
    sql = "update Teachers set TeacherName=?, TeacherSurname=? where TeacherID=?"
    print("TeacherIDs in Teachers: ")
    Continue = True
    for each in IDs:
        print(each)
    while Continue:
        validID = input("Enter a valid ID or Q to exit")
        if validID.upper() == "Q":
            Continue = False
        else:
            try:
                if int(validID) in IDs:
                    Continue = False
                    teacherName = input("Enter TeacherName: ")
                    teacherSurname = input("Enter TeacherSurname: ")
                    values = (teacherName,teacherSurname,int(validID))
                    amend_data(db_name,sql,values)
                else:
                    print("Invalid ID")
            except:
                print("Invalid input")


def amend_ClassStudents_data(db_name):
    select = "select ClassStudentID from ClassStudents"
    IDs = inspectID(db_name,select)
    sql = "update ClassStudents set ClassID=?, StudentID=? where ClassStudentID=?"
    Continue = True
    ContinueTwo = False
    ContinueThree = False
    try:
        if len(IDs) != 0:
            print("ClassStudentIDs in ClassStudents: ")
            for each in IDs:
                print(each)
            while Continue:
                ClassStudentID = input("Enter a valid ID or Q to exit: ")
                if ClassStudentID.upper() == "Q":
                    Continue = False
                else:
                    try:
                        if int(ClassStudentID) in IDs:
                            Continue = False
                            select = "select ClassID from Classes"
                            IDs = inspectID(db_name,select)
                            try:
                                if len(IDs) != 0:
                                    print("ClassIDs in Classes")
                                    for each in IDs:
                                        print(each)
                                    ContinueTwo = True
                            except:
                                print("No ClassIDs in Classes")
                        else:
                            print("Invalid ID")
                    except:
                        print("Invalid input")
    except:
        print("No ClassStudentIDs in ClassStudents ")

    while ContinueTwo:
        ClassID = input("Enter a valid ID or Q to exit: ")
        if ClassID.upper() == "Q":
            ContinueTwo = False
        else:
            try:
                if int(ClassID) in IDs:
                    ContinueTwo = False
                    select = "select StudentID from Students"
                    IDs = inspectID(db_name,select)
                    try:
                        if len(IDs) != 0:
                            print("StudentIDs in Students:")
                            for each in IDs:
                                print(each)
                            ContinueThree = True
                    except:
                        print("No StudentIDs in Students")
                else:
                    print("Invalid ID")
            except:
                print("Invalid input")
                
    while ContinueThree:
        StudentID = input("Enter a valid ID or Q to exit: ")
        if StudentID.upper() == "Q":
            ContinueThree = False
        else:
            try:
                if int(StudentID) in IDs:
                    ContinueThree = False
                    values = (int(ClassID),int(StudentID),int(ClassStudentID))
                    amend_data(db_name,sql,values)
                else:
                    print("Invalid ID")
            except:
                print("Invalid input")

def amend_Students_data(db_name):
    select = "select StudentID from Students"
    IDs = inspectID(db_name,select)
    sql = "update Students set StudentName=?, StudentSurname=? where StudentID=?"
    print("StudentIDs in Students: ")
    Continue = True
    for each in IDs:
        print(each)
    while Continue:
        validID = input("Enter a valid ID or Q to exit")
        if validID.upper() == "Q":
            Continue = False
        else:
                if int(validID) in IDs:
                    Continue = False
                    StudentName = input("Enter StudentName: ")
                    StudentSurname = input("Enter StudentSurname: ")
                    values = (StudentName,StudentSurname,int(validID))
                    amend_data(db_name,sql,values)
                else:
                    print("Invalid ID")

def userInput3(db_name):
    Continue = True
    while Continue:
        print("Choose one of the following options: ")
        print("1. amend_Classes_data")
        print("2. amend_ClassUnits_data")
        print("3. amend_Units_data")
        print("4. amend_UnitAssignments_data")
        print("5. amend_Assignments_data")
        print("6. amend_Teachers_data")
        print("7. amend_ClassStudents_data")
        print("8. amend_Students_data")
        print("Q. Exit")
        print()
        userInput = input()
        if userInput == "1":
            amend_Classes_data(db_name)
        elif userInput == "2":
            amend_ClassUnits_data(db_name)
        elif userInput == "3":
            amend_Units_data(db_name)
        elif userInput == "4":
            amend_UnitAssignments_data(db_name)
        elif userInput == "5":
            amend_Assignments_data(db_name)
        elif userInput == "6":
            amend_Teachers_data(db_name)
        elif userInput == "7":
            amend_ClassStudents_data(db_name)
        elif userInput == "8":
            amend_Students_data(db_name)
        else:
            userInput = userInput.upper()
            if userInput == "Q":
                Continue = False
            else:
                print("Invalid input")

def delete_data(db_name,sql,data):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute(sql,data)
        db.commit()
        
def delete_Classes_data(db_name):
    sql = "delete from Classes where ClassID=?"
    select = "select ClassID from Classes"
    IDs = inspectID(db_name,select)
    Continue = True
    try:
        if len(IDs) != 0:
            print("ClassIDs in Classes:")
            for each in IDs:
                print(each)
            while Continue:
                userInput = input("Enter a valid ClassID or press Q to exit: ")
                try:
                    if int(userInput) in IDs:
                        data = (int(userInput),)
                        delete_data(db_name,sql,data)
                        Continue = False
                    else:
                        print("Invalid ClassID")
                except:
                    userInput = userInput.upper()
                    if userInput == "Q":
                        Continue = False               
    except:
        print("No ClassIDs in Classes")

def delete_ClassUnits_data(db_name):
    sql = "delete from ClassUnits where ClassUnitID=?"
    select = "select ClassUnitID from ClassUnits"
    IDs = inspectID(db_name,select)
    Continue = True
    try:
        if len(IDs) != 0:
            print("ClassUnitIDs in ClassUnits:")
            for each in IDs:
                print(each)
            while Continue:
                userInput = input("Enter a valid ClassUnitID or press Q to exit: ")
                try:
                    if int(userInput) in IDs:
                        data = (int(userInput),)
                        delete_data(db_name,sql,data)
                        Continue = False
                    else:
                        print("Invalid ClassUnitID")
                except:
                    userInput = userInput.upper()
                    if userInput == "Q":
                        Continue = False               
    except:
        print("No ClassUnitIDs in ClassUnits")

def delete_Units_data(db_name):
    sql = "delete from Units where UnitID=?"
    select = "select UnitID from Units"
    IDs = inspectID(db_name,select)
    Continue = True
    try:
        if len(IDs) != 0:
            print("UnitIDs in Units:")
            for each in IDs:
                print(each)
            while Continue:
                userInput = input("Enter a valid UnitID or press Q to exit: ")
                try:
                    if int(userInput) in IDs:
                        data = (int(userInput),)
                        delete_data(db_name,sql,data)
                        Continue = False
                    else:
                        print("Invalid UnitID")
                except:
                    userInput = userInput.upper()
                    if userInput == "Q":
                        Continue = False               
    except:
        print("No UnitIDs in Units")

def delete_UnitAssignments_data(db_name):
    sql = "delete from UnitAssignments where UnitAssignmentID=?"
    select = "select UnitAssignmentID from UnitAssignments"
    IDs = inspectID(db_name,select)
    Continue = True
    try:
        if len(IDs) != 0:
            print("UnitAssignmentIDs in UnitAssignments:")
            for each in IDs:
                print(each)
            while Continue:
                userInput = input("Enter a valid UnitAssignmentID or press Q to exit: ")
                try:
                    if int(userInput) in IDs:
                        data = (int(userInput),)
                        delete_data(db_name,sql,data)
                        Continue = False
                    else:
                        print("Invalid UnitAssignmentID")
                except:
                    userInput = userInput.upper()
                    if userInput == "Q":
                        Continue = False               
    except:
        print("No ClassIDs in Classes")

def delete_Assignments_data(db_name):
    sql = "delete from Assignments where AssignmentID=?"
    select = "select AssignmentID from Assignments"
    IDs = inspectID(db_name,select)
    Continue = True
    try:
        if len(IDs) != 0:
            print("AssignmentIDs in Assignments:")
            for each in IDs:
                print(each)
            while Continue:
                userInput = input("Enter a valid AssignmentID or press Q to exit: ")
                try:
                    if int(userInput) in IDs:
                        data = (int(userInput),)
                        delete_data(db_name,sql,data)
                        Continue = False
                    else:
                        print("Invalid AssignmentID")
                except:
                    userInput = userInput.upper()
                    if userInput == "Q":
                        Continue = False               
    except:
        print("No AssignmentID in Assignments")

def delete_Teachers_data(db_name):
    sql = "delete from Teachers where TeacherID=?"
    select = "select TeacherID from Teachers"
    IDs = inspectID(db_name,select)
    Continue = True
    try:
        if len(IDs) != 0:
            print("TeacherID in Teachers:")
            for each in IDs:
                print(each)
            while Continue:
                userInput = input("Enter a valid TeacherID or press Q to exit: ")
                try:
                    if int(userInput) in IDs:
                        data = (int(userInput),)
                        delete_data(db_name,sql,data)
                        Continue = False
                    else:
                        print("Invalid TeacherID")
                except:
                    userInput = userInput.upper()
                    if userInput == "Q":
                        Continue = False               
    except:
        print("No TeacherIDs in Teachers")

def delete_ClassStudents_data(db_name):
    sql = "delete from ClassStudents where ClassStudentID=?"
    select = "select ClassStudentID from ClassStudents"
    IDs = inspectID(db_name,select)
    Continue = True
    try:
        if len(IDs) != 0:
            print("ClassStudentIDs in ClassStudents:")
            for each in IDs:
                print(each)
            while Continue:
                userInput = input("Enter a valid ClassStudentID or press Q to exit: ")
                try:
                    if int(userInput) in IDs:
                        data = (int(userInput),)
                        delete_data(db_name,sql,data)
                        Continue = False
                    else:
                        print("Invalid ClassStudentID")
                except:
                    userInput = userInput.upper()
                    if userInput == "Q":
                        Continue = False               
    except:
        print("No ClassStudentIDs in ClassStudents")
    
def delete_Students_data(db_name):
    sql = "delete from Students where StudentID=?"
    select = "select StudentID from Students"
    IDs = inspectID(db_name,select)
    Continue = True
    try:
        if len(IDs) != 0:
            print("StudentIDs in Students:")
            for each in IDs:
                print(each)
            while Continue:
                userInput = input("Enter a valid StudentID or press Q to exit: ")
                try:
                    if int(userInput) in IDs:
                        data = (int(userInput),)
                        delete_data(db_name,sql,data)
                        Continue = False
                    else:
                        print("Invalid StudentID")
                except:
                    userInput = userInput.upper()
                    if userInput == "Q":
                        Continue = False               
    except:
        print("No StudentIDs in Students")

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
            delete_Classes_data(db_name)
        elif userInput == "2":
            delete_ClassUnits_data(db_name)
        elif userInput == "3":
            delete_Units_data(db_name)
        elif userInput == "4":
            delete_UnitAssignments_data(db_name)
        elif userInput == "5":
            delete_Assignments_data(db_name)
        elif userInput == "6":
            delete_Teachers_data(db_name)
        elif userInput == "7":
            delete_ClassStudents_data(db_name)
        elif userInput == "8":
            delete_Students_data(db_name)
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
        print("3. Amend  data")
        print("4. Delete data")
        print("Q. Exit")
        print()
        userInput = input()
        if userInput == "1":
            userInput1(db_name)
        elif userInput == "2":
            userInput2(db_name)
        elif userInput == "3":
            userInput3(db_name)            
        elif userInput == "4":
            userInput4(db_name)
        else:
            userInput = userInput.upper()
            if userInput == "Q" or userInput == "q":
                Continue = False
            else:
                print("Invalid Input")

if __name__ == "__main__":
    db_name = "database_testing.db"
    main(db_name)
                    

    
    
        
