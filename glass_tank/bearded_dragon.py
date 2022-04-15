# import the python datetime module to help us create a timestamp
from datetime import date

class BeardedDragon:

    def __init__(self, name, species, shift):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        
        
gandalf = BeardedDragon("Gandalf", "White Bearded Dragon", "afternoon")  

print(f'{gandalf.name} the {gandalf.species} is available to pet during the {gandalf.shift} shift.')
# prints Gandalf the White Bearded Dragon is available to pet during the afternoon shift.       