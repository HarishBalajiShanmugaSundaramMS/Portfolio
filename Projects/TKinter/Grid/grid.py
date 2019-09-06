import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title('Grid Arrangements')

label01 = tk.Label(root,text='Python \n row=0 \n column=0')
label01.config(bd=3,relief='groove',width=10, bg='aqua')

label02 = tk.Label(root,text='Java  \n row=0 \n column=1')
label02.config(bd=3,relief='groove',width=10,bg='#ffaaaa')

label03 = tk.Label(root,text='VisualBasic  \n row=1 \n column=0')
label03.config(bd=3,relief='groove',width=10,bg='#36C5F0')

label04 = tk.Label(root,text='Ruby  \n row=1 \n column=1')
label04.config(bd=3,relief='groove',width=10,bg='#ffc168')

label05 = tk.Label(root,text='PERL  \n row=0 \n column=3 \n rowspan=2 ')
label05.config(bd=3,relief='groove',width=10,bg='#2EB67D')

label06 = tk.Label(root,text='HTML CSS JavaScript \n row=2 \n columnspan=3 \n column=0')
label06.config(bd=3,relief='groove',width=10,bg='#f7e8d5')


label01.grid(row=0, column=0, padx=5,pady=5,sticky=W)
label02.grid(row=0, column=1, padx=5,pady=5,sticky=W)
label03.grid(row=1, column=0, padx=5,pady=5,sticky=W)
label04.grid(row=1, column=1, padx=5,pady=5,sticky=W)

label05.grid(row=0, rowspan=2, column=3, padx=5,pady=5, sticky=W+E+N+S)
label06.grid(row=2, column=0,columnspan=3, padx=5,pady=5, sticky=W+E+N+S)

root.mainloop()
