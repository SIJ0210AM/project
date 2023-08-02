from car import Car


class PassengerCar(Car):
    def refuel(self):
        print(__class__.__name__ + ' заправлен(-а) 95-ым.')

    def drive(self):
        print(__class__.__name__ + ' не спеша везёт людей.')
