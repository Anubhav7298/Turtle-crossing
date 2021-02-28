from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __int__(self):
        self.up()

    def score(self, won):
        self.up()
        self.color("white")
        if won:
            self.write("You have crossed, Yuppie!", align="center", font=FONT)
        else:
            self.write("You lost, try again!", align="center", font=FONT)

