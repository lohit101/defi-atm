from atm import ATM
from bank import Bank
from polygon import Blockchain
import time

def adminmenu():
    inp = input("\n\n+====================+\n\nPLEASE MAKE A CHOICE (ADMIN MENU):\n1. Get all users\n2. Add a user\n3. Delete a user\n\n>>> ")

    if str(inp) == '1':
        card = input("\n\nEnter Card Number: ")
        print(Bank.getusers(card))
        print("\n\nRestarting...")
        time.sleep(3)
        adminmenu()

    elif str(inp) == '2':
        card = input("\n\nEnter Card Number: ")
        pin = input("\nEnter PIN: ")
        print(Bank.adduser(card, pin))
        print("\n\nRestarting...")
        time.sleep(3)
        adminmenu()

    elif str(inp) == '3':
        card = input("\n\nEnter Card Number: ")
        pin = input("\nEnter PIN: ")
        print(Bank.deluser(card, pin))
        print("\n\nRestarting...")
        time.sleep(3)
        adminmenu()

def menu():
    inp = input("\n\n+====================+\n\nPLEASE MAKE A CHOICE:\n1. Check Bank Balance\n2. Deposit Money\n3. Withdraw Money\n\n>>> ")

    if str(inp) == '1':
        card = input("\n\nEnter Card Number: ")
        pin = input("\nEnter PIN: ")
        print(ATM.getbalance(card, pin))
        print("\n\nRestarting...")
        time.sleep(3)
        menu()

    elif str(inp) == '2':
        card = input("\n\nEnter Card Number: ")
        pin = input("\nEnter PIN: ")
        amount = input("\nEnter Amount to Deposit: ")
        print(ATM.addbalance(card, pin, amount))
        print("\n\nRestarting...")
        time.sleep(3)
        menu()

    elif str(inp) == '3':
        card = input("\n\nEnter Card Number: ")
        pin = input("\nEnter PIN: ")
        amount = input("\nEnter Amount to Deposit: ")
        print(ATM.withdraw(card, pin, amount))
        print("\n\nRestarting...")
        time.sleep(3)
        menu()

    elif str(input).lower() == 'admin':
        adminmenu()

if __name__ == '__main__':
    menu()