'''

    NOTE: Works on Windows ONLY
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

        Added Function PrintAllUserRecord()
        Added Function PrintUserRecord()
        Added Function editUserRecord()
        Added Function createUserRecord()
        Added Function deleteUserRecord()
        
        


'''
import mysql.connector
import getpass as gp
import os
from datetime import datetime
#==========     Startup     ========================

print("Starting up...")
print()
print("Date: ", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

print("\n" + "*" * 25 )
"""
print("Enter server IP: ")
ip = input("-> ")
print("Enter username: ")
userName = input("-> ")
print("Enter password: \n->", end='')
password = gp.getpass(prompt='')
"""
ip = 'localhost'
userName = 'tanish'
password = 'admin'


try:
    db = mysql.connector.connect(
        host = ip, #localhost
        user = userName, #tanish
        passwd = password, #admin
        database = 'movieTicketBooking'
    )
    print('*' * 25 + '\nAcess Granted. WELCOME\n' + '*' * 25)
except:
    print("Acess denied. Check login details or try again later")
    os.system('pause')
    exit()

mycursor = db.cursor()



def cls():
    os.system("cls")

#============================================================================
#====================       MySQL Functions         =========================
#============================================================================

#============================================================================
#============       USERBASE TABLE FUNCTION         =========================

def printAllUserRecord():
    mycursor.execute("SELECT * FROM userbase ")
    allRecords = [x for x in mycursor]

    for i in range(len(allRecords)):
        for j in range(len(allRecords[i])):
            print(allRecords[i][j], " |", sep = '', end = '')
        print()
    
def printUserRecord(userID):
    _x = "SELECT * FROM userbase WHERE userid = " + str(userID)
    mycursor.execute(_x)
    record = mycursor.fetchone()
    print(record)

def createUserRecord(userName, userAge, userGender, phoneNumber, email, city):
    _x = "" 
    mycursor.execute("INSERT INTO userbase (name, age, gender, phoneNumber, email, city) VALUES (%s, %s, %s, %s, %s, %s)", (userName, userAge, userGender, phoneNumber, email, city))
    db.commit()

def editUserRecord(id, field, value):
    _x = "UPDATE userbase SET " + str(field) + " = '" + str(value) + "' WHERE userID = " + str(id)
    mycursor.execute(_x)
    db.commit()

def deleteUserRecord(userID):
    _x = "DELETE FROM userbase WHERE userID = " + str(userID)
    mycursor.execute(_x)
    db.commit()

#============================================================================
#====================       MOVIEBASE TABLE FUNCTION         ================

def printAllMovieRecord():
    mycursor.execute("SELECT * FROM moviebase")
    allRecords = [x for x in mycursor]

    for i in range(len(allRecords)):
        for j in range(len(allRecords[i])):
            print(allRecords[i][j], " |", sep = '', end = '')
        print()


def printMovieRecord(movieID):
    _x = "SELECT * FROM moviebase WHERE movieID = " + str(movieID)
    mycursor.execute(_x)
    record = mycursor.fetchone()
    print(record)


def createMovieRecord(movieName, lastDate, basePrice, details, ticketSold):
    mycursor.execute("INSERT INTO moviebase (name, lastDate, basePrice, details, ticketSold) VALUES (%s, %s, %s, %s, %s)", (movieName, lastDate, basePrice, details, ticketSold))
    db.commit()


def editMovieRecord(id, field, value):
    _x = "UPDATE moviebase SET " + str(field) + " = '" + str(value) + "' WHERE movieID = " + str(id)
    mycursor.execute(_x)
    db.commit()


def deleteMovieRecord(userID):
    _x = "DELETE FROM moviebase WHERE movieID = " + str(userID)
    mycursor.execute(_x)
    db.commit()


#============================================================================
#============        TICKETBASE TABLE FUNCTION         ======================

def printAllTicketRecord():
    mycursor.execute("SELECT * FROM ticketbase")
    allRecords = [x for x in mycursor]

    for i in range(len(allRecords)):
        for j in range(len(allRecords[i])):
            print(allRecords[i][j], " |", sep = '', end = '')
        print()


def printTicketRecord(ticketID):
    _x = "SELECT * FROM ticketbase WHERE ticketID = " + str(ticketID)
    mycursor.execute(_x)
    record = mycursor.fetchone()
    print(record)


def createTicketRecord(ticketID, movieID, userID, seatType, timing, theatre, city, refreshment):
    mycursor.execute("INSERT INTO ticketbase (ticketID, movieID, userID, seatType, timing, theatre, city, refreshment) VALUES (%s, %s, %s, %s, %s, %s, %s)", (ticketID, movieID, userID, seatType, timing, theatre, city, refreshment))
    db.commit()


def editTicketRecord(id, field, value):
    _x = "UPDATE ticketbase SET " + str(field) + " = '" + str(value) + "' WHERE ticketID = " + str(id)
    mycursor.execute(_x)
    db.commit()


def deleteTicketRecord(userID):
    _x = "DELETE FROM ticketbase WHERE ticketID = " + str(userID)
    mycursor.execute(_x)
    db.commit()

#============================================================================
#======================     END OF MYSQL FUNCTIONS      =====================
#============================================================================


#def 
def cmdSQL():
    while 1:
        x = input('->')
        if x == 'exit':
            break
        else:
            try:
                mycursor.execute(x)
                print([x for x in mycursor])
                db.commit()
            except:
                print("'", x, "' is not a recognised MySQL command.", sep = '')


#============================================================================
#==================     RANDOM FUNCTIONS       ==============================
#============================================================================
def printDateTime():
    print("Date: ", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    
def printHeader(menu):
    printDateTime()
    
    print("┌" + "─" * (len(menu) + 16) + "┐")
    print("│ Currently in: " + menu + " │")
    print("└" + "─" * (len(menu) + 16) + "┘")
    print('*' * 40)
    print()

#============================================================================
def signIn(): #     Sign in To Admin Account 
    user = input("Enter username: ")
    password = gp.getpass(prompt="Enter password: ")

    if user == 'admin' and password == 'admin':
        return True
    else:
        cls()
        print("Incorrect Username or Password. Please Try Again\n" + '*' * 30)
        mainMenu()
#============================================================================
def printMovies():
    mycursor.execute("SELECT name FROM moviebase")
    listOfMovies = list(mycursor)
    listOfMovies = [listOfMovies[i][0] for i in range(len(listOfMovies)) ]

    mycursor.execute("SELECT lastdate FROM moviebase")
    lastDateOfMovies = list(mycursor)
    lastDateOfMovies = [lastDateOfMovies[i][0] for i in range(len(lastDateOfMovies)) ]

    print('┌─────┬──────────────┬─────────────┐')
    print('│S.no │  Movie Name  │  Last Date  │')
    print('├' + '─' * 5 + '┼' + '─' * 14 + '┼' + '─' * 13 + '┤')
    for i in range(len(listOfMovies)):
        print('│', i + 1,'.   │ ', listOfMovies[i], ' ' * (14 - len(listOfMovies[i]) - 1) , '│ ', lastDateOfMovies[i], '  │'  ,sep = '')

    print('└─────┴──────────────┴─────────────┘')

#============================================================================
def printMovieBase():
    mycursor.execute("SELECT movieID FROM moviebase")
    idOfMovies = list(mycursor)
    idOfMovies = [idOfMovies[i][0] for i in range(len(idOfMovies)) ]


    
    mycursor.execute("SELECT name FROM moviebase")
    listOfMovies = list(mycursor)
    listOfMovies = [listOfMovies[i][0] for i in range(len(listOfMovies)) ]

    mycursor.execute("SELECT lastdate FROM moviebase")
    lastDateOfMovies = list(mycursor)
    lastDateOfMovies = [lastDateOfMovies[i][0] for i in range(len(lastDateOfMovies)) ]

    mycursor.execute("SELECT basePrice FROM moviebase")
    basePriceOfMovies = list(mycursor)
    basePriceOfMovies = [basePriceOfMovies[i][0] for i in range(len(basePriceOfMovies)) ]

    mycursor.execute("SELECT details FROM moviebase")
    detailsOfMovies = list(mycursor)
    detailsOfMovies = [detailsOfMovies[i][0] for i in range(len(detailsOfMovies)) ]

    mycursor.execute("SELECT ticketSold FROM moviebase")
    ticketSoldOfMovies = list(mycursor)
    ticketSoldOfMovies = [ticketSoldOfMovies[i][0] for i in range(len(ticketSoldOfMovies)) ]

    maxMovieLen = 14
    for i in range(len(listOfMovies)):
        if len(listOfMovies[i]) > maxMovieLen:
            maxMovieLen = len(listOfMovies[i]) + 2
    maxTicketLength = 14
    for i in range(len(str(ticketSoldOfMovies))):
        if len(str(ticketSoldOfMovies)[i]) > maxTicketLength:
            maxTicketLength = len(ticketSoldOfMovies[i]) + 2

    #Print
    print('┌' + '─' * 5 + '┬' + '─' * maxMovieLen + '┬' + '─' * 13 + '┬' + '─' * 12 + '┬' + '─' * maxTicketLength +'┐')
    print('│S.no │ Movie Name' + ' ' * (maxMovieLen - 14 + 1) + '  │  Last Date  │ Base Price │ Tickets Sold' + ' ' * (maxTicketLength - 14 + 1) + '│')
    print('├' + '─' * 5 + '┼' + '─' * maxMovieLen + '┼' + '─' * 13 + '┼' + '─' * 12 + '┼' + '─' * 14 +'┤')
    for i in range(len(listOfMovies)):
        print('│', idOfMovies[i],'.   │ ', listOfMovies[i], ' ' * (maxMovieLen - len(listOfMovies[i]) - 1) , '│ ', lastDateOfMovies[i], '  │ ' , basePriceOfMovies[i], ' ' * (12 - len(str(basePriceOfMovies[i])) - 2), ' │ ', ticketSoldOfMovies[i],' ' * (maxTicketLength - ticketSoldOfMovies[i] - 2),  '│ ' ,sep = '')

    print('└' + '─' * 5 + '┴' + '─' * maxMovieLen + '┴' + '─' * 13 + '┴' + '─' * 12 + '┴' + '─' * maxTicketLength +'┘')
    
def printUserBase():
    mycursor.execute("SELECT userID FROM userbase")
    idOfUsers = list(mycursor)
    idOfUsers = [idOfUsers[i][0] for i in range(len(idOfUsers)) ]



    mycursor.execute("SELECT name FROM userbase")
    listOfUsers = list(mycursor)
    listOfUsers = [listOfUsers[i][0] for i in range(len(listOfUsers)) ]

    mycursor.execute("SELECT age FROM userbase")
    ageOfUsers = list(mycursor)
    ageOfUsers = [ageOfUsers[i][0] for i in range(len(ageOfUsers)) ]

    mycursor.execute("SELECT gender FROM userbase")
    genderOfUsers = list(mycursor)
    genderOfUsers = [genderOfUsers[i][0] for i in range(len(genderOfUsers)) ]

    mycursor.execute("SELECT phoneNumber FROM userbase")
    phoneNumberOfUsers = list(mycursor)
    phoneNumberOfUsers = [phoneNumberOfUsers[i][0] for i in range(len(phoneNumberOfUsers)) ]

    mycursor.execute("SELECT email FROM userbase")
    emailOfUsers = list(mycursor)
    emailOfUsers = [emailOfUsers[i][0] for i in range(len(emailOfUsers)) ]
    
    mycursor.execute("SELECT city FROM userbase")
    cityOfUsers = list(mycursor)
    cityOfUsers = [cityOfUsers[i][0] for i in range(len(cityOfUsers)) ]
    
    maxNameLen = 8
    for i in range(len(listOfUsers)):
        if len(listOfUsers[i]) > maxNameLen:
            maxNameLen = len(listOfUsers[i]) + 2

    maxEmailLen = 6
    for i in range(len(emailOfUsers)):
        if len(emailOfUsers[i]) > maxEmailLen:
            maxEmailLen = len(emailOfUsers[i]) + 2
    
    maxCityLen = 6
    for i in range(len(cityOfUsers)):
        if len(cityOfUsers[i]) > maxCityLen:
            maxCityLen   = len(cityOfUsers[i]) + 2
        

    #Print
    print('┌' + '─' * 5 + '┬' + '─' * maxNameLen + '┬' + '─' * 7 + '┬' + '─' * 8 + '┬' + '─' * 14 + '┬' + '─' * (maxEmailLen) + '┬' + '─' * maxCityLen    +'┐')
    print('│S.no │ Name' + ' ' * (maxNameLen - 7 ) + '  │  Age  │ Gender │ Phone Number | email' + ' ' * (maxEmailLen - 7 + 1) + '│ city' + " " * (maxCityLen - 6 + 1) + "|")
    
    print('├' + '─' * 5 + '┼' + '─' * maxNameLen + '┼' + '─' * 7 + '┼' + '─' * 8 + '┼' + '─' * 14 + '┼' + '─' * (maxEmailLen) + '┼' + '─' * maxCityLen    +'┤')
    for i in range(len(listOfUsers)):
        print('│', idOfUsers[i],'.   │ ', listOfUsers[i], ' ' * (maxNameLen - len(listOfUsers[i]) - 1) , '│  ', ageOfUsers[i], '   │   ', genderOfUsers[i],  '    │  ', phoneNumberOfUsers[i], '  │ ', emailOfUsers[i], ' ' * (maxEmailLen - len(emailOfUsers[i] ) - 2), ' │ ', cityOfUsers[i],' ' * (maxCityLen - len(cityOfUsers[i]) - 1), "│" ,sep = '')

    print('└' + '─' * 5 + '┴' + '─' * maxNameLen + '┴' + '─' * 7 + '┴' + '─' * 8 + '┴' + '─' * 14 + '┴' + '─' * (maxEmailLen) + '┴' + '─' * maxCityLen    +'┘')
    
    




def adminFunctions():
    printHeader("Admin Menu")

    print('Press 1 to view and edit movie records')
    print('Press 2 to view and edit movie ticket records')
    print('Press 3 to view and edit user records')
    print('Press 4 to go back to Main menu')
    

    a = input("Enter a number:  ")
   
    if a == '1':
        cls()
        printHeader("Edit Movie Records")

        print("Movie Base: ")
        printMovieBase()
        print('Press 1 to add records')
        print('Press 2 to delete records')
        print('Press 3 to edit records')
        print("Press 4. to go back ")
        x = int(input("\n->"))

        if x == 1:
            print("Enter details in the following format: ")
            print("(<name>, <last date>, <base price>, <datails>, <tickets sold>)")
            y = eval(input("-> "))

            createMovieRecord(y[0], y[1], y[2], y[3], y[4])
            cls()
            print("Movie added sucessfully.")
            adminFunctions()
            return 0
            
        elif x == 2:
            print("Enter S.No of the Movie record you want to delete")
            y = int(input("-> "))
            Q = "DELETE FROM moviebase WHERE movieID = '" + str(y) + "'"
            mycursor.execute(Q)

            cls()
            print("Record deleted sucessfully")
            adminFunctions()
            return 0
        elif x == 3:
            print("Enter S.No of the Movie record you want to edit")
            y = int(input("-> "))
            print("Which field do you want to edit Eg: age")
            z = input("-> ")
            print("Enter New Value")
            g = input("-> ")


            editMovieRecord(y, z, g)
            cls()
            print("Record edited Sucessfully")
            adminFunctions()
            return 0
        elif x == 4:
            cls()
            print("Returning From Edit Movie Records")
            adminFunctions()
            return 0




    if a == '3':
        cls()
        printHeader("Edit User Records")

        print("User Base: ")
        printUserBase()
        print('Press 1 to add records')
        print('Press 2 to delete records')
        print('Press 3 to edit records')
        print("Press 4. to go back ")
        x = int(input("\n->"))

        if x == 1:
            print("Enter details in the following format: ")
            print("(<name>, <age>, <gender>, <phone number>, <email>, <city>)")
            y = eval(input("-> "))

            createUserRecord(y[0], y[1], y[2], y[3], y[4], y[5])
            cls()
            print("User added sucessfully.")
            adminFunctions()
            return 0
            
        elif x == 2:
            print("Enter S.No of the User record you want to delete")
            y = int(input("-> "))
            Q = "DELETE FROM userbase WHERE userID = '" + str(y) + "'"
            mycursor.execute(Q)

            cls()
            print("Record deleted sucessfully")
            adminFunctions()
            return 0
        elif x == 3:
            print("Enter S.No of the User record you want to edit")
            y = int(input("-> "))
            print("Which field do you want to edit Eg: age")
            z = input("-> ")
            print("Enter New Value")
            g = input("-> ")


            editUserRecord(y, z, g)
            cls()
            print("Record edited Sucessfully")
            adminFunctions()
            return 0
        elif x == 4:
            cls()
            print("Returning From Edit User Records")
            adminFunctions()
            return 0

    elif a == '4':
        cls()
        print('Returning from Admin Menu')
        mainMenu()
        return 0
    
    else:
        cls()
        print("Please enter a valid number")
        
        adminFunctions()
        return 0
        
#============================================================================

def mainMenu():
    
    printHeader("Main Menu")

    print("Press 1 to View Available Movie Tickets")
    print("Press 2 to book a ticket")
    print("Press 3 to login as admin")
    print("Press 4 to Quit")
    mainMenuInput = input('-> ')

    if mainMenuInput == '1':
        cls()
        printHeader("View Available Movies")
        printMovies()
        x = input("Press Enter to return to Main Menu...")
        cls()
        mainMenu()
        return 0

    elif mainMenuInput == '2':
        print("Book Ticket")


    elif mainMenuInput == '3':
        if signIn():
            print("Welcome to Admin")
            adminFunctions()
        else:
            cls()
            print("Try again")
            mainMenu()
            return 0

    elif mainMenuInput == '4':
        print("Thank you for using this program!")
        return 0
    else:
        cls()
        print("Please enter a valid input \n" + "*" * 25)
        mainMenu()
        return 0
#printUserRecord(1)

#=======            DRIVER CODE         =======
cls()
#mainMenu()

#printHeader("This is a test Header")

#printMovies()
cls()

#printMovieBase()

#printUserBase()

mainMenu()
