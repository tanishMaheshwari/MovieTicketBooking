'''

    NOTE: Works on Windows ONLY
    
    To D0:
        adminFunctions ticketbase
        printTicketBase()
        Line 406
        


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


def createTicketRecord(movieID, userID, seatType, timing, theatre, city, refreshment):
    mycursor.execute("INSERT INTO ticketbase (movieID, userID, seatType, timing, theatre, city, refreshment) VALUES (%s, %s, %s, %s, %s, %s)", (movieID, userID, seatType, timing, theatre, city, refreshment))
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
        print('│', idOfMovies[i],'.   │ ', listOfMovies[i], ' ' * (maxMovieLen - len(listOfMovies[i]) - 1) , '│ ', lastDateOfMovies[i], '  │ ' , basePriceOfMovies[i], ' ' * (12 - len(str(basePriceOfMovies[i])) - 2), ' │ ', ticketSoldOfMovies[i],' ' * (maxTicketLength - len(str(ticketSoldOfMovies[i])) - 1),  '│ ' ,sep = '')

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
        

    print(listOfUsers)
    #Print
    print('┌' + '─' * 5 + '┬' + '─' * (maxNameLen + 2) + '┬' + '─' * 7 + '┬' + '─' * 8 + '┬' + '─' * 14 + '┬' + '─' * (maxEmailLen) + '┬' + '─' * maxCityLen    +'┐')
    print('│S.no │ Name' + ' ' * (maxNameLen - 7 + 2 ) + '  │  Age  │ Gender │ Phone Number | email' + ' ' * (maxEmailLen - 7 + 1) + '│ city' + " " * (maxCityLen - 6 + 1) + "|")
    
    print('├' + '─' * 5 + '┼' + '─' * (maxNameLen + 2) + '┼' + '─' * 7 + '┼' + '─' * 8 + '┼' + '─' * 14 + '┼' + '─' * (maxEmailLen) + '┼' + '─' * maxCityLen    +'┤')
    for i in range(len(listOfUsers)):
        print('│', idOfUsers[i],'.   │ ', listOfUsers[i], ' ' * (maxNameLen - len(listOfUsers[i])  + 1) , '│  ', ageOfUsers[i], '   │   ', genderOfUsers[i],  '    │  ', phoneNumberOfUsers[i], '  │ ', emailOfUsers[i], ' ' * (maxEmailLen - len(emailOfUsers[i] ) - 2), ' │ ', cityOfUsers[i],' ' * (maxCityLen - len(cityOfUsers[i]) - 1), "│" ,sep = '')

    print('└' + '─' * 5 + '┴' + '─' * (maxNameLen + 2) + '┴' + '─' * 7 + '┴' + '─' * 8 + '┴' + '─' * 14 + '┴' + '─' * (maxEmailLen) + '┴' + '─' * maxCityLen    +'┘')
    
    

#===============================================================================================================


def printTicketBase():
    
    #==========get keys
    mycursor.execute("SELECT ticketID FROM ticketbase")
    ticketID = list(mycursor)
    ticketID = [ticketID[i][0] for i in range(len(ticketID)) ]

    mycursor.execute("SELECT movieID FROM ticketbase")
    movieID = list(mycursor)
    movieID = [movieID[i][0] for i in range(len(movieID)) ]

    mycursor.execute("SELECT userID FROM ticketbase")
    userID = list(mycursor)
    userID = [userID[i][0] for i in range(len(userID)) ]


    mycursor.execute("SELECT seatType FROM ticketbase")
    seatType = list(mycursor)
    seatType = [seatType[i][0] for i in range((len(seatType)))]

    mycursor.execute("SELECT movieDate FROM ticketbase")
    movieDate = list(mycursor)
    movieDate = [movieDate[i][0] for i in range((len(movieDate)))]

    mycursor.execute("SELECT timing FROM ticketbase")
    timing = list(mycursor)
    timing = [timing[i][0] for i in range((len(timing)))]

    mycursor.execute("SELECT theatre FROM ticketbase")
    theatre = list(mycursor)
    theatre = [theatre[i][0] for i in range((len(theatre)))]

    mycursor.execute("SELECT city FROM ticketbase")
    city = list(mycursor)
    city = [city[i][0] for i in range((len(city)))]

    mycursor.execute("SELECT refreshment FROM ticketbase")
    refreshment = list(mycursor)
    refreshment = [refreshment[i][0] for i in range((len(refreshment)))]

    Users = []
    for i in range(len(userID)):
        Q = "SELECT userID FROM ticketbase WHERE ticketID = " + str(i + 1)
        mycursor.execute(Q)
        ID = mycursor.fetchone()[0]
        Q = "SELECT name FROM userbase WHERE userID = " + str(ID)
        mycursor.execute(Q)
        Users.append(mycursor.fetchone()[0])

    Movies = []
    for i in range(len(movieID)):
        Q = "SELECT movieID FROM ticketbase WHERE ticketID = " + str(i + 1)
        mycursor.execute(Q)
        ID = mycursor.fetchone()[0]
        Q = "SELECT name FROM moviebase WHERE movieID = " + str(ID)
        mycursor.execute(Q)
        Movies.append(mycursor.fetchone()[0])


    maxMovieLen = 14
    #for i in range(len())


    
    print(Users, Movies, refreshment)

    print('┌' + '─' * 5)
    print('│S.No │ Name ')





'''
    #Print
    print('┌' + '─' * 5 + '┬' + '─' * maxNameLen + '┬' + '─' * 7 + '┬' + '─' * 8 + '┬' + '─' * 14 + '┬' + '─' * (maxEmailLen) + '┬' + '─' * maxCityLen    +'┐')
    print('│S.no │ Name' + ' ' * (maxNameLen - 7 ) + '  │  Age  │ Gender │ Phone Number | email' + ' ' * (maxEmailLen - 7 + 1) + '│ city' + " " * (maxCityLen - 6 + 1) + "|")
    
    print('├' + '─' * 5 + '┼' + '─' * maxNameLen + '┼' + '─' * 7 + '┼' + '─' * 8 + '┼' + '─' * 14 + '┼' + '─' * (maxEmailLen) + '┼' + '─' * maxCityLen    +'┤')
    for i in range(len(listOfUsers)):
        print('│', idOfUsers[i],'.   │ ', listOfUsers[i], ' ' * (maxNameLen - len(listOfUsers[i]) - 1) , '│  ', ageOfUsers[i], '   │   ', genderOfUsers[i],  '    │  ', phoneNumberOfUsers[i], '  │ ', emailOfUsers[i], ' ' * (maxEmailLen - len(emailOfUsers[i] ) - 2), ' │ ', cityOfUsers[i],' ' * (maxCityLen - len(cityOfUsers[i]) - 1), "│" ,sep = '')

    print('└' + '─' * 5 + '┴' + '─' * maxNameLen + '┴' + '─' * 7 + '┴' + '─' * 8 + '┴' + '─' * 14 + '┴' + '─' * (maxEmailLen) + '┴' + '─' * maxCityLen    +'┘')
    

