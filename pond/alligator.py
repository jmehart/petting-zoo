# import the python datetime module to help us create a timestamp
from datetime import date

class Alligator:

    def __init__(self, name, species, shift):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        
        
dino = Alligator("Dino", "American Alligator", "afternoon")  

print(dino.name)    
#prints Dino