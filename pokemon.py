from random import randint
class Pokemon:
    def __init__(self, name, level, type):
        self.name = name
        self.level = level
        self.type = type.lower()
        self.max_hp = (level + 3) * 3
        self.current_hp = self.max_hp
        self.unconcious = False
        self.xp = 0
        self.xp_cap = level * 2
        self.speed_stat = randint(8, 12) + self.level
        self.attack_stat = randint(5, 7) + self.level
        self.defense_stat = randint(1, 3) + self.level

    def __repr__(self):
      return self.name
#         return """--Pokedex Information on {pokemon}--
#  -Level: {lvl} \t-Type: {type} \t-Health: {currhp}/{maxhp} \t-XP: {xp}/{reqxp}
#  -Speed: {spd} \t-Attack: {atk} \t-Defense: {defense}""".format(
#             pokemon=self.name, lvl=self.level, type=self.type, currhp=self.current_hp, maxhp=self.max_hp,
#             xp=self.xp, reqxp=self.xp_cap, spd=self.speed_stat, atk=self.attack_stat, defense=self.defense_stat)

    def pokedex_information(self):
        print("""\t--Pokedex Information on {pokemon}--
    -Level: {lvl} \t-Type: {type} \t-Health: {currhp}/{maxhp} \t-XP: {xp}/{reqxp}
    -Speed: {spd} \t-Attack: {atk} \t-Defense: {defense}""".format(
pokemon=self.name, lvl=self.level, type=self.type, currhp=self.current_hp, maxhp=self.max_hp,
    xp=self.xp, reqxp=self.xp_cap, spd=self.speed_stat, atk=self.attack_stat, defense=self.defense_stat))

    def lose_health(self, damage):
        self.current_hp -= damage
        if self.current_hp <= 0:
            self.current_hp = 0
            self.unconcious = True
            print("{name} has taken {dmg} damage. {name} has been knocked unconcious!".format(name=self.name, dmg = damage))
        else:
            print("{name} has taken {dmg} damage. They now have {hp}/{max_hp} hp".format(name=self.name, dmg=damage,
             hp=self.current_hp, max_hp=self.max_hp))
        return self.unconcious
    
    def regain_health(self, heal):
        if self.unconcious is False and self.current_hp < self.max_hp:
            self.current_hp += heal
            self.current_hp = self.set_health()
            print("{name} was healed by {health} hp. They now have {hp}/{max_hp} hp".format(name=self.name, 
            health=heal, hp=self.current_hp, max_hp=self.max_hp))
            return True
        elif self.current_hp == self.max_hp:
            print("Cannot heal {pokemon} as they already have full health".format(pokemon=self.name))
        else:
            print("Cannot heal {name}. They are unconcious".format(name=self.name))
        return False

    def revive(self, health):
        if self.unconcious is False:
            print("Cannot revive {pokemon} because they are already concious".format(pokemon=self.name))
        else:
            self.current_hp = health
            self.unconcious = False
            print("{name} was revived. They now have {hp} hp".format(name=self.name, hp=self.current_hp))

    def set_health(self):
        if self.current_hp >= self.max_hp:
            return self.max_hp
        elif self.current_hp <= 0:
            return 0
        else:
            return self.current_hp

    def can_attack(self, other_pokemon):
        if self.unconcious is True:
            print("{name} cannot attack because they are unconcious".format(name=self.name))
            return False
        elif other_pokemon.unconcious is True:
            print("Cannot attack {name} because they are unconcious".format(name=other_pokemon.name))
            return False
        else:
            return True

    def attack(self, other_pokemon):
        if self.can_attack(other_pokemon) is False:
            return
            
        if self.have_advantage(other_pokemon.type) == "yes": 
            if other_pokemon.lose_health((self.attack_stat - self.defense_stat) * 2) is True:
                self.gain_xp(other_pokemon.level)
            print("{name}'s attack was super effective".format(name=self.name))            
        elif self.have_advantage(other_pokemon.type) == "no":
            if other_pokemon.lose_health((self.attack_stat - other_pokemon.defense_stat) * 0.5) is True:
                self.gain_xp(other_pokemon.level)
            print("{name}'s attack wasn't very effective".format(name=self.name))
        else:
            if other_pokemon.lose_health(self.attack_stat - other_pokemon.defense_stat) is True:
                self.gain_xp(other_pokemon.level)
        return other_pokemon.unconcious

    def have_advantage(self, other_pokemon_type):
        #Attacking pokemon has advantage based on type
        if self.type == "fire" and other_pokemon_type == "grass":
            return "yes"
        elif self.type == "electric" and other_pokemon_type == "water":
            return "yes"
        elif self.type == "water" and other_pokemon_type == "fire":
            return "yes"
        #Attacking pokemon has disadvantage
        elif self.type == "water" and other_pokemon_type == "electric":
            return "no"
        elif self.type == "grass" and other_pokemon_type == "fire":
            return "no"
        elif self.type == "fire" and other_pokemon_type == "water":
            return "no"
    
    def gain_xp(self, other_pokemon_level):
        self.xp += other_pokemon_level
        print("{pokemon} gained {xp} xp".format(pokemon=self.name, xp=other_pokemon_level))
        self.level_up()

    def level_up(self):
        if self.xp >= self.xp_cap:
            self.level += 1
            self.max_hp += 1
            self.xp -= self.xp_cap
            self.xp_cap = self.level * 2
            print("* {pokemon} leveled up! * They are now level {lvl}.".format(pokemon=self.name, lvl=self.level))           
            self.evolve()

    def evolve(self):
        evolution_names = {"Pichu": ["Pikachu", "Raichu"], "Charmander": ["Charmeleon", "Charizard"], 
"Squirtle": ["Wartortle", "Blastoise"], "Bulbasaur": ["Ivysaur", "Venusaur"], "Staryu": ["Starmie"]}
            
        for first_evo, next_evos in evolution_names.items():
            if self.name == next_evos[len(next_evos) -1]:
                return
            elif self.level >= 5 and self.name == first_evo:
                print("...{pokemon} is evolving...".format(pokemon=self.name))
                self.level = 2
                self.name = next_evos[0]
                self.max_hp = (self.level + 4) * 4
                print("They have evolved into a level {lvl} {pokemon}!".format(lvl=self.level, pokemon=self.name))
            elif self.level >= 5 and self.name == next_evos[0]:
                print("...{pokemon} is evolving...".format(pokemon=self.name))
                self.level = 2
                self.name = next_evos[1]
                self.max_hp = (self.level + 4) * 5 
                print("They have evolved into a level {lvl} {pokemon}!".format(lvl=self.level, pokemon=self.name))
        self.current_hp = self.max_hp
        self.unconcious = False
        self.xp = 0
        self.xp_cap = self.level * 2
        self.speed_stat += 3
        self.attack_stat += 1
        self.defense_stat += 1

    def first_move(self, other_pokemon, trainer_1, trainer_2):
        if self.speed_stat > other_pokemon.speed_stat:
            print("{player_1} has the first move!".format(player_1=trainer_1))
        else:
            print("{player_2} has the first move!".format(player_2=trainer_2))

    def pokemon_selection(self, starting_pokemon, trainer_name):
        pokemon_squad = []
        display_pokemon = []
        for key in starting_pokemon:
            display_pokemon.append(key)
        print("\n- {}, please choose 3 pokemon to form your squad".format(trainer_name))
        while len(pokemon_squad) < 3:
            selection = input("Please choose a pokemon: " + ", ".join(display_pokemon) + "   ").lower()
            if selection in display_pokemon:
                index = display_pokemon.index(selection)
                pokemon_squad.append(starting_pokemon[selection])
                print("{} joined your squad".format(display_pokemon[index]))
                display_pokemon.pop(index)
            else:
                print("Sorry, {user_input} is not a vaild pokemon selection".format(user_input=selection))
        print("-> {name} your pokemon squad is: {squad}".format(name=trainer_name, squad=pokemon_squad))
        return pokemon_squad

    def starting_pokemon_selection(self, trainer_name, squad):
        display_pokemon = []
        for pokemon in squad:
            pokemon_name = pokemon.name.lower()
            display_pokemon.append(pokemon_name)
        starter = ""
        while starter == "":
            starter = input("\n- {name}, please choose your pokemon to start the battle: ".format(
                name=trainer_name, squad=display_pokemon) + ", ".join(display_pokemon) + "   ").lower()
            if starter in display_pokemon:
                index = display_pokemon.index(starter)
                print("{} selected".format(display_pokemon[index]))
            else:
                print("Sorry, {user_input} is not a vaild pokemon selection".format(user_input=starter))
                starter = ""
        return index


