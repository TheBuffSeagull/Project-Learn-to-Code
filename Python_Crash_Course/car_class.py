class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formated descriptive name."""
        return f"{self.year} {self.make} {self.model}".title()

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())