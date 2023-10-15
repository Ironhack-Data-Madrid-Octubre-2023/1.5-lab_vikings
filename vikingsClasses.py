
# Soldier
import random

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
    def battleCry(self):
        return "Odin Owns You All!"
    def receiveDamage(self, damage):
        self.health -= damage
        
        if self.health <= 0:
            return f"{self.name} has died in act of combat"
        
        else:
            return f"{self.name} has received {damage} points of damage"
            
# Saxon

class Saxon:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health -= damage
        
        if self.health <= 0:
            return f"A Saxon has died in combat"
        
        else:
            return f"A Saxon has received {damage} points of damage"


# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, vik):
        self.vikingArmy.append(vik)

    def addSaxon(self, sax):
        self.saxonArmy.append(sax)

    def vikingAttack(self):

        rand_sax = random.choice(self.saxonArmy)
        rand_viking = random.choice(self.vikingArmy)
        rand_vikin_dmg = rand_viking.strength
    
        result = rand_sax.receiveDamage(rand_vikin_dmg)

        if rand_sax.health <= 0:
            self.saxonArmy.remove(rand_sax)

        return result
    
    def saxonAttack(self):

        rand_viking2 = random.choice(self.vikingArmy)
        rand_sax2 = random.choice(self.saxonArmy)
        rand_sax2_dmg = rand_sax2.strength

        result = rand_viking2.receiveDamage(rand_sax2_dmg)

        if rand_viking2.health <= 0:
            self.vikingArmy.remove(rand_viking2)

        return result

    def showStatus(self):

        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."




        
