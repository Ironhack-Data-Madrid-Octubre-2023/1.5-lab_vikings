#María Sanz Rocamora

import random

# Soldier


class Soldier:

    def __init__(self, health, strength,):
        self.health = health
        self.strength = strength

    def attack(self):
        return(self.strength)
    
    def receiveDamage(self, damage):
        self.health -= damage

# Viking


class Viking(Soldier):

    def __init__(self, name, health, strength):
        self.health = health
        self.strength = strength
        self.name = name

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return (f'{self.name} has received {damage} points of damage')
        else: 
            return (f'{self.name} has died in act of combat')
        
    def battleCry(self):
        return 'Odin Owns You All!'

# Saxon


class Saxon(Soldier):

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return (f'A Saxon has received {damage} points of damage')
        else:
            return(f'A Saxon has died in combat')


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
        Viking_random_1 = random.choice(self.vikingArmy)
        Saxon_random_1 = random.choice(self.saxonArmy)

        batalla_1 = Saxon_random_1.receiveDamage(Viking_random_1.strength) 

        if Saxon_random_1.health <= 0:
            self.saxonArmy.remove(Saxon_random_1)
        else:
            pass 
    
        return batalla_1
    
    def saxonAttack(self):
        Saxon_random_2 = random.choice(self.saxonArmy)
        Viking_random_2 = random.choice(self.vikingArmy)

        batalla_2 = Viking_random_2.receiveDamage(Saxon_random_2.strength)

        if Viking_random_2.health <= 0:
            self.vikingArmy.remove(Viking_random_2)
        else:
            pass

        return batalla_2
    
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return (f'Vikings have won the war of the century!')
        elif len(self.vikingArmy) == 0:
            return (f'Saxons have fought for their lives and survive another day...')
        else:
            return (f'Vikings and Saxons are still in the thick of battle.')