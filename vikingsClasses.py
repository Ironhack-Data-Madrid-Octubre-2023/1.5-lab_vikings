
# Soldier
import random

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

    def receiveDamage(self, damage): # Redefinimos el metodo para esta "hija"
        self.health -= damage
        if self.health > 0:
            return(f'{self.name} has received {damage} points of damage')
        elif self.health <= 0:
            return(f'{self.name} has died in act of combat')
    def battleCry(self):
        return('Odin Owns You All!')
    

# Saxon


class Saxon(Soldier): # Tiene que ser hija de Soldier para poder encontrar lo predefinido
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return(f'A Saxon has received {damage} points of damage')
        elif self.health <= 0:
            return(f'A Saxon has died in combat')
    

# War


class War:
    def __init__(self):
        self.vikingArmy = [] # Creo dos listas vacías donde ir appendeando
        self.saxonArmy = []

    def addViking(self, Viking):
        #self.Viking = Viking
        self.vikingArmy.append(Viking) #Appendeo un vikingo si llaman a la función
    
    def addSaxon(self, Saxon):
        #self.Saxon = Saxon
        self.saxonArmy.append(Saxon) #Appendeo un saxon si llaman a la función
    
    def vikingAttack(self):
        # Menos lioso si defino los random lists aparte - Me quedaba muy larga la llamada a la función sino
        random_viking = random.choice(self.vikingArmy) # He importado arriba el paquete random
        random_saxon = random.choice(self.saxonArmy)
        dmg = random_saxon.receiveDamage(random_viking.strength) # Llamo a la funcion para el saxon sacado al azar y le aplico la strength del vikingo sacado al azar

        # Importante que he tenido que asignar la llamada a la función a una variable porque sino, al hacer el return está ejecutando de nuevo la función y resta el health 2 veces en lugar de una

        if random_saxon.health <= 0: # Si la salud nueva del saxon es menor a cero le elimino de la lista
            self.saxonArmy.remove(random_saxon)
        return dmg # Y devuelvo el resultado de la llamada a la función para el saxon con la fuerza del vikingo
    
    def saxonAttack(self):
        random_viking = random.choice(self.vikingArmy)
        random_saxon = random.choice(self.saxonArmy)
        dmg = random_viking.receiveDamage(random_saxon.strength)

        # Importante que he tenido que asignar la llamada a la función a una variable porque sino, al hacer el return está ejecutando de nuevo la función y resta el health 2 veces en lugar de una

        if random_viking.health <= 0:
            self.vikingArmy.remove(random_viking)
        return dmg
    
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return ('Vikings have won the war of the century!')
        elif len(self.vikingArmy) == 0:
            return ('Saxons have fought for their lives and survive another day...')
        else: # No hace falta otro elif porque ya solo existe la opción de que los valores sean distintos de cero (si no entra en los otros dos elif quiere decir que la longitud de las listas es mayor que 0)
            return('Vikings and Saxons are still in the thick of battle.') 
