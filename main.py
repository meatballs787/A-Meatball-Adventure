import time
import random

gameOver = False
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
        print(f"{self.name} has died./n {self.name} Stats: \n Level: {self.level}\n Strength: {self.strength}\n Defense: {self.defense}\n Max HP: {self.max_hp}\n Experience: {self.experience}\n Mince: {self.mince}\n Magic Mince: {self.magic_mince}")
        delay(2000)
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
        print(f"<><><><><><><><><><><>\n {self.name} leveled up to level {self.level}!\n<><><><><><><><><><><>")
        self.gain_magic_mince(3)
        delay(1500)
    def gain_experience(self, amount):
        self.experience += amount
        print(f"{self.name} gained {amount} experience!")
        delay(1500)
        print(f"{self.name}'s Experience: {self.experience}/{(self.level + 1) * 10}")
        delay(1500)
        while self.experience >= (self.level + 1) * 10:
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
        elif amount < 0:
            print("You can't spend a negative amount of mince")
            return False
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
        elif amount < 0:
            print("Nice try. You can't spend negative amounts of magic mince")
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
    def attack(self, player):
        print("The toothpick pokes you with its sharp end!")
        attack(self, player)
    def die(self):
        print("The toothpick snaps in half.")
        delay(1500)
        super().die()

class skewer(Enemy):
    
    def __init__(self):
        super().__init__(strength=5, hp=15, defense=2, experience_reward=8, mince_reward=3)
        self.name = "Skewer"
    def attack(self, player):
        chance = random.random()
        if chance >.8: 
            print("The skewer critically stabs you!")
            self.strength *= 2
            attack(self, player)
            self.strength /= 2
            delay(500)
        else: 
            print("The skewer stabs you!")
            attack(self, player)
            delay(500)
    def die(self):
        print("The skewer breaks apart.")
        delay(1500)
        super().die()

class sauce_thrower(Enemy):
    def __init__(self):
        super().__init__(strength=7, hp=20, defense=3, experience_reward=12, mince_reward=5)
        self.name = "Sauce Thrower"
    def attack(self, player):
        chance = random.random()
        if chance >.8: 
            print("The sauce thrower throws a boiling glob of sauce at you!")
            self.strength *= 2.5
            attack(self, player)
            self.strength /= 2.5
            delay(500)
        else: 
            print("The sauce thrower splashes a hot glob sauce at you!")
            attack(self, player)
            delay(500)
    def die(self):
        print("The sauce thrower is too weak to throw any more sauce now.")
        delay(1500)
        super().die()

class spoon(Enemy):
    def __init__(self):
        super().__init__(strength=8, hp=25, defense=5, experience_reward=15, mince_reward=6)
        self.name = "Spoon"
    def attack(self, player):
        chance = random.random()
        if chance >.85: 
            print("The spoon slashes you with its sharp edge!")
            self.strength *= 2
            attack(self, player)
            self.strength /= 2
            delay(500)
        else: 
            print("The spoon hits you!")
            attack(self, player)
            delay(500)

    def die(self):
        print("The spoon is bent out of shape and useless now.")
        delay(1500)
        super().die() 

class spaghetti_wrangler(Enemy):
    def __init__(self):
        super().__init__(strength=10, hp=30, defense=6, experience_reward=20, mince_reward=8)
        self.name = "Spaghetti Wrangler"
    def attack(self, player):
        chance = random.random()
        if chance >.7: 
            print("The spaghetti wrangler chokes you with a spaghetti lasso!")
            attack(self, player)
            delay(500)
            print("The spaghetti wrangler prevents you from taking your next turn!")
            delay(1000)
            print("The spaghetti wrangler hits you with a spaghetti whip!")
            attack(self, player)
            delay(500)
        else: 
            print("The spaghetti wrangler hits you with a spaghetti whip!")
            attack(self, player)
            delay(500)

    def die(self):
        print("The spaghetti wrangler's strands have all snapped.")
        delay(1500)
        super().die()  

