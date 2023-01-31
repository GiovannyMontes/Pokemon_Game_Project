from poke import Pokemon
from poke import Trainer
from poke import *


squirtle = Pokemon("squirtle", 8, "water")
charmander = Pokemon("charmander", 7, "fire")
bulbasaur = Pokemon("bulbasaur", 9, "grass")
staryu = Pokemon("staryu", 13, "water")
ponyta = Pokemon("ponyta", 11, "fire")
oddish = Pokemon("oddish", 10, "grass")
lapras = Pokemon("lapras", 16, "water")
flareon = Pokemon("flareon", 18, "fire")
bellsprout = Pokemon("bellsprout", 17, "grass")

gio = Trainer("gio")
julie = Trainer("julie")


#prompt user to choose 3 pokemon while giving trainer 2 the more effective pokemon
julie.poke_lst.append(choose_pokemon(gio, squirtle, charmander, bulbasaur))
julie.poke_lst.append(choose_pokemon(gio, staryu, ponyta, oddish))
julie.poke_lst.append(choose_pokemon(gio, lapras, flareon, bellsprout))

#print(gio.poke_lst[gio.cur_act_poke].name)
#print(julie.poke_lst[julie.cur_act_poke].name)

print("You have been challenged by Trainer " + julie.name + ".")
print(julie.name + " will be using " + julie.poke_lst[julie.cur_act_poke].name)

#prompt user option to switch pokemon
print("Fight with " + gio.poke_lst[gio.cur_act_poke].name + "?")
print("'y' or 'n'")
choice = input()
choice.lower()
if choice == "n":
    gio.switch_poke()

gio.fight(julie)