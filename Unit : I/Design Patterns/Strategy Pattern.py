#Design Pattern
#Strategy Pattern

from abc import ABC, abstractmethod

class TravelStrategy(ABC):
    @abstractmethod
    def travel(self, distance):
        pass


# Concrete Strategies
class Bus(TravelStrategy):
    def travel(self, distance):
        print(f"Travelling {distance}km by Bus")


class Train(TravelStrategy):
    def travel(self, distance):
        print(f"Travelling {distance}km by Train")


class Flight(TravelStrategy):
    def travel(self, distance):
        print(f"Travelling {distance}km by Flight")


class Trip:
    def __init__(self, strategy):
        self.strategy = strategy

    def start(self, distance):
        self.strategy.travel(distance)


trip = Trip(Bus())
trip.start(50)

trip = Trip(Train())
trip.start(300)

trip = Trip(Flight())
trip.start(1500)

#Output 
'''Travelling 50km by Bus
Travelling 300km by Train
Travelling 1500km by Flight'''