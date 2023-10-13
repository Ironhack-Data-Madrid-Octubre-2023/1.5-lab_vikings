
# Soldier

class Soldier:
    def __init__(self, health, strength):

        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health -= damage

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        
        self.name = name
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return (f"{self.name} has received {damage} points of damage")
        else:
            return (f"{self.name} has died in act of combat")

    def battleCry(self):
        return "Odin Owns You All!"
        
# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):

        self.health = health
        self.strength = strength

    def receiveDamage(self, damage):
        self.health -= damage

        if self.health > 0:
            return (f"A Saxon has received {damage} points of damage")
        else:
            return "A Saxon has died in combat"
        
# War

import random

class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking(self, vik):
        self.vikingArmy.append(vik)
    
    def addSaxon(self, sax):
        self.saxonArmy.append(sax)

    def vikingAttack(self):
        random_Viking = random.choice(self.vikingArmy)
        random_Saxon = random.choice(self.saxonArmy)

        Saxon_receive_damage = random_Saxon.receiveDamage(random_Viking.attack())

        if random_Saxon.health <= 0:
            self.saxonArmy.remove(random_Saxon)
        return Saxon_receive_damage

    def saxonAttack(self):
        random_Viking = random.choice(self.vikingArmy)
        random_Saxon = random.choice(self.saxonArmy)

        Viking_receive_damage = random_Viking.receiveDamage(random_Saxon.attack())

        if random_Viking.health <= 0:
            self.vikingArmy.remove(random_Viking)
        return Viking_receive_damage
    
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."