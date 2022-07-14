class Enemy:

    def __init__(self, name, health_points, level):
        self.name = name
        self.health_points = health_points
        self.level = level
        self.damage = self.level * 50
        self.loot_price = self.damage // 2
        self.loot_experience = self.level * 100

    def get_info(self):
        print(f'{self.name} | {self.health_points}hp | {self.level}lvl | {self.damage} damage | {self.loot_price}$ | {self.loot_experience} exp')


class Boss(Enemy):
    def get_super_loot(self):
        self.loot_price = self.damage * 10
        return self.loot_price


enemy1 = Enemy('S', 50, 1)
enemy2 = Enemy('W', 60, 2)
enemy3 = Enemy('I', 70, 3)
enemy4 = Enemy('P', 80, 4)
boss = Boss('E', 1000, 5)

enemy1.get_info()
enemy2.get_info()
enemy3.get_info()
enemy4.get_info()
boss.get_info()



