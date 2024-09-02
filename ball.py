from turtle import Turtle  # class


class Ball(Turtle): # # inherit all the methods and attributes from its parent class (Turtle)
    """
     A class to represent a ball. the ball can move throughout the screen

    """

    def __init__(self):  # override
        """
        The constructor for Ball class. Initialize the ball on the screen

    Attributes
    ----------
    x_direction : int
        horizontal direction of the ball (1 or -1)
    y_direction : int
        vertical direction of the ball (1 or -1)
    move_distance : int
        moving distance of the ball on each frame

        """
        super().__init__()  # call/access the init method defined in the superclass (Turtle)
        self.shape("circle")
        self.color("red")
        self.penup()
        self.x_direction = 1  # default value that can be modified or changed in the future.
        self.y_direction = 1
        self.move_distance = 7  # default value that can be modified

    def move(self):
        """
        move the ball to the next position

        """
        new_x = self.xcor() + self.move_distance * self.x_direction
        new_y = self.ycor() + self.move_distance * self.y_direction
        self.goto(new_x, new_y)

    def bounce_y(self):
        """
        reverse y direction of the ball
        """
        self.y_direction *= -1

    def bounce_x(self):
        """
        reverse x direction of the ball

        """
        self.x_direction *= -1

    def reset_position(self):
        """
        reset position to the original point and then move in the opposite direction

        """
        self.goto(0, 0)
        self.move_distance = 7
        self.bounce_x()

    def increase_speed(self):
        """
        increase the ball speed

        """
        self.move_distance += 0.5









