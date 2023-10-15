

# Soldier
import random as ra

class Soldier:
    def __init__(self,health,strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength
    
    def receiveDamage(self,damage):
        self.health -= damage
   
    pass

# Viking


class Viking(Soldier):
    def __init__(self,name,health,strength):
        self.name = name
        self.health = health
        self.strength = strength
    
    def receiveDamage(self,damage):
        self.health -= damage
   
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
            
          
        else:
            return f"{self.name} has died in act of combat"
            
    
    def battleCry(self):
        return "Odin Owns You All!"

        pass

# Saxon


class Saxon(Soldier):
    def __init__(self,health,strength):
        self.health = health
        self.strength = strength
    
    
    def receiveDamage(self,damage):
        self.health -= damage

        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
               
        else:
            return f"A Saxon has died in combat"
            

    pass

# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking(self,Viking):
        self.vikingArmy.append(Viking)
    
    def addSaxon(self,Saxon):
        self.saxonArmy.append(Saxon)
    
    def vikingAttack(self):
        chosen_Saxon = ra.choice(self.saxonArmy)
        chosen_Viking = ra.choice(self.vikingArmy)

        damage = chosen_Viking.attack()

        result = chosen_Saxon.receiveDamage(damage)

        if chosen_Saxon.health <= 0:
            self.saxonArmy.remove(chosen_Saxon)

        return result
        
    
    def saxonAttack(self):
        chosen_Viking = ra.choice(self.vikingArmy)
        chosen_Saxon = ra.choice(self.saxonArmy)

        damage = chosen_Saxon.attack()
        result = chosen_Viking.receiveDamage(damage)

        if chosen_Viking.health <= 0:
            self.vikingArmy.remove(chosen_Viking)

        return result
 
    
    def showStatus(self):
        
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
        

    pass
