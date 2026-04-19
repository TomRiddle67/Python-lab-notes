class Car:
    def __init__(self, brand, color = 'Unknown'):
        self.brand = brand
        self.color = color

    def __str__(self) :
        return f"{self.brand} is a {self.color} car "

class ParkingLot:
    def __init__(self):
        self.cars = []

    def park_car(self, car):
        self.cars.append(car)
        return f"{car.brand} parked sucessfully"

    def show_cars(self):
        print('Cars in parking lot: ')
        for car in self.cars:
            return car

lot = ParkingLot()
car1 = Car('Toyota', 'Red')
car2 = Car('Toyota', 'blue')

lot.park_car(car1)
lot.park_car(car2)

lot.show_cars()