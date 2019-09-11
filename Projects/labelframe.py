import tkinter as tk
from tkinter import *
root = tk.Tk()
root.title('TKinter Label Frame')
root.resizable(0, 0)
root.config(bg='#ed1965')
userLoginLabelFrame = tk.LabelFrame(
    root, text="User Login", width=1000, height=100)
userLoginLabelFrame.config(width=5, font='Arial 30 bold', bd=5)
userNameLabel = tk.Label(userLoginLabelFrame, text="User Name")
userNameLabel.config(font='Arial 20 bold')
userNameEntry = tk.Entry(userLoginLabelFrame, width=15)
userNameEntry.config(font='Arial 20 bold', bd=3, bg='#f9e498')
userPasswordLabel = tk.Label(userLoginLabelFrame, text="Password")
userPasswordLabel.config(font='Arial 20 bold')
userPasswordEntry = tk.Entry(userLoginLabelFrame, width=15)
userPasswordEntry.config(font='Arial 20 bold', bd=3, show='✪', bg='#f9e498')
userNameLabel.grid(row=0, columnspan=1, sticky=NSEW, padx=5, pady=5)
userNameEntry.grid(row=0, column=1, sticky=NSEW, padx=5, pady=5)
userPasswordLabel.grid(row=1, columnspan=1, sticky=NSEW, padx=5, pady=5)
userPasswordEntry.grid(row=1, column=1, sticky=NSEW, padx=5, pady=5)
userLoginLabelFrame.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
root.mainloop()

