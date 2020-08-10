class Pokemon:
    def __init__(self, name, level, type, max_hp, current_hp, unconcious = False):
        self.name = name
        self.level = level
        self.type = type
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.unconcious = unconcious

    def lose_health(self, damage):
        if damage <= 0:
            print("{name} dodged the attack!".format(name = self.name))
        elif damage >= self.current_hp:
            self.current_hp -= damage
            self.unconcious = True
            print("{name} has taken {dmg} damage and is unable to continue".format(name=self.name, dmg = damage))
        else:
            print("{name} has taken {dmg} damage".format(name=self.name, dmg=damage))
    
    def regain_health(self, heal):
        self.current_hp += heal
        print("{name} was healed by {health} hp".format(name=self.name, health=heal))

pika = Pokemon("Pikachu", 1, "electric", 20, 20, False)
pika.lose_health(10)
pika.regain_health(5)