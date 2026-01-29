import time
import random
def delay(ms):
    time.sleep(ms/1000)

# Global Functions
def attack(attacker, defender):
    if defender.defense*.016 >= 0.5*random.random()+attacker.strength*.011:
        print(f"{defender.name} dodged the attack!")
        delay(1000)
        return
    else:
        damage = attacker.strength - 0.3*defender.defense
        if damage < 0:
            damage = 0
        print(f"{attacker.name} attacked {defender.name} for {damage} damage!")
        defender.take_damage(damage)
        delay(1000)
class meatball():
    def __init__(self, name, istrength, ihp, idefense):
        self.name = name
        self.strength = istrength
        self.istrength = istrength
        self.hp = ihp
        self.imax_hp = ihp
        self.max_hp = ihp
        self.defense = idefense
        self.idefense = idefense
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
        self.hp -= amount
        if self.hp <= 0:
            self.die()
    def level_up(self):
        self.level += 1
        self.magic_mince +=3
        print(f"<><><><><><><><><><><>\n {self.name} leveled up to level {self.level}!\n<><><><><><><><><><><>")
        delay(1500)
    def gain_experience(self, amount):
        self.experience += amount
        print(f"{self.name} gained {amount} experience!")
        delay(1500)
        print(f"{self.name}'s Experience: {self.experience}/{(self.level + 1) * 10}")
        delay(1500)
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
        if self.spend_mince(mince_amount) == True:
            self.heal(mince_amount * 2)
            print(f"{self.name}'s HP: {round(self.hp,1)}/{self.max_hp}")
            delay(1500)
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
class Enemy:
    def __init__(self, strength, hp, defense, experience_reward, mince_reward):
        self.strength = strength
        self.max_hp = hp
        self.hp = hp
        self.defense = defense
        self.experience_reward = experience_reward
        self.mince_reward = mince_reward
    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.die()

    def die(self):
        print("The enemy has been defeated!")
        delay(1500)

class toothpick(Enemy):
    def __init__(self):
        super().__init__(strength=3, hp=10, defense=1, experience_reward=5, mince_reward=2)
        self.name = "Toothpick"
    def poke(self):
        print("The toothpick pokes you with its sharp end!")
    def die(self):
        print("The toothpick snaps in half.")
        delay(1500)
        super().die()
        



