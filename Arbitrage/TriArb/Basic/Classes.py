"""
Classes
"""
# Linear comments

class Car:

    def __init__(self, car_name,  car_color):
        self.name =  car_name
        self.color = car_color
    
    def getName(self):
        print(self.name)

new_car = Car('potin', 'rosadito')
# print(new_car.name)
# print(new_car.color)

new_car.getName()