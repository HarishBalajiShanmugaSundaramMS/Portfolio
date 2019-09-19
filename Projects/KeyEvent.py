import tkinter as tk
from tkinter import *
root = tk.Tk()
root.title('Keyboard <KEY> Event')
root.resizable(0, 0)
root.config(bg='#f7c8c9')
def onReturn(event):
    label02.config(text=entry01.get())
label01 = tk.Label(root, text='Enter Some Text', 
                    font=('calibri', 40, 'bold'))
label01.config(bg='#f7c8c9')
entry01 = tk.Entry(root, font=('calibri', 20, 'bold'))
entry01.focus()  # * Sets Focus
entry01.bind('<$>', onReturn)
label02 = tk.Label(root, text='', font=('calibri', 40, 'bold'))
label02.config(bg='#f7c8c9')
label03=tk.Label(root,text='Type $ after entering some text in Entry widget',
relief='sunken')
label03.config(bg='#e8d4a2')
label01.grid(row=0, column=0, padx=5, pady=5, sticky=W+E+N+S)
entry01.grid(row=1, column=0, padx=5, pady=5, sticky=W+E+N+S)
label02.grid(row=2, column=0, padx=5, pady=5, sticky=W+E+N+S)
label03.grid(row=3, column=0, sticky=W+E+N+S)
root.mainloop()



