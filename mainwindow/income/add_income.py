from tkinter import *
import db.db
from tkinter import messagebox
import income.show_income

class IncomeWindow:

    def __init__(self, data=''):
        self.data = data
        print(self.data)

        self.win = Toplevel()
        canvas = Canvas(self.win, width=600, height=500, bg='white')
        canvas.pack(expand=YES, fill=BOTH)

        # show window in center of screen
        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 500 / 2)
        str1 = "600x500+"+ str(x) + "+" + str(y)
        self.win.geometry(str1)

        # Disable resize of the window
        self.win.resizable(width=False, height=False)
        self.win.title("truTrackerEXP | ADD INCOME")

    def add_frame(self):
        
        # Create an inner frame
        self.frame = Frame(self.win, height=450, width=550)
        self.frame.place(x=80, y=50)

        x, y = 70, 20

        self.img = PhotoImage(file='./mainwindow/images/money.png')
        self.label = Label(self.frame, image = self.img)
        self.label.place(x=x+80, y=y+0)

        self.income = Label(self.frame, text="Source", )
        self.income.config(font=('Segoi', 16, 'bold'))
        self.income.place(x=34, y=y+210)

        self.inc = Entry(self.frame, font='Courier 18')
        self.inc.place(x=154, y=y+210) 

        self.income = Label(self.frame, text="Description")
        self.income.config(font=('Segoi', 16, 'bold'))
        self.income.place(x=34, y=y+260)

        self.des = Entry(self.frame, font='Courier 18')
        self.des.place(x=154, y=y+260) 

        if self.data == '':       
            self.labeltitle = Label(self.frame, text="Add Income Source")
            self.labeltitle.config(font=("Segoi", 28, 'bold'))
            self.labeltitle.place(x=80, y=y+150)

            self.button = Button(self.frame, text="Submit", font="Segoi 20 bold", width = 8, command = self.add_income)
            self.button.place(x = 160, y=y+340)
        else:
            up = dict(self.data).get('values')

            # Set the values to populate the input boxes
            self.inc.insert(0, up[0])
            self.des.insert(0, up[1])
            self.button = Button(self.frame, text="Update", font="Segoi 20 bold", width = 8, command = self.update_income)
            self.button.place(x = 160, y=y+340)

            self.labeltitle = Label(self.frame, text="Update Income Source")
            self.labeltitle.config(font=("Segoi", 28, 'bold'))
            self.labeltitle.place(x=80, y=y+150)

        self.labelmsg = Label(self.frame, text='')
        self.labelmsg.config(font=('Segoi 20 bold'))
        self.labelmsg.place(x = 80, y = y + 300)      

        self.win.mainloop()

    def add_income(self):
        data = (
            self.inc.get(),
            self.des.get()
        )
        if self.inc.get() == '':
            self.labelmsg.config(fg='red')
            self.labelmsg.config(text="Please enter income source")

        elif self.des.get() == '':
            self.labelmsg.config(fg='red')
            self.labelmsg.config(text="Please enter income description")
        
        else:
            res = db.db.add_income(data)
            if res:
                self.labelmsg.config(fg='green')
                self.labelmsg.config(text="Data added successfully")
                # Clear data from inputs once data is submitted successfully
                self.inc.delete(0, 'end')
                self.des.delete(0, 'end')
            else:
                self.labelmsg.config(fg='red')
                self.labelmsg.config(text="Alert! Please try again")

    def update_income(self):
        tup = (
            self.inc.get(),
            self.des.get(),
            dict(self.data).get('text')
        )
        res = db.db.update_income(tup)
        if res:
            messagebox.showinfo("Message", "Income source updated")
            self.win.destroy()
            x = income.show_income.ShowWindow()
            x.add_frame()


    
