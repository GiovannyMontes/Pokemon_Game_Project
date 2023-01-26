from poke import Pokemon
from poke import Trainer


squirtle = Pokemon("squirtle", 8, "water")
charmander = Pokemon("charmander", 7, "fire")
bulbasaur = Pokemon("bulbasaur", 6, "grass")

gio = Trainer("gio")
julie = Trainer("julie")


####################### Make function ##########################
print("Hello " + gio.name + " please choose your starter pokemon: ")
starter_choice = input()

if starter_choice == "squirtle":
    gio.poke_lst.append(squirtle)
elif starter_choice == "charmander":
    gio.poke_lst.append(charmander)
elif starter_choice == "bulbasaur":
    gio.poke_lst.append(bulbasaur)
else:
    print("Invalid starter choice")
################################################################


