
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
    def __init__(self, name, health, strenght):
    
    #attributes
        self.name=name
        self.health=health
        self.strength=strenght

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
        if self.saxonArmy: #army not empty
            
            random_saxon = random.choice(self.saxonArmy) #pick random saxon 
            random_viking = random.choice(self.vikingArmy) #pick random viking 

            result = random_saxon.receiveDamage(random_viking.strength) #equal damage of random saxon to strenght of random viking

            self.saxonArmy = [saxon for saxon in self.saxonArmy if saxon.health >0]

        else:
            print('Saxon army is empty. Sorry Vikings')
