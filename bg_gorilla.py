wolf = "Wolf"
bear = "Bear"
lion = "Lion"
gorilla = "gorilla"

wolf_power = 3
bear_power = 4
lion_power = 5

wolf_damage = 100
bear_damage = 100
lion_damage = 100

gorilla_power = 50
gorilla_damage = 100

while True:
    print("1. Wolf")
    print("2. Bear")
    print("3. Lion")
    character = input("Choose Your Character ")
    if character == "1":
        character = wolf
        mp = wolf_power
        md = wolf_damage
        break

    if character == "2":
        character = bear
        mp = bear_power
        md = bear_damage
        break

    if character == "3":
        character = lion
        mp = lion_power
        md = lion_damage
        break

    else:
        print("Invalid Character! Choose again")
print(f"You have Chosen {character}! ")

while True:
    gorilla_damage = gorilla_damage - mp
    print(f"The {character} has damaged the Gorilla")
    print(f"The Gorilla Damage is now {gorilla_damage}")
    if gorilla_damage <= 0:
        print(f"The Gorilla has lost the battle! Great jod {character}")
        break
    md = md-gorilla_power
    print(f"The Gorilla has damged the {character}")
    print(f"The {character} Damage is now {md}")
    if md <= 0:
        print(f"The {character} has lost the battle")
        break
