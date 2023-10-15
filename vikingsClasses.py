
# Soldier
import random


class Soldier:
    def __init__(self,health,strength):
    
        self.health= health
        self.strength=strength
    
    def attack(self):

        return self.strength
    
    def receiveDamage(self,damage):
        self.health -= damage

# Viking


class Viking(Soldier):

    def __init__(self, name, health, strength):

        Soldier.__init__(self, health, strength)
        self.name=name

    def receiveDamage(self, damage):

        self.health -= damage
        if self.health > 0:
            return (f'{self.name} has received {damage} points of damage')
            
        elif self.health <= 0:
            return (f'{self.name} has died in act of combat')
     
    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon(Soldier):

    def __init__(self, health, strength):
        Soldier.__init__(self, health, strength)

    def receiveDamage(self, damage):

        self.health -= damage

        if self.health > 0:
            return(f'A Saxon has received {damage} points of damage')
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
        random_Saxon=random.choice(self.saxonArmy)
        random_Viking=random.choice(self.vikingArmy)
        resultado = random_Saxon.receiveDamage(random_Viking.strength)
        if random_Saxon.health <= 0:
            self.saxonArmy.remove(random_Saxon)
        return resultado

    def saxonAttack(self):
        random_Saxon=random.choice(self.saxonArmy)
        random_Viking=random.choice(self.vikingArmy)
        resultado = random_Viking.receiveDamage(random_Saxon.strength)
        if random_Viking.health <=0:
            self.vikingArmy.remove(random_Viking)
        return resultado
    
    def showStatus(self):
        if self.saxonArmy == []:
            return "Vikings have won the war of the century!"
        elif self.vikingArmy == []:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."