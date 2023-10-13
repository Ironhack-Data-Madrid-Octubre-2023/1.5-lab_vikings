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
        self.name = name
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        elif self.health <= 0:
            return f"{self.name} has died in act of combat"
        
    def battleCry(self):
        return "Odin Owns You All!"

# Saxon
class Saxon(Soldier):
        
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        elif self.health <= 0:
            return "A Saxon has died in combat"
            
# War
class War:

    # self.vikingArmy = []
    # self.saxonArmy = []

    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        receiveDamage = random.choice(self.vikingArmy).strength
        # receiveDamage = Viking.strength(Viking)
        random.choice(self.saxonArmy).damage -= receiveDamage
        self.saxonArmy -= 1
        return f"result of calling {receiveDamage} of a {Saxon} with the {Viking.strength} of a {Viking}"

    def saxonAttack(self):
        pass

# The `Saxon` version of `vikingAttack()`. A `Viking` receives the damage equal to the `strength` of a `Saxon`.

# - should be a function
# - should receive **0 arguments**
# - should make a `Viking` `receiveDamage()` equal to the `strength` of a `Saxon`
# - should remove dead vikings from the army
# - should return **result of calling `receiveDamage()` of a `Viking`** with the `strength` of a `Saxon`

# #### `showStatus()` method

# Returns the current status of the `War` based on the size of the armies.

# - should be a function
# - should receive **0 arguments**
# - **if the `Saxon` array is empty**, should return _**"Vikings have won the war of the century!"**_
# - **if the `Viking` array is empty**, should return _**"Saxons have fought for their lives and survive another day..."**_
# - **if there are at least 1 `Viking` and 1 `Saxon`**, should return _**"Vikings and Saxons are still in the thick of battle."**_
