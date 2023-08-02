from car import Car


class Truck(Car):
    def refuel(self):
        print(__class__.__name__ + ' заправлен(-а) дизелем.')

    def drive(self):
        print(__class__.__name__ + ' куда-то едет.')
