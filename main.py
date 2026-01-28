class meatball():
    def __init__(self, name, isize, istrength, ihp, idefense):
        self.name = name
        self.size = isize
        self.isize = isize
        self.strength = istrength
        self.istrength = istrength
        self.hp = ihp
        self.ihp = ihp
        self.defense = idefense
        self.idefense = idefense

    def die(self):
        print(f"{self.name} has died./n {self.name} will respawn with  50% stats")
        self.size *= 0.5
        self.strength *= 0.5
        self.hp *= 0.5
        self.defense *= 0.5
        if self.size < self.isize:
            self.size = self.isize
        if self.strength < self.istrength:
            self.strength = self.istrength
        if self.hp < self.ihp:
            self.hp = self.ihp
        if self.defense < self.idefense:
            self.defense = self.idefense
    def size_up(self, amount):
        self.size += amount
    def strength_up(self, amount):
        self.strength += amount
    def defense_up(self, amount):
        self.defense += amount
    def heal(self, amount):
        self.hp += amount

petJames = meatball("James", 10, 15, 100, 5)
petJames.size_up(200)
petJames.strength_up(500)
petJames.defense_up(300)

print(petJames.size)
print(petJames.strength)
print(petJames.hp)
print(petJames.defense)
petJames.die()
print(petJames.size)
print(petJames.strength)
print(petJames.hp)
print(petJames.defense)
