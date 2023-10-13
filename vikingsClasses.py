import random
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
            return f"{self.name} has received {damage} points of damage"
        elif self.health <= 0:
            return f"{self.name} has died in act of combat"
        
    def battleCry(self):
        return "Odin Owns You All!"

# Saxon
class Saxon(Soldier):
        
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        elif self.health <= 0:
            return "A Saxon has died in combat"
            
# War
class War:

    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        randomViking = random.choice(self.vikingArmy)
        randomSaxon = random.choice(self.saxonArmy)
        vikingAtt = randomSaxon.receiveDamage(randomViking.attack())
        if randomSaxon.health <= 0:
            self.saxonArmy.remove(randomSaxon)
        return vikingAtt

    def saxonAttack(self):
        randomViking = random.choice(self.vikingArmy)
        randomSaxon = random.choice(self.saxonArmy)
        saxonAtt = randomViking.receiveDamage(randomSaxon.attack())
        if randomViking.health <= 0:
            self.vikingArmy.remove(randomViking)
        return saxonAtt

    def showStatus(self):
        for viking in self.vikingArmy:
            if viking.health <= 0:
                self.vikingArmy.remove(viking)
        
        for saxon in self.saxonArmy:
            if saxon.health <= 0:
                self.saxonArmy.remove(saxon)

        if self.saxonArmy == []:
            return "Vikings have won the war of the century!"
        elif self.vikingArmy == []:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."