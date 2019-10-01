import random


class Ability:
    def __init__ (self, name, attack_strength):
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
    def __init__(self, name, Max_block):
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
        self.current_health = self.starting_health
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
            self.current_health -= damage - self.defend()
            

    def is_alive(self):
        #TODO: check whether the hero is alive and return true of false
        if self.current_health > 0:
            return True
        else:
            return False

    def fight (self,opponent):
        #TODO: Refactor this method to update the 
        #Number of kills the hero has when opponent dies
        #Also update the number of deaths for whoever dies in the fight
        
        while self.is_alive() and opponent.is_alive():
            self_damage = self.attack()
            opponent.take_damage(self_damage)
            opponent_damage = opponent.attack()
            self.take_damage(opponent_damage)

        if opponent.is_alive():
            opponent.add_kills(1)
            self.add_death(1)
        else:
            self.add_kills(1)
            opponent.add_death(1)
            
    
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
        return

    def list_for_living_heroes(self):
        living_heroes = []
        for hero in self.heroes:
            if hero.is_alive():
                living_heroes.append(hero)
            return living_heroes

    def attack(self, other_team):
        """Battle each team against each other ."""
        #TODO: Randomly select a living hero from each team and have
        #Them fight until one or both teams have no surviving heroes
        
        while len(self.list_for_living_heroes()) >0 and len(other_team.list_for_living_heroes())>0:
            random_hero_1 = random.choice(self.list_for_living_heroes())
            random_hero_2 = random.choice(other_team.list_for_living_heroes())
        
            #self_current_deaths = random_hero_1.deaths
            #other_team_current_deaths = random_hero_2.deaths

            random_hero_1.fight(random_hero_2)
    
                    
        # hero_alive = []
        # opponent_alive = []

        # for hero in self.heroes:
        #     if hero.is_alive():
        #         hero_alive.append(hero)
        # return hero_alive

        # for hero in other_team.heroes:
        #     if opponent_hero.is_alive():
        #         opponent_alive.append(opponent_hero)
        # return opponent_alive

        # while len(hero_alive) > 0 and len(opponent_alive) > 0:
        #     random_hero_1 = random.choice(hero_alive)
        #     random_hero_2 = random.choice(opponent_alive)

        #     random_hero_1.fight(random_hero_2)

        #     for random_hero_1 in self.heroes:
        #         if random_hero_1.current_health < 0:
        #             hero_alive.remove(self.heroes.index(random_hero_1))

        #     for random_hero_2 in other_team.heroes:
        #         if random_hero_2.current_health < 0:
        #             opponent_alive.remove(self.heroes.index(random_hero_2))
        
        # if len(hero_alive) > 0:
        #     return self.name
        # elif len(opponent_alive) > 0:
        #     return other_team.name
        # elif len(hero_alive) == len(opponent_alive):
        #     return "Draw!"

    def revive_heroes(self, health =100):
        """Reset all heroes health to strating_health"""
        #TODO: This methodd should reset all heroes health to their
        #original starting value
        for hero in self.heroes:
            hero.current_health = hero.starting_health
    def stats(self):
        for hero in self.heroes:
            print(f"Kills: {hero.kills} and Death: {hero.deaths}")
    
        
class Arena:
    def __init__(self):
        """instantiate properties"""
        #TODO: create instance variabls name team_one and two
        self.team_one = Team("team_one")
        self.team_two = Team("team_two")

    def create_ability(self):
        """prompt for ability information, return ability with values form user input"""
        #TODO: This method will allow a user to create an ability.
        ability_name = input("Enter an ability")
        ability_damage = int(input ("Enter ability damage "))
        ability = Ability(ability_name, ability_damage)
        return ability

    def create_weapon(self):
        """prompt user fo weapon information return weapon with values from user input"""
        #TODO:THis method will allow a user to create a weapon.
        weapon_name = input ("Enter a weapon")
        weapon_damage = int(input("Enter weapon's damage "))
        weapon = Weapon(weapon_name, weapon_damage)
        return weapon

    def create_armor(self):
        """prompt user for armor information"""
        #TODO:This method will allow a user to create a piece of armor.
        armor_name = input ("Enter a armor")
        armor_block = int(input("Enter armor block "))
        armor = Armor(armor_name, armor_block)
        return armor

    def create_hero(self):
        """Prompt the user for Hero information
        #TODO:This method should allow a user to create a hero.
        #USer should be able to speccify if they want armors, weapons,abilities"""
        
        hero_name = input ("Enter a hero name")
        hero_health = int(input("Enter hero health"))
        new_hero = Hero(hero_name, hero_health)

        add_abilities = input("Do you want to add an ability? Y or N: ")
        if add_abilities.lower() == "y":
            ability = self.create_ability()
            new_hero.add_ability(ability)
 
        add_armors = input("Do you want to add an armor object? Y or N: ")
        if add_armors.lower() == "y":
            armor = self.create_armor()
            new_hero.add_armor(armor)
   
        add_weapon = input ("Do you want to add a weapon? Y or N: ")
        if add_weapon.lower() == "y":
            Weapon = self.create_weapon()
            new_hero.add_weapon(Weapon)
            print("Weapon added")

        return new_hero

    def build_team_one(self):
        """promp the user to build team_one"""
        name = input("Enter team name: ")
        self.team_one = Team(name)
        hero_alive = int(input("How many heroes in team one? : "))
        for x in range(hero_alive):
            hero = self.create_hero()
            self.team_one.heroes.append(hero)
            
    def build_team_two(self):
        """promp the user to build team_two"""
        name = input("Enter Team Name: ")
        self.team_two = Team(name)
        hero_alive = int(input("How many heroes in team two ?: "))
        for x in range(hero_alive):
            hero = self.create_hero()
            self.team_two.heroes.append(hero)

        
    def team_battle(self):
        self.team_one.attack(self.team_two)
        
    def show_stats(self):
        
        if len(self.team_one.list_for_living_heroes())>0:
            print("team one won")
        else:
            print("team two won")

        self.team_one.stats()
        self.team_two.stats()




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
    # game_is_running = True

    #Instantiate Game Arena
    # arena = Arena()
    #build Teams
    # arena.build_team_one()
    # arena.build_team_two()
    # while game_is_running:
        
    #     arena.team_battle()
    #     arena.show_stats()
    #     play_again = input("play Again? Y or N: ")

        #check for player Input
        # if play_again.lower() == "n":
        #     game_is_running = False
        # else:
        #     #revive heroes to play again
        #     arena.team_one.revive_heroes()
        #     arena.team.two.revive_heroes()



