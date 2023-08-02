from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, brand, fuel, horsepower, name):
        self.brand = brand
        self.fuel = fuel
        self.horsepower = horsepower
        self.name = name

    @abstractmethod
    def drive(self):
        ...

    @abstractmethod
    def refuel(self):
        ...

    def __str__(self):
        return f'(name = {self.name}, brand = {self.brand}, fuel = {self.fuel}, horsepower = {self.horsepower}'

    def __repr__(self):
        return self.__str__()
