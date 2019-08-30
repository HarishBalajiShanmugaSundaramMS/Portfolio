import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
root = tk.Tk()
root.title('Tkinter Text')

widthValue = 110
heightValue = 120

img = ImageTk.PhotoImage(Image.open("Tarzan.jpg"))

text1 = tk.Text(root)
text1.image_create(tk.END, image=img)
text1.config(height=20, width=40)
text1.pack(side=tk.LEFT)
text2 = tk.Text(root, height=20, width=45)
text2.tag_configure('big', font=('Verdana', 20, 'bold'))
text2.tag_configure('color',foreground='#476042',font=('Tempus Sans ITC', 8, 'bold'))
text2.insert(tk.END,'\nComboBox\n', 'big')
quote = """
A Combobox is an Entry widget with a dropdown listbox.\n
The users can type into the combobox or pick from the dropdown list.\n
"""
text2.insert(tk.END, quote, 'color')
text2.insert(tk.END,'\nOptionMenu\n', 'big')
quote = """
The OptionMenu is a Button widget with a menu attached.\n 
The choices are fixed, and the users can't type in their own value.\n
"""
text2.insert(tk.END, quote, 'color')
text2.pack(side=tk.RIGHT)
root.mainloop()
