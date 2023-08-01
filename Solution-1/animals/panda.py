from animals.animal import Animal


class Panda(Animal):
    def sleep(self):
        print(self.name + ' отдыхает. (12 часов до бодрствования)')

    def wander(self):
        print(self.name + ' перекатывается с бока на бок.')

    def eat(self):
        print(self.name + ' с кайфом хавает бамбук.')

    def chill(self):
        print(self.name + ' сидит и наслаждается существованием.')
