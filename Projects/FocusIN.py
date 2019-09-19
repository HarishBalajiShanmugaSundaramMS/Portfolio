import tkinter as tk
from tkinter import *
root = tk.Tk()
root.title('Keyboard Focus-In Event')
root.resizable(0, 0)
root.config(bg='#99cc33')
def onReturn(event):
    label02.config(text=entry01.get())
label01 = tk.Label(root, text='Enter Some Text', 
                    font=('calibri', 40, 'bold'))
label01.config(bg='#99cc33',fg='#006c54')
entry01 = tk.Entry(root, font=('calibri', 20, 'bold'))
entry01.focus()  # * Sets Focus
entry02 = tk.Entry(root, font=('calibri', 20, 'bold'))
entry02.bind('<FocusIn>', onReturn)
label02 = tk.Label(root, text='', font=('calibri', 40, 'bold'))
label02.config(bg='#99cc33',fg='#006c54')
label03=tk.Label(root,text='See what happens after the Entry02 widget gets focus',
relief='sunken')
label03.config(bg='#e0d86e')
label01.grid(row=0, column=0, padx=5, pady=5, sticky=W+E+N+S)
entry01.grid(row=1, column=0, padx=5, pady=5, sticky=W+E+N+S)
entry02.grid(row=2, column=0, padx=5, pady=5, sticky=W+E+N+S)
label02.grid(row=3, column=0, padx=5, pady=5, sticky=W+E+N+S)
label03.grid(row=4, column=0, sticky=W+E+N+S)
root.mainloop()



