import random
import sys
import sqlite3

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
    except Error as e:
        print(e)


def printAll(c):
    c.execute("SELECT * FROM passwords")
    rows = c.fetchall()
    for row in rows:
        print(' - '.join(row))

create_connection('passwords.db')

c.execute('''CREATE TABLE passwords (name text, value text)''')



pswdName = input("Name? ").upper()
pswdLen = int(input("Length? "))
incSymbols = input("Include symbols? (Y/n) ").lower()

if incSymbols == 'y':
    symb = 4
else:
    symb = 3

pswd = []

for passwordLenght in range(pswdLen):
    lowUpp = random.randint(1,symb)
    if lowUpp == 1:
        pswdLetter = chr(random.randint(65,90)) #ASCII values for upper alphabet
    elif lowUpp == 2:
        pswdLetter = chr(random.randint(97,122)) #ASCII values for lower alphabet
    elif lowUpp == 3:
        pswdLetter = chr(random.randint(48,57)) #ASCII values for numbers
    elif lowUpp == 4:
        pswdLetter = chr(random.randint(32,47)) or chr(random.randint(58,64)) or chr(random.randint(92,96)) or chr(random.randint(123,126)) #ASCII values for symbols and special characters
    else:
        print("ERROR")
        sys.exit()
    pswd.append(pswdLetter)

password = (''.join(pswd))
params = (pswdName, password)
c.execute("INSERT INTO passwords VALUES (?, ?)", params)
conn.commit()


while True:
    printAll()
    delete = input("Delete something?")
    if delete == "no":
        break
    else:
        id = delete
        sql = 'DELETE FROM passwords WHERE name=?'
        c.execute(sql, (id,))
        conn.commit()
        printAll()
conn.commit()
conn.close()
