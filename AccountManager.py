from tkinter import *
from AccountDB import *
from PinDB import *
import string
from random import randint
from captcha.image import ImageCaptcha
# from PIL import ImageTk,Image  

# applicationn class base/parent class is Tk
class User_Manager(Tk):
    def __init__(self):
        # initializes the base/paent class in this case Tk() creates window
        # self is now the window
        super().__init__()
        # sets the title of window
        self.title("Account Manager")
        # sets the size of window
        self.geometry("1250x650")
        # sets the background color
        self.configure()

        # Creates an instance of Account class
        self.acc = Account()
        # Creates an instance of Pin class
        self.pin = Pin()

        # REMOVE AFTER DONE
        # self.pin_Registration()

        # Generates captcha
        # UNCOMMENT AFTER DONE
        self.generate_Captcha()

        # Tilte
        first_Page_Text = Label(self, text="Account Manager", font=("bold", 50))
        first_Page_Text.place(x=350, y=25) 

        # # New
        # new_Button = Button(self, text="New User", font=("bold", 35))
        # new_Button.place(x=500, y=200)

        # # Returning
        # returning_Button = Button(self, text="Returning User", font=("bold", 35))
        # returning_Button.place(x=440, y=350)

    def new_Captcha(self):
        self.img_Label.destroy()
        self.create_Captcha()

    def create_Captcha(self):
        # Create an image instance of the given size
        self.image = ImageCaptcha(width = 280, height = 90)

        # list of all the digits
        self.digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        # list of the alphabet lowercase and uppercase
        self.alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase) 
        # list of digits and alphabet
        self.random_List = self.digits + self.alphabet

        # captcha_text that will be used to generate captcha
        self.captcha_String = ""

        # generates random chars of lowercase and uppercase alphabet, and digits
        for i in range(8):
            self.random_Char = str(self.random_List[randint(0, len(self.random_List) - 1)])
            self.captcha_String += self.random_Char

        # generate the image of the given text
        self.new_Image = self.image.generate(self.captcha_String)

        # write the image on the given file and save it
        self.image.write(self.captcha_String, "CAPTCHA.png")


        self.image_File = PhotoImage(file = "CAPTCHA.png")
        #self.img = ImageTk.PhotoImage(Image.open("CAPTCHA.png")) 

        self.img_Label = Label(image=self.image_File)
        self.img_Label.place(x=475, y=150)

    def generate_Captcha(self):
        self.create_Captcha()

        # Captcha
        self.captcha_Text= StringVar()
        self.captcha_Label = Label(self, text="Enter Captcha", font=('bold', 30))
        self.captcha_Label.place(x=485, y=260)
        self.captcha_Entry = Entry(self, textvariable=self.captcha_Text, font=('bold', 30))
        self.captcha_Entry.place(x=475, y=330, width=275, height=50)

        # Check
        self.check_Button = Button(self, text="Check", command=self.check_Captcha, font=('bold', 30), bg="gray")
        self.check_Button.place(x=535, y=400)

        # New Captcha
        self.new_Captcha_Button = Button(self, text="New Captcha", command=self.new_Captcha, font=('bold', 30), bg="gray")
        self.new_Captcha_Button.place(x=480, y=500)
        

    def check_Captcha(self):
        if (self.captcha_String.lower() == self.captcha_Text.get().lower()):
            self.correct_Message = Message(self, text="\nCorrect\n", relief=RAISED, font=("bold", 50), bg="#3deb34")
            self.correct_Message.place(x=420, y=150, width=400, height=100)
            self.correct_Message.after(3000, self.correct_Message.destroy)
            self.img_Label.destroy()
            self.captcha_Label.destroy()
            self.captcha_Entry.destroy()
            self.check_Button.destroy()
            self.new_Captcha_Button.destroy()
            self.after(3000, self.pin_Registration)
        else:
            self.incorrect_Message = Message(self, text="\nIncorrect\n", relief=RAISED, font=("bold", 50), bg="#FF0000")
            self.incorrect_Message.place(x=420, y=150, width=400, height=100)
            self.incorrect_Message.after(3000, self.incorrect_Message.destroy)
            self.captcha_Text.set("")

    def account_Registration(self):
        # Account
        self.acc_Text= StringVar()
        self.acc_Label = Label(self, text="Account", font=('bold', 30))
        self.acc_Label.place(x=370, y=170)
        self.acc_Entry = Entry(self, textvariable=self.acc_Text, font=('bold', 30))
        self.acc_Entry.place(x=600, y=170, width=250)

        # Username/Email
        self.user_Text= StringVar()
        self.user_Label = Label(self, text="Username", font=('bold', 30))
        self.user_Label.place(x=370, y=245)
        self.user_Entry = Entry(self, textvariable=self.user_Text, font=('bold', 30))
        self.user_Entry.place(x=600, y=245, width=250)

        # Password
        self.pass_Text= StringVar()
        self.pass_Label = Label(self, text="Password", font=('bold', 30))
        self.pass_Label.place(x=370, y=320)
        self.pass_Entry = Entry(self, textvariable=self.pass_Text, font=('bold', 30))
        self.pass_Entry.place(x=600, y=320, width=250)
        
        # Update
        self.update_Button = Button(self, text="Update", command=self.update_Account, font=('bold', 30))
        self.update_Button.place(x=540, y=400)

        # Create
        self.create_Button = Button(self, text="Create", command=self.add_Account, font=('bold', 30))
        self.create_Button.place(x=370, y=400)

        # Retrieve Data
        self.retrieve_Button = Button(self, text="Show", command=self.show_Accounts, font=('bold', 30))
        # 200, 100
        self.retrieve_Button.place(x=720, y=400)

        # Clear Table
        self.retrieve_Button = Button(self, text="Clear", command=self.acc.remove_All, font=('bold', 30))
        self.retrieve_Button.place(x=370, y=500)

        # Remove
        self.create_Button = Button(self, text="Remove", command=self.remove_Account, font=('bold', 30))
        self.create_Button.place(x=535, y=500)

        # Exit
        self.exit_Button = Button(self, text="Exit", command=self.destroy, font=('bold', 30))
        self.exit_Button.place(x=750, y=500)


    # adds accounts to database
    def add_Account(self):
        self.acc.insert(self.acc_Text.get(), self.user_Text.get(), self.pass_Text.get())
        self.acc_Text.set("")
        self.user_Text.set("")
        self.pass_Text.set("")

    # shows all the accounts currently in database
    def show_Accounts(self):
        self.accounts = Toplevel()
        self.accounts.title("Accounts")
        self.accounts.geometry("500x500")
        # Creates a scrollbar in window accounts
        self.accounts_Scroll = Scrollbar(self.accounts)
        # side makes widget stick to right, make the scrollbar bigger
        self.accounts_Scroll.pack(side=RIGHT, fill=Y)
        self.account_List = Listbox(self.accounts, height=100, width=100, border=0, yscrollcommand=self.accounts_Scroll.set, font=('bold', 25))
        self.account_List.pack()
        
        for row in self.acc.get_All():
            self.account_List.insert(END, row)

    def update_Account(self):
        self.acc.update(self.acc_Text.get(), self.user_Text.get(), self.pass_Text.get())
        self.acc_Text.set("")
        self.user_Text.set("")
        self.pass_Text.set("")

    def remove_Account(self):
        self.acc.remove(self.acc_Text.get())
        self.acc_Text.set("")
        self.user_Text.set("")
        self.pass_Text.set("")

    def pin_Registration(self):
        # Make a function to check whether to display create pin or enter pin
        self.pin_Label = Label(self, text="Create Pin/Enter Pin", font=('bold', 50))
        self.pin_Label.place(x=300, y=125)


        self.pin_Canvas = Canvas(self, bg="black")
        # background pin
        self.pin_Canvas.create_rectangle(0, 0, 525, 500, outline="red", fill="#798485")
        # number 1
        self.num_1_Button = Button(self, text="1", font=('bold', 25), bg="#99a7a8", command=lambda: self.add_Star(1))
        self.num_1_Button.place(x=375, y=350, width=100, height=50) 
        # number 4
        self.num_4_Button = Button(self, text="4", font=('bold', 25), bg="#99a7a8", command=lambda: self.add_Star(4))
        self.num_4_Button.place(x=375, y=410, width=100, height=50)
        # number 7
        self.num_7_Button = Button(self, text="7", font=('bold', 25), bg="#99a7a8", command=lambda: self.add_Star(7))
        self.num_7_Button.place(x=375, y=470, width=100, height=50)
        # number 
        self.num_b1_Button = Button(self, text="", font=('bold', 25), bg="#99a7a8")
        self.num_b1_Button.place(x=375, y=530, width=100, height=50)

        # number 2
        self.num_2_Button = Button(self, text="2", font=('bold', 25), bg="#99a7a8", command=lambda: self.add_Star(2))
        self.num_2_Button.place(x=500, y=350, width=100, height=50) 
        # number 5
        self.num_5_Button = Button(self, text="5", font=('bold', 25), bg="#99a7a8", command=lambda: self.add_Star(5))
        self.num_5_Button.place(x=500, y=410, width=100, height=50)
        # number 8
        self.num_8_Button = Button(self, text="8", font=('bold', 25), bg="#99a7a8", command=lambda: self.add_Star(8))
        self.num_8_Button.place(x=500, y=470, width=100, height=50)
        # number 0
        self.num_0_Button = Button(self, text="0", font=('bold', 25), bg="#99a7a8", command=lambda: self.add_Star(0))
        self.num_0_Button.place(x=500, y=530, width=100, height=50)

        # number 3
        self.num_3_Button = Button(self, text="3", font=('bold', 25), bg="#99a7a8", command=lambda: self.add_Star(3))
        self.num_3_Button.place(x=625, y=350, width=100, height=50) 
        # number 6
        self.num_6_Button = Button(self, text="6", font=('bold', 25), bg="#99a7a8", command=lambda: self.add_Star(6))
        self.num_6_Button.place(x=625, y=410, width=100, height=50)
        # number 9
        self.num_9_Button = Button(self, text="9", font=('bold', 25), bg="#99a7a8", command=lambda: self.add_Star(9))
        self.num_9_Button.place(x=625, y=470, width=100, height=50)
        # number 
        self.num_b2_Button = Button(self, text="", font=('bold', 25), bg="#99a7a8")
        self.num_b2_Button.place(x=625, y=530, width=100, height=50)

        # clear pin
        self.clear_Button = Button(self, text="Clear", font=('bold', 20), bg="#99a7a8", command=self.clear_Star)
        self.clear_Button.place(x=760, y=350, width=100, height=50)
        # cancel pin
        self.cancel_Button = Button(self, text="Cancel", font=('bold', 20), bg="#99a7a8", command=self.delete_Star)
        self.cancel_Button.place(x=760, y=410, width=100, height=50)
        # enter pin
        self.enter_Button = Button(self, text="Enter", font=('bold', 20), bg="#99a7a8", command=self.create_Pin)
        self.enter_Button.place(x=760, y=470, width=100, height=50)
        # pin
        self.fill_Button = Button(self, text="", font=('bold', 20), bg="#99a7a8")
        self.fill_Button.place(x=760, y=530, width=100, height=50)

        self.pin_Canvas.place(x=350, y=250, width=525, height=375)

        self.pin_Text = StringVar()
        self.pin_Entry = Entry(self, textvariable=self.pin_Text, font=('bold', 30))
        self.pin_Entry.place(x=475, y=275, width=250)

        self.pin_List = []

    def add_Star(self, number):
        self.pin_Entry.insert(0, "*")
        self.pin_List.append(number)
        

    def clear_Star(self):
        self.pin_List = []
        self.pin_Text.set("")

    def delete_Star(self):
        self.pin_List.pop()
        self.pin_Entry.delete(len(self.pin_List)-1)
        print(self.pin_List)
    
    # if there is not data in pin 
    def create_Pin(self):
        # check length if length of get data is 1 than go to check_Pin()
        # create a new pin if the length of get All is
        if (len(self.pin.get_All()) == 0):
            self.pin.create_Table()
            self.pin.insert(int(self.string_Pin()))
            self.destroy_Pin()
            self.account_Registration()
        else:
            # create new pin and add to pin database
            self.check_Pin()

    # check the length of pin databse, get
    def check_Pin(self):
        if (self.string_Pin() == (str(self.pin.get_Pin()[0]))):
            self.destroy_Pin()
            self.account_Registration()
        else:
            # incorrect message
            self.pin_Text.set("")
            self.incorrect_Message = Message(self, text="\nIncorrect\n", relief=RAISED, font=("bold", 50), bg="#FF0000")
            self.incorrect_Message.place(x=400, y=255, width=400, height=85)
            self.incorrect_Message.after(3000, self.incorrect_Message.destroy)
            self.pin_List = []

    def string_Pin(self):
        self.pin_String = ""

        for i in range(len(self.pin_List)):
            self.pin_String += str(self.pin_List[i])

        return self.pin_String

    def destroy_Pin(self):
        self.pin_Entry.destroy()
        self.pin_Label.destroy()
        self.pin_Canvas.destroy()
        self.num_0_Button.destroy()
        self.num_1_Button.destroy()
        self.num_2_Button.destroy()
        self.num_3_Button.destroy()
        self.num_4_Button.destroy()
        self.num_5_Button.destroy()
        self.num_6_Button.destroy()
        self.num_7_Button.destroy()
        self.num_8_Button.destroy()
        self.num_9_Button.destroy()
        self.num_b1_Button.destroy()
        self.num_b2_Button.destroy()
        self.enter_Button.destroy()
        self.clear_Button.destroy()
        self.cancel_Button.destroy()
        self.fill_Button.destroy()


if (__name__ == "__main__"):
    app = User_Manager()
    app.mainloop()



