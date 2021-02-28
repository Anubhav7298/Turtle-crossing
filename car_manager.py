from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_car = []

    def create_car(self):
        if random.randint(3, 6) == 6:
            new_car = Turtle()
            new_car.goto(300, random.randint(-240, 260))
            new_car.shape("square")
            new_car.lt(180)
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.up()
            self.all_car.append(new_car)

    def move_car(self):
        for car in self.all_car:
            car.forward(STARTING_MOVE_DISTANCE)


