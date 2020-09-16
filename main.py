####################################################################
# Alejandro Tejada 17584
####################################################################
# Curso: Redes
# Programa: main.py
# Propósito: Programa principal
# Fecha: 09/2020
####################################################################

# ---------------------ZONA DE LIBRERIAS-------------------------------------------------
import sys  # this allows you to use the sys.exit command to quit/logout of the application


def main():
    menu()


def menu():
    print("************MAIN MENU**************")
    # time.sleep(1)
    print()

    choice = input("""
                      A: Create account
                      B: Log In
                      C: Log Out
                      D: Delete Account
                      E: Show ALL users and info about them
                      F: Add a user to my roster
                      G: Show contact details
                      H: Send direct message
                      I: Presence Message
                      J: Join Chat room
                      K: Send room message
                      L: Send File
                      Q: Quit/Exit
                      

                      Please enter your choice: """)

    if choice == "A" or choice == "a":
        createAccount()
    elif choice == "B" or choice == "b":
        logIn()
    elif choice == "C" or choice == "c":
        logOut()
    elif choice == "D" or choice == "d":
        deleAccount()
    elif choice == "E" or choice == "e":
        showAllUsers()
    elif choice == "F" or choice == "f":
        addUserToRoster()
    elif choice == "G" or choice == "g":
        showContactDetails()
    elif choice == "H" or choice == "h":
        sendDirectMessage()
    elif choice == "I" or choice == "i":
        sendPresence()
    elif choice == "J" or choice == "j":
        joinChatRoom()
    elif choice == "K" or choice == "k":
        sendChatRoom()
    elif choice == "L" or choice == "l":
        sendFile()
    elif choice == "Q" or choice == "q":
        killProgram()
    else:
        print("Please select an option")
        print("Try again")
        menu()


def createAccount():
    pass
    # Teacher will enter student details manually
    # These will be appended to the csv file


def logIn():
    pass
# Teacher can press a button to view all students at a glance


def logOut():
    pass
    # Teacher can input an ID number and display the relevant student's details


def deleAccount():
    pass


def showAllUsers():
    pass


def addUserToRoster():
    pass


def showContactDetails():
    pass


def sendDirectMessage():
    pass


def joinChatRoom():
    pass


def sendPresence():
    pass


def sendRoomMessage():
    pass


def joinChatRoom():
    pass


def sendChatRoom():
    pass


def sendFile():
    pass


def killProgram():
    print("Bye Fellow!")
    sys.exit


#! Main del programa
main()
