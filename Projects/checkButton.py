# ======================================
# Title:  Tkinter CheckButtons
# Author: HarishBalaji ShanmugaSundaram
# Date:   21 August 2019
# ======================================

import tkinter as tk
from tkinter import *

form = tk.Tk()
form.title('Tkinter Check Button')
form.geometry('300x100')
form.resizable(0, 0)
chkValue01 = tk.StringVar()
chkValue02 = tk.StringVar()
c1 = Checkbutton(form, text='Checked By Default', var=chkValue01,
                 offvalue='unchecked', onvalue='checked')
c1.config(font='Arial 15 bold')
c1.select()
c1.pack()
labelControl01 = Label(form, text=chkValue01.get(),
                       font='Arial 15 bold', fg='green')
labelControl01.pack()
c2 = Checkbutton(form, text='Unchecked By Default',
                 var=chkValue02, offvalue='unchecked', onvalue='checked')
c2.config(font='Arial 15 bold')
c2.deselect()
c2.pack()
labelControl02 = Label(form, text=chkValue02.get(),
                       font='Arial 15 bold', fg='red')
labelControl02.pack()
form.mainloop()
