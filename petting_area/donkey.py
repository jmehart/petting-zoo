# import the python datetime module to help us create a timestamp
from datetime import date

class Donkey:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        
        
eddie = Donkey("Eddie", "Domestic Donkey")  

print(eddie.name)    
#prints Eddie          