from turtle import Turtle  # class


class Scoreboard(Turtle): # inherit all the methods and attributes from its parent class (Turtle)
    """
     A class to represent a Scoreboard. display the scores on the screen 

    """
    def __init__(self):  # override
        """
        The constructor for Scoreboard class. Initialize the scores on the screen

        Attributes
        ----------
        l_score : int
           initial score of left paddle
        r_score : int
            initial score of right paddle

        """

        super().__init__()  # call/access the init method defined in the superclass (Turtle)
        self.color("yellow")
        self.penup()
        self.hideturtle()
        self.l_score = 0  # default value that can be modified
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Delete the current scores and update the new ones.
        :return: 
        """
        self.clear()  # Delete the turtle’s drawings from the screen. Do not move turtle
        self.goto(-100, 200)
        #  write text at the current turtle position - the turtle don't move
        self.write(self.l_score, align="center", font=("Courier", 60, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 60, "normal"))

    def r_point(self):
        """
        add one point to the right paddle
        """
        self.r_score += 1
        self.update_scoreboard()

    def l_point(self):
        """
           add one point to the left paddle
           """
        self.l_score += 1
        self.update_scoreboard()

