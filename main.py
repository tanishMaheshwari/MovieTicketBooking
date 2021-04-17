'''
    Currently only works for windows (Due to os implementation)
    Currently, CLI only
    

    #Things To Do
        Working on adding, deleting and editing records
        Working on admin functions
        Add User Information
        Add city
        Add Movie Details
        implement integration with mysql

    Tables
        1. User Base:- 
            User ID - int
            Name - varchar
            Phone Number - char
            E-mail - varchar
            City - carchar
        2. Ticket Base
            Movie ID - int  
            Movie Name - varchar
            Last date of Movie - char / varchar
            Seat Type - char
            Timing - varchar
            Theatre - varchar
            City - varchar
            Refreshment - bool
        3. Movie Base
            movie ID - int
            Movie Base - varchar
            Last Date of Movie - varchar
            Base Price - int
            Movie Details - varchar
            Tickets Sold - int


        IDLE\Class_12_Project\MovieTicketBooking

'''

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
