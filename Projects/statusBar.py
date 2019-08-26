# =================================================
# Title:  Customized StatusBar Using Tkinter Label
# Author: HarishBalaji ShanmugaSundaram
# Date:   24 August 2019
# =================================================

import time
from tkinter import *

form = Tk()
form.title('Tkinter StatusBar Using Label')
form.geometry('300x150')
form.resizable(0, 0)
form.config(bg='#4D148C')
time_string = time.strftime('%H:%M')
s = str(time_string)


def showButton():
    status = Label(form, text='System Time is '+s,
                   bd=2, relief=SUNKEN, anchor=W)
    status.config(bg='#FF6600')
    status.pack(side=BOTTOM, fill=X)
    b1.configure(state=DISABLED)


label01 = Label(form, text='Tkinter Has No In-Built StatusBar Widget')
label01.config(font='Arial 15 bold', bg='#4D148C', fg='white')
label01.pack()
label02 = Label(form, text='This StatusBar Displays \n System Time')
label02.config(font='Arial 15 bold', bg='#4D148C', fg='white')
label02.pack()
b1 = Button(form, text='Show Customized StatusBar',
            command=showButton, bd=5, width=25)
b1.config(font='Arial 15 bold')
b1.pack()
form.mainloop()
