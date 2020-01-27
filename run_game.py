import characters

def selection_char():
    player_choice = input("\nChoisissez une classe de personnage avec laquelle vous voulez jouer "
                          "(M)agicien "
                          "(A)rcher "
                          "(G)uerrier : ").upper()
    return player_choice

def selection_target():
    attack_choice = input("Choisissez la classe de personnage que vous voulez attaquer "
                          "(M)agicien "
                          "(A)rcher "
                          "(G)uerrier : ").upper()
    return attack_choice

def show_health(wizard,archer,warrior):
    print("\nPoints de vie actuel:\n"
          "Magicien : {} "
          "Archer : {} "
          "Guerrier : {}".format(wizard.current_health, archer.current_health, warrior.current_health))

def attack_management(choice_char, wizard, archer, warrior):
    if choice_char == "M":
        print(wizard)
        attack = wizard.attack()
    elif choice_char == "A":
        print(archer)
        attack = archer.attack()
    else:
        print(warrior)
        attack = warrior.attack()
    weapon,points=attack
    print("\nAttaque avec l'arme '{}' et fait '{}' points de dégats".format(weapon,points))
    return attack

def defence_management(target_selected,attack,wizard,archer,warrior):
    weapon,points = attack
    if target_selected == "M":
        defend = wizard.defend(weapon, points)
    elif target_selected == "A":
        defend = archer.defend(weapon, points)
    else:
        defend = warrior.defend(weapon, points)
    print("\nPoints de vie restant : {}".format(defend))



def main():
    wizard = characters.Wizard("Gandalf")
    archer = characters.Archer("Legolas")
    warrior = characters.Warrior("Aragorn")
    print(wizard)
    print(archer)
    print(warrior)

    while (warrior.current_health > 0) and (wizard.current_health > 0) and (archer.current_health > 0):
        show_health(wizard, archer, warrior)
        choice_char = selection_char()
        while choice_char not in ["M","A","G"]:
            print("Choix non compris dans les possibilités")
            choice_char = selection_char()
        show_health(wizard, archer, warrior)
        target_selected = selection_target()
        while target_selected not in ["M","A","G"]:
            print("Choix non compris dans les possibilités")
            target_selected = selection_target()

        attack = attack_management(choice_char, wizard, archer, warrior)
        defence_management(target_selected,attack,wizard,archer,warrior)

if __name__ == '__main__':
    main()