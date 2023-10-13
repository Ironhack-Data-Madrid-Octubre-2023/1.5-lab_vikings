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

    def __init__(self, name):
        
        self.name = name
        
        
    def receiveDamage(self, damage):
        if self.health > 0:
            self.health = self.health - damage

        elif self.health == 0:
            return (f'{self.name} has died in act of combat')
    


    def battleCry(self):
        return ("Odin Owns You All!")


    

# Saxon


class Saxon(Soldier):

    def receiveDamage(self, damage):
        
        if self.health > damage:
            self.health = self.health - damage
            
            return (f'A Saxon has received {damage} points of damage')
        
        elif self.health <= damage:
            return ('A Saxon has died in combat')





# War


vikingArmy = []
saxonArmy = []

class War():
    
    
    def __init__(self):
        vikingArmy.append([])
        saxonArmy.append([])

    def addViking(self, Viking):
        for place in vikingArmy:
            vikingArmy.append(Viking)


    def addSaxon(self, Saxon):
        for place in saxonArmy:
            saxonArmy.append(Saxon)

    def vikingAttack(self):
        saxon = random.choice(saxonArmy)

    def saxonAttack():
        pass

    def showStatus():
        pass
    
