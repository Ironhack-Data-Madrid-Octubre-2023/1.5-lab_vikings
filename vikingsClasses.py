
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


class Saxon:
    pass

# War


class War:
    pass