class Pikachu(Pokemon):
    def __repr__(self):
        return super().__repr__() + " -Strong against Water type Pokemon \n -Weak against Ground type Pokemon"
         
    def quick_attack(self, other_pokemon):
        if self.can_attack(other_pokemon) is False:
            return

        print("{pokemon} used Quick Attack".format(pokemon=self.name))
        if other_pokemon.lose_health(self.attack_stat - other_pokemon.defense_stat) is True:
            self.gain_xp(other_pokemon.level)


class Trainer():
    def __init__(self, name, pokemon, current_pokemon):
        self.name = name
        self. pokemon = pokemon
        self.potions = 3
        self.current_pokemon = current_pokemon
        
    def use_potion(self):
        if self.potions <= 0:
            print("{name} has no potions to use".format(name=self.name))
        elif self.pokemon[self.current_pokemon].regain_health(10) is True:
            self.potions -= 1
            #self.pokemon[self.current_pokemon].regain_health(10)
            print("{trainer} now has {potions}/3 potions remaining".format(trainer=self.name, 
            potions=self.potions))


    def attack_trainer(self, other_trainer):
        self.pokemon[self.current_pokemon].attack(other_trainer.pokemon[other_trainer.current_pokemon])
        #self.current_pokemon.attack(other_trainer.pokemon[other_trainer.current_pokemon])
        self.did_win(other_trainer)

    def switch_pokemon(self, current_index):
        #issue is str of pokemon vs pokemon obj. should use dict? or list of all pokemon
        available_pokemon = []
        for pokemon in self.pokemon:
            available_pokemon.append(pokemon.name.lower())
        while self.current_pokemon == current_index:
            pokemon_selection = input("{name}, please choose a pokemon to switch to: ".format(name=self.name) + 
            ", ".join(available_pokemon) + "   ").lower()
            if pokemon_selection in available_pokemon:
                index = available_pokemon.index(pokemon_selection)
                if index == self.current_pokemon:
                    print("{} is already your current pokemom".format(self.pokemon[self.current_pokemon]))
                elif self.pokemon[index].unconcious is False:
                    print("{trainer}: {pokemon} return. Go {new_pokemon}".format(trainer=self.name, 
                    pokemon=self.pokemon[self.current_pokemon], new_pokemon=self.pokemon[index]))
                    self.current_pokemon = index
                    #self.pokemon[self.current_pokemon]
                else:
                    print("{trainer} cannot send out {new_pokemon} because they are unconcious".format(
                trainer=self.name, new_pokemon=self.pokemon[index].name))
            else:
                print("{} is not a valid pokemon".format(pokemon_selection))


    def did_win(self, other_trainer):
        unconcious_count = 0
        for monster in other_trainer.pokemon:
            if monster.unconcious is True:
                unconcious_count += 1
        if unconcious_count == len(other_trainer.pokemon):
            print("{opp_trainer} has no more Pokemon to send out...".format(opp_trainer=other_trainer.name))
            print("** {name} wins the pokemon battle! **".format(name=self.name))
            return True
        else:
            return False

    def player_turn(self, other_trainer):
        actions = ["attack", "potion", "switch", "switch pokemon", "pokedex"]
        curr_pokemon = self.pokemon[self.current_pokemon]

        print("\n- {}'s turn".format(self.name))
        player_input = input("* What will {pokemon} do? *   {currhp}/{maxhp} hp".format(pokemon=curr_pokemon, 
        currhp=curr_pokemon.current_hp, maxhp=curr_pokemon.max_hp)
        + "\n- Attack \t- Potion \t- Switch Pokemon \t- Pokedex   ").lower()
        
        if player_input in actions:
            #print("valid action")
            if player_input == actions[1]:
                #player_1.pokemon[player_1.current_pokemon].lose_health(6)
                self.use_potion()
            elif player_input == actions[2] or player_input == actions[3]:
                self.switch_pokemon(self.current_pokemon)
            elif player_input == actions[0]:
                #print("Attacking...")
                self.attack_trainer(other_trainer)
            elif player_input == actions[4]:
                #print("Using pokedex...")
                curr_pokemon.pokedex_information()
        else:
            print("Sorry. {} is not a valid action".format(player_input))

