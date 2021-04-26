import turtle as t

def sierpinski(length, n):
    if n == 0:
        t.pd()
        for i in range(0, 6):
            t.fd(length)
            t.left(60)
        t.penup()
    else:
        sierpinski(length / 2, n - 1)

        t.fd(length)

        sierpinski(length / 2, n - 1)

        t.bk(length)

        t.left(60)
        t.penup()
        t.fd(length)

        t.right(60)
        sierpinski(length / 2, n - 1)
        t.left(60)

        t.bk(length)

        t.right(60)

t.speed(10)
t.pensize(2)
t.penup()
t.goto(-200, -200)
t.pendown()
sierpinski(300, 6)
t.exitonclick()