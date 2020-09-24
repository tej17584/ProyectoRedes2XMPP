<h1 align="center">
<br>
  <img src="https://www.briskbraintech.com/wp-content/uploads/2019/10/IoT-briskbraintech-1-1024x871.jpg" alt="UkronTadd" width="664"> 
<br>
<br>
Project: Using XMPP Protocol
</h1>
    
<p align="center">
  
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/static/v1?label=License&message=NoLicense&color=<COLOR>" alt="No license">
  </a>
</p>

<p align="center">University Project :mortar_board:</p>

<hr />

## Description

This project is part of the Networks course at the Universidad del Valle de Guatemala. The objective of this project is to use an existing protocol and build on it to implement a client with certain functionalities.

## Description of Project and Files

### List of tools used for the project:

- Python 3.7
- XMPP: The Definitive Guide
- VS Code

### Libraries used

- sys
- logging
- getpass
- xmpp
- time
- threading
- binascii
- sleekxmpp
- optparse
- xml

### Files

- `main.py ` (officially: The Client)
  - Contains the menu for the client. This menu has all the functionalities for the client.
- `func.py` THE LOGIC
  - Contains all the logic and the functions for the `main.py` methods and functionalities.
- All the other files are examples, pdf and other stuff.

## Instructions for use the Client

### Step 1: run the client

`python main.py`

### Step 2: choose an option

When you run client (`main.py`) has the main menu, on the menu, you will se the next options.

```python
                      A: Create account
                      B: Log In
                      C: Log Out
                      D: Delete Account
                      E: Show ALL users + info about them
                      F: Add a user to my roster
                      G: Show contacts details
                      H: Send direct message
                      I: Join Chat room
                      J: Create Room
                      k: Send room message
                      L: Send File
                      Q: Quit/Exit


                      Please enter your choice:
```

You must choose one option. You can enter a letter and then enter.

### Step 3: enter the functionality and do your stuff

In this part, you use the functionalitie thath you want.

### Presence and notifications Warnings
The program has several functions to receive messages. Actually, these messages are printed ABOVE the prompt. If in any case someone enters, you will be shown a presence message. If someone sends you a message, you will see a "typing" notification on your terminal. If someone enters a room, then you will see a notification.

In these cases, it is better to press ENTER to return to the menu and continue with the functions.
## Instructions for use every Client Option

### A: Create Account

In this option the user can create an account.
First you select the option from the menu. Then you enter the name of your account, and then, you enter your password.

#### Parameters

- Account name
  - Something like: whatever@redes2020.xyz
- Password
  - something tricky

#### Posible Outputs

You will see the next outputs

- Good
  - `User succesfully created`
- Failed
  - `Fail!!! Try again`

#### Notes and warnings

- The account creation fails if you enter and already created account.
- You can create accounts only **if you are not logged in**

### B: Log In

In this option the user can log in.
First you enter your username and then your password.

#### Parameters

- Account name
  - Something like: whatever@redes2020.xyz
- Password
  - your password

#### Posible Outputs

You will see the next outputs

- Good
  - `You have succesfully Loged In`
- Failed
  - `We could not connect to redes2020.xyz`

#### Notes and warnings

- There is an issue, if you delete your account, and then you log in, it actually works!! So, sorry for that. **DO NOT DO THAT PLEASE**
- You can't login into your account **if you haven't created it**

### C: Log Out (**You must have been logging into your account**)

In this option you log out

#### Parameters

- No parameters

#### Posible Outputs

You will see the next outputs

- Good
  - `You logged out. BYE!!`
- Failed
  - `Error`

#### Notes and warnings

- If you logged out. **You must log in for making other functions like send message, etc.** Do not log out and then send message, it wont work.

### D: Delete Account (**You must have been logging into your account**)

In this option you can delete your account

#### Parameters

- Account name
  - Something like: whatever@redes2020.xyz

#### Posible Outputs

You will see the next outputs

- Good
  - `Account deleted succesfuly`
  - `Bye friend, you DELETED YOUR ACCOUNT`
- Failed
  - `We could not Delete the account`

#### Notes and warnings

- There is an issue, if you delete your account, and then you log in, it actually works!! So, sorry for that. **DO NOT DO THAT PLEASE**. If you delete your acccount and want to check, you can create a new account withe **the same user** and it works.

