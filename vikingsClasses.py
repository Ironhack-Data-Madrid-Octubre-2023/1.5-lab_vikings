
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

    def receiveDamage(self, damage): # Redefinimos el metodo para esta "hija"
        self.health -= damage
        if self.health > 0:
            return(f'{self.name} has received {damage} points of damage')
        elif self.health <= 0:
            return(f'{self.name} has died in act of combat')
    def battleCry(self):
        return('Odin Owns You All!')
    

# Saxon


class Saxon(Soldier): # Tiene que ser hija de Soldier para poder encontrar lo predefinido
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return(f'A Saxon has received {damage} points of damage')
        elif self.health <= 0:
            return(f'A Saxon has died in combat')
    

# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        #self.Viking = Viking
        self.vikingArmy.append(Viking)
    
    def addSaxon(self, Saxon):
        #self.Saxon = Saxon
        self.saxonArmy.append(Saxon)
    
    def vikingAttack(self):
        # Menos lioso si defino los random aparte
        random_viking = random.choice(self.vikingArmy)
        random_saxon = random.choice(self.saxonArmy)
        random_saxon.receiveDamage(random_viking.strength)

        if random_saxon.health <= 0:
            self.saxonArmy.remove(random_saxon)
        return random_saxon.receiveDamage(random_viking.strength)
    
    def saxonAttack(self):
        random_viking = random.choice(self.vikingArmy)
        random_saxon = random.choice(self.saxonArmy)
        random_viking.receiveDamage(random_saxon.strength)

        if random_viking.health <= 0:
            self.vikingArmy.remove(random_viking)
        return random_viking.receiveDamage(random_saxon.strength)
    
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return ('Vikings have won the war of the century!')
        elif len(self.vikingArmy) == 0:
            return ('Saxons have fought for their lives and survive another day...')
        elif len(self.saxonArmy) >= 1 and len(self.vikingArmy) >= 1:
            return('Vikings and Saxons are still in the thick of battle.') 
