# =======================================
# Title:  Tkinter ProgressBars
# Author: HarishBalaji ShanmugaSundaram
# Date:   22 August 2019
# =======================================

import tkinter as tk
from tkinter import *
from tkinter import ttk

form = tk.Tk()
form.title('Tkinter ProgressBars')
form.geometry('300x150')
form.resizable(0, 0)
label01 = Label(form)
label01.config(text='Determinate ProgressBar', font='Arial 15 bold', fg='blue')
label01.pack()
progress01 = ttk.Progressbar(
    form, orient=HORIZONTAL, length=100, mode='determinate')
progress01.pack()
progress01.start()
label02 = Label(form)
label02.config(text='Indeterminate ProgressBar',
               font='Arial 15 bold', fg='red')
label02.pack()
progress02 = ttk.Progressbar(
    form, orient=HORIZONTAL, length=200, mode='indeterminate')
progress02.pack()
progress02.start()
label03 = Label(form, text='Horizontal ProgressBars',
                font='Arial 23 bold', fg='Green')
label03.pack()
label04 = Label(form, text='Indeterminate ProgressBars Appear Static on Mac :-(',
                font='Arial 8 bold', fg='Red')
label04.pack()
form.mainloop()
