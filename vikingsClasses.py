
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
        Soldier.__init__(self,health,strength)
        self.name = name
        
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f'{self.name} has received {damage} points of damage'
        if self.health <= 0:
            return f'{self.name} has died in act of combat'   
    
    def battleCry(self):
        return "Odin Owns You All!"
    
# Saxon

class Saxon(Soldier):
   
    def __init__(self, health, strength):
        Soldier.__init__(self,health,strength)
    
    def receiveDamage(self,damage):
        self.health -= damage
        if self.health > 0:
            return f'A Saxon has received {damage} points of damage'
        if self.health <= 0:
            return f'A Saxon has died in combat'
    

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
        poor_sax = random.choice(self.saxonArmy)
        ind = self.saxonArmy.index(poor_sax)
        great_vik = random.choice(self.vikingArmy)
        s = poor_sax.receiveDamage(great_vik.attack())
        
        if poor_sax.health <= 0:
            self.saxonArmy.pop(ind)
        return s
    
    def saxonAttack(self):
        poor_vik = random.choice(self.vikingArmy)
        ind = self.vikingArmy.index(poor_vik)
        great_sax = random.choice(self.saxonArmy)
        s = poor_vik.receiveDamage(great_sax.attack())
        
       
        if poor_vik.health <= 0:
            self.vikingArmy.pop(ind)
        return s
    
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."       
    
