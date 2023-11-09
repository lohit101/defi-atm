import sqlite3

class Bank():
    def getallusers():
        db = sqlite3.connect("./blockchain-atm/database")
        cursor = db.cursor()

        command = "SELECT * FROM users;"
        result = cursor.execute(command)

        for data in result:
            print(data)

    def getuser(card):
        db = sqlite3.connect("./blockchain-atm/database")
        cursor = db.cursor()

        command = "SELECT * FROM users WHERE card={card};".format(card=card)
        result = cursor.execute(command)

        for data in result:
            return data

    def adduser(card, pin):
        db = sqlite3.connect("./blockchain-atm/database")
        cursor = db.cursor()

        command = "INSERT INTO 'users'('card','pin','balance') VALUES ({card},{pin},0);".format(card=int(card), pin=int(pin))
        result = cursor.execute(command)
        db.commit()

        return "\n\nUser {card} added successfully!\n\n".format(card=card)

    def deluser(card, pin):
        db = sqlite3.connect("./blockchain-atm/database")
        cursor = db.cursor()

        command = "SELECT pin FROM users WHERE card={card};".format(card=card)
        result = cursor.execute(command)

        for data in result:
            if int(data[0]) == int(pin):
                command = "DELETE FROM users WHERE card={card};".format(card=card)
                result = cursor.execute(command)
                db.commit()
                return "\n\nUser {card} deleted successfully!\n\n".format(card=card)
            else:
                return "\n\nUser {card} could not be deleted. Enter correct PIN.\n\n".format(card=card)
                # deluser(card=card, pin=pin)
                pass


# print(Bank.deluser('123456789067890', '1234'))
# print(Bank.adduser('123456789067890', '1234'))
# print(Bank.getuser('123456789067890'))
# print(Bank.getallusers())