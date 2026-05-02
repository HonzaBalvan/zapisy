import turtle

class TlustaZelva(turtle.Turtle):
    def __init__(self, tloustka=10):
        super().__init__()
        self.width(tloustka)
        self.pencolor("orange")

t1 = TlustaZelva()
t1.left(90)
t1.forward(100)
t1.left(-90)
t1.forward(100)
t1.left(-135)
t1.forward(141)
t1.left(135)
t1.forward(100)
t1.left(135)
t1.forward(141)
t1.left(-90)
t1.forward(70)
t1.left(-90)
t1.forward(70)
t1.left(-45)
t1.forward(100)

t3 = TlustaZelva()
t3.forward(100)
t3.left(90)
t3.forward(100)
t3.left(-90)
t3.forward(100)
t3.left(-135)
t3.forward(141)
t3.left(135)
t3.forward(100)
t3.left(135)
t3.forward(141)
t3.left(-90)
t3.forward(70)
t3.left(-90)
t3.forward(70)
t3.left(-45)
t3.forward(100)

t2 = TlustaZelva()
for i in range(10):
    t2.left(35)
    t2.forward(20+-i)
    i += 1

turtle.done()
