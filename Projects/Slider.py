from tkinter import *
form = Tk()
form.title('Tkinter Scale')
form.geometry('350x180')
form.resizable(0, 0)
form.config(bg='#F4B400')
scale01 = Scale(form, from_=0, to=5, orient=HORIZONTAL,width=15, length=250)
scale01.config(font='Arial 15 bold', label='From 0 to 5 Default Value: 5',
bg='#4285F4',fg='white')
scale01.set(5)
scale01.pack()
scale02 = Scale(form, from_=1, to=3, orient=HORIZONTAL,width=15, length=250)
scale02.config(font='Arial 15 bold', label='From 1 to 3 Default Value: 1',
bg='#DB4437',fg='white')
scale02.set(1)
scale02.pack()
scale03 = Scale(form, from_=0, to=10, orient=HORIZONTAL, width=15, length=250)
scale03.config(font='Arial 15 bold', label='From 0 to 10 Default Value: 6',
bg='#0F9D58',fg='white')
scale03.set(6)
scale03.pack()
form.mainloop()


