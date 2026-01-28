import time
def delay(ms):
    time.sleep(ms/1000)
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
        self.experience = 0

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
        self.magic_mince +=3
        print(f"<><><><><><><><><><><>\n {self.name} leveled up to level {self.level}!\n<><><><><><><><><><><>")
        delay(1500)
    def gain_experience(self, amount):
        self.experience += amount
        if self.experience >= (self.level + 1) * 10:
            self.experience -= (self.level + 1) * 10
            self.level_up()
    def gain_mince(self, amount):
        self.mince += amount
        print(f"{self.name} gained {amount} mince!")
        delay(1500)
    def spend_mince(self, amount):
        if amount > self.mince:
            print("Not enough mince!")
            return False
            delay(1500)
        self.mince -= amount
        delay(1500)
        return True
    def restore_HP(self,mince_amount):
        if spend_mince(self, mince_amount) == True:
            self.heal(mince_amount * 2)
    def gain_magic_mince(self, amount):
        self.magic_mince += amount
        print(f"{self.name} gained {amount} magic mince!")
        delay(1500)
    def spend_magic_mince(self, amount):
        if amount > self.magic_mince:
            print("Not enough magic mince!")
            return False
            delay(1500)
        else:
            self.magic_mince -= amount
            return True

class MainLoop:
    def __init__(self, player):
        self.player = player
    def openEnhanceMenu(self):
        while True:
            print("-----Enhancement Menu-----")
            print(f"Magic Mince Available: {self.player.magic_mince}")
            delay(1500)
            print("Current Stats:")
            print(f"Strength: {self.player.strength}")
            print(f"Defense: {self.player.defense}")
            print(f"Max HP: {self.player.max_hp}")
            print("press enter to continue")
            input()
            delay(1500)
            print("choose a stat to enhance:")
            print("1. Strength")
            print("2. Defense")
            print("3. Max HP")
            print("4. Exit Enhancement Menu")
            choice = input()
            delay(1500)

            print("How much magic mince do you want to spend? 1 mince = +1 to stat")
            amount = int(input())
            delay(1500)
            
            if self.player.spend_magic_mince(amount):
                if choice == "1":
                    self.player.strength_up(amount)
                    print(f"Strength increased by {amount}!")
                    break
                elif choice == "2":
                    self.player.defense_up(amount)
                    print(f"Defense increased by {amount}!")
                    break
                elif choice == "3":
                    self.player.max_hp += amount
                    print(f"Max HP increased by {amount}!")
                    break
                elif choice == "4":
                    print("Exiting Enhancement Menu.")
                    break
                else:
                    print("Invalid choice.") 
            else:
                print("Enhancement failed due to insufficient magic mince.")
            
    def start(self):
        print(f"It has been 50 years since the invasion of the hands. Hands came from the sky with steely forks, sharp skewers, jars of hot alfredo sauce, and dense nets of spaghetti. \n")
        delay(2000)
        print(
            f"The rest of {self.player.name}'s family were imprisoned in the world of pasta,\n"
            f"and {self.player.name} has been left alone to fend for themselves.\n"
        )
        delay(2000)
        print(
            f"One day, while scavenging for food, {self.player.name} stumbles upon a mysterious glowing pile of minced meat.\n"
        )
        delay(2000)
        print("In this game you must make choices. Do you want to eat the meat(1) or leave it alone(2)?")
        eatchoice = input()
        delay(1500)
        if eatchoice == "2":
            print("this time your choice doesn't matter. You are eating the meat anyway.")
        delay(1500)
        self.player.gain_magic_mince(1)
        print(f"when {self.player.name} consumes magical mince, stats of their choosing are enhanced")
        delay(1500)
        print("Strength enhances attack power. Defense reduces damage taken. Max HP is pretty self explanatory.")
        delay(1500)
        print("Now it's time to enhance your meatball! Choose which stat you want to raise first.")
        self.openEnhanceMenu()



print("Welcome to a Meatball Adventure! Please enter your meatball's name:")
name = input()
player = meatball(name, 5, 20, 2, 0)
game = MainLoop(player)
game.start()