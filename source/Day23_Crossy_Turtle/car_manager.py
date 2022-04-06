from lib2to3.pgen2.pgen import generate_grammar
import turtle as t
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
NUM_CARS = 12

class CarManager:

    def __init__(self, num_cars_to_place=NUM_CARS):
        self.cars = []
        self.num_cars = num_cars_to_place
        self.speed = STARTING_MOVE_DISTANCE
        self.generate_cars()

    def generate_cars(self):
        for i in range(0,self.num_cars):
            color = random.choice(COLORS)
            self.cars.append(t.Turtle(shape='square'))
            self.cars[-1].color(color)
            self.cars[-1].shapesize(stretch_len=2)
            self.cars[-1].penup()
            heading = random.choice([0, 180])
            self.cars[-1].setheading(heading)
            random_x = random.randint(-250, 250)
            self.cars[-1].goto(random_x, -200 + i*40)

    
    def move(self):
        for car in self.cars:
            step_size = random.randint(1,STARTING_MOVE_DISTANCE)
            car.forward(step_size + self.speed)
            if car.xcor() < -300 and car.heading() == 180:
                car.setx(300)
            if car.xcor() > 300 and car.heading() == 0:
                car.setx(-300)


    def increase_speed(self):
        self.speed += MOVE_INCREMENT

    