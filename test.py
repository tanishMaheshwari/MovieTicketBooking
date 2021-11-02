import prettytable
import mysql.connector
import os

db, mycursor = None, None


#                   ┌───── •✧✧• ─────┐
#                        FUNCTIONS 
#                   └───── •✧✧• ─────┘

def startServer():
    ip = 'localhost'
    userName = 'tanish'
    password = 'admin'

    global db, mycursor

    db = mysql.connector.connect(
        host=ip,  # localhost
        user=userName,  # tanish
        passwd=password,  # admin
        database='movieTicketBooking'
    )
    
    mycursor = db.cursor()


###
#   PRINTING FUNCTIONS
###

cls = lambda: os.system('cls')



def printUserbaseTable(): 
    mycursor.execute("DESCRIBE userbase;")
    userbaseHeadings = [x[0] for x in mycursor]

    mycursor.execute("SELECT * FROM userbase;")
    userbaseRecords = mycursor.fetchall()
    userbaseTable = prettytable.PrettyTable(userbaseHeadings)
    for i in userbaseRecords:
        userbaseTable.add_row(list(i))
    
    return userbaseTable

def printMoviebaseTable():
    mycursor.execute("DESCRIBE moviebase;")
    moviebaseHeadings = [x[0] for x in mycursor]
    mycursor.execute("SELECT * FROM moviebase;")
    moviebaseRecords = mycursor.fetchall()
    moviebaseTable = prettytable.PrettyTable(moviebaseHeadings)
    for i in moviebaseRecords:
        moviebaseTable.add_row(list(i))
    
    return moviebaseTable

def printTicketbaseTable():
    mycursor.execute("DESCRIBE ticketbase;")
    ticketbaseHeadings = [x[0] for x in mycursor]
    mycursor.execute("SELECT * FROM ticketbase;")
    ticketbaseRecords = mycursor.fetchall()
    ticketbaseTable = prettytable.PrettyTable(ticketbaseHeadings)
    for i in ticketbaseRecords:
        ticketbaseTable.add_row(list(i))
        print(list(i))
    
    return ticketbaseTable
###


def addRecords(table, data):
    if table not in ['userbase', 'ticketbase', 'moviebase']:
        print("Error Code 1.")
        exit()
    mycursor.execute("DESCRIBE " + str(table) +';') #DESCRIBE Table;
    headings = [x[0] for x in mycursor]
    mycursor.execute("INSERT INTO " + table +" (" + str([x for x  in headings[1:]])[1:-1].replace("'", "`") + ") VALUES (" + str([x for x  in data])[1:-1] + ");")
    db.commit()


def deleteRecords(table, id):
    if table not in ['userbase', 'ticketbase', 'moviebase']:
        print("Error Code 1.")
        exit()
    id = str(id)
    mycursor.execute("DESCRIBE " + table + ";")
    tableid = mycursor.fetchone()[0]
    mycursor.execute("DELETE FROM " + table + " WHERE " + tableid + " = " + id + ";")
    db.commit()

#Driver Code
if __name__ == "__main__":
    startServer()
    mycursor.execute("DESCRIBE userbase;")
    userbaseHeadings = [x[0] for x in mycursor]

    mycursor.execute("DESCRIBE ticketbase;")
    ticketbaseHeadings = [x[0] for x in mycursor]

    mycursor.execute("DESCRIBE moviebase;")
    moviebaseHeadings = [x[0] for x in mycursor]
    
    
    print(printUserbaseTable())
    # print(printMoviebaseTable())
    # print(printTicketbaseTable())



    commandsTable = prettytable.PrettyTable(['Movie Ticket Management System'])
    commandsTable.add_row(['Press 1. to View Currently Airing Movies'])
    commandsTable.add_row(['Press 2. to View all User Records'])
    commandsTable.add_row(['Press 3. to View All Ticket Records'])
    commandsTable.add_row(['Press 4. to Add User Record'])
    commandsTable.add_row(['Press 5. to Add Movie Record'])
    commandsTable.add_row(['Press 6. to Add Ticket Record'])
    commandsTable.add_row(['Press 7. to Edit Records'])
    commandsTable.add_row(['Press 8. to Delete Records'])
    commandsTable.add_row(['Press 9. to Quit the Program'])
    commandsTable.add_row(['Press 10. to Clear the Screen'])
    

    while True:
        try:
            printUserbaseTable()
            print(commandsTable)
            btn = (input("\n-> "))

            if btn ==  '1':
                print(printMoviebaseTable())
            elif btn == '2':
                print(printUserbaseTable())
            elif btn == '3':
                print(printTicketbaseTable())
            elif btn == '4':
                print("")
                # Add user record
            elif btn == '5':
                pass
            # Add Movie Record
            elif btn == '6':
                pass
            # Add Ticket Record
            elif btn == '7':
                pass #Edit Records
            elif btn == '8':
                pass #Delete Records
            elif btn == '9': # Quit the program
                print("Thank you for using this program☺☻")
                quit()
            elif btn == '10': # Clear the Screen
                os.system('cls')
            else:   # Invalid Input
                print("Invalid Input. Please Try Again.")
        except KeyboardInterrupt:
            print("Thank you for using this program☺☻")
            quit()





#  logo

# problem
# scope
# schedule
# cost
# hardware / software requirements
# number of tables
# menus
# structure of table
# 
