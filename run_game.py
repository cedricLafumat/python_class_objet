import characters

def selection_char():
    race_choice = input("\nChoisissez une race de personnage avec laquelle vous voulez jouer "
                          "(E)lfe "
                          "(N)ain : ").upper()
    char_choice = input("\nChoisissez une classe de personnage avec laquelle vous voulez jouer "
                          "(M)agicien "
                          "(A)rcher "
                          "(G)uerrier : ").upper()
    player_choice = race_choice+char_choice
    return player_choice

def selection_target():
    race_attack_choice = input("Choisissez la race de personnage que vous voulez attaquer "
                          "(E)lfe "
                          "(N)ain : ").upper()
    char_attack_choice = input("Choisissez la classe de personnage que vous voulez attaquer "
                          "(M)agicien "
                          "(A)rcher "
                          "(G)uerrier : ").upper()
    return race_attack_choice+char_attack_choice

def show_health(elfewizard, dwarfwizard, elfearcher, dwarfarcher, elfewarrior, dwarfwarrior):
    print("\nPoints de vie actuel:\n"
          "ElfeMage : {} / "
          "NainMage : {} / "
          "ElfeArcher : {} / "
          "NainArcher : {} / "
          "ElfeGuerrier : {} / "
          "NainGuerrier : {}".format(elfewizard.current_health, dwarfwizard.current_health, elfearcher.current_health,
                                 dwarfarcher.current_health, elfewarrior.current_health, dwarfwarrior.current_health))

def attack_management(choice_char, elfewizard, dwarfwizard, elfearcher, dwarfarcher, elfewarrior, dwarfwarrior):
    if choice_char == "EM":
        print(elfewizard)
        attack = elfewizard.attack()
    elif choice_char == "NM":
        print(dwarfwizard)
        attack = dwarfwizard.attack()
    elif choice_char == "EA":
        print(elfearcher)
        attack = elfearcher.attack()
    elif choice_char == "NA":
        print(dwarfarcher)
        attack = dwarfarcher.attack()
    elif choice_char == "EG":
        print(elfewarrior)
        attack = elfewarrior.attack()
    else:
        print(dwarfwarrior)
        attack = dwarfwarrior.attack()
    weapon,points=attack
    print("\nAttaque avec l'arme '{}' et fait '{}' points de dégats".format(weapon,points))
    return attack

def defence_management(target_selected, attack, elfewizard, dwarfwizard, elfearcher, dwarfarcher, elfewarrior, dwarfwarrior):
    weapon,points = attack
    if target_selected == "EM":
        defend = elfewizard.defend(weapon, points)
    elif target_selected == "NM":
        defend = dwarfwizard.defend(weapon, points)
    elif target_selected == "EA":
        defend = elfearcher.defend(weapon, points)
    elif target_selected == "NA":
        defend = dwarfarcher.defend(weapon, points)
    elif target_selected == "EG":
        defend = elfewarrior.defend(weapon, points)
    else:
        defend = dwarfwarrior.defend(weapon, points)
    print("\nPoints de vie restant : {}".format(defend))



def main():
    elfewizard = characters.ElfeWizard("Galadriel")
    dwarfwizard = characters.DwarfWizard("Toto")
    elfearcher = characters.ElfeArcher("Legolas")
    dwarfarcher = characters.DwarfArcher("Tutu")
    elfewarrior = characters.ElfeWarrior("Tete")
    dwarfwarrior = characters.DwarfWarrior("Gimli")
    print(elfewizard)
    print("Taille : {}cm / Poids : {}kg\n".format(elfewizard.height,elfewizard.weight))
    print(dwarfwizard)
    print("Taille : {}cm / Poids : {}kg\n".format(dwarfwizard.height,dwarfwizard.weight))
    print(elfearcher)
    print("Taille : {}cm / Poids : {}kg\n".format(elfearcher.height,elfearcher.weight))
    print(dwarfarcher)
    print("Taille : {}cm / Poids : {}kg\n".format(dwarfarcher.height, dwarfarcher.weight))
    print(elfewarrior)
    print("Taille : {}cm / Poids : {}kg\n".format(elfewarrior.height, elfewarrior.weight))
    print(dwarfwarrior)
    print("Taille : {}cm / Poids : {}kg".format(dwarfwarrior.height, dwarfwarrior.weight))

    while (elfewizard.current_health > 0) and (dwarfwizard.current_health > 0) and (elfearcher.current_health > 0)\
        and (dwarfarcher.current_health > 0) and (elfewarrior.current_health > 0) and (dwarfwarrior.current_health > 0):
        show_health(elfewizard, dwarfwizard, elfearcher, dwarfarcher, elfewarrior, dwarfwarrior)
        choice_char = selection_char()
        while choice_char not in ["EM","NM","EA","NA","EG","NG"]:
            print("Choix non compris dans les possibilités")
            choice_char = selection_char()
        show_health(elfewizard, dwarfwizard, elfearcher, dwarfarcher, elfewarrior, dwarfwarrior)
        target_selected = selection_target()
        while target_selected not in ["EM","NM","EA","NA","EG","NG"]:
            print("Choix non compris dans les possibilités")
            target_selected = selection_target()

        attack = attack_management(choice_char, elfewizard, dwarfwizard, elfearcher, dwarfarcher, elfewarrior, dwarfwarrior)
        defence_management(target_selected, attack, elfewizard, dwarfwizard, elfearcher, dwarfarcher, elfewarrior, dwarfwarrior)

if __name__ == '__main__':
    main()