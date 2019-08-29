import turtle
import tkinter as tk
def forward():
    t.forward(100)
    t.speed(1)
def rotate():
    t.right(90)
form=tk.Tk()
form.title('Tkinter Canvas')
canvas=tk.Canvas(form,width=300,height=300)
canvas.pack()
t= turtle.RawTurtle(canvas)
t.pencolor('#34B7F1')
t.pensize(3)
button01=tk.Button(form,text='Move',command=forward)
button02=tk.Button(form,text='Rotate',command=rotate)
button01.pack()
button02.pack()
form.mainloop()





