

import datetime 
tday = datetime.datetime.now()
import random
from getpass import getpass 

database_user = {
    4761639617: ['Abel', 'Flomo' , 'passwordAbel', 'flomoabelt@gmail.com' , 1000]
}


    
def init():
    print("Welcome to Central Bank of Liberia ! ")

    have_account = int(input("Do you have account with us: 1(yes) 2(No) /n  "))
    if (have_account  == 1):

        login()

    elif (have_account == 2):
        register()

    else:
        print("You have selected invalid option") 


def login():
     print('Central Bank of Liberia, RL')
     print("******* login ******")
     print("Date:", tday )
     account_number_from_user = int(input ("What is your account number?/n  "))

     is_valid_account_number = account_number_from_user
     
     if is_valid_account_number:
         password = getpass("What is your password:/n  ")
         bankOperation()

     else:
         print("Invalid account number or password") 
         login()  
     login_info = open("login.txt","w")           

     
def register() :
    print("****** register ****** ") 
    email = input ("What is your email address? /n  ") 
    first_name = input("What is your first name? /n  ") 
    last_name = input("What is your last name? /n  ")
    password = getpass("Create password : /n  ") 
    account_number = random.randrange(1111111111,9999999999)
    print("Your account has been created")
    print("== ==================== ==")
    print("Your account number is:",  account_number )
    print("Make sure you keep it safe")
    login()
    bankOperation() 
    file = open('register.txt','w')
    file.close()


''

def bankOperation(): 
    print(" Welcome to Central Bank of Liberia")
    print(tday)
    Selectedoption = int(input("What would you like to do, (1) Deposit, (2) Withdraw, (3) Logout, (4) Exit"))

    if (Selectedoption == 1):
        OperationDeposit() 

    elif Selectedoption == 2:
        OperationWithdraw()

    elif Selectedoption == 3:
        login()
    elif Selectedoption == 4:
        exit ()
    else:
        bankOperation()
                 

def logout ():
    login()
    f = delete()

def OperationWithdraw():
     print ("Withdraw")
     Balance = open("OperationWithdraw.txt","w")
     Balance.close()
     print(Balance)


def OperationDeposit():
    print('Deposit')    
    Balance = 'your balance is 1000dh'
    Balance = open("OperationWithdraw.txt","w")
    Balance.close() 

init()

