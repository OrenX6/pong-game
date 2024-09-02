from turtle import Turtle  # class

MOVE_DISTANCE = 40
UP = 90
DOWN = 270


class Paddle(Turtle):  # inherits all the methods and attributes from another class.
    """
       A class to represent a paddle. the paddle can move up and down
    ...

    Attributes
    ----------
    position : tuple
        Initial position of the paddle on the screen

    """

    def __init__(self, position):  # override
        """
        The constructor for Paddle class/Constructs all the necessary attributes for the Paddle object
        initialize the paddle on the screen

        :param position: x and y coordinates of the paddle
        :type position: tuple

        """
        super().__init__()   # call/access the init method defined in the superclass Turtle
        self.goto(position)  # initial object state
        self.color("blue")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()

    def move_up(self):
        """
        move the paddle up with specific distance

        """
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)
        if self.ycor() >= 250:
            self.sety(250)

    def move_down(self):
        """
        move the paddle down with specific distance

        """
        self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)
        if self.ycor() <= -250:
            self.sety(-250)
