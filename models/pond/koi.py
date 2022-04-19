from models import Animal, Swimming

class Koi(Animal, Swimming):

    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
        self.swimming = True

    def __str__(self):
        return f"{self.name} the {self.species}"