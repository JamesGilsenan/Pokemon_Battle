class Pokemon:
    def __init__(self, name, level, type, max_hp, current_hp, unconcious = false):
        self.name = name
        self.level = level
        self.type = type
        self.max_hp = max_hp + (2 * level)
        self.current_hp = current_hp
        self.unconcious = unconcious
