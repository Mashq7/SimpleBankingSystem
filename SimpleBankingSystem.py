import random

# function to create account
def creatAcount(name ,account_number):
    if int(account_number)<len(ids_names):
        return False
    else :
        ids_names[account_number]=name
        ids_Balance[account_number]=0
        if  len(name)==0 :
            return False
        return True


# function to deposite to account
def deposit(id,number):
    if type(number)!= int :
        return False
    else :
        ids_Balance[id]+=number
        print(f"The deposit is done ,your balance now is {ids_Balance[id]}")
        return True


#  function to withfrawal
def withdrawal(id,number):
    if number>ids_Balance[id]:
        return False
    else :
        ids_Balance[id]-=number
        print(f"The operation withdrawal is done , your balance now is {ids_Balance[id]}")
        return True


# dunction to checkbalance
def checkbalance(id):
    print(f"Hellow {ids_names[id]} your balance is {ids_Balance[id]}")


# function to transfer
def transfer(id,toid,number):
    print(f"{ids_Balance[id]}-{number}")
    ids_Balance[id]-=number
    ids_Balance[toid]+=number
    print(f"The transfer is done your account balance now is {ids_Balance[id]}")

#  function for menu
def menuop(finish):
    while finish != True:
        operation = input("What operation you want to do ? \n"
                          "1-Deposit \n"
                          "2-Transfer \n"
                          "3-Withdrawal \n"
                          "4-Check balance \n")
        if operation == "1":
            accountid = input("Please enter the account number").strip()
            dep = int(input("Please enter the amount you need to deposit").strip())
            # loop to make the user enter a number
            while deposit(accountid, dep) != True:
                print("please enter an number to deposit")
                accountid = input("Please enter the account number").strip()
                dep = int(input("Please enter the amount you need to deposit").strip())
        elif operation == "2":
            useraccount = input("Please enter the account number").strip()
            accountto = input("Plese enter the id for account you want to transfer to him").strip()
            number = input("Please enter the number of ammount you want to transfer").strip()
            transfer(useraccount, accountto, int(number))

        elif operation == "3":
            userid = input("Please enter your account number").strip()
            number = input("Please enter the number you want to withdrawal").strip()
            withdrawal(userid, int(number))
        elif operation == "4":
            userId = input("Please enter your account number").strip()
            checkbalance(userId)
        else:
            print("please enter valid number between 1-4")
        status = input("you want to do more opearation (yes/no)?").lower().strip()
        if status == "no":
            finish = True

# new acc
def newacc():
    info = input("You want to creat account (yes/no) ?").lower().strip()
    if info == "yes":
        accountnumber = random.randint(0, 32131)
        yourname = input("Please enter your name").strip()
        # loop to make user enter valid acc number
        while creatAcount(yourname, accountnumber) != True:
            print("The id you Enter is exist ")
            accountnumber = input("Please enter an account number")
            yourname = input("Please enter your name")
    else:
        print("Thank you for using our banking System")
# main
if __name__ == "__main__":
    ids_names = {"1": "John", "2": "Jane", "3": "Bob"}
    ids_Balance = {"1": 2103, "2": 20000, "3": 12341}

    check = input("Hellow , do hou have an account (yes/no)?").lower().strip()
    finish = False
    if check == "yes":
       menuop(finish)
    elif check == "no":
        newacc()
    else:
        print("There was an error in your input")