class Pokemon:
    def __init__(self, name, level, type, max_hp, current_hp, unconcious = False):
        self.name = name
        self.level = level
        self.type = type
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.unconcious = unconcious

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
            print("{name} was healed by {health} hp. They now have {hp} hp".format(name=self.name, health=heal, 
            hp=self.current_hp))
        else:
            print("Cannot heal {name}. They are unconcious".format(name=self.name))

    

pika = Pokemon("Pikachu", 1, "electric", 20, 20, False)
pika.lose_health(25)
pika.regain_health(5)