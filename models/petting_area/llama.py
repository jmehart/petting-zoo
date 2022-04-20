# import the python datetime module to help us create a timestamp
from datetime import date
from models.animals.animals import Animal
from models.movements.walking import Walking

# Designate Llama as a child class by adding (Animal) after the class name
class Llama(Animal, Walking):

    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        self.shift = shift

    def __str__(self):
        return f"{self.name} the {self.species}"
    
    def feed_llama(self):
        print(f'On {date.today()}, {self.name} had "Rockytop" sung to it so it would eat its {self.food}')