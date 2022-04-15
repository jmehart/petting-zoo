# import the python datetime module to help us create a timestamp
from datetime import date

class BeardedDragon:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        
        
gandalf = BeardedDragon("Gandalf", "White Bearded Dragon")  

print(gandalf.name) 
#prints Gandolf         