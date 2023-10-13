
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
        Soldier.__init__(self, health, strength)
        self.name = name
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
        
    def battleCry(self):
        return f"Odin Owns You All!"


# Saxon

class Saxon(Soldier):

    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"
        


# War
import random
class War:

    def __init__(self):
        self.vikingArmy= []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        
        random_viking = random.choice(self.vikingArmy)  
        random_saxon = random.choice(self.saxonArmy)    

        damage = random_viking.strength
        result = random_saxon.receiveDamage(damage) 

        if random_saxon.health <= 0:
            self.saxonArmy.remove(random_saxon)  

        return result

    def saxonAttack(self):
        random_saxon = random.choice(self.saxonArmy)  
        random_viking = random.choice(self.vikingArmy)

        damage = random_saxon.strength
        result = random_viking.receiveDamage(damage)

        if random_viking.health <= 0:
            self.vikingArmy.remove(random_viking) 
        
        return result
    

    def showStatus(self):
        if not self.saxonArmy:
            return f'Vikings have won the war of the century!'
        elif not self.vikingArmy:
            return f'Saxons have fought for their lives and survive another day...'
        elif self.saxonArmy and self.vikingArmy:
            return f'Vikings and Saxons are still in the thick of battle.'







pass

