import json
import sqlite3
import random
import base64
import datetime

class Blockchain():
    def create(txnid, card, amount, tp):
        df = []
        for i in range(4):
            x = ""
            for j in range(16):
                x += str(random.randint(0,9))
            df.append(x)

        data = {
            'txnid': txnid,
            'user': card,
            'amount': amount,
            'type': tp,
            'date': 'date',
            'chain': 'Polygon Matic',
            'det': {
                'df0': df[0],
                'df1': df[1],
                'df2': df[2],
                'df3': df[3]
            },
            'additional': {
                'add0': "",
                'add1': "",
                'add2': "",
                'add3': ""
            }
        }

        new = base64.b64encode(str(data).encode('utf-8'))
        return new

# print(base64.b64encode(json.dumps(Blockchain.create('123', '123', '123', 'withdraw'))))

# print(json.dumps(Blockchain.create('123', '123', '123', 'withdraw')))

# Blockchain.create('123', '123', '123', 'withdraw')