'''


def adminFunctions():
    cls()
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
        else:
            cls()
            print("INVAID INPUT. Please Try Again")
            adminFunctions()
            return 0

    elif a == '2':
        cls()
        printHeader("Edit Ticket Records")

        print("Ticket Base: ")
        printTicketBase()
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
            pass
        elif x == 3:
            pass
        elif x  == 4:
            pass

        pass



    elif a == '3':
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
        else:
            cls()
            print("INVALID INPUT. Please Try Again")
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
def bookTicketCheck():
    printHeader("Booking A Ticket")
    print("Is this your first time booking a ticket?(y/n)")
    x = input("-> ")
    if x.lower() == 'y':
        cls()
        printHeader("Registering A User")
        
        print("Enter name: ")
        userName = input("-> ")

        print("Enter Age: ")
        userAge = input("-> ")
        
        print("Enter Gender(M/F/O)")
        userGender = input("-> ").upper()

        print("Enter Phone number: ")
        userPhone = input("-> ")

        print("Enter e-mail: ")
        userEmail = input("-> ")

        print("Enter City: ")
        userCity = input("-> ")

        createUserRecord(userName, userAge, userGender, userPhone, userEmail, userCity)

        cls()
        print("User Added Sucessfully")
        bookTicket(id)
        return 0
    
    elif x.lower() == 'n':
        print("Enter your ID")
        userID = int(input("-> "))
        
        Q = "SELECT name from userbase WHERE userID = " + str(userID)
        mycursor.execute(Q)
        cls()
        print("Welcome, ", mycursor.fetchone()[0], ".", sep = "")
        printHeader("Booking a Ticket")

        bookTicket(id)
        return 0


def bookTicket(id):

    
    printMovies()
    print("Enter Movie ID")
    movieID = int(input("-> "))

    print("Enter Date: ")
    movieDate = input("-> ")

    seat = ['Normal', 'Executive', 'Luxury']

    print("Select seat type: ")
    print("     Press 1 for Normal(Rs. 100)")
    print("     Press 2 for Executive(Rs 250)")
    print("     Press 3 for Luxury(Rs 500)")

    movieSeat = int(input("->"))

    print("Enter Start Time: ")
    movieTiming = input("-> ")

    theatre =  ['INOX', 'PVR', 'Cinepolis', 'Carnival']

    print("Do you want refreshments(y/n): ")
    refreshment = input("-> ")

    print("Select Theatre: ")
    for i in range(len(theatre)):
        print("     Press", i + 1, "for", theatre[i])
    
    movieTheatre = int(input("-> "))

    print("Enter City: ")
    movieCity = input("-> ")

    createTicketRecord(movieID, id, movieSeat, movieTiming, movieTheatre,movieCity, refreshment)
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
        bookTicketCheck()


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

#=======            DRIVER CODE         =======

#mainMenu()

#printUserBase()

#printMovieBase()

#printTicketBase()

#printAllTicketRecord()


mainMenu()


'''
            CODE REPO

    OLD VERSION(No SQL Integration)



