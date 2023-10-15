
# Soldier

import random

class Soldier:
    
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health-=damage


# Viking


class Viking(Soldier):
    
    def __init__(self, name, health, strength):
        Soldier.__init__(self, health, strength)
        self.name = name


    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
        
    def battleCry(self):
        return "Odin Owns You All!"

    
        

# Saxon


class Saxon(Soldier):
    
    def __init__(self, health, strength):
        Soldier.__init__(self, health, strength)

    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

    
# War


class War:
    
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        random_v = random.choice(self.vikingArmy)
        random_s = random.choice(self.saxonArmy)

        dam1 = random_s.receiveDamage(random_v.strength)

        if random_s.health <= 0:
            self.saxonArmy.remove(random_s)
        return dam1

    def saxonAttack(self):
        random_s = random.choice(self.saxonArmy)
        random_v = random.choice(self.vikingArmy)

        dam2 = random_v.receiveDamage(random_s.strength)

        if random_v.health <= 0:
            self.vikingArmy.remove(random_v)
        return dam2

    def showStatus(self):
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