starting_level = 1
pika = Pokemon("Pichu", starting_level, "Electric")
squirtle = Pokemon("Squirtle", starting_level, "Water")
bulbasaur = Pokemon("Bulbasaur", starting_level, "Grass")
charmander = Pokemon("Charmander", starting_level, "fire")
starmie = Pokemon("Starmie", starting_level, "water")
starting_pokemon = {"pika": pika, "squirtle": squirtle, "bulbasaur": bulbasaur, "charmander": charmander, 
"starmie": starmie}
"""
opponent_level = 3
pikachu = Pikachu("Pikachu", starting_level, "Electric")
starmie = Pokemon("Starmie", opponent_level, "water")
starmie2 = Pokemon("Starmie", opponent_level, "water")
starmie3 = Pokemon("Starmie", opponent_level, "water")
starmie4 = Pokemon("Starmie", opponent_level, "water")
starmie5 = Pokemon("Starmie", opponent_level, "water")
starmie6 = Pokemon("Starmie", opponent_level, "water")
starmie7 = Pokemon("Starmie", opponent_level, "water")
starmie8 = Pokemon("Starmie", opponent_level, "water")
starmie9 = Pokemon("Starmie", opponent_level, "water")
starmie10 = Pokemon("Starmie", opponent_level, "water")

staryu = Pokemon("Staryu", 2, "water")

ash = Trainer("Ash", [pika, bulbasaur], 3, 0)
misty = Trainer("Misty", [starmie, squirtle, starmie2, starmie3, starmie4, starmie5, starmie6, starmie7, starmie8,
starmie9, starmie10], 3, 0)

test_trainer_1 = ash
test_trainer_2 = misty
test_pokemon_1= squirtle
test_pokemon_2 = staryu

# print("{name}: Spd {spd}: \tAtk: {atk}\t\tDef: {defense}".format(name=test_pokemon_1.name, 
# spd=test_pokemon_1.speed_stat, atk=test_pokemon_1.attack_stat, defense=test_pokemon_1.defense_stat))
# print("{name}: Spd {spd}: \tAtk: {atk}\t\tDef: {defense}".format(name=test_pokemon_2.name, 
# spd=test_pokemon_2.speed_stat, atk=test_pokemon_2.attack_stat, defense=test_pokemon_2.defense_stat))
#test_pokemon_1.attack(test_pokemon_2)
print(test_pokemon_1)

test_pokemon_1.level = 5

print(test_pokemon_1)
test_pokemon_1.evolve()
print(test_pokemon_1)
test_pokemon_1.level = 5
print(test_pokemon_1)
test_pokemon_1.evolve()
print(test_pokemon_1) """

