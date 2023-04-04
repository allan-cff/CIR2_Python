import turtle
turtle.setup(500, 500)
""" EX 1
turtle.up()
turtle.goto(100, 100)
turtle.down()

for i in range(4):
    turtle.forward(20)
    turtle.left(90)

turtle.exitonclick()
"""


def dessiner_carre(x, y, c):
    turtle.up()
    turtle.goto(x-(c//2), y+(c//2))
    turtle.down()
    for i in range(4):
        turtle.forward(c)
        turtle.right(90)
    turtle.up()    

""" EX 2
dessiner_carre(0, 0, 20)
dessiner_carre(0, 0, 60)
dessiner_carre(0, 0, 100)
turtle.exitonclick()
"""

def dessiner_cercle(x, y, r):
    turtle.up()
    turtle.goto(x, y-r)
    turtle.down()
    turtle.circle(r)
    turtle.up()

""" EX 3
dessiner_cercle(0, 0, 20)
dessiner_cercle(0, 0, 60)
dessiner_cercle(0, 0, 100)
turtle.exitonclick()
"""

dessiner_carre(0, 0, 100)
dessiner_cercle(0, 0, 50)
turtle.exitonclick()