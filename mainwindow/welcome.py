from tkinter import *
import login

class WelcomeWindow:

    # create a constructor
    def __init__(self):
        # create a tkinter window
        self.win = Tk()

        # reset the window and background color
        self.canvas = Canvas(self.win, width = 600, height = 400, bg = 'white')
        self.canvas.pack(expand=YES, fill=BOTH)

        # show window in center of screen
        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 400 / 2)
        str1 = "600x400+"+ str(x) + "+" + str(y)
        self.win.geometry(str1)

        # Disable resize of the window
        self.win.resizable(width=False, height=False)

        # Customize the title of the window
        self.win.title("WELCOME | truTrackerEXP | ADMINISTRATOR")

    def add_frame(self):
        # Create an inner frame
        self.frame = Frame(self.win, height=300, width=400)
        self.frame.place(x=100, y=50)

        x, y = 70, 20

        # Place image in the frame
        self.img = PhotoImage(file='mainwindow/images/box.png')
        self.label = Label(self.frame, image = self.img)
        self.label.place(x=x+60, y=y+0)

        self.labeltitle = Label(self.frame, text="Welcome to truTrackerEXP")
        self.labeltitle.config(font=("Segoi", 20, 'bold'))
        self.labeltitle.place(x=60, y=y+150)

        self.button = Button(self.frame, text="Continue", font="Segoi 20 bold", width = 8
                    , command=self.login)

        self.button.place(x=x+70, y=y+220)

        self.win.mainloop()

    # Open a new window on button click
    def login(self):
        # Destroy current window
        self.win.destroy()
        # Open the new window
        log = login.LoginWindow()
        log.add_frame()

        

if __name__ == "__main__":
    x = WelcomeWindow()
    x.add_frame()


# ATTRIBUTION FOR DESIGN WORK USED IN THIS FILE #
# <div>Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
