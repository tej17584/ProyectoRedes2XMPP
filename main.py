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
import func
clientForUser = None


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
                      G: Show contacts details
                      H: Send direct message
                      I: Join Chat room
                      J: Create Room
                      k: Send room message
                      L: Send File
                      Q: Quit/Exit


                      Please enter your choice: """)

    if choice == "A" or choice == "a":
        createAccount()
        menu()
    elif choice == "B" or choice == "b":
        global clientForUser
        clientForUser = logIn()
        status = "Connected to SERVER"
        menu()
    elif choice == "C" or choice == "c":
        logOut(clientForUser)
        menu()
    elif choice == "D" or choice == "d":
        deleteAccount(clientForUser)
        print("Bye friend, you DELETED YOUR ACCOUNT")
        sys.exit
    elif choice == "E" or choice == "e":
        showAllUsers(clientForUser)
        menu()
    elif choice == "F" or choice == "f":
        addUserToRoster(clientForUser)
        menu()
    elif choice == "G" or choice == "g":
        showContactDetails(clientForUser)
        menu()
    elif choice == "H" or choice == "h":
        sendDirectMessage(clientForUser)
        menu()
    elif choice == "I" or choice == "i":
        joinChatRoom(clientForUser)
        menu()
    elif choice == "J" or choice == "j":
        createNewChatRoom(clientForUser)
        menu()
    elif choice == "K" or choice == "k":
        sendChatRoom(clientForUser)
        menu()
    elif choice == "Q" or choice == "q":
        print("Bye Fellow!")
        sys.exit
    else:
        print("Please select an option")
        print("Try again")
        menu()


#! Crear cuenta


def createAccount():
    print("You are going to create account")
    userName = input(
        "Type username please:   ")
    passWord = input("Type the password:    ")
    # print(userName)
    # print(passWord)
    ansRegister = func.registerNewUser(userName, passWord)
    if (ansRegister):
        print("User succesfully created")
    else:
        print("Fail!!!! Try again")


def logIn():
    print("You are going to maje LOGIN")
    userName = input(
        "Type username please:   ")
    passWord = input("Type the password:    ")
    clientReturn = func.ClientXMPP(userName, passWord)
    return clientReturn


def logOut(clientForUser):
    clientForUser.disconnectFromServer()
    print("Yoy have succesfully loged out from your account")


def deleteAccount(clientForUser):
    answerToDelete = input('''
            Press 1 for YES
            Pres 2 for NO
    ''')
    if(answerToDelete == "1"):
        accountToDelete = input("Type your account name please  ")
        clientForUser.deleteUserFromServer(accountToDelete)
    elif (answerToDelete == "2"):
        print("Ok Go on with the Main Menu")
        menu()


def showAllUsers(clientForUser):
    clientForUser.listALLServerUsers()


def addUserToRoster(clientForUser):
    print("You are going to add a new User")
    userName = input(
        "Type username from your friend:   ")
    responseFromServer = clientForUser.addJIDToRoster(userName)
    if(responseFromServer):
        print("User succesfully added to roster")
    else:
        print("Failed to add user to roster")


def showContactDetails(clientForUser):
    # we get the contact information from users
    clientForUser.getInformationFromUsersAtRoster()


def sendDirectMessage(clientForUser):
    print("You are going to send a Message")
    userName = input(
        "Type username from your friend/not friend:   ")
    msg = input(
        "Type your message:   ")
    clientForUser.sendMessage(userName, msg)


def joinChatRoom(clientForUser):
    print("")
    print("Example for room NAME: ROOMNAME@conference.redes2020.xyz")
    roomName = input("type the Room Name CONNECT :  ")
    NickName = input("type the Nickname or user thath you want:   ")
    if("conference" in roomName):
        print("We are going to connect....")
        clientForUser.Joinchatroom(roomName, NickName)
        menu()
    else:
        print("Nop, try again....")
        menu()


def createNewChatRoom(clientForUser):
    print("")
    print("Example for room NAME: ROOMNAME@conference.redes2020.xyz")
    roomName = input("type the Room Name for CREATE :  ")
    NickName = input("type the Nickname or user thath you want:   ")
    if("conference" in roomName):
        print("We are going to connect....")
        clientForUser.createNewChatRoom(roomName, NickName)
        menu()
    else:
        print("Nop, try again....")
        menu()


def sendChatRoom(clientForUser):
    print("---------------------------------------")
    print("")
    room = input("Type the room you want to send the message...")
    message = input("Type the message to send to the room...")
    clientForUser.sendMessageToRoom(room, message)


def sendFile():
    pass


#! Main del programa
main()
