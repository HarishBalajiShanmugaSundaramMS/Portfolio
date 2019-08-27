# ==========================================
# Title:  Tkinter Separators With For Loop
# Author: HarishBalaji ShanmugaSundaram
# Date:   26 August 2019
# ==========================================
from tkinter import *
from tkinter import ttk

form = Tk()
form.title('Tkinter Separator')
form.geometry('300x150')
form.config(bg='#007F2D')
comboBox01 = ttk.Combobox(form,
                          values=['Python', 'Java', 'C++', 'C#', 'C'])
comboBox01.current(0)
comboBox01.pack()
# We use for loop to simulate the width of the Seperator
for x in range(15):
    separator01 = ttk.Separator(form, orient=HORIZONTAL)
    separator01.pack()
comboBox02 = ttk.Combobox(form,
                          values=['Japan', 'Germany', 'Ireland', 'Belgium', 'Netherlands'])
comboBox02.current(0)
comboBox02.pack()
# Use ''' to create Multi-Line Strings
status = Label(form, text='''Horizontal Separators 
Using a For Loop''',
               bd=2, relief=SUNKEN, anchor=W)
status.config(bg='#E30613', fg='#BDBCBC')
status.pack(side=BOTTOM, fill=X)
form.mainloop()
