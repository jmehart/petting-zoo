from models import Animal, Slithering

class RatSnake(Animal, Slithering):

    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Slithering.__init__(self)

    def __str__(self):
        return f"{self.name} the {self.species}"