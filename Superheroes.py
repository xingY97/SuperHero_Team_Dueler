import random
import copy #inspired by Joey Gaitan, Jerome Schimidt

class Ability:
    def __init__ (self,name,attack_strength):
        """Create Instance Variables"""
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
    def add_armor(self,armor):
        """add armor to self.armors
        #TODO:This method wiill armor object into armor objejcts list."""
        self.armors.append(armor_object)

    def add_weapon(self,weapon):
        """Add weapon to self.abilities"""
        #TODO:This method will append the weapon object passed in as as argument to self.abilities
        self.abilities.append(weapon)
    
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
        self.heroes = []
    
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
class Arena:
    def __init__(self):
        """instantiate properties"""
        #TODO: create instance variabls name team_one and two
        self.team_one = None
        self.team_two = None

        self.team_one = Team("team1")
        self.team_two = Team("team2")
    def create_ability(self):
        """prompt for ability information, return ability with values form user input"""
        #TODO: This method will allow a user to create an ability.
        ability_name = input("Enter an ability")
        return ability_name
    def create_weapon(self):
        """prompt user fo weapon information return weapon with values from user input"""
        #TODO:THis method will allow a user to create a weapon.
        weapon_name = input ("Enter a weapon")
        return weapon_name
    def create_armor(self):
        """prompt user for armor information"""
        #TODO:This method will allow a user to create a piece of armor.
        armor_name = input ("Enter a armor")
        return armor_name
    def create_hero(self):
        """Prompt the user for Hero information
        #TODO:This method should allow a user to create a hero.
        #USer should be able to speccify if they want armors, weapons,abilities"""
        hero_name = input ("Enter a hero name")
        new_hero = Hero(hero_name)

        add_abilities = input("Do you want to add an ability? Y or N: ")
        if add_abilities.lower() == "Y":
            Ability = self.create_ability()
            new_hero.add_abilities(Ability)
 
        
        add_armors = input("Do you want to add an armor object? Y or N: ")
        if add_armors.lower() == "Y":
            Armor = self.create_armor()
            new_hero.add_armors(Armor)

        
        add_weapon = input ("Do you want to add a weapon? Y or N: ")
        if add_weapon.lower() == "Y":
            Weapon = self.create_weapon()
            new_hero.add_weapon(Weapon)


        return new_hero

    def build_team_one(self):
        """promp the user to build team_one"""
        #TODO:THis method should allow a user to create team one.
        #Prompt the user for the number of heroes on team one
        #call self.create_hero() for every hero that the user wants to add
        #add the create hero to team one 
        team_one_amount = int(input ("how many heroes on team one ?"))

        for i in range(team_one_amount):
            team1_hero = self.create_hero()
            self.team_one.add_hero(team1_hero)
            
    def build_team_two(self):
        """promp the user to build team_two"""
        #TODO:THis method should allow a user to create team two.
        #Prompt the user for the number of heroes on team two
        #call self.create_hero() for every hero that the user wants to add
        #add the create hero to team two
        team_two_amount = int(input("how many heroes in team two ?"))

        for i in range(team_two_amount):
            team2_hero = self.create_hero()
            self.team_two.add_hero(team2_hero)

    def team_battle(self):
        """Battle team_one and team_two together."""
        #TODO:This method should battle the teams together.
        #Call the attack method that exists in your team objects
        self.team_one.attack(self.team_two)
        
    def show_stats(self):
        """Prints team statistics to terminal."""
        #TODO: This method should print out battle statistics
        #including each team's average kill/death ratio.
        #Declare winning team, show surviving heroes.
        team_one_alive_heroes = []
        team_two_alive_heroes = []

        print("stats for team one")
        team_one_heroes = 0
        for hero in self.team_one_heroes:
            if hero.is_alive():
                live_one_heroes += 1
                team_one_alive_heroes.append(hero.name)
                print(hero.name + "Survived")
        print("stats for team two")
        team_two_heroes = 0
        for hero in self.team_two_heroes:
            if hero.is_alive():
                live_two_heroes += 1
                team_two_alive_heroes.append(hero.name)
                print(hero.name + "Survived")

        if len(team_one_alive_heroes) > len(team_two_alive_heroes):
            print("Team one won!")
        if len(team_one_alive_heroes) < len(team_two_alive_heroes):
            print("Team two won!")
            
            
            


if __name__ == "__main__":
   # hero = Hero("Grace Hopper", 200)
    #shield = Armor("shield",50)
    #hero.add_armor(shield)
    #hero.take_damage(150)
   # print(hero.is_alive())
   # hero.take_damage(15000)
   # print(hero.is_alive())
    #hero1 = Hero("Wonder Woman",200)
    #hero2 = Hero("Dumbledore")
    #ability1 = Ability("Super Speed", 300)
    #ability2 = Ability("Super Eyes", 130)
    #ability3 = Ability("Wizard Wand", 80)
    #ability4 = Ability("Wizard Beard", 20)
    #hero1.add_ability(ability1)
    #hero1.add_ability(ability2)
    #hero2.add_ability(ability3)
    #hero2.add_ability(ability4)
    #hero1.fight(hero2)
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()







        
