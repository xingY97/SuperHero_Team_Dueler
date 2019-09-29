import random
import copy #inspired by Joey Gaitan, Jerome Schimidt

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
    
class Weapon(Ability):
    def attack(self):
        """This method returns a random value between one half to the full attack power ofthe weapon.
        """
        return random.randint(self.attack_strength//2,self.attack_strength)

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
        self.deaths = 0
        self.kills = 0
    
    def add_kills(self, num_kills):
        """update kills with num_kills"""
        #TODO: This method should add the number of kills to self.kills
        self.kills += num_kills
    def add_death(self,num_deaths):
        """update deaths with num_deaths"""
        #TODO: This method should add the numbe of deaths to self.deaths
        self.deaths += num_deaths

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

    def defend (self,damage_amt=0):
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
        #TODO: Refactor this method to update the 
        #Number of kills the hero has when opponent dies
        #Also update the number of deaths for whoever dies in the fight
        
        while self.is_alive() == True and opponent.is_alive() == True:
            opponent.take_damage(self.attack())
            self.take_damage(opponent.attack())
        if self.is_alive():
            print(self.name + " won!")
            self.add_kills(1)
            opponent.add_death(1)
        else:
            print(opponent.name  + "won!")
            opponent.add_kills(1)
            self.add_death(1)

        
class Team:
    def __init__(self,name):
        #TODO: Implement this constructor by assigning the name and heroes.
        
        self.name = name
        self.heroes = list()
    
    def remove_hero(self,name):
        """"remove hero from heroes list. if hero isn't found return 0"""
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
        return 0
    def view_all_heroes(self):
        """print out all heroes to the console."""
        #TODO: loop over the list of heroes and print their name to the terminal.
        for heroes in self.heroes:
            print(heroes.name)
    def add_hero(self,hero):
        """Add Hero object to self.heroes."""
        #TODO: Add the hero object that is passedi n to the list of heroes in
        self.heroes.append(hero)
    def attack(self, other_team):

        """Battle each team against each other ."""
        #TODO: Randomly select a living hero from each team and have
        #Them fight until one or both teams have no surviving heroes
        copy_my_team = copy.copy(self.heroes)
        copy_opponents_team = copy.copy(other_team.heroes)
        while len(copy_my_team) > 0 and len(copy_opponents_team) > 0:
            my_team_hero = random.choice(copy_my_team)
            other_team_hero = random.choice(copy_opponents_team)

            my_team_current_deaths = my_team_hero.deaths
            other_team_hero_deaths = other_team_hero.deaths

            my_team_hero.fight(other_team_hero)

            if(my_team_hero.deaths > my_team_current_deaths):
                my_team_hero.remove(my_team_hero)
            else:
                copy_opponents_team.remove(other_team_hero)
        if len(copy_my_team) == 0 or len(copy_opponents_team) != 0:
            print(other_team.name + "won" )
        if len(copy_my_team) != 0 or len(copy_opponents_team) == 0:
            print(self.name + "won")

        
        
    def revive_heroes(self, health =100):
        """Reset all heroes health to strating_health"""
        #TODO: This methodd should reset all heroes health to their
        #original starting value
        for hero in self.heroes:
            hero.current_health = hero.starting_health
    def stats(self):
        """Print team statistics"""
        #TODO: THis method should print the ratio of kills/deaths for each
        #Member of the team to the screen
        #This data must be output to the console
        print("hero{}. kills{}, death{},". format(hero.name,hero.kills, hero.death))


            


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







        
