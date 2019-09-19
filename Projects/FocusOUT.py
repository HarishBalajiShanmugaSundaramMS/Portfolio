import tkinter as tk
from tkinter import *
root = tk.Tk()
root.title('Keyboard Focus-Out Event')
root.resizable(0, 0)
root.config(bg='#00AFB9')
def onReturn(event):
    label02.config(text=entry01.get())
label01 = tk.Label(root, text='Enter Some Text', 
                    font=('calibri', 40, 'bold'))
label01.config(bg='#00AFB9',fg='#fdfcdc')
entry01 = tk.Entry(root, font=('calibri', 20, 'bold'))
entry02 = tk.Entry(root, font=('calibri', 20, 'bold'))
entry02.bind('<FocusOut>', onReturn)
label02 = tk.Label(root, text='', font=('calibri', 40, 'bold'))
label02.config(bg='#00AFB9',fg='#fdfcdc')
label03=tk.Label(root,text='See what happens after the Entry02 widget loses focus',
relief='sunken')
label03.config(bg='#fed9b7')
label01.grid(row=0, column=0, padx=5, pady=5, sticky=W+E+N+S)
entry01.grid(row=1, column=0, padx=5, pady=5, sticky=W+E+N+S)
entry02.grid(row=2, column=0, padx=5, pady=5, sticky=W+E+N+S)
label02.grid(row=3, column=0, padx=5, pady=5, sticky=W+E+N+S)
label03.grid(row=4, column=0, sticky=W+E+N+S)
root.mainloop()



