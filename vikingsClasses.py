import random

# Soldier

class Soldier:
    
    def __init__(self, health, strength):
        self.health = health 
        self.strength = strength

    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health -= damage    # Aqui remueve damage de health, es decir, le quita vida 


# Viking


class Viking(Soldier): 
    def __init__(self, name, health, strength):
        Soldier.__init__(self, health, strength)
        self.name = name 

    def receiveDamage(self,damage):
        self.health -= damage 
        if self.health > damage: 
            return f"{self.name} has received {damage} points of damage"
        elif self.health <= 0:
            return f"{self.name} has died in act of combat"
    
    def battleCry(self):
        return "Odin Owns You All!"


# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        Soldier.__init__(self, health, strength)
        self.health = health 
        self.strength = strength
    
    def receiveDamage(self,damage):
        self.health -= damage    # Aqui remueve damage de health, es decir, le quita vida 
        if self.health > 0: 
            return f"A Saxon has received {damage} points of damage"
        else: 
            self.health <= 0
            return f"A Saxon has died in combat"
    

# War


class War:

    def __init__(self):
        # atributos (datos)
        self.vikingArmy = []
        self.saxonArmy = []
    

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        if self.saxonArmy:
            rand_Sax = random.choice(self.saxonArmy)
            rand_Vik = random.choice(self.vikingArmy)
            damage = Viking.attack()
            result = Saxon.receiveDamage(damage)
            if Saxon.health <= 0:
                self.saxonArmy.remove(Saxon)
            return result
        
    def saxonAttack(self):
        if self.vikingArmy:
            rand_Sax = random.choice(self.saxonArmy)
            rand_Vik = random.choice(self.vikingArmy)
            damage = Saxon.attack()
            result = Viking.receiveDamage(damage)
            
            if rand_Vik.health <=0:
                self.vikingArmy.remove(rand_Vik)
        
    def showStatus(self):
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."