class MainLoop:
    def __init__(self, player):
        self.player = player
        self.escape = False
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
            print(f"Magic Mince Available: {self.player.magic_mince}")
            print("choose a stat to enhance:")
            print("1. Strength")
            print("2. Defense")
            print("3. Max HP")
            print("4. Exit Enhancement Menu")
            choice = input()
            delay(1500)

            print("How much magic mince do you want to spend? 1 mince = +1 to strength and defense, +3 to max HP")
            print(f"Magic Mince Available: {self.player.magic_mince}")
            delay(500)
            amount = int(input())
            delay(1500)
            if choice == "4":
                print("Exiting Enhancement Menu.")
                break
            
            if self.player.spend_magic_mince(amount):
                if choice == "1":
                    self.player.strength_up(amount)
                    print(f"Strength increased by {amount}!")
                    delay(2000)
                    break
                elif choice == "2":
                    self.player.defense_up(amount)
                    print(f"Defense increased by {amount}!")
                    delay(2000)
                    break
                elif choice == "3":
                    self.player.max_hp += 3*amount
                    self.player.hp += 3*amount
                    print(f"Max HP increased by {3*amount}!")
                    delay(2000)
                    break
                else:
                    print("Invalid choice.")
                    delay(2000) 
            else:
                print("Enhancement failed due to insufficient magic mince.")
                delay(2000)
    def actionMenu(self, enemy):
        while True:
            print("|/|-- Action Menu --|/|")
            delay(500)
            print(f"{self.player.name}'s Mince: {self.player.mince}")
            delay(500)
            print("choose your action:")
            delay(300)
            print("1. Attack")
            print("2. Use Mince to Heal")
            print("3. Escape (not implemented yet)")
            choice = input()
            delay(1000)
            if choice == "1":
                self.attackMenu(enemy)
                break
            elif choice == "2":
                print("How much mince do you wish to consume? (1 mince = 2 HP)")
                amount = int(input())
                delay(1000)
                self.player.restore_HP(amount)
                break
            elif choice == "3":
                print(f"{self.player.name} attempts to escape...")
                delay(1000)
                if random.random()+enemy.strength*.011 < 0.8:
                    self.escape=True
                    print("Escape successful!")
                    delay(1000)
                else:
                    print("Escape failed!")
                    delay(1000)
                break
            else:
                print("invalid choice")
                delay(1000)

    def attackMenu(self, enemy):
        while True:
            print("|/|-- Attack Menu --|/|")
            delay(500)
            print("choose your attack:")
            delay(300)
            print("1. Normal Attack")
            print("2. Heavy Attack (Not implemented yet)")
            choice = input()
            delay(1000)
            if choice == "1":
                print(f"{self.player.name} uses Normal Attack!")
                attack(self.player, enemy)
                delay(1000)
                return
            elif choice == "2":
                print("Heavy Attack is not implemented yet.")
                delay(1000)
            else:
                print("invalid choice")
                delay(1000)

    def fight(self, enemy) :
        while enemy.hp > 0 and self.player.hp > 0 and not self.escape:
            attack(enemy, self.player)
            delay(2000)
            print(f"{self.player.name}'s HP: {round(self.player.hp,1)}/{self.player.max_hp}")
            delay(1500)
            self.actionMenu(enemy)
        if enemy.hp <= 0:
            self.player.gain_experience(enemy.experience_reward)
        self.escape = False

    def NeutMenu(self):
        while True:
            print("-----Main Menu-----")
            print("1. Enhance Stats")
            print("2. Enter into Hostile Territories")
            choice = input()
            if choice == "1":
                self.openEnhanceMenu()
                break
            elif choice == "2":
                self.HostileTerritories()

    def HostileTerritories(self):
        print("-----Hostile Territories-----")
        print("DL = Danger Level")
        print("1. Isle of Toothpicks. Contains Toothpicks(DL:1) and Skewers(DL:2)")
        print("2. Sauce Swamps. Contains Sauce Throwers(DL:3) and Spoons(DL:5)")
        print("3. Pasta Plains. Contains Spaghetti Wranglers(DL:6) and Rigatoni Trappers(DL:8)")
        print("4. Edge of the World. Contains Steely Forks(DL:10) and The Hands(DL:10)")
        print("5. Return to Main Menu")
        print("Choose your destination:")
        choice = input()
        delay(1000)
        print("This area is under construction. Returning to Main Menu.")
        delay(2000)
            
    def start(self):
        print(f"It has been 50 years since the invasion of the hands. \nHands came from the sky with steely forks, sharp skewers, jars of hot alfredo sauce, and dense nets of spaghetti. \n")
        delay(3000)
        print(
            f"The rest of {self.player.name}'s family were imprisoned in the world of pasta,\n"
            f"and {self.player.name} has been left alone to fend for themselves.\n"
        )
        delay(3000)
        print(
            f"One day, while scavenging for food, {self.player.name} stumbles upon a mysterious glowing pile of minced meat.\n"
        )
        delay(2000)
        print("In this game you must make choices. Do you want to eat the meat(1) or leave it alone(2)?")
        eatchoice = input()
        delay(1500)
        if eatchoice == "2":
            print("this time your choice doesn't matter. You are eating the meat anyway.")
        delay(2000)
        self.player.gain_magic_mince(1)
        print(f"when {self.player.name} consumes magical mince, stats of their choosing are enhanced")
        delay(1500)
        print("Strength enhances attack power. Defense reduces damage taken. Max HP is pretty self explanatory.")
        delay(1500)
        print("Now it's time to enhance your meatball! Choose which stat you want to raise first.")
        self.openEnhanceMenu()
        delay(1500)
        print("One last thing before you go on your adventure. You need to have a little combat experience.")
        delay(1000)
        print("Here is a little bit of normal mince meat. It will heal you when you consume it.")
        delay(1500)
        self.player.gain_mince(4)
        print("An aggressive toothpick appears!")
        delay(1500)
        enemy = toothpick()
        self.fight(enemy)
        print("Good job on winning your first fight! a Toothpick is the weakest enemy you'll face so be prepared.")
        delay(2000)
        print("Don't take stupid risks, because once you die, your meatball is dead forever.")
        delay(2000)
        print("Now, go forth and escape the clutches of the Hands!")

    def mainLoop(self):
        while self.player.hp > 0:
            self.NeutMenu()


print("Welcome to a Meatball Adventure! Please enter your meatball's name:")
name = input()
delay(1000)
player = meatball(name, 5, 20, 3)
game = MainLoop(player)
game.start()
game.mainLoop()