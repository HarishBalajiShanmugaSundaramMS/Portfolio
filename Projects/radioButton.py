# ======================================
# Title:  Tkinter RadioButtons
# Author: HarishBalaji ShanmugaSundaram
# Date:   09 August 2019
# ======================================
import tkinter as tk
from tkinter import *

form = tk.Tk()
form.title('Tkinter Radio Button')
form.geometry('300x200')
form.resizable(0, 0)


def selectionCall():
    selection = "The Selected Option is " + str(radValue.get())
    label.config(text=selection, font='Arial 15 bold', fg='green')


radValue = IntVar()
r1 = tk.Radiobutton(form, text='Option 1', variable=radValue,
                    value=1, command=selectionCall)
r1.pack(side='top', anchor='w')
r2 = tk.Radiobutton(form, text='Option 2', variable=radValue,
                    value=2, command=selectionCall)
r2.pack(side='top', anchor='w')
r3 = tk.Radiobutton(form, text='Option 3', variable=radValue,
                    value=3, command=selectionCall)
r3.pack(side='top', anchor='w')
label = Label(form)
label.pack()
form.mainloop()
