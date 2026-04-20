class Car:
    def __init__(self, brand, color = 'Unknown'):
        self.brand = brand
        self.color = color

    def __str__(self) :
        return f"{self.brand} is a {self.color} car "

    def drive(self):
        return f"{self.brand} is driving"

class ParkingLot:
    def __init__(self):
        self.cars = []

    def park_car(self, car):
        if len(self.cars) < 2:
            self.cars.append(car)
            return f"{car.brand} parked"
        else:
            return 'Car park is full'

    def remove_car(self, brand):
        for car in self.cars:
            if car.brand == brand:
                self.cars.remove(car)
                return f"{brand} has been removed."
            else:
                return 'car not found'

    def show_cars(self):
        
        for car in self.cars:
            return f"Cars in parking lot: {car}"

class ElectricCar(Car):
    def __init__(self, brand, color, battery):
        super().__init__(brand, color)
        self.battery = battery
    
    def charge(self):
        return (f"{self.brand} is charging 🪫 {self.battery}%")
    
    def drive(self):
        return f"{self.brand} is driving silently"

class GasCar(Car):
    def fuel_tank(self):
        return (f"{self.brand} is fueling ⛽️")
    
    def drive(self):
        return f"{self.brand} is driving with engine sound"


regular_car = Car('Toyota', 'Red')
print(regular_car.drive())

gas_car = GasCar('Volvo', 'Green')
print(gas_car)

fuel_gas_car = gas_car.fuel_tank()
print(fuel_gas_car)

electric = ElectricCar('Tesla', 'White', 30)
print (electric)

charge = electric.charge()
print(charge)

drive_electric = electric.drive()
print(drive_electric)



lot = ParkingLot()
print(lot.park_car(regular_car))
print(lot.park_car(electric))
print(lot.remove_car(regular_car.brand))
print(lot.show_cars())