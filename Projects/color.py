#from tkinter import *
import tkinter as tk

form = tk.Tk()
form.title('Tkinter Colors')
form.geometry('300x150')
form.config(bg='#4267B2')
#form.wm_attributes('-transparentcolor','red')
#form.wm_attributes('-fullscreen','true')
form.wm_attributes('-toolwindow','true')

def onReturn(event):
    if(len(entry01.get())<8):
        form.config(bg='red')
    else:
        form.config(bg='light green')

    

entry01 = tk.Entry(form)
entry01.focus()
entry01.bind('<Return>',onReturn)

entry01.pack()
tk.mainloop()