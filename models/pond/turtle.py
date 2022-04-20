from datetime import date
from models.animals.animals import Animal
from models.movements.swimming import Swimming

class Turtle(Animal, Swimming):

    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
        self.swimming = True

    def __str__(self):
        return f"{self.name} the {self.species}"
    
    def feed(self):
        print(f'{self.name} ate {self.food} on {date.today()} and then snapped at Tina')   