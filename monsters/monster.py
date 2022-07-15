from random import randint


class Monster:

    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.damage = 10 * self.level * 0.4
        self.hit_points = 10 * self.level * 10
        self.experience = 100 * self.level
        self.money = 10 * self.level * 1.2
        self.monster_dialogs = ['На тобi КУРВА!', 'Отримуй!', 'Джета топ!', 'Получай!']

    def hit(self):
        print(f'{self.monster_dialogs[int(randint(0, 3))]}')
        return self.damage

    def get_damage(self, damage_value):
        if self.hit_points <= int(damage_value):
            self.hit_points = 0
            print(f'{self.name} RIP')
        else:
            self.hit_points -= int(damage_value)

    def drop_experience(self):
        return self.experience

    def drop_money(self):
        return self.money
