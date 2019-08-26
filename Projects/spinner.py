# ======================================
# Title:  Tkinter Spinners
# Author: HarishBalaji ShanmugaSundaram
# Date:   22 August 2019
# ======================================
import tkinter as tk
from tkinter import *

form = tk.Tk()
form.title('Tkinter Spinners')
form.geometry('250x200')
form.resizable(0, 0)
label01 = Label(form)
label01.config(text='Spins from -10 to +10', font='Arial 15 bold', fg='blue')
label01.pack()
spin01 = Spinbox(form, from_=-10, to=10, bd=5)
spin01.config(font='Arial 15 bold', fg='black', bg='aqua')
spin01.pack()
label02 = Label(form)
label02.config(text='Spins from 1 to 5', font='Arial 15 bold', fg='red')
label02.pack()
spin02 = Spinbox(form, from_=1, to=5, bd=5)
spin02.config(font='Arial 15 bold', fg='black', bg='pink')
spin02.pack()
label03 = Label(form)
label03.config(text='Spins from -15 to -10', font='Arial 15 bold', fg='Brown')
label03.pack()
spin03 = Spinbox(form, from_=-15, to=-10, bd=5)
spin03.config(font='Arial 15 bold', fg='black', bg='lightyellow')
spin03.pack()
form.mainloop()
