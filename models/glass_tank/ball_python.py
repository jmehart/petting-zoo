from datetime import date
from models.animals.animals import Animal
from models.movements.slithering import Slithering

class BallPython(Animal, Slithering):

    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Slithering.__init__(self)

    def __str__(self):
        return f"{self.name} the {self.species}"
    
    
    def feed(self):
        print(f'{self.name} ate a boy named Dudley instead of eating {self.food} on {date.today()}')      