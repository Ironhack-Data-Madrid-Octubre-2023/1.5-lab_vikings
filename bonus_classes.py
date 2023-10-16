import random 
import statistics as stat
import sys

# Soldier (Mother / Father)
class Soldier:
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage
    def attack(self):
        return self.damage
    def receiveDamage(self,damage):
        self.health -= damage

# Viking (Son / Daughter)

class Viking(Soldier):
    def __init__(self, name, health, damage):
        Soldier.__init__(self, health, damage)
        self.name = name

    def receiveDamage(self,damage):
        self.health = self.health - damage
        if self.health > 0:
            return f'{self.name} has received {damage} points of damage'
        else:
            return f'{self.name} has died in a heroic act of combat.'        
        
# Roman (Son / Daughter)        
class Roman(Soldier):
    def __init__(self, name, health, damage):
        super().__init__(health, damage)
        self.name = name
    
    def receiveDamage(self,damage):
        self.health = self.health - damage
        if self.health > 0:
            return f'{self.name} has received {damage} points of damage'
        else:
            return f'{self.name} has died in a heroic act of combat.'        
        
# War (grand)

class War:
    def __init__(self,turn):
        self.vikingArmy = []
        self.romanArmy = []
        self.turn = turn

    #Functions to append soldiers to the armies
    def addViking(self,Viking):
        self.vikingArmy.append(Viking)
    def addRoman(self,Roman):
        self.romanArmy.append(Roman)

    def turn_count(self):
        self.turn += 1
        print("----------------")
        print("Turn:",self.turn)

    def vikingAttack(self): 
        vik = random.choice(self.vikingArmy)
        rom = random.choice(self.romanArmy)

        # print("The one attacking: ")
        print(f'Viking attacker (name: {vik.name}, vida: {vik.health}, ataque: {vik.damage})')
        # print("The one receiving damage: ")
        print(f'Roman defender (name: {rom.name}, vida: {rom.health}, ataque: {rom.damage})')

        result = rom.receiveDamage(vik.damage)
        if rom.health <= 0:
            self.romanArmy.remove(rom)
            print(f"Roman attacker {rom.name} has been removed from battle")
        return result
        
    def romanAttack(self):
        vik = random.choice(self.vikingArmy)
        rom = random.choice(self.romanArmy)

        # print("The one attacking: ")
        print(f'Roman attacker (name: {rom.name}, vida: {rom.health}, ataque: {rom.damage})')
        # print("The one receiving damage: ")
        print(f'Viking defender (name: {vik.name}, vida: {vik.health}, ataque: {vik.damage})')
    
        result = vik.receiveDamage(rom.damage)
        if vik.health <= 0:
            self.vikingArmy.remove(vik)
            print(f"Viking attacker {vik.name} has been removed from battle")
        return result
    
    def showStatus(self):
        if  len(self.vikingArmy) == 0:
            print("The Roman army has emerged victorious.")
            sys.exit()
        if len(self.romanArmy) == 0:
            print("The Viking army has emerged victorious.")
            sys.exit()
        else:
            print( "Vikings and Romans are still in the thick of battle")