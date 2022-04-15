# import the python datetime module to help us create a timestamp
from datetime import date

class RatSnake:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
                
        
stuart = RatSnake("Stuart", "Black Rat Snake")  

print(stuart.name)    
#prints Stuart  