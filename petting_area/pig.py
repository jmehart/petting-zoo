# import the python datetime module to help us create a timestamp
from datetime import date

class Pig:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        
        
wilbur = Pig("Wilbur", "Pot-bellied Pig")  

print(wilbur.name)    
#prints Wilbur  