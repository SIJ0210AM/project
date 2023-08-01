from animals.animal import Gender
from animals.monkey import Monkey
from animals.panda import Panda
from animals.tiger import Tiger
from zoo import Zoo

zoo = Zoo('Moscow', '12:00-19:00', )
animals = [
    Monkey('Heroin', 9, Gender.FEMALE),
    Monkey('Cocao', 9, Gender.MALE),
    Panda('Kuni', 5, Gender.MALE),
    Panda('Alina', 5, Gender.FEMALE),
    Tiger('Gena', 14, Gender.MALE),
    Tiger('Lef', 14, Gender.FEMALE)
]
for animal in animals:
    zoo.animal_registration(animal)

zoo.view_table_sheet()
print(zoo)
print(animals)