class rigatoni_trapper(Enemy):
    def __init__(self):
        super().__init__(strength=12, hp=35, defense=7, experience_reward=25, mince_reward=10)
        self.name = "Rigatoni Trapper"
    def attack(self, player):
        chance = random.random()
        if chance >.85: 
            print("The rigatoni trapper crushes you with a heavy rigatoni tube!")
            self.strength *= 3
            attack(self, player)
            self.strength /= 3
            delay(500)
        else: 
            print("The rigatoni trapper hits you with a rigatoni tube!")
            attack(self, player)
            delay(500)

    def die(self):
        print("The rigatoni trapper's tubes have all cracked.")
        delay(1500)
        super().die() 

class steely_fork(Enemy):
    def __init__(self):
        super().__init__(strength=15, hp=40, defense=10, experience_reward=30, mince_reward=15)
        self.name = "Steely Fork"
    def attack(self, player):
        chance = random.random()
        if chance >.7:
            print("The steely fork impales you with its sharp tines!")
            self.strength *= 2.5
            attack(self, player)
            self.strength /= 2.5
            delay(500)
        else: 
            print("The steely fork stabs you!")
            attack(self, player)
            delay(500)

    def die(self):
        print("The steely fork is bent and unusable now.")
        delay(1500)
        super().die()

class the_hands(Enemy):
    def __init__(self):
        super().__init__(strength=20, hp=50, defense=12, experience_reward=50, mince_reward=25)
        self.name = "The Hands"
    def attack(self, player):
        chance = random.random()
        if chance >.7:
            print("The Hands crush you with immense strength!")
            self.strength *= 3
            attack(self, player)
            self.strength /= 3
            delay(500)
        else: 
            print("The Hands hit you!")
            attack(self, player)
            delay(500)

    def die(self):
        print("The Hand has been defeated and retreats!")
        delay(1500)
        super().die()   

class Territories():
    def __init__(self, enemy1, enemy2, level):
        self.enemy1 = enemy1
        self.enemy2 = enemy2
        self.level = level

    def crossroads(self):
        chance1 = .01*random.randint(20,60)
        chance1b = .01*random.randint(10,35)
        chance2 = .01*random.randint(20,60)
        chance2b = .01*random.randint(10,35)
        chance3 = .01*random.randint(20,60)
        chance3b = .01*random.randint(10,35)
        print(
        "You have reached a crossroads. Choose your path:\n"
        f"1. left (chance at finding {self.enemy1.name},{self.enemy2.name},Treasure : "
        f"{100*chance1:.0f}%, {100*chance1b:.0f}%, {100*(1 - (chance1 + chance1b)):.0f}%)\n"
        f"2. right (chance at finding {self.enemy1.name},{self.enemy2.name},Treasure : "
        f"{100*chance2:.0f}%, {100*chance2b:.0f}%, {100*(1 - (chance2 + chance2b)):.0f}%)\n"
        f"3. straight (chance at finding {self.enemy1.name},{self.enemy2.name},Treasure : "
        f"{100*chance3:.0f}%, {100*chance3b:.0f}%, {100*(1 - (chance3 + chance3b)):.0f}%)\n"
        )
        choice = input()
        delay(1000)   
        if choice == "1" or choice == "2" or choice == "3":
            roll = random.random()
            if choice == "1":
                if roll < chance1:
                    print(f"You have encountered a {self.enemy1.name}!")
                    delay(1000)
                    return self.enemy1
                elif roll < chance1 + chance1b:
                    print(f"You have encountered a {self.enemy2.name}!")
                    delay(1000)
                    return self.enemy2
                else:
                    print("You found a treasure chest!")
                    delay(1000)
                    return None
            elif choice == "2":
                if roll < chance2:
                    print(f"You have encountered a {self.enemy1.name}!")
                    delay(1000)
                    return self.enemy1
                elif roll < chance2 + chance2b:
                    print(f"You have encountered a {self.enemy2.name}!")
                    delay(1000)
                    return self.enemy2
                else:
                    print("You found a treasure chest!")
                    delay(1000)
                    return None
            elif choice == "3":
                if roll < chance3:
                    print(f"You have encountered a {self.enemy1.name}!")
                    delay(1000)
                    return self.enemy1
                elif roll < chance3 + chance3b:
                    print(f"You have encountered a {self.enemy2.name}!")
                    delay(1000)
                    return self.enemy2
                else:
                    print("You found a treasure chest!")
                    delay(1000)
                    return None
        else:
            print("invalid input.")
            self.crossroads()
    def loop(self):
        for i in range(8):
            if player.hp <= 0:
                return
            enemy = self.crossroads()
            if enemy is not None:
                game.fight(enemy)
            else:
                mince_roll = self.level*random.randint(1, 5)
                magic_mince_roll = random.random()
                additional = ""
                if magic_mince_roll < 0.2:
                    additional = " and 1 magic mince"
                
                print(f"You open the treasure chest and find {mince_roll} mince {additional}!")
                player.gain_mince(mince_roll)
                if additional == " and 1 magic mince":
                    player.gain_magic_mince(1)
                delay(1500)
        if self.level != 4:
            print("You have successfully navigated the territory and return to safety!")
        print("Your HP has been fully restored.")
        player.hp = player.max_hp
