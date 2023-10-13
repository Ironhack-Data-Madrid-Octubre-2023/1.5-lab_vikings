
# Soldier
from ast import Pass
from curses import nocbreak
from msilib.schema import SelfReg
from os import lstat, name
from typing import Self


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    def attack(self):
        return self.strength
    def receiveDamage(self, damage):
        self.health -= damage
    pass

# Viking


class Viking (Soldier):
    def __init__(self, name ,  health , strength ):
        self.name=name
        self.health=health
        self.strength=strength
        
            

    def receiveDamage (self,damage):
        self.health -= damage

        if self.health > 0:
            return f'{self.name} has received {damage} points of damage'
        else:
            return f'{self.name} has died in act of combat'

        

    def battleCry(self):
        
        return 'Odin Owns You All!'

    pass

# Saxon


class Saxon(Soldier):
     def __init__(self,  health , strength ):
        self.health=health
        self.strength=strength
              

     def receiveDamage (self,damage):
        self.health -= damage
        if self.health > 0:
            return f'A Saxon has received {damage} points of damage'
        else:
            return f"A Saxon has died in combat"

        
pass

# War


class War ():
    def __init__ (self):
        self.vikingArmy=[]
        self.saxonArmy=[]

    def addViking (self):
        self.vikingArmy.append()

    def addSaxon(self):
        self.saxonArmy.append()

    
    def vikingAttack():
            

        def receiveDamage ():
            pass