import getpass as gp #Used to input the password
import os   #Used to cls the screen


listOfMovies = ['Interstellar', 'Inseption', 'Avengers', 'Pokemon']
lastDateOfMovies = ['01/01/21', '01/01/21', '01/01/21', '01/01/21']
seatType = ['Normal ( Rs 250 )', 'Executive ( Rs 500 )']
timing = ['9:00 a.m.', '12:00 p.m', '3:00 p.m', '6:00 p.m', '9:00 p.m']
theatre =  ['INOX', 'PVR', 'Cinepolis', 'Carnival']



seats = [
    ['♦', '♦', '♦', '♦', '♦', '♦', '♦', '♦'],
    ['♦', '♦', '♦', '♦', '♦', '♦', '♦', '♦'],
    ['♦', '♦', '♦', '♦', '♦', '♦', '♦', '♦'],
    ['♦', '♦', '♦', '♦', '♦', '♦', '♦', '♦'],
    ['♦', '♦', '♦', '♦', '♦', '♦', '♦', '♦'],
    ['♦', '♦', '♦', '♦', '♦', '♦', '♦', '♦'],
    ['♦', '♦', '♦', '♦', '♦', '♦', '♦', '♦'],
    ['♦', '♦', '♦', '♦', '♦', '♦', '♦', '♦']
]

tickets = {'movie' : [], 'theatre': [], 'timing': [], 'seatType': [], 'seat': [], 'refreshments' : [],  'price' : []}

#======================         FUNCTIONS       ==================================================
#=================================================================================================

#           PRINT FUNCTIONS


def printMovies():
    print('┌─────┬──────────────┬───────────┐')
    print('│S.no │  Movie Name  │ Last Date │')
    print('├' + '─' * 5 + '┼' + '─' * 14 + '┼' + '─' * 11 + '┤')
    for i in range(len(listOfMovies)):
        print('│', i + 1,'.   │ ', listOfMovies[i], ' ' * (14 - len(listOfMovies[i]) - 1) , '│ ', lastDateOfMovies[i], '  │'  ,sep = '')

    print('└─────┴──────────────┴───────────┘')

