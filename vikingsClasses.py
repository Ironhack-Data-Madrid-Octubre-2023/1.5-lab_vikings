
#Import libraries 
import random 


# Soldier


class Soldier:
    def __init__(self,health,strength):
    
    #attributes
        self.health=health
        self.strength=strength

    #methods
    def attack(self):
        return self.strength

    def receiveDamage(self,damage):
        self.health -= damage

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
    
    #attributes
        self.name=name
        self.health=health
        self.strength=strength

    #methods
    #will inherit attack() from Soldier

    def receiveDamage(self,damage):
        self.health -= damage
        if self.health > 0:
            return f'{self.name} has received {damage} points of damage' 
        else: 
            return f'{self.name} has died in act of combat'
        
    def battleCry(self):
        return 'Odin Owns You All!'

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
    
    #attributes
        self.health=health
        self.strength=strength

    #methods
    #will inherit attack() from Soldier

    def receiveDamage(self, damage):
        self.health -= damage 
        if self.health > 0:
            return f'A Saxon has received {damage} points of damage'
        else:
            return 'A Saxon has died in combat'
            

# War


class War:
    def __init__(self):
    
    #attributes 
        self.vikingArmy = []
        self.saxonArmy = []
        
    #methods

    def addViking(self,viking):
        self.vikingArmy.append(viking)

    def addSaxon(self,saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        if self.saxonArmy: #saxon army not empty
            
            random_saxon = random.choice(self.saxonArmy) #pick random saxon 
            random_viking = random.choice(self.vikingArmy) #pick random viking 

            result = random_saxon.receiveDamage(random_viking.strength) #equal damage of random saxon to strength of random viking

            self.saxonArmy = [saxon for saxon in self.saxonArmy if saxon.health >0]

            return result 

        else:
            print('Saxon army is empty. Sorry Vikings!')

    def saxonAttack(self): 
        if self.vikingArmy: #viking army is not empty 

            random_viking = random.choice(self.vikingArmy) #pick a random viking
            random_saxon = random.choice(self.saxonArmy) #pick a random saxon 

            result = random_viking.receiveDamage(random_saxon.strength) 

            self.vikingArmy = [viking for viking in self.vikingArmy if viking.health >0]

            return result
        
        else: 
            print('Viking army is empty. Sorry Saxons!')


    def showStatus(self):
        if not self.saxonArmy: #list is empty 
            return 'Vikings have won the war of the century!'
        elif not self.vikingArmy: #list is empty 
            return 'Saxons have fought for their lives and survive another day...'
        else: 
            return 'Vikings and Saxons are still in the thick of battle.'


