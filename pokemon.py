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
        else:
            print("Cannot heal {name}. They are unconcious".format(name=self.name))
        return False

    def revive(self, health):
        if self.unconcious is False:
            print("Cannot revive {pokemon} because they are already concious".format(pokemon=self.name))
        else:
            self.unconcious = False
            self.current_hp = health
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
                print("{name}'s attack was super effective".format(name=self.name)) 
                self.gain_xp(other_pokemon.level)
        elif self.have_advantage(other_pokemon.type) == "no":
            if other_pokemon.lose_health((self.attack_stat - other_pokemon.defense_stat) * 0.5) is True:
                print("{name}'s attack wasn't very effective".format(name=self.name))
                self.gain_xp(other_pokemon.level)
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

    def pokemon_selection(self, starting_pokemon, trainer_name):
        pokemon_squad = []
        display_pokemon = []
        for key in starting_pokemon:
            display_pokemon.append(key)
        print("\n- {}, please choose 3 pokemon to form your squad".format(trainer_name))
        while len(pokemon_squad) < 3:
            selection = input("-> Please choose a pokemon: " + ", ".join(display_pokemon) + "   ").lower()
            if selection in display_pokemon:
                index = display_pokemon.index(selection)
                pokemon_squad.append(starting_pokemon[selection])
                print("{} joined your squad".format(display_pokemon[index]))
                display_pokemon.pop(index)
            else:
                print("Sorry, {user_input} is not a vaild pokemon selection".format(user_input=selection))
        print("- {name} your pokemon squad is: {squad}".format(name=trainer_name, squad=pokemon_squad))
        return pokemon_squad

    def starting_pokemon_selection(self, trainer_name, squad):
        display_pokemon = []
        for pokemon in squad:
            pokemon_name = pokemon.name.lower()
            display_pokemon.append(pokemon_name)
        starter = ""
        while starter == "":
            starter = input("\n-> {name}, please choose your pokemon to start the battle: ".format(
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
    
    def first_move(self, other_trainer):
        if self.pokemon[self.current_pokemon].speed_stat > other_trainer.pokemon[
            other_trainer.current_pokemon].speed_stat:
            print("{player_1} has the first move!".format(player_1=self.name))
            return 0
        else:
            print("{player_2} has the first move!".format(player_2=other_trainer.name))
            return 1

    def use_potion(self):
        if self.pokemon[self.current_pokemon].current_hp == self.pokemon[self.current_pokemon].max_hp:
            print("Cannot heal {pokemon} as they already have full health".format(
                pokemon=self.pokemon[self.current_pokemon]))
        elif self.pokemon[self.current_pokemon].regain_health(10) is True:
            self.potions -= 1
            print("{trainer} now has {potions}/3 potions remaining".format(trainer=self.name, 
            potions=self.potions))
            return True
        return False

    def attack_trainer(self, other_trainer):
        if self.pokemon[self.current_pokemon].attack(other_trainer.pokemon[other_trainer.current_pokemon]
        ) == True and other_trainer.unconcious_count() <= len(other_trainer.pokemon) - 1:
            other_trainer.switch_pokemon(other_trainer.current_pokemon)
            if self.unconcious_count() <= len(other_trainer.pokemon) - 2:
                player_input = ""
                while player_input == "":
                    player_input = input(
                        "-> {plyr}, do you want switch pokemon? {enmy} is about to send out {pokemon}!   yes/no:   ".format(
                        plyr=self.name, enmy=other_trainer.name, pokemon=other_trainer.pokemon[
                        other_trainer.current_pokemon])).lower()
                    if player_input == "yes":
                        self.switch_pokemon(self.current_pokemon)
                    elif player_input == "no":
                        break
                    else:
                        print("{} is not a valid input".format(player_input))
                        player_input == ""
        self.did_win(other_trainer)

    def switch_pokemon(self, current_index):
        display_pokemon = []
        for pokemon in self.pokemon:
            display_pokemon.append(pokemon.name.lower())
        while self.current_pokemon == current_index:
            pokemon_selection = input("\n-> {name}, please choose a pokemon to switch to: ".format(
                name=self.name) + ", ".join(display_pokemon) + "   ").lower()
            if pokemon_selection in display_pokemon:
                index = display_pokemon.index(pokemon_selection)
                if index == self.current_pokemon:
                    print("{} is already your current pokemom".format(self.pokemon[self.current_pokemon]))
                elif self.pokemon[index].unconcious is False:
                    print("{trainer}: {pokemon} return. Go {new_pokemon}!".format(trainer=self.name, 
                    pokemon=self.pokemon[self.current_pokemon], new_pokemon=self.pokemon[index]))
                    self.current_pokemon = index
                else:
                    print("{trainer} cannot send out {new_pokemon} because they are unconcious".format(
                trainer=self.name, new_pokemon=self.pokemon[index].name))
            else:
                print("{} is not a valid pokemon".format(pokemon_selection))

    def unconcious_count(self):
        count = 0
        for monster in self.pokemon:
            if monster.unconcious is True:
                count += 1
        return count

    def did_win(self, other_trainer):
        unconcious_count = other_trainer.unconcious_count()
        if unconcious_count == len(other_trainer.pokemon):
            return True
        else:
            return False

    def player_turn(self, other_trainer):
        actions = ["attack", "potion", "switch", "switch pokemon", "pokedex"]
        curr_pokemon = self.pokemon[self.current_pokemon]
        player_input = ""

        print("\n- {}'s turn".format(self.name))
        while player_input not in actions:
            player_input = input("\n-> What will {pokemon} do?   {currhp}/{maxhp} hp".format(pokemon=curr_pokemon, 
            currhp=curr_pokemon.current_hp, maxhp=curr_pokemon.max_hp)
            + "\n-> Attack \t-> HP Potion \t-> Switch Pokemon \t-> Pokedex   ").lower()
            
            if player_input in actions:
                if player_input == actions[1]:
                    if self.potions == 0:
                        print("Cannot complete action. {name} has {count} potions remaining".format(
                            name=self.name, count=self.potions))
                        return False
                    print("Using potion")
                    self.use_potion()
                elif player_input == actions[2] or player_input == actions[3]:
                    if self.unconcious_count() >= len(self.pokemon) - 1:
                        print("Cannot complete action. All other pokemon are unconcious")
                        return False
                    print("Switching pokemon")
                    self.switch_pokemon(self.current_pokemon)
                elif player_input == actions[0]:
                    self.attack_trainer(other_trainer)
                elif player_input == actions[4]:
                    curr_pokemon.pokedex_information()
                print("Turn Over")
                return True
            else:
                print("Sorry. {} is not a valid action. Try again".format(player_input))
                return False


starting_level = 1
pika = Pokemon("Pichu", starting_level, "Electric")
squirtle = Pokemon("Squirtle", starting_level, "Water")
bulbasaur = Pokemon("Bulbasaur", starting_level, "Grass")
charmander = Pokemon("Charmander", starting_level, "fire")
starmie = Pokemon("Starmie", starting_level, "water")
starting_pokemon = {"pika": pika, "squirtle": squirtle, "bulbasaur": bulbasaur, "charmander": charmander, 
"starmie": starmie}

#for testing
"""
name_1 = "Jim"
name_2 = "Bob"
squad_1 = [pika, charmander, bulbasaur]
squad_2 = [squirtle, bulbasaur, starmie]
starter_1 = 0
starter_2 = 0
"""

name_1 = input("-> Enter Player 1's name: ")
name_2 = input("-> Enter player 2's name: ")
print("Welcome Pokemon Trainers {p1} and {p2}".format(p1=name_1, p2=name_2))
squad_1 = pika.pokemon_selection(starting_pokemon, name_1)
squad_2 = pika.pokemon_selection(starting_pokemon, name_2)
starter_1 = pika.starting_pokemon_selection(name_1, squad_1)
starter_2 = pika.starting_pokemon_selection(name_2, squad_2)
player_1 = Trainer(name_1, squad_1, starter_1)
player_2 = Trainer(name_2, squad_2, starter_2)
turn_counter = player_1.first_move(player_2)

while player_1.did_win(player_2) == False and player_2.did_win(player_1) == False:
    turn_counter += 1
    if turn_counter % 2 == 1:
        if player_1.player_turn(player_2) == False:
            turn_counter -= 1
    else:
        if player_2.player_turn(player_1) == False:
            turn_counter -= 1

print("\n{opp_trainer} has no more Pokemon to send out...".format(opp_trainer=player_2.name))
print("*------------------------------------------*")
print("\t{name} wins the pokemon battle!".format(name=player_1.name))
print("*------------------------------------------*")

#Known Bugs



#Improvements
#Pokemon types - Dict? How they're checked to see if there oppenent has an adv/disadv
#Pokedex - Display pokemon types they are strong/ weak against
#Damage calculation - balance dmg dealth by pokemon
