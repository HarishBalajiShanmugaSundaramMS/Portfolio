# ======================================
# Title:  Tkinter ComboBox
# Author: HarishBalaji ShanmugaSundaram
# Date:   26 August 2019
# ======================================
from tkinter import *
from tkinter import ttk

form = Tk()
form.title('Tkinter ComboBoxes')
form.geometry('300x150')
form.config(bg='#4267B2')
label01 = Label(form, text='Various Alignments & States')
label01.config(bg='#4267B2', fg='white')
label01.pack()
comboBox01 = ttk.Combobox(form,
                          values=['Python', 'Java', 'C++', 'C#', 'C'], state='normal')
comboBox01.current(0)
comboBox01.pack()
comboBox02 = ttk.Combobox(form,
                          values=['India', 'Germany',
                                  'Sweden', 'Norway', 'Denmark'],
                          state='readonly')
comboBox02.current(1)
comboBox02.config(justify='right')
comboBox02.pack()
comboBox03 = ttk.Combobox(form,
                          values=['MySQL', 'PostgreSQL', 'Oracle'], state='disabled')
comboBox03.current(2)
comboBox03.config(justify='center')
comboBox03.pack()
form.mainloop()
