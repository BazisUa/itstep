class Human:
    def __init__(self, name="Human"):
        self.name = name


class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passengers(self, human):
        self.passengers.append(human)

    def print_passengers_names(self):
        if self.passengers != []:
            print(f"Names of {self.brand} passengers:")
            for passenger in self.passengers:
                print(passenger.name)

        else:
            print(f"There are no passenger in {self.brand}")


nick = Human("Nick")
kate = Human("Kate")

car = Auto("Mercedes-Benz")
car.add_passengers(nick)
car.add_passengers(kate)
car.print_passengers_names()
