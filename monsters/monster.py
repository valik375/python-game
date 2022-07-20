class Monster:

    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.damage = 10 * self.level * 0.4
        self.hit_points = 100 * self.level * 0.6
        self.experience = 100 * self.level
        self.money = 10 * self.level * 1.2
        self.dialogs = ['На тобi КУРВА!', 'Отримуй!', 'Джета топ!', 'Получай!']

    def get_damage(self, damage_value):
        if self.hit_points <= int(damage_value):
            self.hit_points = 0
            print(f'{self.name} RIP')
        else:
            self.hit_points -= int(damage_value)
