# import the python datetime module to help us create a timestamp
from datetime import date

class Goldfish:

    def __init__(self, name, species, food, chip_num):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food
        self.__chip_number = chip_num
    # setting class data type enforcer
    @property
    # getter returns privately scoped attribute
    def chip_num(self):
      return self.__chip_number
    # setter prevents user from changing chip_number value to keep permanent
    @chip_num.setter
    def chip_number(self, number):
      pass
        
        
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')        
        
        
        