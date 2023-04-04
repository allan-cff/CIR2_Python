import cmath
import turtle
import time
import random
turtle.setup(500, 500)


def list_n_sqrt(n, start_angle=0):
    angle = cmath.exp(1j*2*cmath.pi/n)
    result = []
    complex_value = cmath.rect(1, start_angle)
    for i in range(n):
        result.append(complex_value)
        complex_value = complex_value * angle
    return result


def dessiner_forme(liste_points):
    turtle.up()
    turtle.goto(liste_points[0])
    turtle.down()
    for point in liste_points:
        turtle.goto(point)
    turtle.goto(liste_points[0])
    turtle.up()


def get_random_rgb():
    red = str(random.randint(0, 99))
    green = str(random.randint(0, 99))
    blue = str(random.randint(0, 99))
    result = red if len(red) == 2 else ('0' + red)
    result = result + (green if len(green) == 2 else ('0' + green))
    result = result + (blue if len(blue) == 2 else ('0' + blue))
    return result

"""
while True:
    for i in range(3, 100):
        turtle.clear()
        turtle.fillcolor('#000000')
        turtle.begin_fill()
        dessiner_forme([(comp.real * 100, comp.imag * 100) for comp in list_n_sqrt(i)])
        turtle.end_fill()
        time.sleep(1)
"""

while True:
    turtle.speed(0)
    for i in range(0, 20):
        turtle.clear()
        turtle.fillcolor('#'+get_random_rgb())
        turtle.begin_fill()
        dessiner_forme([(comp.real * 100, comp.imag * 100) for comp in list_n_sqrt(3, 2*i*cmath.pi/20)])
        turtle.end_fill()
        time.sleep(0.5)

turtle.exitonclick()