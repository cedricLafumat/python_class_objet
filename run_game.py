import characters

wizard = characters.Wizard("Gandalf")
archer = characters.Archer("Legolas")
warrior = characters.Warrior("Aragorn")
print(wizard)
print(archer)
print(warrior)

while (warrior.current_health > 0) and (wizard.current_health > 0) and (archer.current_health > 0):
    player_choice = input("\nChoisissez une classe de personnage avec laquelle vous voulez jouer "
                          "(M)agicien "
                          "(A)rcher "
                          "(G)uerrier : ").upper()
    if player_choice == "M":
        print(wizard)
        attack = wizard.attack()
    elif player_choice ==  "A":
        print(archer)
        attack = archer.attack()
    elif player_choice == "G":
        print(warrior)
        attack = warrior.attack()
    weapon,points=attack
    print("\nAttaque avec l'arme '{}' et fait '{}' points de dégats".format(weapon, points))
    print("\nPoints de vie actuel:\n"
          "Magicien : {} "
          "Archer : {} "
          "Guerrier : {}".format(wizard.current_health, archer.current_health, warrior.current_health))
    attack_choice = input("Choisissez la classe de personnage que vous voulez attaquer "
                          "(M)agicien "
                          "(A)rcher "
                          "(G)uerrier : ").upper()
    if attack_choice == "M":
        defend = wizard.defend(weapon, points)
    elif attack_choice == "G":
        defend = warrior.defend(weapon, points)
    elif attack_choice == "A":
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
