import pandas as pd

from animals.animal import Animal
from typing import NewType

TypeAnimal = NewType('TypeAnimal', str)


class Zoo:
    def __init__(self, address: str, opening_hours: str):
        self.address = address
        self.opening_hours = opening_hours
        self.list_animals: dict[TypeAnimal, list[Animal]] = {}

    def animal_registration(self, animal: Animal):
        type_animal = TypeAnimal(animal.__class__.__name__)
        if type_animal in self.list_animals.keys():
            self.list_animals[type_animal].append(animal)
        else:
            self.list_animals[type_animal] = [animal, ]

    def view_table_sheet(self):
        anim = pd.DataFrame(self.list_animals)
        anim.to_excel('animals.xlsx')

    def __str__(self):
        return f'Animal(address = {self.address}, opening_hours = {self.opening_hours},' \
               f' list_animals = {self.list_animals})'
