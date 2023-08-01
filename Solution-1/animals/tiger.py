from animals.animal import Animal


class Tiger(Animal):
    def sleep(self):
        print(self.name + ' отдыхает. (9 часов до бодрствования)')

    def wander(self):
        print(self.name + ' грозно ходит по вольеру.')

    def eat(self):
        print(self.name + ' жадно уплетает стейк.')

    def lick_up(self):
        print(self.name + ' вылизывет свою шерсть.')
