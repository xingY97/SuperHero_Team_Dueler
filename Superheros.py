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
    
    def attack (self):
        """Return a value between 0 and the value set by self.max_damage."""
        #TODO: Use random randint(a,b) to select a random attack value.
        #Return an attack value between 0 and the full attack.
        #Hint: The constructor initializes the maximum attack value.
        attack_strength = random.randint(0,self.attack_strength)
        return attack_strength

class Armor_Class:
    def __init__(self,name,Max_block):
        """Instantiate instance properties.
            name: String
            max_block: Integer"""
            #TODO Create instance variables for the values passed in
        self.name = name
        self.Max_block = Max_block

    def block(self):
        Max_block = random.randint(0,self.Max_block)
        return Max_block

class Hero:
    def __init__ (self,name,current_health,starting_health=100):
        self.ability = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = current_health
    def add_ability (self,ability):
        #adding abilities to ability list
        self.ability = ability
    def armor(self,armor):
        #adding armors to armor list
        self.armor = armor
    def attack(self):
        self.attack = attack
    def defend (self,incoming_damage=0):
        self.incoming_damage = incoming_damage
    def take_damage (self,damage):
        self.damage =damage
    def is_alive(self):
        self.is_alive = is_alive
    def fight (self,opponent):
        self.opponent = opponent
        


if __name__ == "__main__":
    my_hero = Hero("Grace Hopper",200)
    print(my_hero.name)
    print(my_hero.current_health)
    """ability = Ability("Debuggin Ability", 20)
    print(ability.name)
    print(ability.attack())"""




        
