from tkinter import *
from tkinter.ttk import Treeview
import db.db
from tkinter import messagebox
import income.add_income

class ShowWindow:

    def __init__(self):
        self.win = Toplevel()
        canvas = Canvas(self.win, width=800, height=400, bg='white')
        canvas.pack(expand=YES, fill=BOTH)

        # show window in center of screen
        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width / 2 - 800 / 2)
        y = int(height / 2 - 400 / 2)
        str1 = "800x400+"+ str(x) + "+" + str(y)
        self.win.geometry(str1)

        # Disable resize of the window
        self.win.resizable(width=False, height=False)
        self.win.title("truTrackerEXP | SHOW INCOME SOURCES")

    def add_frame(self):

        
        self.frame = Frame(self.win, width=600, height=350)
        self.frame.place(x=80, y=20)

        x, y = 70, 20

        # Use treeview to show the data in forms of table
        # Mention number of columns
        self.tr = Treeview(self.frame, columns=('A', 'B', 'C', 'D'), selectmode="extended")

        #  Heading key + text
        self.tr.heading('#0', text = 'Sr No')
        self.tr.column('#0', minwidth=0, width=40, stretch=NO)
        self.tr.heading('#1', text = 'Source')
        self.tr.column('#1', minwidth=0, width=100, stretch=NO)
        self.tr.heading('#2', text = 'Description')
        self.tr.column('#2', minwidth=0, width=200, stretch=NO)
        self.tr.heading('#3', text = 'Update')
        self.tr.column('#3', minwidth=0, width=60, stretch=NO)
        self.tr.heading('#4', text = 'Delete')
        self.tr.column('#4', minwidth=0, width=60, stretch=NO)

        j = 0
        for i in db.db.show_income():
            self.tr.insert('', index=j, text=i[2], values=(i[0], i[1], 'Update', 'Delete'))
            j+=1

        # Create action on selected row
        self.tr.bind('<Double-Button-1>', self.actions)

        # Position the table on the frame
        self.tr.place(x = 50, y = y + 50)

        self.win.mainloop()

    def actions(self, e):
        # Get the value of the selected row
        tt = self.tr.focus()

        # Get the column id
        col = self.tr.identify_column(e.x)
        print(compile)
        print(self.tr.item(tt))

        tup = (
            self.tr.item(tt).get('text'),
        )

        if col == '#4':
            res = messagebox.askyesno("Message", "Are you sure you want to delete?")
            if res:
                rs = db.db.delete_income(tup)
                if rs:
                    messagebox.showinfo("Message", "Data has been deleted.")
                    self.win.destroy()
                    z = ShowWindow()
                    z.add_frame() 
            else:
                self.win.destroy()
                z = ShowWindow()
                z.add_frame() 

        if col == '#3':
            res = income.add_income.IncomeWindow(self.tr.item(tt))
            self.win.destroy()
            res.add_frame()
            