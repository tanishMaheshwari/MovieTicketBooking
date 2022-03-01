'''ticket book request not reaching database'''
import mysql.connector
import os
from datetime import datetime
#==========     Startup     ===============
print("Starting up...\n")
print("Date: ", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
print("\n" + "*" * 25 )
# print("Enter server IP: ")
# ip = input("-> ")
# print("Enter username: ")
# userName = input("-> ")
# print("Enter password:")
# password = input('-> ')
ip = 'localhost'
userName = 'tanish'
password = 'admin'
try:
    db = mysql.connector.connect(
        host = ip, #localhost
        user = userName, #tanish
        passwd = password, #admin
        database = 'movieTicketBooking')
    print('*' * 25 + '\nAcess Granted. WELCOME\n' + '*' * 25)
except:
    print("Acess denied. Check login details or try again later")
    os.system('pause')
    exit()
cur = db.cursor()
def cls():
    try:
        os.system("cls") # for Windows
    except:
        os.system("clear") # for linux / mac 
#================================
def createUserRecord(userName, userAge, userGender, phoneNumber, email, city):
    _x = "" 
    cur.execute("INSERT INTO userbase (name, age, gender, phoneNumber, email, city) VALUES (%s, %s, %s, %s, %s, %s)", (userName, userAge, userGender, phoneNumber, email, city))
    db.commit()
def editUserRecord(id, field, value):
    _x = "UPDATE userbase SET " + str(field) + " = '" + str(value) + "' WHERE userID = " + str(id)
    cur.execute(_x)
    db.commit()
def deleteUserRecord(userID):
    _x = "DELETE FROM userbase WHERE userID = " + str(userID)
    cur.execute(_x)
    db.commit()
#===============================
def createMovieRecord(movieName, lastDate, basePrice, details, ticketSold):
    cur.execute("INSERT INTO moviebase (name, lastDate, basePrice, details, ticketSold) VALUES (%s, %s, %s, %s, %s)", (movieName, lastDate, basePrice, details, ticketSold))
    db.commit()
def editMovieRecord(id, field, value):
    _x = "UPDATE moviebase SET " + str(field) + " = '" + str(value) + "' WHERE movieID = " + str(id)
    cur.execute(_x)
    db.commit()
def deleteMovieRecord(userID):
    _x = "DELETE FROM moviebase WHERE movieID = " + str(userID)
    cur.execute(_x)
    db.commit()
#============   TICKETBASE TABLE FUNCTION    ===
def createTicketRecord(movieID, userID, seatType, movieDate,timing, theatre, city, refreshment):
    cur.execute("INSERT INTO ticketbase (movieID, userID, seatType, movieDate, timing, theatre, city, refreshment) VALUES ({}, {}, '{}', '{}', '{}', '{}', '{}', '{}')".format(movieID, userID, seatType, movieDate,timing, theatre, city, refreshment))
    db.commit()
def editTicketRecord(id, field, value):
    _x = "UPDATE ticketbase SET " + str(field) + " = '" + str(value) + "' WHERE ticketID = " + str(id)
    cur.execute(_x)
    db.commit()
def deleteTicketRecord(userID):
    _x = "DELETE FROM ticketbase WHERE ticketID = " + str(userID)
    cur.execute(_x)
    db.commit()
#==================  RANDOM FUNCTIONS    ============
def printHeader(menu):
    print("Date: ", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    print("┌" + "─" * (len(menu) + 16) + "┐")
    print("│ Currently in: " + menu + " │")
    print("└" + "─" * (len(menu) + 16) + "┘")
    print('*' * 40)
    print()
#==========
def signIn(): #     Sign in To Admin Account 
    print('Username: admin\nPassword: admin')
    user = input("Enter username: ")
    password = input("Enter password: ")
    if user == 'admin' and password == 'admin':
        return True
    else:
        cls()
        print("Incorrect Username or Password. Please Try Again\n" + '*' * 30)
        mainMenu()
#==========
def printMovies():
    cur.execute("SELECT name FROM moviebase")
    listOfMovies = list(cur)
    listOfMovies = [listOfMovies[i][0] for i in range(len(listOfMovies)) ]
    cur.execute("SELECT lastdate FROM moviebase")
    lastDateOfMovies = list(cur)
    lastDateOfMovies = [lastDateOfMovies[i][0] for i in range(len(lastDateOfMovies)) ]
    print('┌─────┬──────────────┬─────────────┐')
    print('│S.no │  Movie Name  │  Last Date  │')
    print('├' + '─' * 5 + '┼' + '─' * 14 + '┼' + '─' * 13 + '┤')
    for i in range(len(listOfMovies)):
        print('│', i + 1,'.   │ ', listOfMovies[i], ' ' * (14 - len(listOfMovies[i]) - 1) , '│ ', lastDateOfMovies[i], ' ' * (12-len(lastDateOfMovies[i])), '│'  ,sep = '')
    print('└─────┴──────────────┴─────────────┘')
#==========
def printMovieBase():
    cur.execute("SELECT movieID FROM moviebase")
    idOfMovies = list(cur)
    idOfMovies = [idOfMovies[i][0] for i in range(len(idOfMovies)) ]
    cur.execute("SELECT name FROM moviebase")
    listOfMovies = list(cur)
    listOfMovies = [listOfMovies[i][0] for i in range(len(listOfMovies)) ]
    cur.execute("SELECT lastdate FROM moviebase")
    lastDateOfMovies = list(cur)
    lastDateOfMovies = [lastDateOfMovies[i][0] for i in range(len(lastDateOfMovies)) ]
    cur.execute("SELECT basePrice FROM moviebase")
    basePriceOfMovies = list(cur)
    basePriceOfMovies = [basePriceOfMovies[i][0] for i in range(len(basePriceOfMovies)) ]
    cur.execute("SELECT details FROM moviebase")
    detailsOfMovies = list(cur)
    detailsOfMovies = [detailsOfMovies[i][0] for i in range(len(detailsOfMovies)) ]
    cur.execute("SELECT ticketSold FROM moviebase")
    ticketSoldOfMovies = list(cur)
    ticketSoldOfMovies = [ticketSoldOfMovies[i][0] for i in range(len(ticketSoldOfMovies)) ]
    maxMovieLen = 14
    for i in range(len(listOfMovies)):
        if len(listOfMovies[i]) > maxMovieLen:
            maxMovieLen = len(listOfMovies[i]) + 2
    maxTicketLength = 14
    for i in range(len(str(ticketSoldOfMovies))):
        if len(str(ticketSoldOfMovies)[i]) > maxTicketLength:
            maxTicketLength = len(ticketSoldOfMovies[i]) + 2
    print('┌' + '─' * 5 + '┬' + '─' * maxMovieLen + '┬' + '─' * 13 + '┬' + '─' * 12 + '┬' + '─' * maxTicketLength +'┐')
    print('│S.no │ Movie Name' + ' ' * (maxMovieLen - 14 + 1) + '  │  Last Date  │ Base Price │ Tickets Sold' + ' ' * (maxTicketLength - 14 + 1) + '│')
    print('├' + '─' * 5 + '┼' + '─' * maxMovieLen + '┼' + '─' * 13 + '┼' + '─' * 12 + '┼' + '─' * 14 +'┤')
    for i in range(len(listOfMovies)):
        print('│', idOfMovies[i],'.   │ ', listOfMovies[i], ' ' * (maxMovieLen - len(listOfMovies[i]) - 1) , '│ ', lastDateOfMovies[i], '  │ ' , basePriceOfMovies[i], ' ' * (12 - len(str(basePriceOfMovies[i])) - 2), ' │ ', ticketSoldOfMovies[i],' ' * (maxTicketLength - len(str(ticketSoldOfMovies[i])) - 1),  '│ ' ,sep = '')
    print('└' + '─' * 5 + '┴' + '─' * maxMovieLen + '┴' + '─' * 13 + '┴' + '─' * 12 + '┴' + '─' * maxTicketLength +'┘')
def printUserBase():
    cur.execute("SELECT userID FROM userbase")
    idOfUsers = list(cur)
    idOfUsers = [idOfUsers[i][0] for i in range(len(idOfUsers)) ]
    cur.execute("SELECT name FROM userbase")
    listOfUsers = list(cur)
    listOfUsers = [listOfUsers[i][0] for i in range(len(listOfUsers)) ]
    cur.execute("SELECT age FROM userbase")
    ageOfUsers = list(cur)
    ageOfUsers = [ageOfUsers[i][0] for i in range(len(ageOfUsers)) ]
    cur.execute("SELECT gender FROM userbase")
    genderOfUsers = list(cur)
    genderOfUsers = [genderOfUsers[i][0] for i in range(len(genderOfUsers)) ]
    cur.execute("SELECT phoneNumber FROM userbase")
    phoneNumberOfUsers = list(cur)
    phoneNumberOfUsers = [phoneNumberOfUsers[i][0] for i in range(len(phoneNumberOfUsers)) ]
    cur.execute("SELECT email FROM userbase")
    emailOfUsers = list(cur)
    emailOfUsers = [emailOfUsers[i][0] for i in range(len(emailOfUsers)) ]
    cur.execute("SELECT city FROM userbase")
    cityOfUsers = list(cur)
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
    print('┌' + '─' * 5 + '┬' + '─' * (maxNameLen + 2) + '┬' + '─' * 7 + '┬' + '─' * 8 + '┬' + '─' * 14 + '┬' + '─' * (maxEmailLen) + '┬' + '─' * maxCityLen    +'┐')
    print('│S.no │ Name' + ' ' * (maxNameLen - 7 + 2 ) + '  │  Age  │ Gender │ Phone Number | email' + ' ' * (maxEmailLen - 7 + 1) + '│ city' + " " * (maxCityLen - 6 + 1) + "|")
    
    print('├' + '─' * 5 + '┼' + '─' * (maxNameLen + 2) + '┼' + '─' * 7 + '┼' + '─' * 8 + '┼' + '─' * 14 + '┼' + '─' * (maxEmailLen) + '┼' + '─' * maxCityLen    +'┤')
    for i in range(len(listOfUsers)):
        print('│', idOfUsers[i],'.   │ ', listOfUsers[i], ' ' * (maxNameLen - len(listOfUsers[i])  + 1) , '│  ', ageOfUsers[i], '   │   ', genderOfUsers[i],  '    │  ', phoneNumberOfUsers[i], '  │ ', emailOfUsers[i], ' ' * (maxEmailLen - len(emailOfUsers[i] ) - 2), ' │ ', cityOfUsers[i],' ' * (maxCityLen - len(cityOfUsers[i]) - 1), "│" ,sep = '')
    print('└' + '─' * 5 + '┴' + '─' * (maxNameLen + 2) + '┴' + '─' * 7 + '┴' + '─' * 8 + '┴' + '─' * 14 + '┴' + '─' * (maxEmailLen) + '┴' + '─' * maxCityLen    +'┘')
#=============================
def printTicketBase():
    cur.execute("SELECT ticketID FROM ticketbase")
    ticketID = list(cur)
    ticketID = [ticketID[i][0] for i in range(len(ticketID)) ]
    cur.execute("SELECT movieID FROM ticketbase")
    movieID = list(cur)
    movieID = [movieID[i][0] for i in range(len(movieID)) ]
    cur.execute("SELECT userID FROM ticketbase")
    userID = list(cur)
    userID = [userID[i][0] for i in range(len(userID)) ]
    cur.execute("SELECT seatType FROM ticketbase")
    seatType = list(cur)
    seatType = [seatType[i][0] for i in range((len(seatType)))]
    cur.execute("SELECT movieDate FROM ticketbase")
    movieDate = list(cur)
    movieDate = [movieDate[i][0] for i in range((len(movieDate)))]
    cur.execute("SELECT timing FROM ticketbase")
    timing = list(cur)
    timing = [timing[i][0] for i in range((len(timing)))]
    cur.execute("SELECT theatre FROM ticketbase")
    theatre = list(cur)
    theatre = [theatre[i][0] for i in range((len(theatre)))]
    cur.execute("SELECT city FROM ticketbase")
    city = list(cur)
    city = [city[i][0] for i in range((len(city)))]
    cur.execute("SELECT refreshment FROM ticketbase")
    refreshment = list(cur)
    refreshment = [refreshment[i][0] for i in range((len(refreshment)))]
    Users = []
    for i in range(len(userID)):
        Q = "SELECT userID FROM ticketbase WHERE ticketID = " + str(i + 1)
        cur.execute(Q)
        ID = cur.fetchone()[0]
        Q = "SELECT name FROM userbase WHERE userID = " + str(ID)
        cur.execute(Q)
        Users.append(cur.fetchone()[0])
    Movies = []
    for i in range(len(movieID)):
        Q = "SELECT movieID FROM ticketbase WHERE ticketID = " + str(i + 1)
        cur.execute(Q)
        ID = cur.fetchone()[0]
        Q = "SELECT name FROM moviebase WHERE movieID = " + str(ID)
        cur.execute(Q)
        Movies.append(cur.fetchone()[0])
    maxMovieLen = 12
    for i in range(len(Movies)):
        if len(Movies[i]) > maxMovieLen:
            maxMovieLen = len(Movies[i]) + 2
    maxNameLen = 6
    for i in range(len(Users)):
        if len(Users[i]) > maxNameLen:
            maxNameLen = len(Users[i]) + 2
    maxSeatLen = 6
    for i in range(len(seatType)):
        if len(seatType[i]) > maxSeatLen:
            maxSeatLen = len(seatType[i]) + 2
    maxDateLen = 10
    maxTimingLen = 10
    maxTheatreLen = 9
    for i in range(len(theatre)):
        if len(theatre[i]) > maxTheatreLen:
            maxTheatreLen = len(theatre[i]) + 2
    maxCityLen = 6
    for i in range(len(city)):
        if len(city[i]) > maxCityLen:
            maxCityLen = len(city[i]) + 2
    print('┌──────┬' + '─' * (maxNameLen + 2) + '┬' + '─' * maxMovieLen + '┬' + '─' * max(11, maxSeatLen) + '┬' + '─' * maxDateLen + '┬' + '─' * 10 + '┬' + '─' * maxTheatreLen + '┬' + '─' * maxCityLen + '┬' + '─' * 14 + '┐')
    print('│ S.No │ Name' + ' ' * (maxNameLen - 4) + ' | Movie Name' + ' ' * (maxMovieLen - 12) +  ' | Seat Type' + ' ' * (maxSeatLen - 11) + ' | Date     | Timing   | Theatre' + ' ' * (maxTheatreLen - 9) + ' | City' + ' ' * (maxCityLen - 6) + ' | Refreshments |')
    for i in range(len(Users)):
        print('├──────┼' + '─' * (maxNameLen + 2) + '┼' + '─' * maxMovieLen + '┼' + '─' * maxSeatLen + '┼' + '─' * maxDateLen + '┼' + '─' * 10 + '┼' + '─' * maxTheatreLen + '┼' + '─' * maxCityLen + '┼' + '─' * 14 + '┤')
        print('| ' + str(i + 1) + ' ' * (4 - len(str(i + 1))) + ' | ' + str(Users[i]) + ' ' * (maxNameLen - len(str(Users[i]))) + ' | ' + Movies[i] + ' ' * (maxMovieLen - len(str(Movies[i])) - 2) + ' | ' + str(seatType[i]) + ' ' * (maxSeatLen - len(str(seatType[i])) - 2) + ' | ' + str(movieDate[i]) + ' ' * (maxDateLen - len(str(movieDate[i])) - 2) + ' | ' + str(timing[i]) + ' ' * (maxTimingLen - len(str(timing[i])) - 2) + '| ' + str(theatre[i]) + ' ' * (maxTheatreLen - len(str(theatre[i])) - 2) + ' | ' + str(city[i]) + ' ' * (maxCityLen - len(str(city[i])) - 2) + ' | ' + str(refreshment[i]) + ' ' * 11 + ' | ')
    print('└──────┴' + '─' * (maxNameLen + 2) + '┴' + '─' * maxMovieLen + '┴' + '─' * max(11, maxSeatLen) + '┴' + '─' * maxDateLen + '┴' + '─' * 10 + '┴' + '─' * maxTheatreLen + '┴' + '─' * maxCityLen + '┴' + '─' * 14 + '┘')

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
            try:
                y = eval(input("-> "))
                createMovieRecord(y[0], y[1], y[2], y[3], y[4])
                cls()
                print("Movie added sucessfully.")
                adminFunctions()
                return 0
            except:
                cls()
                print("invalid Input. Please try again.")
                adminFunctions()
                return 0
        elif x == 2:
            print("Enter S.No of the Movie record you want to delete")
            try:
                y = int(input("-> "))
                Q = "DELETE FROM moviebase WHERE movieID = '" + str(y) + "'"
                cur.execute(Q)
                cls()
                print("Record deleted sucessfully")
                adminFunctions()
                return 0
            except:
                cls()
                print("Something went wrong. Please try again.")
                adminFunctions()
                return 0
        elif x == 3:
            try:
                print("Enter S.No of the Movie record you want to edit")
                y = int(input("-> "))
                print("Which field do you want to edit")
                print("NOTE: Fields are: name, lastDate, basePrice, details, ticketSold")
                z = input("-> ")
                print("Enter New Value")
                g = input("-> ")
                editMovieRecord(y, z, g)
                cls()
                print("Record edited Sucessfully")
                adminFunctions()
                return 0
            except:
                cls()
                print("Something went wrong. Please try again.")
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
            print("(<movieID>, <userID>, <seatType>, <movieDate>, <timing>, <theatre>, <city>, <refreshment>)")
            print("NOTE: put strings in ''") 
            y = eval(input("-> "))
            createUserRecord(y[0], y[1], y[2], y[3], y[4], y[5], y[6], y[7])
            cls()
            print("Ticket Record added sucessfully.")
            adminFunctions()
            return 0
        elif x == 2:
            print("Enter Record Number: ")
            try:
                y = int(input("-> "))
                deleteTicketRecord(y)
                cls()
                print("Record Deleted Sucessfully")
                adminFunctions()
                return 0
            except:
                cls()
                print("Invalid input.")
                adminFunctions()
                return 0
        elif x == 3:
            try:
                print("Enter Record Number: ")
                y = int(input("-> "))
                print("Enter Field: ")
                print("NOTE\nFields are: movieID, userID, seatType, movieDate, timing, theatre, city, refreshment")
                z = input("-> ")
                print("Enter Value: ")
                aa = input("-> ")
                editTicketRecord(y, z, aa)
                cls()
                print("Record Edited Sucessfully")
                adminFunctions()
                return 0
            except:
                cls()
                print("Invalid Input.")
                adminFunctions()
                return 0
        elif x  == 4:
            cls()
            adminFunctions()
            return 0
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
            try:
                print("Enter details in the following format: ")
                print("(<name>, <age>, <gender>, <phone number>, <email>, <city>)")
                y = eval(input("-> "))
                createUserRecord(y[0], y[1], y[2], y[3], y[4], y[5])
                cls()
                print("User added sucessfully.")
                adminFunctions()
                return 0
            except:
                cls()
                print("Invalid input.") 
                adminFunctions()
                return 0    
        elif x == 2:
            try:
                print("Enter S.No of the User record you want to delete")
                y = int(input("-> "))
                Q = "DELETE FROM userbase WHERE userID = '" + str(y) + "'"
                cur.execute(Q)
                db.commit()
                cls()
                print("Record deleted sucessfully")
                adminFunctions()
                return 0
            except:
                cls()
                print("Invalid Input")
                adminFunctions()
                return 0
        elif x == 3:
            try:
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
            except:
                cls()
                print("Invalid Input")
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
#==========
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
        cur.execute("SELECT userID FROM userbase")
        cls()
        print("User Added Sucessfully")
        print("IMPORTANT: Your User ID is", cur.fetchall()[-1][0])
        bookTicket(cur.fetchall()[-1][0])
        return 0
    elif x.lower() == 'n':
        print("Enter your ID")
        userID = int(input("-> "))
        Q = "SELECT name from userbase WHERE userID = " + str(userID)
        cur.execute(Q)
        cls()
        print("Welcome, ", cur.fetchone()[0], ".", sep = "")
        printHeader("Booking a Ticket")

        bookTicket(userID)
        return 0
    else:
        cls()
        print("Please select from y/n")
        mainMenu()
        return 0
def bookTicket(uid):
    printMovies()
    print("Enter Movie ID")
    movieID = input("-> ")
    print("Enter Date: ")
    movieDate = input("-> ")
    print("Select seat type: ")
    print("     Press 1 for Normal(Rs. 100)")
    print("     Press 2 for Executive(Rs 250)")
    print("     Press 3 for Luxury(Rs 500)")
    movieSeat = input("->")
    print("Enter Start Time: ")
    movieTiming = input("-> ")
    theatre =  ['INOX', 'PVR', 'Cinepolis', 'Carnival']
    print("Do you want refreshments(y/n): ")
    refreshment = input("-> ")
    print("Select Theatre: ")
    for i in range(len(theatre)):
        print("     Press", i + 1, "for", theatre[i])
    movieTheatre = input("-> ")
    print("Enter City: ")
    movieCity = input("-> ")
    createTicketRecord(movieID, uid, movieSeat, movieDate,movieTiming, movieTheatre,movieCity, refreshment)
    cls()
    print('Ticket Booked Sucessfully.')
    mainMenu()
    return 0
#==========
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
            cls()
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
mainMenu()