# import the python datetime module to help us create a timestamp
from datetime import date

class BallPython:

    def __init__(self, name, species, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food
        
        
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}') 
        
        
        
    def __str__(self):
        return f"{self.name} is a {self.species}"   
        