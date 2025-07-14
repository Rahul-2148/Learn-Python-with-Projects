from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass #dummy statement (No implementation)
    
class Car(Vehicle):
    def start(self):
        print("Car starts with a key")
        
class Bike(Vehicle):
    def start(self):
        print("Bike starts with a kick")
        
car = Car()
bike = Bike()

car.start()
bike.start()