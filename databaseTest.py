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

#mycursor.execute("CREATE TABLE userbase(userid int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), phoneNumber VARCHAR(10), email VARCHAR(50), city VARCHAR(25))")


mycursor.execute("INSERT INTO userbase (name, phonenumber, email, city) VALUES (%s, %s, %s, %s)", ("Tanish", '9876543210', 'user@example.com', 'new delhi'))
db.commit()

mycursor.execute("SELECT * FROM userbase")

print([x for x in mycursor])
