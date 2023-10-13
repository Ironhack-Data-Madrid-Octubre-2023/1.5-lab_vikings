
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

class Viking (Soldier):
     
     def __init__(self, name, health, strength):

        self.health = health
        self.strength = strength
        self.name = name

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

class Saxon (Soldier):

    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return (f"A Saxon has received {damage} points of damage")
        else:
            return ("A Saxon has died in combat")   

# War
import random

class War:

    def __init__(self):
        self.vikingArmy= []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        if self.saxonArmy:
            random_Vik = random.choice(self.vikingArmy)
            random_Sax = random.choice(self.saxonArmy)

            sax_rec_dam = random_Sax.receiveDamage(random_Vik.attack())

            if random_Sax.health <= 0:
                self.saxonArmy.remove(random_Sax)

            return sax_rec_dam

    def saxonAttack(self):
        if self.vikingArmy:
            random_Vik = random.choice(self.vikingArmy)
            random_Sax = random.choice(self.saxonArmy)

            vic_rec_dam = random_Vik.receiveDamage(random_Sax.attack())

            if random_Vik.health <= 0:
                self.vikingArmy.remove(random_Vik)

            return vic_rec_dam
        
    def showStatus(self):
        if not self.saxonArmy:
            return ("Vikings have won the war of the century!")
        
        elif not self.vikingArmy:
            return ("Saxons have fought for their lives and survive another day...")
        
        else:
            return ("Vikings and Saxons are still in the thick of battle.")