#Design Pattern
#Factory pattern

# Base class
class Vehicle:
    def build(self):
        print("Building vehicle...")


# Concrete classes
class Car(Vehicle):
    def build(self):
        print("Building a Car")


class Bike(Vehicle):
    def build(self):
        print("Building a Bike")


class Truck(Vehicle):
    def build(self):
        print("Building a Truck")


# Factory class
class VehicleFactory:
    @staticmethod
    def get_vehicle(vehicle_type):
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "bike":
            return Bike()
        elif vehicle_type == "truck":
            return Truck()
        else:
            return None


# Client code
vehicle_type = input("Enter vehicle type: ").lower()
vehicle = VehicleFactory.get_vehicle(vehicle_type)

if vehicle:
    vehicle.build()
else:
    print("Vehicle not available")

# Output 
'''Enter vehicle type: Bike
Building a Bike'''