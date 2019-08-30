import tkinter as tk
from tkinter import *
form = tk.Tk()
form.title('Tkinter Labels')
form.geometry('400x150')
form.resizable(0, 0)
label01 = Label(form)
label01.config(text='Arial 15 Bold Green', 
                        font='Arial 15 bold', fg='green')
label01.pack()
label02 = Label(form)
label02.config(text='Arial 20 Italic Red', 
                        font='Arial 20 italic', fg='red')
label02.pack()
label03 = Label(form)
label03.config(text='Arial 25 Underline Blue',
               font='Arial 25 underline', fg='blue')
label03.pack()
label04 = Label(form)
label04.config(text='Arial 30 Overstrike Violet',
               font='Arial 30 overstrike', fg='violet')
label04.pack()
form.mainloop()

