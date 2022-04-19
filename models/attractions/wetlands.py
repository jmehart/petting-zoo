class Wetlands:

    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

    def add_animal(self, animal):
        self.animals.append(animal)
        
    @property    
    def last_critter_added(self):
        return f'{self.animals[-1].name} the {self.animals[-1].species}'