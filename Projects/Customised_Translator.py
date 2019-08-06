import csv
import os
import os.path
import re
import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox, ttk
import smtplib
import pymysql
from googletrans import Translator
from PIL import Image, ImageTk
from PyDictionary import PyDictionary
from PyQt5 import QtGui
from tkcalendar import Calendar, DateEntry

#dictionary = PyDictionary("Dogs")
#print (dictionary.translateTo("ta"))

form = tk.Tk()
form.title('Translate')
form.geometry('500x400')
form.resizable(0, 0)


# creates the directory if not existing
dir = r'/Users/harishbalaji/documents/Translations'
if not os.path.exists(dir):
    os.mkdir(dir)


# deletes the file to avoid row appends on every execution of the program
if os.path.exists('/Users/harishbalaji/documents/Translations/Learning German.csv'):
    os.remove(
        '/Users/harishbalaji/documents/Translations/Learning German.csv')


# adds the header portion of the csv file
with open(os.path.join(dir, 'Learning German.csv'), 'a+') as translation_file:
    translation_writer = csv.writer(
        translation_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    translation_writer.writerow(
        ['English Text', 'German Text'])


def __CancelCommand(event=None): pass
form.protocol('WM_DELETE_WINDOW', __CancelCommand)

tab_parent = ttk.Notebook(form)
tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)
tab3 = ttk.Frame(tab_parent)
tab4 = ttk.Frame(tab_parent)
tab5 = ttk.Frame(tab_parent)


tab_parent.add(tab1, text='Translate')
tab_parent.add(tab2, text='Reports')
tab_parent.add(tab3, text='Preferences')
tab_parent.add(tab4, text='Calendar')
tab_parent.add(tab5, text='Feedback')


