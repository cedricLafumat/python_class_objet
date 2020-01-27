import characters

wizard = characters.Wizard("Gandalf")
archer = characters.Archer("Legolas")
warrior = characters.Warrior("Aragorn")
print(wizard)
print(archer)
print(warrior)

while (warrior.current_health > 0) and (wizard.current_health > 0) and (archer.current_health > 0):
    print(wizard)
    attack = wizard.attack()
    weapon,points=attack
    print("\nAttaque avec l'arme '{}' et fait '{}' points de dégats".format(weapon, points))
    attack_choice = input("Choisissez quel classe de personnage vous voulez attaquer : ").lower()
    if attack_choice == "wizard":
        defend = wizard.defend(weapon, points)
    elif attack_choice == "warrior":
        defend = warrior.defend(weapon, points)
    else:
        defend = archer.defend(weapon, points)
    print("\nPoints de vie restant : {}".format(defend))

    # print(archer)
    # attack = archer.attack()
    # weapon,points=attack
    # print("\nAttaque avec l'arme '{}' et fait '{}' points de dégats".format(weapon, points))
    # attack_choice = input("Choisissez quel classe de personnage vous voulez attaquer : ").lower()
    # if attack_choice == "wizard":
    #     defend = wizard.defend(weapon, points)
    # elif attack_choice == "warrior":
    #     defend = warrior.defend(weapon, points)
    # elif attack_choice == "archer":
    #     defend = archer.defend(weapon, points)
    # print("\nPoints de vie restant : {}".format(defend))
    #
    # print(warrior)
    # attack = warrior.attack()
    # weapon,points=attack
    # print("\nAttaque avec l'arme '{}' et fait '{}' points de dégats".format(weapon, points))
    # attack_choice = input("Choisissez quel classe de personnage vous voulez attaquer : ").lower()
    # if attack_choice == "wizard":
    #     defend = wizard.defend(weapon, points)
    # elif attack_choice == "warrior":
    #     defend = warrior.defend(weapon, points)
    # elif attack_choice == "archer":
    #     defend = archer.defend(weapon, points)
    # print("\nPoints de vie restant : {}".format(defend))
    #
    #
    #
