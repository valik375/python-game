class Weapon:
    def __init__(self, weapon_name, damage, price):
        super().__init__()
        self.weapon_name = weapon_name
        self.damage = damage
        self.price = price

    def hit(self):
        pass


