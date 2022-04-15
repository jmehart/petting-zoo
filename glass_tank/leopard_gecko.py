# import the python datetime module to help us create a timestamp
from datetime import date

class LeopardGecko:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        
        
frank = LeopardGecko("Frank", "Common Leopard Gecko")  

print(frank.name)    
#prints Frank  