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
        if len(self.cars) < 2:
            self.cars.append(car)
            print(f"{car.brand} parked")
        else:
            print('Car park is full')

    def remove_car(self, brand):
        for car in self.cars:
            if car.brand == brand:
                self.cars.remove(car)
                print(f"{brand} has been removed.")
                return
        print ('car not found')

    def show_cars(self):
        print("Cars in parking lot:")
        for car in self.cars:
            print(car)

    

lot = ParkingLot()
car1 = Car('Toyota', 'Red')
car2 = Car('Honda', 'blue')
car3 = Car('Benz', 'Black')

lot.park_car(car1)
lot.park_car(car2)
lot.park_car(car3)

lot.remove_car(car1.brand)
lot.show_cars()