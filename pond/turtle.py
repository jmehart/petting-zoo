# import the python datetime module to help us create a timestamp
from datetime import date

class Turtle:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        
        
reggie = Turtle("Reggie", "Ridgeback Turtle")  

print(reggie.name)    
#prints Reggie         