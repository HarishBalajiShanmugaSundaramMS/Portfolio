import turtle
pT = turtle.Turtle(shape="arrow")
def olympics():
    pT.hideturtle();pT.pensize(10);pT.speed(10)
    pT.pencolor("#009F3D");pT.circle(50)
    pT.penup();pT.setposition(-120, 0)
    pT.pendown();pT.pencolor("#F4C300")
    pT.circle(50);pT.penup()
    pT.setposition(60,60);pT.pendown()
    pT.pencolor("#DF0024");pT.circle(50)
    pT.penup();pT.setposition(-60, 60)
    pT.pendown();pT.pencolor("#000000")
    pT.circle(50);pT.penup()
    pT.setposition(-180, 60);pT.pendown()
    pT.pencolor("#0085C7");pT.circle(50)
def box():
    pT.penup();pT.setpos(-240,260)
    pT.pendown();pT.pensize(3)
    pT.pencolor("gray");pT.forward(360)
    pT.right(90);pT.forward(360)
    pT.right(90);pT.forward(360)
    pT.right(90);pT.forward(360)
olympics(); box()
turtle.getscreen()._root.mainloop()



