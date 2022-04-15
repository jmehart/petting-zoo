# import the python datetime module to help us create a timestamp
from datetime import date

class BallPython:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        
        
snape = BallPython("Snape", "Royal Ball Python Snake")  

print(snape.name) 
#prints Snape         