import sqlite3
import random
from polygon import Blockchain

class ATM():
    def getbalance(card, pin):
        db = sqlite3.connect("./blockchain-atm/database")
        cursor = db.cursor()

        command = "SELECT pin FROM users where card={card};".format(card=card)
        result = cursor.execute(command)

        for data in result:
            if int(data[0]) == int(pin):
                command = "SELECT balance FROM users WHERE card={card};".format(card=card)
                result = cursor.execute(command)
                for value in result:
                    return "\n\nYour bank balance is: Rs. {balance}".format(balance=value[0])
            else:
                pass

    def addbalance(card, pin, amount):
        db = sqlite3.connect("./blockchain-atm/database")
        cursor = db.cursor()

        command = "SELECT pin FROM users where card={card};".format(card=card)
        result = cursor.execute(command)

        for data in result:
            if int(data[0]) == int(pin):
                command = "SELECT balance FROM users WHERE card={card};".format(card=card)
                result = cursor.execute(command)

                for value in result:
                    newbal = int(value[0]) + int(amount)

                command = "UPDATE users SET balance={newbal} WHERE card={card};".format(newbal=newbal, card=card)
                result = cursor.execute(command)

                db.commit()

                txnid = ""

                for i in range(16):
                    txnid += str(i)

                cid = Blockchain.create(txnid, card, amount, 'deposit')

                return "\nYour updated bank balance is: Rs. {newbal}\n\nYour Polygon smart contract ID is: {cid};".format(newbal=newbal, cid=cid)
            else:
                pass

    def withdraw(card, pin, amount):
        db = sqlite3.connect("./blockchain-atm/database")
        cursor = db.cursor()

        command = "SELECT pin FROM users where card={card};".format(card=card)
        result = cursor.execute(command)

        for data in result:
            if int(data[0]) == int(pin):
                command = "SELECT balance FROM users WHERE card={card};".format(card=card)
                result = cursor.execute(command)

                for value in result:
                    newbal = int(value[0]) - int(amount)

                command = "UPDATE users SET balance={newbal} WHERE card={card};".format(newbal=newbal, card=card)
                result = cursor.execute(command)

                db.commit()

                txnid = ""

                for i in range(16):
                    txnid += str(i)

                cid = Blockchain.create(txnid, card, amount, 'deposit')

                return "\nYour updated bank balance is: Rs. {newbal}\n\nYour Polygon smart contract ID is: {cid};".format(newbal=newbal, cid=cid)
            else:
                pass

# print(ATM.getbalance('1234567890', '1234'))
# print(ATM.withdraw('1234567890', '1234', '19000'))


# print(Blockchain.create('123', '123', '123', 'withdraw'))