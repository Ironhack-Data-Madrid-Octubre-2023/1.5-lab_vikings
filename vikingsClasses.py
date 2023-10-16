
import random

# Soldier
class Soldier:
    def __init__ (self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
        
    def receiveDamage(self, damage):
        self.health -= damage
        

# Viking

class Viking (Soldier):
    def __init__ (self, name, health, strength):
        self.health= health
        self.strength= strength
        self.name= name

    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health -= damage
        
        if self.health >0: 
            return  f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
        
    def battleCry(self):
        return 'Odin Owns You All!'
    

# Saxon

class Saxon (Soldier):
    def __init__ (self, health, strenght):
        self.health= health
        self.strength= strenght

    def attack (self):
        return self.strength
    
    def receiveDamage(self, damage):

        self.health -= damage
    
        if self.health> 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"
    

# War

class War:
    def __init__ (self):
        self.vikingArmy= []
        self.saxonArmy= []
    
    def addViking(self, vik):
        self.vikingArmy.append(vik)

    def addSaxon(self, sax):
        self.saxonArmy.append(sax)

    def vikingAttack(self):
        vik = random.choice(self.vikingArmy)
        sax = random.choice(self.saxonArmy) 

        var = sax.receiveDamage(vik.attack())

        if sax.health <= 0:
            self.saxonArmy.remove(sax)

        return var
    
    def saxonAttack(self):
        vik = random.choice(self.vikingArmy)
        sax = random.choice(self.saxonArmy) 


        var = vik.receiveDamage(sax.attack())

        if vik.health <= 0 :
            self.vikingArmy.remove(vik)

        return var
    
    def showStatus(self):

        if len (self.saxonArmy) == 0:  
            return "Vikings have won the war of the century!"
        elif len (self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        
        elif len(self.saxonArmy) == 1 and len(self.vikingArmy) == 1:
            return "Vikings and Saxons are still in the thick of battle."
        
       
        



