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
    def __init__(self,name,health,strength):
        Soldier.__init__(self,health, strength)
        # self.health = health
        # self.strength = strength
        self.name = name

    def receiveDamage(self,damage):
        self.health = self.health - damage
        if self.health > 0:
            return f'{self.name} has received {damage} points of damage'
        else:
            return f'{self.name} has died in act of combat'

    def battleCry(self):
        return "Odin Owns You All!"
    
# Saxon

class Saxon(Soldier):
    def __init__(self,health,strength):
        self.health = health
        self.strength = strength
    
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return f'A Saxon has received {damage} points of damage'
        else:
            return 'A Saxon has died in combat'

# War

class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    #def vikingArmy(self):
        #return self.vikingArmy
    
    #def saxonArmy(self):
        #return self.saxonArmy
    
    def addViking(self,Viking):
        self.vikingArmy.append(Viking)
        
    def addSaxon(self,Saxon):
        self.saxonArmy.append(Saxon)
        
    def vikingAttack(self):
        Viking_random = random.choice(self.vikingArmy)
        Saxon_random = random.choice(self.saxonArmy)
        resultado = Saxon_random.receiveDamage(Viking_random.strength)
        if Saxon_random.health <= 0:
            self.saxonArmy.remove(Saxon_random)
        return resultado
    
    def saxonAttack(self):
        Viking_random = random.choice(self.vikingArmy)
        Saxon_random = random.choice(self.saxonArmy)
        resultado = Viking_random.receiveDamage(Saxon_random.strength)
        if Viking_random.health <= 0:
            self.vikingArmy.remove(Viking_random)
        return resultado
        
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return 'Vikings have won the war of the century!'
        elif len(self.vikingArmy) == 0:
            return 'Saxons have fought for their lives and survive another day...'
        elif len(self.vikingArmy) >= 1 or len(self.vikingArmy) >= 1:
            return 'Vikings and Saxons are still in the thick of battle.'