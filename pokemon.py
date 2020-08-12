class Pokemon:
    def __init__(self, name, level, type):
        self.name = name
        self.level = level
        self.type = type.lower()
        self.max_hp = level + 3
        self.current_hp = self.max_hp
        self.unconcious = False
        self.xp = 0
        self.xp_cap = level * 2

    def lose_health(self, damage):
        self.current_hp -= damage
        if self.current_hp <= 0:
            self.current_hp = 0
            self.unconcious = True
            print("{name} has taken {dmg} damage. {name} has been knocked unconcious!".format(name=self.name, dmg = damage))
        else:
            print("{name} has taken {dmg} damage. They now have {hp} hp".format(name=self.name, dmg=damage,
             hp=self.current_hp))
        return self.unconcious
    
    def regain_health(self, heal):
        if self.unconcious is False and self.current_hp < self.max_hp:
            self.current_hp += heal
            self.current_hp = self.set_health()
            print("{name} was healed by {health} hp. They now have {hp} hp".format(name=self.name, health=heal, 
            hp=self.current_hp))
        elif self.current_hp == self.max_hp:
            print("Cannot heal {pokemon} as they already have full health".format(pokemon=self.name))
        else:
            print("Cannot heal {name}. They are unconcious".format(name=self.name))

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

    def attack(self, other_pokemon):
        if self.unconcious is True:
            print("{name} cannot attack because they are unconcious".format(name=self.name))
            return
        elif other_pokemon.unconcious is True:
            print("Cannot attack {name} because they are unconcious".format(name=other_pokemon.name))
            return
            
        if self.have_advantage(other_pokemon.type) == "yes": 
            if other_pokemon.lose_health(self.level * 2) is True:
                self.gain_xp(other_pokemon.level)
            print("{name}'s attack was super effective".format(name=self.name))            
        elif self.have_advantage(other_pokemon.type) == "no":
            if other_pokemon.lose_health(self.level * 0.5) is True:
                self.gain_xp(other_pokemon.level)
            print("{name}'s attack wasn't very effective".format(name=self.name))
        else:
            if other_pokemon.lose_health(self.level) is True:
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
            self.xp -= self.xp_cap
            self.xp_cap = self.level * 2
            print("* {pokemon} leveled up! * They are now level {lvl}. XP test = {xp}".format(pokemon=self.name,
            lvl=self.level, xp=self.xp))           


class Trainer():
    def __init__(self, name, pokemon, potions=3, current_pokemon=0):
        self.name = name
        self. pokemon = pokemon
        self.potions = 3
        self.current_pokemon = pokemon[0]
        
    def use_potion(self):
        if self.potions <= 0:
            print("{name} has no potions to use".format(name=self.name))
        self.potions -= 1
        self.current_pokemon.regain_health(10)

    def attack_trainer(self, other_trainer):
        self.current_pokemon.attack(other_trainer.current_pokemon)
        self.did_win(other_trainer)

    def switch_pokemon(self, pokemon_index):
        if self.pokemon[pokemon_index].unconcious is True:
            print("{trainer} cannot send out {new_pokemon} because they are unconcious".format(
            trainer=self.name, new_pokemon=self.pokemon[pokemon_index].name))
            return
        print("{trainer} has recalled {prev_pokemon}. {trainer} has sent out {new_pokemon}!".format(
            trainer=self.name, prev_pokemon=self.current_pokemon.name, new_pokemon=self.pokemon[pokemon_index].name))
        self.current_pokemon = self.pokemon[pokemon_index]

    def did_win(self, other_trainer):
        unconcious_count = 0
        for monster in other_trainer.pokemon:
            if monster.unconcious is True:
                unconcious_count += 1
        if unconcious_count == len(other_trainer.pokemon):
            print("{opp_trainer} has no more Pokemon to send out...".format(opp_trainer=other_trainer.name))
            print("** {name} wins the pokemon battle! **".format(name=self.name))



pika = Pokemon("Pikachu", 2, "Electric")
squirtle = Pokemon("Squirtle", 1, "Water")
bulbasour = Pokemon("Bulbasour", 3, "Grass")
charmander = Pokemon("Charmander", 4, "fire")
starme = Pokemon("Starme", 3, "water")
starme2 = Pokemon("Starme", 3, "water")
starme3 = Pokemon("Starme", 3, "water")
starme4 = Pokemon("Starme", 3, "water")
starme5 = Pokemon("Starme", 3, "water")
starme6 = Pokemon("Starme", 3, "water")
starme7 = Pokemon("Starme", 3, "water")
starme8 = Pokemon("Starme", 3, "water")
starme9 = Pokemon("Starme", 3, "water")
starme10 = Pokemon("Starme", 3, "water")
#ash = Trainer("Ash", [pika, charmander, bulbasour], 3, 0)
#misty = Trainer("Misty", [starme, squirtle], 3, 0)
ash = Trainer("Ash", [pika, bulbasour], 3, 0)
misty = Trainer("Misty", [starme, squirtle, starme2, starme3, starme4, starme5, starme6, starme7, starme8,
starme9, starme10], 3, 0)


#pika.attack(starme)
#pika.attack(starme)
#pika.attack(bulbasour)
#pika.attack(bulbasour)
#pika.attack(bulbasour)
#charmander.attack(squirtle)
#charmander.attack(squirtle)

#pika.revive(50)
#pika.attack(squirtle)
#squirtle.attack(charmander)
#bulbasour.attack(pika)
#charmander.attack(squirtle)
#bulbasour.lose_health(50)
#ash.use_potion()
#misty.attack_trainer(ash)
#ash.switch_pokemon(2)
for i in range(len(misty.pokemon) - 1):
    ash.attack_trainer(misty)
    ash.attack_trainer(misty)
    misty.switch_pokemon(i + 1)