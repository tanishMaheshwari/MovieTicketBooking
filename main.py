'''
    Currently only works for windows (Due to os library)
    Currently, CLI only


'''

import getpass as gp #Used to input the password
import os   #Used to clear the screen


listOfMovies = ['Interstellar', 'Inseption', 'Avengers', 'Pokemon']
lastDateOfMovies = ['01/01/21', '01/01/21', '01/01/21', '01/01/21']
tickets = {'movie' : [], 'seat': [], 'price' : [], 'refreshments' : [], 'timing': []}


def printMovies():
    print('┌─────┬──────────────┬───────────┐')
    print('│S.no │  Movie Name  │ Last Date │')
    print('├' + '─' * 5 + '┼' + '─' * 14 + '┼' + '─' * 11 + '┤')
    for i in range(len(listOfMovies)):
        print('│', i + 1,'.   │ ', listOfMovies[i], ' ' * (14 - len(listOfMovies[i]) - 1) , '│ ', lastDateOfMovies[i], '  │'  ,sep = '')

    print('└─────┴──────────────┴───────────┘')
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

def bookTicket():
        print("List of Movies: \n\n")
        printMovies()
        
        print("Select the Movie: ")
        x = int(input("-> "))

        try:
            tickets['movie'].append(listOfMovies[x])
        except:
            print("Unknown ERROR occured. Please try again")
        
        print("\n\nSelect Type of seat: \n")
        print("1. Normal    (₹250)")
        print("2. Executive (₹500)")






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
    elif a == 2:
        print("List of Movies: \n\n")
        printMovies()
        
        print("Select the Movie: ")
        x = int(input("-> "))

        


    elif a == 3:
        if signIn():
            print("Access granted")
        
    elif a == 4:
        print("Thank you for using the program ☺☻")
        
    else:
        os.system('cls')
        print("ERROR: Please enter a valid number\n" + '*' * 30 + '\n')
        main()

'''
print('Press 3 to edit the available movies')
print('Press 4 to check and edit movie ticket records')
'''



if __name__ == "__main__":
    print("Movie Ticket Booking Software")
    print("Made by Tanish M and Rohan P")
    print('*' * 30)
    print()
    main()
