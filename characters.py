import random

class Characters:
    max_health = 12

    def attack(self):
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
            print("\nLa Défense à échouée\nPerte de '{}' points de vie".format(loss_health))
        else:
            print("\nLa Défense à réussie\nPerte de '{}' points de vie".format(loss_health))
        return self.current_health

    def __repr__(self):
        return "{} the {}".format(self.name, self.__class__.__name__.lower())


class Wizard(Characters):
    magic_dice = 12
    sword_dice = 8
    bow_dice = 10

    def __init__(self,name):
        self.name = name
        self.current_health = self.max_health

    def attack(self):
        attack = super().attack()
        weapon, points = attack
        print("\nLancé 1 : {}".format(attack))
        throw2 = ["magic", random.randint(1, self.magic_dice)]
        print("Lancé 2 : {}".format(throw2))
        if throw2[1] >= points:
            return throw2
        return attack

class Archer(Characters):
    magic_dice = 10
    sword_dice = 8
    bow_dice = 12

    def __init__(self, name):
        self.name = name
        self.current_health = self.max_health

    def attack(self):
        attack = super().attack()
        weapon,points=attack
        print(points)
        if weapon in ["sword","magic"]:
            points += 1
            print(points)
        return [weapon,points]


class Warrior(Characters):
    magic_dice = 8
    sword_dice = 12
    bow_dice = 10
    max_health = 16

    def __init__(self, name):
        self.name = name
        self.current_health = self.max_health