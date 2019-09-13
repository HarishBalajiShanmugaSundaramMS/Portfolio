from tkinter import *
from tkinter import ttk
import tkinter as tk

root = tk.Tk()
root.title('Frame and LabelFrame')
root.resizable(0, 0)
root.config(bg='#00d2f3')

frame = ttk.Frame(root)
frame.config(borderwidth=5, width=280, height=150,
             relief=SUNKEN)

labelFrame = tk.LabelFrame(root,text='LabelFrame')
labelFrame.config(borderwidth=5, width=280, height=150,
                  relief=SUNKEN,bg='#a560e8')

frame.grid(row=0,column=0,sticky='NSEW',padx=5,pady=5)
labelFrame.grid(row=1,column=0,sticky='NSEW',padx=5,pady=5)


root.mainloop()