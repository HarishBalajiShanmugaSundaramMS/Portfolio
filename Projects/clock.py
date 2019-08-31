from datetime import datetime
from tkinter import *
from tkinter import ttk


from pytz import all_timezones, country_timezones, timezone

root = Tk()
root.title('Dual Clock')
root.resizable(0, 0)
root.config(bg='#25D366')



def center_window(w, h):
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

# To Display System Time, uncomment this
#
# f time():
#  string_01 = strftime('%I:%M:%S %p \n %d-%b-%Y')
#  lbl.config(text=string_01, bg='#25D366',
#             fg='#075E54')
#  lbl.after(1000, time)


def germantime():
    germany = timezone('Europe/Berlin')
    de_time = datetime.now(germany)
    string_01 = de_time.strftime('%I:%M:%S %p \n %d-%b-%Y')
    lbl1.config(text=string_01, bg='#25D366',
                fg='#075E54')
    lbl1.after(1000, germantime)


def indiantime():
    india = timezone('Asia/Kolkata')
    in_time = datetime.now(india)
    string_03 = in_time.strftime('%I:%M:%S %p \n %d-%b-%Y')
    lbl2.config(text=string_03, bg='#25D366',
                fg='#075E54')
    lbl2.after(1000, indiantime)


lbl1 = Label(root, font=('calibri', 40, 'bold'))
lbl2 = Label(root, font=('calibri', 40, 'bold'))

lbl1.pack(anchor='e')
lbl2.pack(anchor='e')

center_window(380, 250)

germantime()
indiantime()

status = Label(root, text='The German Time and the Indian Time are Displayed Here',
               relief=SUNKEN, anchor=W)
status.config(bg='#34B7F1')
status.pack(side=BOTTOM, fill=X)

# print(all_timezones)

germany = timezone('Europe/Berlin')
india = timezone('Asia/Kolkata')
de_time = datetime.now(germany)
in_time = datetime.now(india)
time_diff = (in_time - de_time)



root.mainloop()
