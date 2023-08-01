from animals.animal import Animal


class Monkey(Animal):
    def sleep(self):
        print(self.name + ' отдыхает. (7 часов до бодрствования)')

    def wander(self):
        print(self.name + ' бегает по всему вольеру!')

    def eat(self):
        print(self.name + ' нервно ест свой банан.')

    def looking_bugs(self):
        print(self.name + ' ищет у себя в волосах букашек.')
