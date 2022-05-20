import turtle

turtle.pensize(4)

k=0
j=0

for a in range(3):
    turtle.penup()
    turtle.goto(-180+j, 30)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor("yellow")
    for i in range(5):
        turtle.forward(100+k)
        turtle.right(144)
    turtle.end_fill()    
    j=j+180
    k=k+20
   
    


turtle.penup()
turtle.goto(80,-140)
turtle.pendown()      

# choose pen color
turtle.pencolor('Black')
turtle.done()
