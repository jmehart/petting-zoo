from pond import Alligator, Goldfish, Koi, Mallard, Turtle
from petting_area import Donkey, Goat, Llama, Pig, Rabbit
from glass_tank import BallPython, BeardedDragon, Copperhead, LeopardGecko, RatSnake

# MAIN MODULE


print(Turtle)
print(Mallard)
print(Goldfish)
print(Alligator)
print(Koi)
print(Llama)
print(Goat)
print(Donkey)
print(Rabbit)
print(Pig)
print(Copperhead)
print(BeardedDragon) 
print(BallPython)
print(RatSnake)
print(LeopardGecko)



dino = Alligator("Dino", "American Alligator", "afternoon", "duck pate")

print(dino.feed())  
#prints Dino was fed duck pate on 04/15/2022

parmesan = Goldfish("Parmesan", "Meteor Goldfish", "fish food")  

print(parmesan.name)    

troy = Koi("Troy", "Kohaku Koi", "fish food")  

print(troy.name)    

daisy = Mallard("Daisy", "Mallard Wild Duck", "morning", "escargot") 

print(daisy.name)

reggie = Turtle("Reggie", "Ridgeback Turtle", "squash")  

print(reggie.name)

eddie = Donkey("Eddie", "Domestic Donkey", "morning", "waffles") 

print(eddie.name)  

billy = Goat("Billy", "Mountain Goat", "midday", "grass")  

print(billy.name) 

tina = Llama("Tina", "Lama Glama", "afternoon", "casserole")  

print(tina.name)  

wilbur = Pig("Wilbur", "Pot-bellied Pig", "morning", "corn") 

print(wilbur.name) 

lola = Rabbit("Lola", "American Fuzzy Lop Rabbit", "midday", "carrots")  

print(lola.name) 

stuart = RatSnake("Stuart", "Black Rat Snake", "mice")  

print(stuart.name)    

frank = LeopardGecko("Frank", "Common Leopard Gecko", "afternoon", "crickets")  

print(frank.name)    

draco = Copperhead("Draco", "Eastern Copperhead Snake", "mice")  

print(draco.name)  

gandalf = BeardedDragon("Gandalf", "White Bearded Dragon", "afternoon", "crickets")  

print(f'{gandalf.name} the {gandalf.species} is available to pet during the {gandalf.shift} shift.')
# prints Gandalf the White Bearded Dragon is available to pet during the afternoon shift.   

snape = BallPython("Snape", "Royal Ball Python Snake", "mice")  

print(snape) 
# prints Snape is a Royal Ball Python Snake because of the __str__ magic method on class
