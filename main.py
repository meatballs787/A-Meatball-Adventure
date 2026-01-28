class meatball():
    def __init__(self, name, istrength, ihp, idefense, class_type):
        self.name = name
        self.strength = istrength
        self.istrength = istrength
        self.hp = ihp
        self.imax_hp = ihp
        self.max_hp = ihp
        self.defense = idefense
        self.idefense = idefense
        self.class_type = class_type
        # class type should start off as 0. 1 = warrior, 2 = thrower, 3 = tank 4 = bandit
        self.level = 0
        self.magic_mince = 0
        self.mince = 0

    def die(self):
        print(f"{self.name} has died./n {self.name} will respawn with  50% health")
        self.hp = self.max_hp // 2
    def strength_up(self, amount):
        self.strength += amount
    def defense_up(self, amount):
        self.defense += amount
    def heal(self, amount):
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp
    def take_damage(self, amount):
        damage_taken = amount - self.defense
        if damage_taken < 0:
            damage_taken = 0
        self.hp -= damage_taken
        if self.hp <= 0:
            self.die()
    def change_class(self, new_class):
        self.class_type = new_class
    def level_up(self):
        self.level += 1
        self.magic_mince +=1