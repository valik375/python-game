class Enemy:

    def __init__(self, name, health_points, level, damage, loot):
        self.name = name
        self.health_points = health_points
        self.level = level
        self.damage = damage
        self.loot = loot

    def get_loot(self):
        return self.loot * 2


class Boss(Enemy):
    pass

