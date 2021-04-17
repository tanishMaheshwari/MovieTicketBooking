'''
    Things Done:
        added tanish as a user with password admin

        granted user 'tanish' all privlages to 'movieticketbooking' database
            done using GRANT all privileges ON movieticketbooking TO 'tanish';
        
        Created userbase table 

        To add Records:
            mycursor.execute("INSERT INTO userbase (name, phonenumber, email, city) VALUES (%s, %s, %s, %s)", ("Tanish", '9876543210', 'user@example.com', 'new delhi'))
            db.commit()

        To fetch Records:
            mycursor.execute("SELECT * FROM userbase")
            for i in mycursor:
                print(i)


        


'''
import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'tanish',
    passwd = 'admin',
    database = 'movieTicketBooking'
)

mycursor = db.cursor()



#   ADD RECORD
"""
mycursor.execute("INSERT INTO test1 (name, age, gender) VALUES (%s, %s, %s)", ('User 12', 11, 'F'))
db.commit()

#   VIEW ALL RECORDS
mycursor.execute("SELECT * FROM test1")

print([x for x in mycursor])
"""

"""
print("Enter 1. to add record")
print("Enter 2. to view all records")
x = int(input("\n-> "))

if x == 1:
    print("Enter Name: ")
    userName = input("\n-> ")
    
    print("\nEnter age")
    userAge = int(input("\n-> "))

    print("Enter gender(M / F / O)")
    userGender = input("\n-> ")

    mycursor.execute("INSERT INTO test1 (name, age, gender) VALUES (%s, %s, %s)", (userName, userAge, userGender))
    db.commit()

    print("\n\nData Entered Sucessfully")

elif x == 2:
    mycursor.execute("SELECT * FROM test1")
    print([x for x in mycursor])

"""

def printAllUserRecord():
    mycursor.execute("SELECT * FROM test1 ")
    allRecords = [x for x in mycursor]

    for i in range(len(allRecords)):
        for j in range(len(allRecords[i])):
            print(allRecords[i][j], " |", sep = '', end = '')
        print()
    
def printUserRecord(x):
    _x = "SELECT * FROM test1 WHERE id = " + str(x)
    mycursor.execute(_x)
    record = mycursor.fetchone()
    print(record)

def editUserRecord(id, field, value):
    _x = "UPDATE test1 SET " + str(field) + " = '" + str(value) + "' WHERE id = " + str(id)
    mycursor.execute(_x)
    db.commit()

def createUserRecord(userName, userAge, userGender):
    _x = "" 
    mycursor.execute("INSERT INTO test1 (name, age, gender) VALUES (%s, %s, %s)", (userName, userAge, userGender))
    db.commit()

def deleteUserRecord(userID):
    _x = "DELETE FROM test1 WHERE id = " + str(userID)
    mycursor.execute(_x)
    db.commit()


#Actual Code


createUserRecord('User 5', '44', 'F')
editUserRecord(4, 'age', '4')
printUserRecord(5)
deleteUserRecord(5)
printAllUserRecord()
