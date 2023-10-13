
import random

def not0fun (x):
        return x.health > 0

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
        Soldier.__init__(self, health, strength)
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f'{self.name} has received {damage} points of damage'
        elif self.health <= 0:
            return f'{self.name} has died in act of combat'
            
    def battleCry(self):
        return f'Odin Owns You All!'
    
# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        Soldier.__init__(self, health, strength)
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f'A Saxon has received {damage} points of damage'
        elif self.health <= 0:
            return f'A Saxon has died in combat' 

# War
class War:
    def __init__(self) :
        self.vikingArmy = [ ]
        self.saxonArmy = [ ]

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
        
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):

        thesaxon = self.saxonArmy[random.randint(0,len(self.saxonArmy)-1)]
        theviking = self.vikingArmy[random.randint(0,len(self.vikingArmy)-1)]

        result = thesaxon.receiveDamage(theviking.attack())
        self.saxonArmy=list(filter(not0fun, self.saxonArmy))
        return result

    
    def saxonAttack(self):

        thesaxon = self.saxonArmy[random.randint(0,len(self.saxonArmy)-1)]
        theviking = self.vikingArmy[random.randint(0,len(self.vikingArmy)-1)]

        result=theviking.receiveDamage(thesaxon.attack())
        self.vikingArmy=list(filter(not0fun, self.vikingArmy))
        return result

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return f'Vikings have won the war of the century!'        
        if len(self.vikingArmy) == 0:
            return f'Saxons have fought for their lives and survive another day...'
        else:
            return f'Vikings and Saxons are still in the thick of battle.'
        