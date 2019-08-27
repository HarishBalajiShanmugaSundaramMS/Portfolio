# ======================================
# Title:  Tkinter OptionMenu
# Author: HarishBalaji ShanmugaSundaram
# Date:   26 August 2019
# ======================================
import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title('Tkinter OptionMenu')
root.geometry('250x100')
root.config(bg='#128C7E')
root.resizable(0, 0)
OptionList1 = ['MacBook Pro', 'MacBook Air',
               'iMac Pro', 'Mac Mini']
var = tk.StringVar(root)
var.set(OptionList1[1])
opt1 = tk.OptionMenu(root, var, *OptionList1)
opt1.config(width=15, font='Arial 15 bold',
            bg='#34B7F1', fg='#075E54')
opt1.pack()
label = tk.Label(root, textvariable=var,
                 relief=SUNKEN, anchor=W)
label.config(width=15, bg='#25D366')
label.pack(side=BOTTOM, fill=X)
root.mainloop()
