# Account-Manager
Technologies used were Python and SQLite.
Python modules used were tkinter, sqlite3, random, captcha

I recently ran into the problem of forgetting passwords to different websites and having to constantly reset my passwords. I know that password managers like this have been done in the past however, I wanted to see if I could create my own. I had a vision for a pin that was inpsired by the google password manager. I wanted to learn how to use the tkinter module to create a graphical user interface and wanted to store information using sql. By completing this project I was able to learn a little about how to use the tkinter module and some sql I hope to learn more about user interface in the future.

## Captcha Window
![Captcha Window](/Images/Captcha Window.png)
* When the user opens the program they are prompted to enter a captcha image that is generated from uppercase letters, lowercase letters, and digits. 
* The user is prompted to enter the captcha from the image into a textbox.  
* New Captcha button is used to generate a new captcha image, in situations where it is too difficult for the user to read. 
* Gray check button to check if the captcha they entered matches the captcha, it is not case sensitive. 
* If the user enters the captcha incorrectly, then a red "incorrect" message appears. 
* If the user enters the captcha correctly, then a green "correct" message appears and all buttons and text boxes are cleared and showing the Pin window. 

## Pin Window
![Pin Window](/Images/Pin Window.png)
* The user is prompted by text to either create a pin or enter the pin they had created.  
* The user is shown a bank pin that has buttons with numbers 0-9 with buttons at the right side, clear, cancel, and enter. 
* When the user hits any of the digit buttons an asterisk is put onto the textbox and the number is stored. 
* When the user hits the clear button, all the numbers currently stored in the entry box and asterisk on screen are cleared. 
* When the user hits the cancel button, the most recent number is deleted from the entry box and one asterisk is removed. 
* When the user hits the enter button, the pin is created, creating a table in SQLite, and storing the pin. 
* Or checked with the pin that is stored in an SQLite table. 
* If the user enters the incorrect pin, then an "incorrect" message appears blocking the entry box. 
* If the user enters the correct pin, then the screen is cleared of all buttons and shows the Manage Accounts window. 

## Manage Accounts Window 
![Account Window](/Images/Account Window.png)
* The user prompted to enter an account name, username, and password. Ex. “google”, “123@gmail.com”, “Password123”. 
* After entering these text boxes, they are allowed to hit any of the six buttons, update, create, show, clear, remove, and exit 
* The create button takes the text from the account, username, and password entries and creates a table in SQLite if it is the first row. Otherwise
adds the data to a row in an SQLite table. 
* The update button retrieves the row with the same account and username then updates the password in the SQLite database. 
* The clear button removes all the accounts, by removing all the rows from the SQLite table. 
* The remove button removes the name of the accounts in the account entry box, from the SQLite table. 
* The show button retrieves all rows from the SQLite database and displays them in a new window. 

