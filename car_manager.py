import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager():

    def __init__(self):
        self.all_cars_list = []
        self.car_speed = STARTING_MOVE_DISTANCE


    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.color(random.choice(COLORS))
            new_ycor = random.randint(-250,250)
            new_car.goto(300,new_ycor)
            self.all_cars_list.append(new_car)

    def move_cars(self):
        for car in self.all_cars_list:
            car.backward(self.car_speed)

    def speed_plus(self):
        self.car_speed += 1













