import tkinter as tk
from tkinter import *
root = tk.Tk()
root.resizable(0, 0)
root.title('TKinter Grid Arrangements')
label01 = tk.Label(root, text='Row=0\nColumn=0')
label01.config(bd=3, relief='groove', width=10, bg='aqua', justify='left')
label01.grid(row=0, column=0, padx=5, pady=5, sticky=W)

label02 = tk.Label(root, text='Row=0\nColumn=1')
label02.config(bd=3, relief='groove', width=10, bg='#ffaaaa', justify='left')
label02.grid(row=0, column=1, padx=5, pady=5, sticky=W)

label03 = tk.Label(root, text='Row=1\nColumn=0')
label03.config(bd=3, relief='groove', width=10, bg='#36C5F0', justify='left')
label03.grid(row=1, column=0, padx=5, pady=5, sticky=W)

label04 = tk.Label(root, text='Row=1\nColumn=1')
label04.config(bd=3, relief='groove', width=10, bg='#ffc168', justify='left')
label04.grid(row=1, column=1, padx=5, pady=5, sticky=W)

label05 = tk.Label(root, text='Row=0\nColumn=2\nRowSpan=3 ')
label05.config(bd=3, relief='groove', width=10,
               bg='#075e54', justify='left', fg='white')
label05.grid(row=0, rowspan=3, column=2, padx=5, pady=5, sticky=W+E+N+S)

label06 = tk.Label(root, text='Row=2\nColumn=0\nColumnSpan=2')
label06.config(bd=3, relief='groove', width=10, bg='#f7e8d5', justify='left')
label06.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky=W+E+N+S)

label07 = tk.Label(root, text='Row=3\nColumn=0\nColumnSpan=3')
label07.config(bd=3, relief='groove', width=10, bg='#d2ea32', justify='left')
label07.grid(row=3, column=0,columnspan=3, sticky=W+E+N+S, padx=5, pady=5)

label08 = tk.Label(root, text='Row=4\nColumn=0\nColumnSpan=4')
label08.config(bd=3, relief='groove', width=10,
               bg='#ea4335', justify='left', fg='white')
label08.grid(row=4, column=0,columnspan=4, sticky=W+E+N+S, padx=5, pady=5)

label09 = tk.Label(root, text='Row=0\nColumn=3\nRowSpan=4')
label09.config(bd=3, relief='groove', width=10,
               bg='#a560e8', justify='right', fg='white')
label09.grid(row=0, column=3, rowspan=4, sticky=W+E+N+S, padx=5, pady=5)
root.mainloop()
