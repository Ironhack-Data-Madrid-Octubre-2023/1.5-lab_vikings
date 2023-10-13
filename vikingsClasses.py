
import random

# Soldier

class Soldier:
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength

    def attack(self):  
        return self.strength
    
    def receiveDamage(self, damage):
        self.health-=damage
    
# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        Soldier.__init__(self, health, strength)
        self.name=name
    
    #def attack(self): 
        #return Soldier.__init__(self.health, self.strength) # super(), es igual que llamar al padre directamente por si nombre

    def receiveDamage(self, damage):
        self.health-=damage
        if self.health>0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    
    def battleCry(self):
        return "Odin Owns You All!"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        Soldier.__init__(self, health, strength)

    #def attack(self): 
        #return Soldier.__init__(self.health, self.strength) 

    def receiveDamage(self, damage):
        self.health-=damage
        if self.health>0: 
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"

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
        rand_vik = random.choice(self.vikingArmy)
        rand_sax = random.choice(self.saxonArmy)

        dmg1 = rand_sax.receiveDamage(rand_vik.strength)

        if rand_sax.health <= 0:
            self.saxonArmy.remove(rand_sax)
        return dmg1

    def saxonAttack(self):
        rand_sax = random.choice(self.saxonArmy)
        rand_vik = random.choice(self.vikingArmy)

        dmg2 = rand_vik.receiveDamage(rand_sax.strength)

        if rand_vik.health <= 0:
            self.vikingArmy.remove(rand_vik)
        return dmg2

    def showStatus(self):
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."

#print(Soldier)
