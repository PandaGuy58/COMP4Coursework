variable = "String"
data = (variable,)

for each in data:
    print(each)

def insert_Assignments_data(db_name):
    sql = "insert into Assignments(AssignmentName,AssignmentMark,AssignmentMaxMark) values (?,?,?)"
    List = []
    messages = ["Enter the AssignmentName or Q to exit: ","Enter the AssignmentMark or Q to exit: ","Enter the AssignmentMaxMark or Q to exit: "]
    Continue = True
    ContinueTwo = True
    userInput = input(messages[0])
    if userInput.upper() != "Q":
        List.append(userInput)
        Continue = False
        while  Continue:
            userInput = input(messages[1])
            if userInput.upper() = "Q":
                Continue = False
            else:
                try:
                    List.append(int(userInput))
                    Continue = False
                    while ContinueTwo:
                        userInput = input(messages[2])
                        if userInput.upper() = "Q":
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