#for testing
name_1 = "jim"
name_2 = "bob"
squad_1 = [pika, charmander, bulbasaur]
squad_2 = [squirtle, bulbasaur, starmie]
starter_1 = 1
starter_2 = 2


#name_1 = input("Enter Player 1's name: ")
#name_2 = input("Enter player 2's name: ")
print("Welcome Pokemon Trainers {p1} and {p2}".format(p1=name_1, p2=name_2))
#squad_1 = pika.pokemon_selection(starting_pokemon, name_1)
#squad_2 = pika.pokemon_selection(starting_pokemon, name_2)
#starter_1 = pika.starting_pokemon_selection(name_1, squad_1)
#starter_2 = pika.starting_pokemon_selection(name_2, squad_2)
player_1 = Trainer(name_1, squad_1, starter_1)
player_2 = Trainer(name_2, squad_2, starter_2)
player_1.pokemon[starter_1].first_move(player_2.pokemon[starter_2], player_1.name, player_2.name)

turn_counter = 0

while player_1.did_win(player_2) is False or player_2.did_win(player_1) is False:
    turn_counter += 1
    if turn_counter % 2 == 1:
        player_1.player_turn(player_2)
    else:
        player_2.player_turn(player_1)

#Known Bugs
#Modify battle system so player's turn is a method
#pokemon gets knocked out. Need to prompt player to switch pokemon
#test use_potion(), regain_health() methods
#test game over logic and while loop that prompts players to take action
#Jim wins pokemon battle prints out twice
#Change battle system so player with fastest pokemon starts first

#Improvements
#Pokemon types - Dict? How they're checked to see if there oppenent has an adv/disadv
#Pokedex - Display pokemon types they are strong/ weak against
#Damage calculation
#Display Health - pokemon hp when prompting player for an action