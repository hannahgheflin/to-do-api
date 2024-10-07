import csv

#User account class
class User:
    #establish a user
    def __init__(self, username, password):
        self.username=username
        self.password=password
        tasks = []

#user tasks class
class Task:
    def __init__(self, id, description, status):
        self.id=id
        self.description=description
        self.status=status
    #add a task to a user        
    def addTask(name, description):
        return 0

#initialize array
users = []

#check if username exists already
def checkUser(newUsername):
    for User in users:
        if(User.username == newUsername):
            return 0
        else:
            return 1

#adds a new user to the array 
def addUser():
    #get username
    u = input("Username: ")
    if(checkUser(u)==1):
        pass
    else:
        print("This user already exists. Try logging in.")
        return False
        
    #get user password (user verifies by entering password twice)
    p = input("Password: ")
    pcheck = input("Renter Password: ")
    if(p==pcheck):
        newuser=User(u,p)
        #append user to array (Will eventually append to database)
        users.append(newuser)
        return True
    else:
        print("Passwords don't match.")
  
def login():
    return True
  
  
  
#main funtion menu      
def main():
    while(1):
        print("1. Create Account")
        print("2. Login")
        option = input(">>> ")
        if option=="1":
            if addUser()==True:
                break
        elif option=="2":
            if login()==True:
                break
        else:
            print("Not an option. Choose 1 or 2.")
            
    while(1):
        print("1.View Tasks")
        print("2.Add Task")
        print("3.Change status of a Task")
        print("4.Delete Task")
        opt = input(">>> ")
        
        
main()
