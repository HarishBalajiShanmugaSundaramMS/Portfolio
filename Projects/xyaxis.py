import tkinter as tk
from tkinter import *
root = tk.Tk()
root.title('Mouse Pointer Click Positions')
root.resizable(0, 0)
root.geometry('350x300')
root.config(bg='#9381FF')
def callback(event):
    xPosition=str(event.x)
    yPosition=str(event.y)
    mousePosition=str('Mouse clicked at '+ 'X: '+xPosition+' ' 
    +'Y:'+ yPosition)
    statusBar.config(text=mousePosition)
def center_window(w, h):
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.bind("<Button-1>", callback)
statusBar=tk.Label(root,text='Click Anywhere in the Window', 
relief='sunken')
statusBar.config(bg='#B8B8FF')
statusBar.pack(side=BOTTOM, fill=X)
center_window(350,300)
root.mainloop()