#**********************************************************************************
def printSeat():
    print("     a     b     c     d     e     f     g     h ")
    print("  ┌" + "─────┬" * 7 + "─────" + "┐" )
    for i in range(8):
        print(str(i + 1) + " │", sep = '', end = '')
        
        for j in range(8):
            print(" ", seats[i][j], " │", end = '')
            
        if i < 7:
            print("\n"  + "  ├" + "─────┼" * 7 + "─────" + "┤" )
        else:
            print("\n  └" + "─────┴" * 7 + "─────" + "┘" )
        

#=================================================================================

def printTicket(l):
    a = ['Movie', 'Theatre', 'Timings', 'Type of Seat', 'Seat', 'Refreshments', 'Total Price']
    maxLen = 0
    for i in range(len(l)):
        if maxLen < len(str(l[i])):
            maxLen = len(l[i])
    print("┌" + "─" * 16, '┬', '─' * (maxLen + 1), '┐', sep = '')
    
    for i in range(len(l)):
        print("│", end  = '', sep = '')
        print(' ', a[i], ' ' * (12 - len(a[i])), '│' , end = '')
        print(' ', l[i], ' ' * (maxLen - len(str(l[i]))), '│'   , sep = ''  )

        if i < len(l) - 1:
            print("├" + '─' * 16 + '┼' + '─' * (maxLen + 1), '┤', sep = '')
        else:
            print("└" + '─' * 16 + '┴' + '─' * (maxLen + 1), '┘', sep = '')    





#**********************************************************************************
#**********************************************************************************

#==============         Book Ticket and Helper Functions        ===================


def signIn(): #     Sign in To Admin Account 
    user = input("Enter username: ")
    password = gp.getpass(prompt="Enter password: ")

    if user == 'admin' and password == 'admin':
        return True
    else:
        os.system('cls')
        print("Incorrect Username or Password. Please Try Again\n" + '*' * 30)
        main()
#**********************************************************************************
def checkSeat(x):
    char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    col = int(char.index(x[0]))
    row = int(x[1]) - 1
    #print(row, col)
    if seats[row][col] == '♦':
        return True
    else:
        return False


#=================================================================================

def getTicket(y):
    listOfElements = list(tickets.values())
    l = []
    for i in range(len(listOfElements)):
        l.append(listOfElements[i][y])
    return l




#**********************************************************************************


def bookTicket():
        x = 0
        print("List of Movies: \n\n")
        printMovies()
        
        print("Select the Movie: ")
        
        x = int(input("-> "))
        tickets['movie'].append(listOfMovies[x - 1])

        print('\n\nSelect the theatre: \n')
        for i in theatre:
            print(str(theatre.index(i) + 1), '. ', i, sep = '')
        x = int(input("\n->"))
        tickets['theatre'].append(theatre[x - 1])
        
        
        print("\n\nSelect Type of seat: \n")
        for i in seatType:
            print(str(seatType.index(i) + 1), '. ', i, sep = '')

        x = int(input("-> "))
        tickets['seatType'].append(seatType[x - 1])

             


        print("\n\nSelect Your Seat")
        print("\nNote: ")
        print("      ♦:- Available")
        print("      X:- Not Available\n\n")
        printSeat()

        x = input("Enter seat(Eg:- g8): ")
        char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        col = int(char.index(x[0]))
        row = int(x[1]) - 1
        #print(row, col)
        if seats[row][col] == '♦':
            seats[row][col] = 'X'
            tickets['seat'].append(x)
            print("\nSeat chosen sucsessfully")
        else:
            raise

        print("\n\nDo you want refeshments(popcorn and cola) (Rs 100) y/n")
        x = input("-> ")
        if x.lower() == 'y':
            tickets['refreshments'].append(True)
        else:
            tickets['refreshments'].append(False)

        print("\n\nPlease choose the time: ")
        for i in range(len(timing)):
            print(str(i+1), '. ', timing[i], sep = '')
        x = int(input("-> "))
        tickets['timing'].append(timing[x - 1])
        tickets['price'].append(0)

        #============================
        l = getTicket(len(tickets['movie']) - 1)




        print("Your ticket has been booked ☻")
        #print(len(tickets['movie']))
        printTicket(l)
        main()



