import sys
def withdraw(account):
    global history
    global balance
    amount = input("Input Amount to withdraw: ")
    history[account].append("-" + amount)
    balance[account] = int(balance[account]) - int(amount)
    print("The remaining balance is: " + str(balance[account]))

def deposit(account):
    global history
    global balance
    amount = input("Input Amount to deposit: ")
    history[account].append(amount)
    balance[account] = int(balance[account]) + int(amount)
    print("New balance: " + str(balance[account]))

def transfer(account):
    global history
    global balance
    amount = input("Input Amount to transfer: ")
    destination = input("Input destination account: ")
    history[account].append("-" + amount)
    balance[account] = int(balance[account]) - int(amount)
    print("The remaining balance is: " + str(balance[account]))
    print(amount + " has been transfered to bank account " + destination)

def balance_amount(account):
    global balance
    print(balance[account])

def history_amount(account):
    global history
    print(history[account])

def command_list(account):
    command = input("Input Command: ")
    if(command == "withdraw"):
        withdraw(account)
        login(accounts, passwords)
    elif(command == "balance"):
        balance_amount(account)
        login(accounts, passwords)
    elif(command == "deposit"):
        deposit(account)
        login(accounts, passwords)
    elif(command == "transfer"):
        transfer(account)
        login(accounts, passwords)
    elif(command == "history"):
        history_amount(account)
        login(accounts, passwords)
    elif(command == "end"):
        sys.exit()
    command_list(command)


def login(accounts, passwords):
    global user_guess

    while user_guess not in accounts:
        user_guess = input("Input Username: ")

    account_id = accounts.index(user_guess)
    pass_guess = input("Input PIN: ")

    while pass_guess not in passwords[account_id]:
        pass_guess = input("Input PIN: ")

    print("Successfully Logged In")
    command_list(account_id)

accounts = ["123123", "789789"]
passwords = ["321321", "987987"]
history = [[0], [0]]
balance = [7500, 5000]

print("Accessing Bank Accounts")
print(" ")

user_guess = input("Input Bank Account Number: ")
login(accounts, passwords)
