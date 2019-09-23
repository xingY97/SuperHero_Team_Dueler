import random
class Ability:
    def __init__ (self,name,attack_strength):
        """Create Instance Variables:
            name:String
            max_damage: Integer"""
            #TODO: INstantiate the variables listed in the docstring with then
            # values passed in
        self.name = name
        self.attack_strength = attack_strength
        #Integer = Ability.attack_strength()
    def attack (self):
        """Return a value between 0 and the value set by self.max_damage."""
        #TODO: Use random randint(a,b) to select a random attack value.
        #Return an attack value between 0 and the full attack.
        #Hint: The constructor initializes the maximum attack value.
        attack_strength = random.randint(0,self.attack_strength)
        return attack_strength
"""class Armor_Class:
    def __init__(self,name,Max_block):
        self.name = name
        self.Max_block = Max_block
    def block(self):
        return Max_block
class Hero_class:
    def __init__ (self,name,starting_health):
        self.name = name
        self.starting_health = 100 #default 100
    def add_ability (self,ability):
        self.ability = ability
    def attack (self):
    def defend(self,incoming_damage):
        self.incoming_damage = incoming_damage
    def take_damage (self,damage):
        self.damage = damage
    def is_alive (self):
    def fight (self,opponent):
        self.opponent = opponent"""


if __name__ == "__main__":
    ability = Ability("Debuggin Ability", 20)
    print(ability.name)
    print(ability.attack())




        
