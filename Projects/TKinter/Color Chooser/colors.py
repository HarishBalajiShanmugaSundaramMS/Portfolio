from tkinter import *
from tkinter.colorchooser import *
form = Tk()
form.title('Color Chooser')
form.geometry('300x300')
def center_window(w, h):
    ws = form.winfo_screenwidth()
    hs = form.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    form.geometry('%dx%d+%d+%d' % (w, h, x, y))
def chooseColor():
    color=askcolor()
    print(color)
    strColor=str(color)
    substr = strColor[-9:-2]
    print(substr)
    form.config(bg=substr)
button01 = Button(text='Click',command=chooseColor)
button01.pack(side=BOTTOM)
center_window(300, 300)
mainloop() 
