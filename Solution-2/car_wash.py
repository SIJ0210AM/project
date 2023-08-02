from cars.car import Car


class CarWash:
    def __int__(self, address, opening_hours, price_list, application_list):
        self.address = address
        self.opening_hours = opening_hours
        self.price_list = price_list
        self.processing_cars: list[Car] = []
        # application_list - список автомобилей находящихся на мойке-заправке

    def washing(self, car: Car):
        for car in self.processing_cars:
            print(car.__name__ + ' car is wahing.')
            print(car.__name__ + 'is washed.')
            self.processing_cars.remove(car)

    def registration(self, car: Car):
        self.processing_cars.append(car)
