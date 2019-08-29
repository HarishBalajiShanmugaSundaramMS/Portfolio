from tkinter import *
from tkinter import ttk
from time import strftime 
root = Tk() 
root.title('System Time')
root.resizable(0, 0)
root.config(bg='#25D366')
def center_window(w, h):
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)    
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
def time(): 
	string_01 = strftime('%I:%M:%S %p') 
	lbl.config(text = string_01, bg='#25D366',
    fg='#075E54') 
	lbl.after(1000, time)
def date(): 
    string_02 = strftime('%d-%b-%Y')
    lbl2.config(text = string_02, bg='#25D366',
    fg='#075E54')
    lbl2.after(1000, date) 
lbl = Label(root, font = ('calibri', 40, 'bold'))
lbl2 = Label(root, font = ('calibri', 40, 'bold'))
lbl.pack(anchor = 'center')
lbl2.pack(anchor = 'center')
center_window(300, 150) 
time();date();
status = Label(root, text='The System Time is Displayed Here', 
relief=SUNKEN, anchor=W)
status.config(bg='#34B7F1')
status.pack(side=BOTTOM, fill=X)
root.mainloop() 



