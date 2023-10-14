from vikingsClasses import *
import random as rd
try:
    from art import *
    
    art = text2art("Viking war simulator")
    print(art)

except:
    print('-' * 15)
    print('VIKING WAR SIMULATOR')
    print('-' * 15)
    print('(!pip install art=6.1 to see a much cooler title)')

# create War

war = War()

# create Viking army

while True:
    try:
        nVikings = int(input("How many vikings: "))

        if (nVikings < 0) | (nVikings > 10):
            print("Please, enter a number between 1 and 10")
            print('-' * 15)
            continue

    except:
        print("Please, enter a number between 1 and 10")
        print('-' * 15)

    else:
        break

while True:
    conf = input("Would you like to name the vikings? [y/n]: ").lower()

    if (conf != 'y') & (conf != 'n'):
        print("Please, enter 'y' or 'n'")
        print('-' * 15)
        continue 

    elif conf == 'y':
        for i in range(nVikings):
            vName = input(f"Enter the name of viking number {i + 1}: ")

            if vName == '':
                vName = 'Sven'

        viking = Viking(vName, rd.randint(10, 100), rd.randint(10, 100))
        war.addViking(viking)

    else:
        for i in range(nVikings):
            viking = Viking(f"Sven {i + 1}", rd.randint(10, 100), rd.randint(10, 100))
            war.addViking(viking)
    
    break

# Create saxon army

while True:
    try:
        nSaxons = int(input("How many saxons: "))

        if (nSaxons < 0) | (nSaxons > 10):
            print("Please, enter a number between 1 and 10")
            print('-' * 15)
            continue

    except:
        print("Please, enter a number between 1 and 10")
        print('-' * 15)

    else:
        for i in range(nSaxons):
            saxon = Saxon(rd.randint(10, 100), rd.randint(10, 100))
            war.addSaxon(saxon)
        break

# war title

try:
    art = text2art("Fight!")
    print(art)
except:
    print('-' * 15)
    print('Let the fight begin!')
    print('-' * 15)

# war

round = 0

while True:
    print("-" * 15)
    print(f"Round {round}")
    print("-" * 15)
    
    if len(war.vikingArmy) != 0:
        v = war.vikingAttack()

    if len(war.saxonArmy) != 0:
        s = war.saxonAttack()
    
    print(v)
    print(s)

    print(war.showStatus())

    if (len(war.saxonArmy) == 0) | (len(war.vikingArmy) == 0):
        break

    else:
        round += 1