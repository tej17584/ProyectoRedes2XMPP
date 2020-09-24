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
You will see the next options
- Good
  - `User succesfully created`
- Failed
  - `Fail!!! Try again`

#### Notes and warnings
- The account creation fails if you enter and already created account.
- You can create accounts only **if you are not logged in**
### B: 

### C: 
### D: 
### E: 
### F: 
### G: 
### H: 
### I: 
### J: 
### K: 
### L: 
### Q: 
## Credits and References
Course teacher: Vinicio Paz

- 

## Licence
No license
