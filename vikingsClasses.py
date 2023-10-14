
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
        
        Soldier.__init__(self, health, strength)
        self.name = name
    
    def receiveDamage(self, damage):
        self.health -= damage

        if self.health > 0:
            return f'{self.name} has received {damage} points of damage'
        
        elif self.health <= 0:
            return f'{self.name} has died in act of combat'

    def battleCry(self):
        return ('Odin Owns You All!')


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

    def __init__(self):

        self.vikingArmy=[]
        self.saxonArmy=[]

    def addViking(self, Viking):

        self.vikingArmy.append(Viking)
   

    def addSaxon(self,Saxon):

        self.saxonArmy.append(Saxon)


    def vikingAttack(self):
                        
            random_viking = random.choice(self.vikingArmy)
            random_saxon = random.choice(self.saxonArmy)

            dmg_vk = random_saxon.receiveDamage(random_viking.attack())

            if random_saxon.health <= 0:
                self.saxonArmy.remove(random_saxon)

            return dmg_vk
    

    def saxonAttack(self):

            random_viking = random.choice(self.vikingArmy)
            random_saxon = random.choice(self.saxonArmy)

            dmg_sax = random_viking.receiveDamage(random_saxon.attack())

            if random_viking.health <= 0:
                self.vikingArmy.remove(random_viking)

            return dmg_sax


    def showStatus(self):

        if len(self.saxonArmy) == 0:
            return f'Vikings have won the war of the century!'
        
        elif len(self.vikingArmy) == 0:
            return f'Saxons have fought for their lives and survive another day...'
        
        elif len(self.vikingArmy) >=1 and len(self.saxonArmy) >= 1:
            return f'Vikings and Saxons are still in the thick of battle.'
