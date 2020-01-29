import random

class Animal:
    hair_type = None
    life_esperance = None
    sound = None
    diet = None
    food = None
    weight = None

    def __init__(self, name):
        self.name = name
        self._age = random.randint(1,self.life_esperance)

    @property
    def age(self):
        return self._age

    def __repr__(self):
        return self.name

    def talk(self):
        if self.sound is None:
            raise Exception("Error, no sound")
        return self.sound

    def get_diet(self):
        if self.diet is None:
            raise Exception("Error, no diet list")
        return self.diet

    def eat(self, food):
        for foods in self.get_diet():
            if foods == food:
                return True
            return False




class Cat(Animal):
    sound = "miaou"
    diet = ["lait", "croquette"]
    life_esperance = 20
    weight = 4
    hair_type = "poil"


class Snail(Animal):
    sound = "chplokchplok"
    diet = ["feuille", "herbe"]
    life_esperance = 10
    weight = 1
    hair_type = "coquille"


class Snake(Animal):
    sound = "tsssssssssss"
    diet = ["souris", "rat"]
    life_esperance = 15
    weight = 2
    hair_type = "ecaille"


def main():
    cat = Cat("Chat")
    print("Age : '{}'".format(cat.age))
    print("Le chat parle : '{}'".format(cat.talk()))
    print("Le chat peut manger : {}".format(cat.get_diet()))
    food = "lait"
    print("Il a un poids de : '{}kg'".format(cat.weight))
    ate = cat.eat(food)
    if ate == True:
        print("Le chat a mangé '{}'".format(food))
        new_weight = cat.weight * 1.05
        print("Le chat a donc grossi, voici son nouveau poids : '{}kg'\n".format(new_weight))
    elif ate == False:
        print("Le chat n'a pas mangé '{}' puisque ça ne fait pas parti de la liste d'aliment\n".format(food))

    snail = Snail("Escargot")
    print("Age : '{}'".format(snail.age))
    print("L'escargot parle : '{}'".format(snail.talk()))
    print("L'escargot peut manger : {}".format(snail.get_diet()))
    food = "feuille"
    print("Il a un poids de : '{}kg'".format(snail.weight))
    ate = snail.eat(food)
    if ate == True:
        print("L'escargot a mangé '{}'".format(food))
        new_weight = snail.weight * 1.05
        print("L'escargot a donc grossi, voici son nouveau poids : '{}kg'\n".format(new_weight))
    elif ate == False:
        print("L'escargot n'a pas mangé '{}' puisque ça ne fait pas parti de la liste d'aliment\n".format(food))

    snake = Snake("Serpent")
    print("Age : '{}'".format(snake.age))
    print("Le serpent parle : '{}'".format(snake.talk()))
    print("Le serpent peut manger : {}".format(snake.get_diet()))
    food = "ggds"
    print("Il a un poids de : '{}kg'".format(snake.weight))
    ate = snake.eat(food)
    if ate == True:
        print("Le serpent a mangé '{}'".format(food))
        new_weight = snake.weight * 1.05
        print("Le serpent a donc grossi, voici son nouveau poids : '{}kg'".format(new_weight))
    elif ate == False:
        print("Le serpent n'a pas mangé '{}' puisque ça ne fait pas parti de la liste d'aliment".format(food))


if __name__ == "__main__":
    main()
