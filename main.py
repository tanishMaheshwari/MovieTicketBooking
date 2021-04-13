'''
    Currently only works for windows (Due to os library)
    Currently, CLI only


'''

import getpass as gp #Used to input the password
import os   #Used to clear the screen


listOfMovies = ['Interstellar', 'Inseption', 'Avengers', 'Pokemon']
lastDateOfMovies = ['01/01/21', '01/01/21', '01/01/21', '01/01/21']
seatType = ['Normal', 'Executive']
timing = ['9:00 a.m.', '12:00 p.m', '3:00 p.m', '6:00 p.m', '9:00 p.m']

seats = [
    ['X', '♦', '♦', '♦', '♦', '♦', '♦', '♦'],
    ['♦', '♦', '♦', '♦', '♦', '♦', '♦', '♦'],
    ['♦', '♦', '♦', '♦', '♦', '♦', '♦', '♦'],
    ['♦', '♦', '♦', '♦', '♦', '♦', '♦', '♦'],
    ['♦', '♦', '♦', '♦', '♦', '♦', '♦', '♦'],
    ['♦', '♦', '♦', '♦', '♦', '♦', '♦', '♦'],
    ['♦', '♦', '♦', '♦', '♦', '♦', '♦', '♦'],
    ['♦', '♦', '♦', '♦', '♦', '♦', '♦', '♦']
]

tickets = {'movie' : [], 'seatType': [], 'seat': [],  'price' : [], 'refreshments' : [], 'timing': []}


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
        
#**********************************************************************************
#**********************************************************************************
def signIn():
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
        return 


#=================================================================================

def getTicket(x):
    
    x = 0
    listOfElements = list(tickets.values())
    l = []
    for i in range(len(listOfElements)):
        l.append(listOfElements[i][x])
    return l

#**********************************************************************************


def bookTicket():
        print("List of Movies: \n\n")
        printMovies()
        
        print("Select the Movie: ")
        
        x = int(input("-> "))
        tickets['movie'].append(listOfMovies[x - 1])
        
        
        print("\n\nSelect Type of seat: \n")
        print("1. Normal    (₹250)")
        print("2. Executive (₹500)")

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
            seats[row][col] == 'X'
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
        tickets['timing'].append(timing[x])
        tickets['price'].append(0)

        #============================
        l = getTicket(len(tickets['movie']) - 1)




        print("Your ticket has been booked ☻")
        print(l)
        print(len(tickets['movie']))
        main()



#**********************************************************************************

def adminFunctions():
    print('Press 1 to edit the available movies')
    print('Press 2 to check and edit movie ticket records')
    try:
        a = int(input("Enter a number:  "))
    except:
        os.system('cls')
        print("ERROR: Please enter a valid number\n" + '*' * 30 + '\n')
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
            print("Access granted")
        
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
