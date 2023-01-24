"""
Pokemon Game Project using Python with a focus on classes and OOP
"""

class Pokemon:
  def __init__(self, name, level, race ):
    self.name = name
    self.lvl = level
    #determine pokemon type
    self.race = race        
    self.max_hp = level*5
    self.cur_hp = level*5
    #check for alive or fiented
    self.is_feinted = False


  def lose_health(self, dmg_received):
      print(self.name + " lost " + dmg_received + " health")

  def reg_health(self):
      print(self.name + " now has " + self.curr_health + " health")

  def knockout(self):
      print(self.name + " has feinted")

  def revive(self):
      print(self.name + " has been revived")

  def attack(self, opponent):
    if (self.race == "water" and opponent.race == "fire") or (self.race == "fire" and opponent.race == "grass") or (self.race == "grass" and opponent.race == "water"):
      print(self.name + " is super effective!")
      opponent.lose_health(opponent.level*2)
      opponent.cur_health -= opponent.level*2
      #Check if opponent health is less than 0
      if opponent.cur_health <= 0:
        print(opponent.name + " has feinted!")
        opponent.is_feinted = True
        opponent.cur_health = 0
      
    elif (self.race == "water" and opponent.race == "grass") or (self.race == "fire" and opponent.race == "water") or (self.race == "grass" and opponent.race == "fire"):
      print(self.name + " is not effective!")
      opponent.lose_health(opponent.level/2)
      opponent.cur_health -= opponent.level/2
      #Check if opponent health is less than 0
      if opponent.cur_health <= 0:
        print(opponent.name + " has feinted!")
        opponent.is_feinted = True
        opponent.cur_health = 0
    else:
      print(self.name + " has used " + move_name)         # *** Add move_name instance variable *** #
      opponent.lose_health(opponent.level)
      opponent.cur_health -= opponent.level
      #Check if opponent health is less than 0
      if opponent.cur_health <= 0:
        print(opponent.name + " has feinted!")
        opponent.is_feinted = True
        opponent.cur_health = 0