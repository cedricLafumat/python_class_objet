import characters

wizard = characters.Wizard("Gandalf")
attack = wizard.attack()
weapon,points=attack
print("\nAttaque avec l'arme '{}' et fait '{}' points de dégats".format(weapon, points))
defend=wizard.defend(weapon,points)
print("\nPoints de vie restant : {}".format(defend))