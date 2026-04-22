# class Car:
    
#     def __init__(self, brand, color = 'Unknown'):
#         self.brand = brand
#         self.color = color

#     def __str__(self) :
#         return f"{self.brand} is a {self.color} car "

#     def drive(self):
#         return f"{self.brand} is driving"

# class ParkingLot:

#     def __init__(self):
#         self.cars = []

#     def park_car(self, car):
#         if len(self.cars) < 2:
#             self.cars.append(car)
#             return f"{car.brand} parked"
#         else:
#             return 'Car park is full'

#     def remove_car(self, brand):
#         for car in self.cars:
#             if car.brand == brand:
#                 self.cars.remove(car)
#                 return f"{brand} has been removed."
#             else:
#                 return 'car not found'

#     def show_cars(self):
        
#         for car in self.cars:
#             return f"Cars in parking lot: {car}"

# class ElectricCar(Car):

#     def __init__(self, brand, color, battery):
#         super().__init__(brand, color)
#         self.battery = battery
    
#     def charge(self):
#         return (f"{self.brand} is charging 🪫 {self.battery}%")
    
#     def drive(self):
#         return f"{self.brand} is driving silently"

# class GasCar(Car):

#     def fuel_tank(self):
#         return (f"{self.brand} is fueling ⛽️")
    
#     def drive(self):
#         return f"{self.brand} is driving with engine sound"

# class SportCar(Car):

#     def __init__(self, brand, color):
#         super().__init__(brand, color)
#         self._color = color

#     def set_color(self):
#         return self._color

#     def get_color(self, new_color):
#         self._color = new_color


# regular_car = Car('Toyota', 'Red')
# print(regular_car.drive())

# gas_car = GasCar('Volvo', 'Green')
# print(gas_car)

# fuel_gas_car = gas_car.fuel_tank()
# print(fuel_gas_car)

# electric = ElectricCar('Tesla', 'White', 30)
# print (electric)

# charge = electric.charge()
# print(charge)

# drive_electric = electric.drive()
# print(drive_electric)



# lot = ParkingLot()
# print(lot.park_car(regular_car))
# print(lot.park_car(electric))
# print(lot.remove_car(regular_car.brand))
# print(lot.show_cars())


# #Create a user that has a username, age, gender, another user with a driver's liscense

class User:
    def __init__(self, username, age, gender):
        self.username = username
        self.age = age
        self.gender = gender

    def __str__(self) -> str:
        return f"{self.username} is a {self.age} year old {self.gender}"

admin_user = User('admin', 25, 'male')
print(admin_user)

class User2(User):
    def __init__(self, username, age, gender, id_card ):
        super().__init__(username, age, gender)
        self.id_card = id_card

    def can_drive(self):
        return f"{self.username} is {self.age} years old {self.gender} and has a {self.id_card}"

user = User2('Celeste', 19, 'female', 'National_id')
print(user.can_drive())