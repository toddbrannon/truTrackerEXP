from tkinter import *
from tkinter import messagebox
import db.db
import dashboard

class LoginWindow:

    def __init__(self):
        self.win = Tk()

        # reset the window and background color
        self.canvas = Canvas(self.win, width = 600, height = 500, bg = 'white')
        self.canvas.pack(expand=YES, fill=BOTH)

        # show window in center of screen
        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 500 / 2)
        str1 = "600x500+"+ str(x) + "+" + str(y)
        self.win.geometry(str1)

        # Disable resize of the window
        self.win.resizable(width=False, height=False)

        # Customize the title of the window
        self.win.title("WELCOME | truTrackerEXP | LOGIN")

    def add_frame(self):
        self.frame = Frame(self.win, height=400, width=450)
        self.frame.place(x=80, y=50)

        x, y = 70, 20

        self.label = Label(self.frame, text="User Login")
        self.label.config(font=('Segoi', 30, 'bold'))
        self.label.place(x=136, y = y + 0)

        self.img = PhotoImage(file='mainwindow/images/login.png')
        self.label = Label(self.frame, image = self.img)
        self.label.place(x=x+80, y=y+60)

        # Create login form

        self.unlabel = Label(self.frame, text="Enter User Name")
        self.unlabel.config(font=('Segoi', 20))
        self.unlabel.place(x=135, y = y + 200)

        self.user_name = Entry(self.frame, font='Courier 20')
        self.user_name.place(x=80,  y = y + 230)

        self.pslabel = Label(self.frame, text="Enter Password")
        self.pslabel.config(font=('Segoi', 20))
        self.pslabel.place(x=140, y = y + 270)

        self.password = Entry(self.frame, font='Courier 20', show="*")
        self.password.place(x=80,  y = y + 300)

        self.button = Button(self.frame, text="Login", font="Segoi 20 bold", width = 8,
                        command=self.login)
        self.button.place(x = 156, y=y+350)

        self.win.mainloop()

    def login(self):
        # Get the data and store it into tuple (data)
        data = (
            self.user_name.get(),
            self.password.get()
        )

        # Validation
        if self.user_name.get() == "":
            messagebox.showinfo("Alert!", "User Name is required!")
        elif self.password.get() == "":
            messagebox.showinfo("Alert!", "Password is required!")
        else:
            res = db.db.user_login(data)
            if res:
                # messagebox.showinfo("Message", "Login Successful")
                self.win.destroy()
                x = dashboard.DashboardWindow()
                x.add_menu()
                x.add_frame()
                
            else:
                messagebox.showinfo("Message", "Wrong User Name/Password")