### E: Show all users and info about them (**You must have been logging into your account**)

In this option you can see all the user info

#### Parameters

- No parameters

#### Posible Outputs

You will see the next outputs

- Good
  - `All the user data`
- Failed
  - `Unable list users`

#### Notes and warnings

- Sometimes the response of XML can't be parsed properly, so it might print all the XML.

### F: Add a user to my roster (**You must have been logging into your account**)

In this option you can add a person to your roster.

#### Parameters

- Account name for add to your roster
  - Something like: myfriendJIDtoADDtoRoster@redes2020.xyz

#### Posible Outputs

You will see the next outputs

- Good
  - `User succesfully added to roster`
- Failed
  - `Failed to add user to roster`

#### Notes and warnings

- None for this feature.

### G: Show contact details (**You must have been logging into your account**)

In this option you can see your contact details

#### Parameters

- None

#### Posible Outputs

You will see the next outputs

- Good
  - `Your contact info`
- Failed
  - `Error: Request timed out`

#### Notes and warnings

- If you see the error: `Error: Request timed out` it is probably because you have not logged in.

### H: Send Direct message (**You must have been logging into your account**)

In this option you can delete your account

#### Parameters

- Account name
  - Something like: whatever@redes2020.xyz
- Message to send
  - A message like: "Hi Fellow"

#### Posible Outputs

You will see the next outputs

- Good
  - `Message sended!!!`
- Failed
  - `Error`

#### Notes and warnings

- Be sure to enter the correct username and message in the prompt. If a message came in and you couldn't write the message or the user, please try again.

### I: Join chat room (**You must have been logging into your account**)

In this option you can **Join** to a chat room.

#### Parameters

- room name
  - Example for room NAME: ROOMNAME@conference.redes2020.xyz
- Nickname
  - Like: PedritoTrueno

#### Posible Outputs

You will see the next outputs

- Good
  - `You have succesfully connected to: " + room + "with NickName: "+nickname`
- Failed
  - `The room could not been created/entered`

#### Notes and warnings

- This is **only for joining**. There is a function for create one.

### J: Create Room (**You must have been logging into your account**)

In this option you can **create** a room

#### Parameters

- The room name
  - Example for room NAME: ROOMNAME@conference.redes2020.xyz
- Your nickname
  - Like: PreditoTrueno

#### Posible Outputs

You will see the next outputs

- Good
  - `You have succesfully created the room: " + room + "with NickName: "+nickname`
- Failed
  - `Nop, try again....`
  - `The room could not been created/entered`

#### Notes and warnings

- You must not create a room already created, it will launch an error. The room only stays "alive" if the prompt who created it is still up.

### K: Send Room Message (**You must have been logging into your account AND been in a room**)

In this option you can send a room message

#### Parameters

- Room Name
  - Example for room NAME: ROOMNAME@conference.redes2020.xyz
- Message
  - The message, like: HI FELLOWS!!

#### Posible Outputs

You will see the next outputs

- Good
  - `Message sended!!`
- Failed
  - `We could not send the message`

#### Notes and warnings

- You must haven been logging into your account AND been in a room. If you are not, it wont work.

### L: Send files **Not implemented, sorry... :(**

### Q: Quit

In this option you can kill the prompt.

#### Parameters

- None

#### Posible Outputs
- None

#### Notes and warnings

- Sometimes the `sys.exit` fails, so it is better to kill the entire terminal.

## Credits and References

Course teacher: Vinicio Paz

- https://pypi.org/project/sleekxmpp/
- https://sleekxmpp.readthedocs.io/en/latest/
- https://github.com/fritzy/SleekXMPP/blob/develop/sleekxmpp/clientxmpp.py
- https://sleekxmpp.readthedocs.io/en/latest/getting_started/echobot.html
- https://sleekxmpp.readthedocs.io/en/latest/getting_started/sendlogout.html
- https://stackoverflow.com/questions/17791783/sleekxmpp-send-a-message-at-will-and-still-listen-for-incoming-messages/25621058
- https://stackoverflow.com/questions/22890437/xmpp-send-message-not-working/22911804#22911804
- Partners of the classroom

## Licence

No license
