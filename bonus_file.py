from bonus_classes import Viking, Roman, War
import random 
import time
import sys

batalla = War(0)

character = "vikings"

# Viking and Roman names to choose in the creation of the soldiers
viking_names = ["Ragnar", "Erik", "Bjorn", "Leif", "Harald", "Olaf", "Gunnar", "Thorstein", "Sven", "Ivar", "Ulf", "Sigurd", "Haldor", "Einar", "Orm", "Knut", "Odd", "Hrothgar", "Valdimar", "Vili", "Grim", "Frode", "Birkir", "Torbjorn", "Stig""Astrid", "Freydis", 'Lageertha', 'Ingrid', "Thyra", "Runa", "Eir", "Brynhild", "Gudrun", "Sigrid", "Sif", "Thora", "Hilde", "Elin", "Solveig", "Aslaug", "Hervor", "Ragnhild", "Geirny", "Helga", "Alva", "Tora", "Jurunn", "Gisla", "Sunniva"]
roman_names = ["Julius", "Augustus", "Lucius", "Gaius", "Marcus", "Tiberius", "Quintus", "Maximus", "Antonius","Nero", "Cicero", "Cornelius", "Decimus", "Titus", "Flavius", "Hadrian", "Octavius", "Vespasian", "Aurelius", "Spartacus", "Valerius", "Severus", "Plinius", "Galerius", "Claudius","Julia", "Livia", "Claudia", "Octavia", "Aurelia", "Agrippina", "Cornelia", "Fulvia", "Sylvia", "Valeria", "Antonia", "Domitia", "Tullia", "Calpurnia", "Drusilla", "Pompeia", "Severa", "Vibia", "Acilia", "Vipsania", "Horatia", "Minucia", "Servilia", "Messalina"]

# Choose the size of the battlee
soldiers = int(input("How many soldiers must each army have: "))

# We add the "soldiers input into the armies"
for viking in range(soldiers):
    if viking < len(viking_names):
        v = Viking(random.choice(viking_names), random.randint(100, 200), random.randint(30, 60))
        batalla.addViking(v)

for roman in range(soldiers):
    if roman < len(roman_names):
        r = Roman(random.choice(roman_names), random.randint(100, 200), random.randint(30, 60))
        batalla.addRoman(r)

# Print the armies to the player
for i in batalla.vikingArmy:
    print(f'Viking (name: {i.name}, vida: {i.health}, ataque: {i.damage})')
print("\n")
for i in batalla.romanArmy:
    print(f'Roman (name: {i.name}, vida: {i.health}, ataque: {i.damage})')
print("\n")

while len(batalla.vikingArmy) >= 0 or len(batalla.romanArmy) >= 0:

    if len(batalla.romanArmy) <= 0:
        break
    elif len(batalla.vikingArmy) <= 0:
        break

    # Launch the counter of turns
    batalla.turn_count()

    # Decide who attacks first
    begin = random.randint(0, 1)

    if begin == 1:
        print("First, the Vikings attack:")
        result_viking = batalla.vikingAttack()
        print(result_viking)
        batalla.showStatus()
        print("Then, the Romans attack:")
        result_roman = batalla.romanAttack()
        print(result_roman)

    elif begin == 0:
        print("First, the Romans attack:")
        result_roman = batalla.romanAttack()
        print(result_roman)
        batalla.showStatus()
        print("Then, the Vikings attack:")
        result_viking = batalla.vikingAttack()
        print(result_viking)

    # Add a delay for readability
    time.sleep(1)

    batalla.showStatus()