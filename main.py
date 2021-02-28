import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)

player = Player()
screen.listen()
screen.onkeypress(player.move_up, "Up")
car_manager = CarManager()
screen.tracer(0)
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()
    for car in car_manager.all_car:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard = Scoreboard()
            scoreboard.score(won=False)
    if player.ycor() > 280:
        game_is_on = False
        scoreboard = Scoreboard()
        scoreboard.score(won=True)
screen.exitonclick()