show = Label(form, text='Using Translation to Learn a New Language')
show.config(font='Arial 23 bold', bg='#ececec')
show.pack()

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
            l.config(bg='#ececec', font='Arial 15 bold', fg='Green')
            # print(translations[0])
            print('English Text: ', translations[0].pronunciation)
            print('German Text: ', translations[0].text)
            #print('Exta Text: ',translations[0].extra_data)
            with open(os.path.join(dir, 'Learning German.csv'), 'a+') as translation_file:
                translation_writer = csv.writer(
                    translation_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                translation_writer.writerow(
                    [translations[0].pronunciation, translations[0].text])


def calldelete():
    e1.delete('0', END)
    l.config(text=(' '))


def applySettings():
    tex = str(e2.get())
    msg = messagebox.showwarning('Alert', tex)


def closeWindow():
    form.destroy()


def sendFeedback():
    content=str(t2.get('1.0', END))
    mail=smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    mail.login('translated2020@gmail.com','Translate@2020')
    mail.sendmail('translated2020@gmail.com','balajiharishmca@gmail.com',content)
    mail.close()


def previewCSV():
    root2 = tk.Tk()

    with open('/Users/harishbalaji/documents/Translations/Learning.csv', newline='') as file:
        reader = csv.reader(file)
        r = 0
        for col in reader:
            c = 0
            for row in col:
                # i've added some styling
                labelss = Label(form, width=10, height=2,
                                text=row, relief=RIDGE)
                labelss.grid(row=r, column=c)
                c += 1
            r += 1
    root2.mainloop()


textlab6 = Label(tab1, text='Select Number of Words:', bg='#ececec')
textlab6.config(font='Arial 15 bold')
textlab6.pack()

w = Scale(tab1, from_=2, to=5, orient=HORIZONTAL, bg='#ececec',
          width=15, sliderlength=25, length=350, font='Arial 15 bold')
w.set(5)
w.pack()

textlab1 = Label(tab1, text='Enter Your Text:', bg='#ececec')
textlab1.config(font='Arial 15 bold')
textlab1.pack()

e1 = Entry(tab1)
e1.config(bg='light yellow', font=('bold'), bd=3, width=400)
e1.pack()


#mystr = str(e1.get())
#wordList = re.sub("[^\w]", " ",  mystr).split()
# print(wordList)

l = Label(tab1, bd=5)
l.config(bg='#ececec', font='Arial 15 bold')
l.pack()


b1 = Button(tab1, text='Translate', command=callback, bd=5, width=10)
b1.config(font='Arial 15 bold')
b2 = Button(tab1, text='Clear', command=calldelete, width=10, bd=5)
b2.config(font='Arial 15 bold')
b4 = Button(tab1, text='Progress', command=previewCSV, width=10, bd=5)
b4.config(font='Arial 15 bold')


c1 = Checkbutton(tab1, text='Capture Datalogs', bg='#ececec',
                 offvalue='unchecked', onvalue='checked')
c1.config(font='Arial 15 bold')
c1.select()
c1.pack()


for widget_tab1 in (e1, l, b1, b2, b4):
    widget_tab1.pack()

# Controls of Second Tab

textlab2 = Label(tab2, text='You Can See Your Reports Here:', bg='#ececec')
textlab2.config(font='Arial 15 bold')
textlab2.pack()

MODES = [
    ('Progress Graph', 1),
    ('Weekly Report', 2),
    ('Monthly Report', 3),
    ("Leader Board", 4),
]

v = StringVar()
v.set(1)  # initialize

for text, mode in MODES:
    b = Radiobutton(tab2, text=text,
                    variable=v, value=mode, bg='#ececec')
    b.pack(anchor=W)

# Controls of Third Tab

textlab6 = Label(tab3, text='Select Your Path:', bg='#ececec')
textlab6.config(font='Arial 15 bold')
textlab6.pack()

e2 = Entry(tab3)
e2.config(bg='light yellow', font=('bold'), bd=3, width=400)
e2.pack()

textlab3 = Label(
    tab3, text='Select the Language You Want to Learn:', bg='#ececec')
textlab3.config(font='Arial 15 bold')
textlab3.pack()

OptionList1 = ["English", "German", "Tamil"]
o_variable1 = StringVar(tab3)
o_variable1.set(OptionList1[1])
opt1 = OptionMenu(tab3, o_variable1, *OptionList1)
opt1.config(width=5, font='Arial 15 bold')
opt1.pack()

textlab4 = Label(
    tab3, text='Select the Language You Want to Learn Through:', bg='#ececec')
textlab4.config(font='Arial 15 bold')
textlab4.pack()

OptionList2 = ["English", "German", "Tamil"]
o_variable2 = StringVar(tab3)
o_variable2.set(OptionList2[0])
opt2 = OptionMenu(tab3, o_variable2, *OptionList2)
opt2.config(width=5, font='Arial 15 bold')
opt2.pack()


textlab5 = Label(tab3, text='Select Your Native Language:', bg='#ececec')
textlab5.config(font='Arial 15 bold')
textlab5.pack()


OptionList3 = ["English", "German", "Tamil"]
o_variable3 = StringVar(tab3)
o_variable3.set(OptionList3[2])
opt3 = OptionMenu(tab3, o_variable3, *OptionList3)
opt3.config(width=5, font='Arial 15 bold')
opt3.pack()


b5 = Button(tab3, text='Save Preferences',
            command=applySettings, width=15, bd=5)
b5.config(font='Arial 15 bold')
b5.pack()


# Controls of Fourth Tab

cal = Calendar(tab4, selectmode='none', background='#ececec', foreground='Black',
               tooltipforeground='Green', bordercolor='Black', selectbackground='Red', selectforeground='Green',
               weekendbackground='Red', weekendforeground='Red',
               othermonthforeground='Lightgray', showothermonthdays=True,
               headersforeground='Blue', borderwidth=2, font='Arial 15 bold')

cal.tag_config('reminder', highlightbackground='red', foreground='green')

cal.pack(fill="both", expand=True)


tab_parent.pack(expand=1, fill='both')

b3 = Button(form, text='Close', command=closeWindow,
            width=10, bd=5, fg='black', bg='lightblue')
b3.config(font='Arial 15 bold')
b3.pack()


t2 = Text(tab5, height=1, width=45, bg='lightyellow')
t2.configure(font='Arial 15 bold')
t2.pack()


b6 = Button(tab5, text='Send', command=sendFeedback(),
            width=10, bd=5, fg='black', bg='lightblue')
b6.config(font='Arial 15 bold')
b6.pack()


form.mainloop()
