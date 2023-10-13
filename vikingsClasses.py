
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

        War.__init__(self)

        self.saxonArmy.append(Saxon)


    def vikingAttack(self):
                        
            random_viking = random.choice(self.vikingArmy)
            random_saxon = random.choice(self.saxonArmy)

            damage = random_saxon.receiveDamage(random_viking.strength)

            if random_saxon.health <= 0:
                self.saxonArmy.remove(random_saxon)

            return damage
    

    def saxonAttack():



        pass

    def showStatus():

        pass
