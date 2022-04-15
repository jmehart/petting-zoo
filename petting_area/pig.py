# import the python datetime module to help us create a timestamp
from datetime import date

class Pig:

    def __init__(self, name, species, shift):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        
        
wilbur = Pig("Wilbur", "Pot-bellied Pig", "morning") 

print(wilbur.name)    
#prints Wilbur  