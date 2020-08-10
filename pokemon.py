class Pokemon:
    def __init__(self, name, level, type, max_hp, current_hp):
        self.name = name
        self.level = level
        self.type = type.lower()
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.unconcious = False

    def lose_health(self, damage
    ):
        def knocked_out(self):
            self.current_hp = 0
            self.unconcious = True
            print("{name} has been knocked unconcious".format(name=self.name))

        if damage <= 0:
            print("{name} dodged the attack!".format(name = self.name))
        elif damage >= self.current_hp:
            self.current_hp -= 0
            print("{name} has taken {dmg} damage. They have 0 hp".format(name=self.name, dmg = damage))
            knocked_out(self)
        else:
            self.current_hp -= damage
            print("{name} has taken {dmg} damage. They now have {hp} hp".format(name=self.name, dmg=damage,
             hp=self.current_hp))
    
    def regain_health(self, heal):
        if self.unconcious is False:
            self.current_hp += heal
            if self.current_hp > self.max_hp:
                self.current_hp = self.max_hp
            print("{name} was healed by {health} hp. They now have {hp} hp".format(name=self.name, health=heal, 
            hp=self.current_hp))
        else:
            print("Cannot heal {name}. They are unconcious".format(name=self.name))

    def revive(self, health):
        if health >= self.max_hp:
            self.current_hp = self.max_hp
            self.unconcious = False
        else:
            self.current_hp = health
        print("{name} was revived. They now have {hp} hp".format(name=self.name, hp=self.current_hp))

    def attack(self, other_pokemon):
        if self.unconcious is True:
            print("{name} cannot attack because they are unconcious".format(name=self.name))
            return
        elif other_pokemon.unconcious is True:
            print("Cannot attack {name} because they are unconcious".format(name=other_pokemon.name))
            return

        effective_attack = ""
        #Attacking pokemon has advantage based on type
        if self.type == "fire" and other_pokemon.type == "grass":
            effective_attack = "yes"
        elif self.type == "electric" and other_pokemon.type == "water":
            effective_attack = "yes"
        elif self.type == "water" and other_pokemon.type == "fire":
            effective_attack = "yes"
        #Attacking pokemon has disadvantage
        elif self.type == "water" and other_pokemon.type == "electric":
            effective_attack = "no"
        elif self.type == "grass" and other_pokemon.type == "fire":
            effective_attack = "no"
        elif self.type == "fire" and other_pokemon.type == "water":
            effective_attack = "no"
            
        if effective_attack == "yes": 
            other_pokemon.lose_health(self.level * 2)
            print("{name}'s attack was super effective".format(name=self.name))
        elif effective_attack == "no":
            other_pokemon.lose_health(self.level * 0.5)
            print("{name}'s attack wasn't very effective".format(name=self.name))
        else:
            other_pokemon.lose_health(self.level)


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

    def switch_pokemon(self, pokemon_index):
        if self.pokemon[pokemon_index].unconcious is True:
            print("{trainer} cannot send out {new_pokemon} because they are unconcious".format(
            trainer=self.name, new_pokemon=self.pokemon[pokemon_index].name))
            return
        print("{trainer} has recalled {prev_pokemon}. {trainer} has sent out {new_pokemon}!".format(
            trainer=self.name, prev_pokemon=self.current_pokemon.name, new_pokemon=self.pokemon[pokemon_index].name))
        self.current_pokemon = self.pokemon[pokemon_index]




pika = Pokemon("Pikachu", 2, "Electric", 20, 20)
squirtle = Pokemon("Squirtle", 1, "Water", 15, 15)
bulbasour = Pokemon("Bulbasour", 3, "Grass", 30, 30)
charmander = Pokemon("Charmander", 4, "fire", 35, 35)
starme = Pokemon("Starme", 3, "water", 30, 30)
ash = Trainer("Ash", [pika, charmander, bulbasour], 3, 0)
misty = Trainer("Misty", [starme, squirtle], 3, 0)

#pika.lose_health(25)
#pika.regain_health(5)
#pika.revive(50)
#pika.attack(squirtle)
#squirtle.attack(charmander)
#bulbasour.attack(pika)
#charmander.attack(squirtle)
bulbasour.lose_health(50)
#ash.use_potion()
ash.attack_trainer(misty)
misty.switch_pokemon(1)
misty.attack_trainer(ash)
ash.attack_trainer(misty)
ash.switch_pokemon(2)
