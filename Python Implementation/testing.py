import sqlite3

db_name = "database_testing.db"
select = "select AssignmentID from Assignments"

def inspectID(db_name,select):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute(select)
        IDs = cursor.fetchall()
        for each in IDs:
            print(each[0])

inspectID(db_name,select)

if len(IDs) == 0:
    print("No ClassIDs in Classes")
else:
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
    
    

        
        
            
    
    


    
