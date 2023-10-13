import random
from vikingsClasses import Viking, Saxon, War

# Create random teams of Vikings and Saxons
def create_teams(num_vikings, num_saxons):
    viking_team = [Viking(f"Viking-{i}", random.randint(50, 100), random.randint(10, 30)) for i in range(num_vikings)]
    saxon_team = [Saxon(random.randint(50, 100), random.randint(10, 30)) for i in range(num_saxons)]
    return viking_team, saxon_team

# Simulate the battle
def simulate_battle(viking_team, saxon_team):
    war = War()
    for viking in viking_team:
        war.addViking(viking)
    for saxon in saxon_team:
        war.addSaxon(saxon)

    while war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
        if random.choice([True, False]):
            result = war.vikingAttack()
        else:
            result = war.saxonAttack()
        print(result)

    return war.showStatus()

if __name__ == "__main__": 
    num_vikings = 5  # Number of Vikings
    num_saxons = 5   # Number of Saxons

    viking_team, saxon_team = create_teams(num_vikings, num_saxons)

    print("Teams created:")
    for viking in viking_team:
        print(f"{viking.name} (Viking) - Health: {viking.health}, Strength: {viking.strength}")
    for saxon in saxon_team:
        print(f"A Saxon was created: - Health: {saxon.health}, Strength: {saxon.strength}")

    result = simulate_battle(viking_team, saxon_team)
    print("\nBattle result:", result)
