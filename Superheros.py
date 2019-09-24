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

class Armor:
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
    def __init__ (self,name,starting_health=100):
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def add_ability (self,ability):
        #adding abilities to ability list
        self.abilities.append(ability)

    def add_armor(self,armor):
        #adding armors to armor list
        self.armors.append(armor)

    def attack(self):
        #This method returns the total ability attack as an integer
        total_attack = 0
        for attack in self.abilities:
            total_attack += attack.attack()
        return total_attack

    def defend (self,damage_amt):
        #runs 'block' method on each armor.
        #Returns sum of all blocks
        #TODO:This method should run the block method on each armor in self.armors
        total_defend = 0
        for defend in self.armors:
            total_defend += defend.block()
        return total_defend

    def take_damage (self,damage):
        if (damage > self.defend(damage)):
            self.current_health = self.current_health - (damage-self.defend(damage))
        else:
            self.current_health = self.current_health

    def is_alive(self):
        #TODO: check whether the hero is alive and return true of false
        is_alive = True
        if self.current_health > 0:
            return  True
        else:
            return False

    def fight (self,opponent):
        #TODO:Fight each hero until a victor emerges.
        #print the victor's name to the screen
        while self.is_alive() == True and opponent.is_alive() == True:
            opponent.take_damage(self.attack())
            self.take_damage(opponent.attack())
        if self.is_alive():
            print(self.name + " won!")
        else:
            print(opponent.name  + "won!")
       

        
        
if __name__ == "__main__":
   # hero = Hero("Grace Hopper", 200)
    #shield = Armor("shield",50)
    #hero.add_armor(shield)
    #hero.take_damage(150)
   # print(hero.is_alive())
   # hero.take_damage(15000)
   # print(hero.is_alive())
    hero1 = Hero("Wonder Woman",200)
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)







        
