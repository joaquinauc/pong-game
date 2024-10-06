from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.turtlesize(1, 5)
        self.setposition(position)
        self.left(90)

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)


