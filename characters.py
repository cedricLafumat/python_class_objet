import random

class Wizard:
    def __init__(self,name):
        self.name = name
        self.max_health = 12
        self.current_health = self.max_health

    def attack(self):
        self.magic_dice = 12
        self.sword_dice = 8
        self.bow_dice = 10
        dice = [
            ["magic",random.randint(1,self.magic_dice)],
            ["sword",random.randint(1,self.sword_dice)],
            ["bow",random.randint(1,self.bow_dice)]
        ]
        sort = sorted(dice, key=lambda dice: dice[1], reverse=True)
        return sort[0]

    def defend(self,weapon,attack_points):
        defend_roll = 0
        loss_health = 0
        if weapon == "magic":
            defend_roll = random.randint(1,self.magic_dice)
        elif weapon == "sword":
            defend_roll = random.randint(1,self.sword_dice)
        elif weapon == "bow":
            defend_roll = random.randint(1,self.bow_dice)
        print("\nDéfense avec l'arme '{}' avec '{}' points".format(weapon,defend_roll))
        if attack_points > defend_roll:
            loss_health = attack_points - defend_roll
            self.current_health -= loss_health
            print("\nLa Défense à échouchée\nPerte de '{}' points de vie".format(loss_health))
        else:
            print("\nLa Défense à réussie\nPerte de '{}' points de vie".format(loss_health))
        return self.current_health

    def __repr__(self):
        return "{} the {}".format(self.name, self.__class__.__name__.lower())

# wizard = Wizard("Gandalf")
# print(wizard)