class Weapon:

    def __init__(self, name, damage, stamina, price):
        self.name = name
        self.damage = damage
        self.stamina = stamina
        self.price = price

    def hit(self):
        return self.damage


class Axe(Weapon):
    pass


class Sword(Weapon):
    pass

