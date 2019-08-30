import tkinter as tk
from tkinter import *

form = tk.Tk()
form.title('Tkinter Entry Widget')
form.geometry('300x150')
form.resizable(0, 0)
form.config(bg='light yellow')

label01 = Label(form, text='Enter Some Text:')
label01.config(font='Arial 15 bold',bg='light yellow')
label01.pack()
entry01 = Entry(form)
entry01.config(bg='aqua', bd=5)
entry01.pack()

label02 = Label(form, text='Enter Some Text:')
label02.config(font='Arial 15 bold',bg='light yellow')
label02.pack()
entry02 = Entry(form)
entry02.config(bg='light green', bd=5, show="●")
entry02.pack()

form.mainloop()


