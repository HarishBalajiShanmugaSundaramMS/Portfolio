# =================================================
# Title:  Tkinter Images on Other Widgets
# Author: HarishBalaji ShanmugaSundaram
# Date:   26 August 2019
# =================================================

import tkinter.messagebox
from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk

form = Tk()
form.title('Tkinter Image')
form.geometry('300x303')
form.config(bg='#008C15')
form.resizable(0, 0)


def callback():
    text1.insert(END, '••••••Button Clicked••••••', 'color')


widthValue = 110
heightValue = 120
img = Image.open("Mickey.jpg")
img = img.resize((widthValue, heightValue), Image.ANTIALIAS)
photoImg = ImageTk.PhotoImage(img)
panel = Label(form, image=photoImg, cursor='dotbox')
panel.pack()
b = Button(form, image=photoImg, command=callback, width=widthValue,
           height=heightValue, cursor='arrow')
b.pack()
quote = """First Image is a Label•••Note the Cursors
Second Image is a Button•••Click on it
"""
text1 = Text(form)
text1.config(bg='#FFC600')
text1.insert(END, quote, 'color')
text1.pack(side=LEFT)
form.mainloop()
