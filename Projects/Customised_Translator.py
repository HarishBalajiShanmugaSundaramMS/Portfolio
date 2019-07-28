import csv
import os
import os.path
#import shutil
import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox, ttk

import pymysql
from googletrans import Translator
from PIL import Image, ImageTk

form = tk.Tk()
form.title('Translate')
form.geometry('500x400')
form.resizable(0, 0)


def __CancelCommand(event=None): pass
form.protocol('WM_DELETE_WINDOW', __CancelCommand)

tab_parent = ttk.Notebook(form)
tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)
tab3 = ttk.Frame(tab_parent)


tab_parent.add(tab1, text='Translate')
tab_parent.add(tab2, text='Reports')
tab_parent.add(tab3, text='Preferences')


show = Label(form, text='Translation Gets Attention')
show.config(font=('bold'))
show.pack()
show1 = Label(form, text='*****************************************')
show1.config(font=('bold'))
show1.pack()

# Controls of First Tab

translator = Translator()


def callback():
    if len(e1.get()) == 0:
        msg = messagebox.showwarning('Alert', 'Empty Input')
    else:
        translations = translator.translate([e1.get()], dest='de')
        for translation in translations:
            total = str(e1.get())
            l.config(text='Translation = %s' % translation.text)
            l.config(font=('bold'))


def calldelete():
    e1.delete('0', END)
    l.config(text=(' '))


def closeWindow():
    form.destroy()


def previewCSV():
    with open('test.csv', newline = '') as file:
        reader = csv.reader(file)
        r = 0
        for col in reader:
            c = 0
            for row in col:
            # i've added some styling
                label = Label(form, width = 10, height = 2, \
                               text = row, relief = RIDGE)
                label.grid(row = r, column = c)
                c += 1
            r += 1


textlab6 = Label(tab1, text='Select number of words:',bg='#ececec')
textlab6.config(font=('bold'))
textlab6.pack()

w = Scale(tab1, from_=2, to=4, orient=HORIZONTAL, bg='#ececec')
w.set(4)
w.pack()

textlab1 = Label(tab1, text='Enter Your Text:', bg='#ececec')
textlab1.config(font=('bold'))
textlab1.pack()
e1 = Entry(tab1)
e1.config(bg='light yellow', font=('bold'), bd=3)
e1.pack()
l = Label(tab1, bd=5, bg='#ececec')
b1 = Button(tab1, text='Translate', command=callback, bd=5, width=10)
b1.config(font=('bold'))
b2 = Button(tab1, text='Clear', command=calldelete, width=10, bd=5)
b2.config(font=('bold'))
b4 = Button(tab1, text='Progress', command=previewCSV, width=10, bd=5)
b4.config(font=('bold'))
b3 = Button(tab1, text='Close', command=closeWindow, width=10, bd=5)
b3.config(font=('bold'))
c1 = Checkbutton(tab1, text='Capture Datalogs', bg='#ececec')
c1.config(font=('bold'))
c1.pack()
for widget_tab1 in (e1, l, b1, b2, b4, b3):
    widget_tab1.pack()

# Controls of Second Tab

textlab2 = Label(tab2, text='You can see your reports here:',bg='#ececec')
textlab2.config(font=('bold'))
textlab2.pack()

MODES = [
        ('Progress Graph', 1),
        ('Weekly Report', 2),
        ('Monthly Report', 3),
        ("Leader Board", 4),
    ]

v = StringVar()
v.set(1) # initialize

for text, mode in MODES:
    b = Radiobutton(tab2, text=text,
                        variable=v, value=mode,bg='#ececec')
    b.pack(anchor=W)

# Controls of Third Tab

textlab3 = Label(tab3, text='Select the langage you want to learn:',bg='#ececec')
textlab3.config(font=('bold'))
textlab3.pack()

OptionList1 = ["English","German","Tamil"]
o_variable1 = StringVar(tab3)
o_variable1.set(OptionList1[1])
opt1 = OptionMenu(tab3, o_variable1, *OptionList1)
opt1.config(width=5, font=('TkDefaultFont', 9,'bold'))
opt1.pack()

textlab4 = Label(tab3, text='Select the langage you want to learn through:',bg='#ececec')
textlab4.config(font=('bold'))
textlab4.pack()

OptionList2 = ["English","German","Tamil"]
o_variable2 = StringVar(tab3)
o_variable2.set(OptionList2[0])
opt2 = OptionMenu(tab3, o_variable2, *OptionList2)
opt2.config(width=5, font=('TkDefaultFont', 9,'bold'))
opt2.pack()


textlab5 = Label(tab3, text='Select your native langage:',bg='#ececec')
textlab5.config(font=('bold'))
textlab5.pack()


OptionList3 = ["English","German","Tamil"]
o_variable3 = StringVar(tab3)
o_variable3.set(OptionList3[2])
opt3 = OptionMenu(tab3, o_variable3, *OptionList3)
opt3.config(width=5, font=('TkDefaultFont', 9,'bold'))
opt3.pack()

tab_parent.pack(expand=1, fill='both')

form.mainloop()