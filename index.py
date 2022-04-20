from models import Alligator, Goldfish, Koi, Mallard, Turtle, Donkey, Goat, Llama, Pig, Rabbit, BallPython, BeardedDragon, Copperhead, LeopardGecko, RatSnake, PettingZoo, SnakePit, Wetlands



critter_cove = Wetlands("Critter Cove", "feathered friends and fantastic fish")

dino = Alligator("Dino", "American Alligator", "afternoon", "duck pate", 606060)

print(dino.feed()) 
#prints Dino was fed duck pate on 04/15/2022

parmesan = Goldfish("Parmesan", "Meteor Goldfish", "fish food", 123789)  

# This should not change the state of the object
parmesan.chip_number = 555783

# But printing it should work
print(parmesan.chip_number)
#prints 123789

troy = Koi("Troy", "Kohaku Koi", "fish food", 876523)  

print(troy.name)    

daisy = Mallard("Daisy", "Mallard Wild Duck", "morning", "escargot", 982556) 

print(daisy.name)

reggie = Turtle("Reggie", "Ridgeback Turtle", "squash", 123987)  

print(reggie.name)

critter_cove.add_animal(dino)
critter_cove.add_animal(parmesan)
critter_cove.add_animal(troy)
critter_cove.add_animal(daisy)
critter_cove.add_animal(reggie)

print(critter_cove.last_critter_added)



varmint_village = PettingZoo("Varmint Village", "cute and fuzzy critters to cuddle")  

eddie = Donkey("Eddie", "Domestic Donkey", "morning", "waffles", 234567) 

print(eddie.name)

billy = Goat("Billy", "Mountain Goat", "midday", "grass", 876543)  

print(billy.name) 

tina = Llama("Tina", "Lama Glama", "afternoon", "casserole", 345677)  

print(tina.name)  

wilbur = Pig("Wilbur", "Pot-bellied Pig", "morning", "corn", 543457) 

print(wilbur.name) 

lola = Rabbit("Lola", "American Fuzzy Lop Rabbit", "midday", "carrots", 257955)  

print(lola.name)

varmint_village.add_animal(eddie)
varmint_village.add_animal(billy)
varmint_village.add_animal(tina)
varmint_village.add_animal(wilbur)
varmint_village.add_animal(lola)

print(varmint_village.last_critter_added)



slither_inn = SnakePit("Slither Inn", "stupendous snakes of all sizes")

stuart = RatSnake("Stuart", "Black Rat Snake", "mice", 123456)  

print(stuart.name)    

frank = LeopardGecko("Frank", "Common Leopard Gecko", "afternoon", "crickets", 777744)  

print(frank.name)    

draco = Copperhead("Draco", "Eastern Copperhead Snake", "mice", 333775)  

print(draco.name)  

gandalf = BeardedDragon("Gandalf", "White Bearded Dragon", "afternoon", "crickets", 888532)  

print(f'{gandalf.name} the {gandalf.species} is available to pet during the {gandalf.shift} shift.')
# prints Gandalf the White Bearded Dragon is available to pet during the afternoon shift.   

snape = BallPython("Snape", "Royal Ball Python Snake", "mice", 157777)  

print(snape) 
# prints Snape is a Royal Ball Python Snake because of the __str__ magic method on class

slither_inn.add_animal(stuart)
slither_inn.add_animal(frank)
slither_inn.add_animal(draco)
slither_inn.add_animal(gandalf)
slither_inn.add_animal(snape)

print(slither_inn.last_critter_added)



print(f"{varmint_village.attraction_name} is where you'll find {varmint_village.description}, like")
for animal in varmint_village.animals:
    print(f'   * {animal.name} the {animal.species}')

print(f"{slither_inn.attraction_name} is where you'll find {slither_inn.description}, like")
for animal in slither_inn.animals:
    print(f'   * {animal.name} the {animal.species}')

print(f"{critter_cove.attraction_name} is where you'll find {critter_cove.description}, like")
for animal in critter_cove.animals:
    print(f'   * {animal.name} the {animal.species}')