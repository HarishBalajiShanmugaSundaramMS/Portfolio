# ===================================================
# Title:  Deactivating Close Button in the Title Bar
# Author: HarishBalaji ShanmugaSundaram
# Date:   21 August 2019
# ===================================================

import tkinter as tk
from tkinter import *

form = tk.Tk()
form.title('Deactivated Close Button')
form.geometry('300x100')
form.resizable(0, 0)


def closeWindow():
    form.destroy()


def __CancelCommand(event=None): pass


form.protocol('WM_DELETE_WINDOW', __CancelCommand)
labelControl01 = Label(
    form, text='The Close Button Is Deactivated', font='Arial 15 bold', fg='red')
labelControl01.pack()
labelControl02 = Label(
    form, text='Click The Below Button To Close', font='Arial 15 bold')
labelControl02.pack()
button01 = Button(form, text='Close', command=closeWindow,
                  width=10, bd=5, fg='black')
button01.config(font='Arial 15 bold')
button01.pack()
labelControl02 = Label(
    form, text='This Feature Is Useful While Working With File System',
    font='Arial 10 bold', fg='green')
labelControl02.pack()
form.mainloop()
