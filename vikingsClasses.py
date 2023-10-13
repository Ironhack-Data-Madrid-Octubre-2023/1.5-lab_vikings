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

    def __init__(self, name, health, strenght):

        self.name = name
        self.health = health
        self.strength = strenght

    def attack(self):
        return self.strength
    
    def battleCry(self):
        return "Odin Owns You All!"

    def receiveDamage(self, damage):

        self.health -= damage

        if self.health <= 0: # If viking's health is 0 or less
            return f"{self.name} has died in act of combat"
        
        else:
            return f"{self.name} has received {damage} points of damage"
    

# Saxon
class Saxon:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):

        self.health -= damage

        if self.health <= 0: # If health is 0 or less
            return "A Saxon has died in combat"
        else:
            return f"A Saxon has received {damage} points of damage"


# War
class War:

    def __init__(self):

        self.vikingArmy = []
        self.saxonArmy = []

    # Add a viking to the vikingArmy list
    def addViking(self, vik):
        self.vikingArmy.append(vik)

    # Add a saxon to the saxonArmy list
    def addSaxon(self, sax):
        self.saxonArmy.append(sax)

    # Find the strenght of a RANDOM viking, Select a RANDOM Saxon and apply it with Saxon.recievesDamage(x)
    def vikingAttack(self):

        chose_one = random.choice(self.saxonArmy)

        # 2. pick a random dmg from a viking
        rand_viking = random.choice(self.vikingArmy)
        rand_viking_dmg = rand_viking.strength

        result = chose_one.receiveDamage(rand_viking_dmg)


        if chose_one.health <= 0:
            self.saxonArmy.remove(chose_one)

        #should return result of calling receiveDamage() of a Saxon with the strength of a Viking
        return result

    # Find the strenght of a RANDOM viking, Select a RANDOM Saxon and apply it with Saxon.recievesDamage(x)
    def saxonAttack(self):

        chose_one_vik = random.choice(self.vikingArmy)

        # 2. pick a random dmg from a viking
        rand_sax = random.choice(self.saxonArmy)
        rand_sax_dmg = rand_sax.strength

        result = chose_one_vik.receiveDamage(rand_sax_dmg)


        if chose_one_vik.health <= 0:
            self.vikingArmy.remove(chose_one_vik)

        #should return result of calling receiveDamage() of a Saxon with the strength of a Viking
        return result
    
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy) > 0 and len(self.vikingArmy) >0:
            return "Vikings and Saxons are still in the thick of battle."