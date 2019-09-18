import tkinter as tk
from tkinter import *
root = tk.Tk()
root.title('Mouse Pointer Enter Event')
root.resizable(0, 0)
root.config(bg='#832561')
def onReturn(event):
    label02.config(text=entry01.get())
label01 = tk.Label(root, text='Enter Some Text', 
                    font=('calibri', 40, 'bold'),fg='white')
label01.config(bg='#832561')
entry01 = tk.Entry(root, font=('calibri', 20, 'bold'))
entry01.focus()  # * Sets Focus
entry01.bind('<Enter>', onReturn)
label02 = tk.Label(root, text='', font=('calibri', 40, 'bold'),fg='white')
label02.config(bg='#832561')
label03=tk.Label(root,text='Move the mouse pointer inside the Entry widget',
relief='sunken')
label03.config(bg='#00c6d7')
label01.grid(row=0, column=0, padx=5, pady=5, sticky=W+E+N+S)
entry01.grid(row=1, column=0, padx=5, pady=5, sticky=W+E+N+S)
label02.grid(row=2, column=0, padx=5, pady=5, sticky=W+E+N+S)
label03.grid(row=3, column=0, sticky=W+E+N+S)
root.mainloop()