class IsleOfToothpicks(Territories):
    def __init__(self):
        super().__init__(toothpick(), skewer(), level=1)
class SauceSwamps(Territories):
    def __init__(self):
        super().__init__(sauce_thrower(), spoon(), level=2)
class PastaPlains(Territories):
    def __init__(self):
        super().__init__(spaghetti_wrangler(), rigatoni_trapper(), level=3)
class EdgeOfTheWorld(Territories):
    def __init__(self):
        super().__init__(steely_fork(), the_hands(), level=4)
    def loop(self):
        super().loop()
        print("One final set of hands stands between you and your goal:")
        delay(1000)
        self.enemy2.strength += 10
        self.enemy2.max_hp *= 2
        self.enemy2.hp *= 2
        game.fight(self.enemy2)
        self.enemy2.strength -= 10
        self.enemy2.max_hp /= 2
        self.enemy2.hp /= 2
        print("Congratulations on reaching the Edge of the World! You've faced the toughest challenges yet.")
        delay(2000)
        print(f"{player.name} saves his family and escapes the world of pasta. You win! ")
        delay(2000)
        print("Thank you for playing A Meatball Adventure!")
        gameOver = True

    
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
            if choice == "4":
                print("Exiting Enhancement Menu.")
                break
            print("How much magic mince do you want to spend? 1 mince = +1 to strength and defense, +3 to max HP")
            print(f"Magic Mince Available: {self.player.magic_mince}")
            delay(500)
            amount = int(input())
            delay(1500)
            
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
            if enemy.hp< 80:
                print("3. Escape (50 percent success rate)")
            else:
                print("3. You can't escape. You can only fight for your life.")
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
                if random.random() < 0.5:
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
            print("2. Chance Attack (50 percent hit rate, double strength)")
            choice = input()
            delay(1000)
            if choice == "1":
                print(f"{self.player.name} uses Normal Attack!")
                attack(self.player, enemy)
                delay(1000)
                if enemy.hp > 0:
                    print(f"{enemy.name}'s HP: {round(enemy.hp,1)}/{enemy.max_hp}")
                return
            elif choice == "2":
                chance = random.random()
                if chance < 0.5:
                    print(f"{self.player.name}'s Chance Attack missed!")
                    delay(1000)
                    return
                else:
                    print(f"{self.player.name} uses Chance Attack!")
                    self.player.strength *= 2
                    attack(self.player, enemy)
                    self.player.strength /= 2
                    delay(1000)
                    if enemy.hp > 0:
                        print(f"{enemy.name}'s HP: {round(enemy.hp,1)}/{enemy.max_hp}")
                    return
                delay(1000)
            else:
                print("invalid choice")
                delay(1000)
    def fight(self, enemy) :
        while enemy.hp > 0 and self.player.hp > 0 and not self.escape:
            enemy.attack(self.player)
            delay(2000)
            if self.player.hp <= 0:
                return
            print(f"{self.player.name}'s HP: {round(self.player.hp,1)}/{self.player.max_hp}")
            delay(1500)
            print(f"{enemy.name}'s HP: {round(enemy.hp,1)}/{enemy.max_hp}")
            delay(500)
            self.actionMenu(enemy)
        if enemy.hp <= 0:
            self.player.gain_experience(enemy.experience_reward)
            self.player.gain_mince(enemy.mince_reward)
        self.escape = False
        enemy.hp = enemy.max_hp

    def NeutMenu(self):
        while True:
            if self.player.hp <= 0:
                print(f"{self.player.name} has perished in the adventure. Game Over.")
                return
            if gameOver:
                return
            print("-----Main Menu-----")
            print("1. Enhance Stats")
            print("2. Enter into Hostile Territories")
            choice = input()
            if choice == "1":
                self.openEnhanceMenu()
                break
            elif choice == "2":
                self.HostileTerritories()
            elif choice == "activatecheatmode":
                self.player.gain_magic_mince(100)
                self.player.gain_mince(100)
                self.player.strength += 50
                self.player.defense += 50
                self.player.max_hp += 180
                self.player.hp = self.player.max_hp
                print("Cheat mode activated!")
                delay(2000)

    def HostileTerritories(self):
        print("-----Hostile Territories-----")
        print("DL = Danger Level")
        print("1. Isle of Toothpicks. Contains Toothpicks(DL:1) and Skewers(DL:2)")
        print("2. Sauce Swamps. Contains Sauce Throwers(DL:3) and Spoons(DL:5)")
        print("3. Pasta Plains. Contains Spaghetti Wranglers(DL:6) and Rigatoni Trappers(DL:8)")
        print("4. Edge of the World. Contains Steely Forks(DL:10) and The Hands(DL:10+)")
        print("5. Return to Main Menu")
        print("Choose your destination:")
        choice = input()
        delay(1000)
        if choice == "1":
            territory = IsleOfToothpicks()
            print("Entering the Isle of Toothpicks...")
            delay(2000)
            territory.loop()
        elif choice == "2":
            territory = SauceSwamps()
            print("Entering the Sauce Swamps...")
            delay(2000)
            territory.loop()
        elif choice == "3":
            territory = PastaPlains()
            print("Entering the Pasta Plains...")
            delay(2000)
            territory.loop()
        elif choice == "4":
            territory = EdgeOfTheWorld()
            print("Entering the Edge of the World...")
            delay(2000)
            territory.loop()
        elif choice == "5":
            print("Returning to Main Menu...")
            delay(2000)
        else:
            print("Invalid choice. Returning to Main Menu...")
            delay(2000)
            
    def start(self):
        print(f"It has been 50 years since the invasion of the hands. \nHands came from the sky with steely forks, sharp skewers, jars of hot alfredo sauce, and dense nets of spaghetti. \n")
        delay(4000)
        print(
            f"{self.player.name} and his family were taken away to the world of pasta.\n"
            f"Once there, {self.player.name} and his family got seperated\n"
            f"and {self.player.name} has been left alone to fend for themselves.\n"
        )
        delay(5000)
        print(
            f"One day, while scavenging for food, {self.player.name} stumbles upon a mysterious glowing pile of minced meat.\n"
        )
        delay(2000)
        print("In this game you must make choices. Do you want to eat the meat(1) or leave it alone(2)?")
        eatchoice = input()
        delay(1500)
        if eatchoice == "2":
            print("this time your choice doesn't matter. You are eating the magical mince anyway.")
        delay(2000)
        self.player.gain_magic_mince(1)
        print(f"when {self.player.name} consumes magical mince, stats of their choosing are enhanced")
        delay(1500)
        print("Strength enhances attack power. Defense reduces damage taken, and improves the chance to dodge.\n Max HP is pretty self explanatory.")
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
        if self.player.hp > 0:
            print("Good job on winning your first fight! a Toothpick is the weakest enemy you'll face so be prepared.")
            delay(2000)
            print("After you get back from each adventure, your hp completely restores, and you can enhance your meatball's stats")
            delay(2000)
            print("Don't take stupid risks, because once you die, your meatball is dead forever.")
            delay(2000)
            print("Now, go forth and escape the clutches of the Hands!")
            self.player.hp = self.player.max_hp
        
        delay(2000)


    def mainLoop(self):
        while self.player.hp > 0 and not gameOver:
            self.NeutMenu()


print("Welcome to a Meatball Adventure! Please enter your meatball's name:")
name = input()
delay(1000)
player = meatball(name, 5, 20, 5)
game = MainLoop(player)
game.start()
game.mainLoop()