#**********************************************************************************

def adminFunctions():
    print('Press 1 to edit the available movies')
    print('Press 2 to check movie ticket records')
    print('Press 3 to view and edit seat records')
    print('Press 4 to go back to Main menu')
    
    try:
        a = int(input("Enter a number:  "))
    except:
        os.system('cls')
        print("ERROR: Please enter a valid number\n" + '*' * 30 + '\n\n')
        adminFunctions()
    if a == 1:
        print("Current List of Movies: ")
        print(listOfMovies)
        print('Press 1 to add records')
        print('Press 2 to delete records')
        print('Press 3 to edit records')
        x = int(input("\n->"))

        if x == 1:
            print("Enter Movie Name: ")
            y = input("-> ")
            print("Enter last date: ")
            z = input("->")
            listOfMovies.append(y)
            lastDateOfMovies.append(z)
            print("Movie added sucessfully.")
            print("\n\n")
            adminFunctions()
        elif x == 2:
            print(listOfMovies)
            print("Enter the number of movie you want to delete: ")
            y = int(input("->  "))
            listOfMovies.pop(y - 1)
            lastDateOfMovies.pop(y-1)
            print("Movie removed sucessfully\n\n")
            adminFunctions()
        elif x == 3:
            print("Which movie do you want to change the name of(Enter the number):  ")
            y = int(input("-> "))
            print("Enter name of the movie")
            z = input("-> ")
            print("Enter the last date of the movie: ")
            b = input("-> ")
            listOfMovies[y-1] = z
            lastDateOfMovies[y-1] = b
            print("Movie edited sucessfully\n\n")
            adminFunctions()

    elif a == 2:
        print("Do you want to view all records? y/n")
        x = input('-> ')
        if x.lower() == 'y':
            #printAllTicket
            for i in range(len(tickets['movie'])):
                printTicket(getTicket(i))
            
        elif x.lower() == 'n':
            print("Which record do you want to see(Enter number): ")
            y = int(input('-> '))
            printTicket(getTicket(y - 1))
        print('\n\n')
        adminFunctions()
        
    elif a == 3:
        print("\n\nSelect The Seat")
        print("\nNote: ")
        print("      ♦:- Available")
        print("      X:- Not Available\n\n")
        printSeat()

        x = input("Enter seat(Eg:- g8) \n-> ")
        char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        col = int(char.index(x[0]))
        row = int(x[1]) - 1
        print("Press 1. to set to available")
        print('Press 2. to set to booked')
        y = int(input("-> "))
        if y == 1:
            seats[row][col] = '♦'
            print("Seat", x, "changed to ♦\n\n")
            adminFunctions()
        else:
            seats[row][col] = 'X'
            print('Seat', x, 'changed to X\n\n')
            adminFunctions()


    elif a == 4:
        print('\n\n')
        main()
    
    else:
        print("Please enter a valid number\n\n")
        print("*" * 30)
        adminFunctions()
    


#*********************************************************************************
def main():
    print('Press 1 to view the movies available in theatres ')
    print('Press 2 book a ticket')
    print('Press 3 to sign in as admin')
    print('Press 4 to Quit')

    try:
        a = int(input("Enter a number:  "))
    except:
        os.system('cls')
        print("ERROR: Please enter a valid number\n" + '*' * 30 + '\n')
        main()
    
    #Case select

    if a == 1:
        printMovies()
        main()
    elif a == 2:
        bookTicket()
        


    elif a == 3:
        if signIn():
            print("Access granted\n\n")
            adminFunctions()

        
    elif a == 4:
        print("Thank you for using the program ☺☻")
        
    else:
        os.system('cls')
        print("ERROR: Please enter a valid number\n" + '*' * 30 + '\n')
        main()




if __name__ == "__main__":
    print("Movie Ticket Booking Software")
    print("Made by Tanish M and Rohan P")
    print('*' * 30)
    print()
    main()


'''