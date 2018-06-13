#The module for creating different items
class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects!")

    def __str__(self):
        return self.name

class Rock(Weapon):
    def __init__(self):
        self.name = "Rock"
        self.description = "A fist sized rock, suitable for bludgeoning."
        self.damage = 8

class Stick(Weapon):
    def __init__(self):
        self.name = "Stick"
        self.description = "Definitely not the most powerful or versatile weapon, but it's better than nothing."
        self.damage = 5

class Gold:
    def __init__(self, amount):
        self.amount = amount
        self.name = "Gold"
        self.description = "A piece of gold. It's worth around {}.".format(self.amount)

    def __str__(self):
        return self.name

class Consumable:

    def __init__(self):
        raise NotImplementedError("Don't create a raw consumable.")

class Apple(Consumable):

    def __init__(self):
        self.restore = 5


