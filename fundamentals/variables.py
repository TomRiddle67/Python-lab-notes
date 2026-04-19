#oop

class Car:
    def __init__(self, brand, color = 'Unknown'):
        self.brand = brand
        self.color = color

    def honk(self):
        print(f"{self.brand} is {self.color} and says Beep Beep!")

    def describe(self):
        print(f"{self.brand} is a {self.color} car ")

    def __str__(self) :
        return f"{self.brand} is a {self.color} car "
    
    def repaint(self, new_color):
        self.color = new_color
        return f" {self.brand} is now {self.color} car"



        

first_car = Car('Toyota', 'Red')
first_car.repaint('blue')
second_car = Car('Honda')

first_car.honk()
first_car.describe()

second_car.honk()
second_car.describe()

print(first_car)
print(second_car)
