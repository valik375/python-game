class Hero:
    def __init__(self, name, money, right_hand_weapon):
        self.name = name
        self.level = 1
        self.next_level_experience = 100
        self.experience = 0

        self.strengths = 10
        self.max_hit_points = self.strengths * 10
        self.hit_points = self.strengths * 10

        self.money = money
        self.right_hand_weapon = right_hand_weapon

        self.attacks = [
            {
                'name': 'Нести бред',
                'damage': 10
            },
            {
                'name': 'Перекур',
                'damage': 10
            },
            {
                'name': 'У мене питання',
                'damage': 10
            },
            {
                'name': 'Влупити (Default)',
                'damage': self.right_hand_weapon.damage
            },
        ]

    def attack(self, attack_index):
        if self.attacks[attack_index]['name'] != 'Влупити (Default)':
            return self.attacks[attack_index]['damage'] * self.level + 10
        else:
            return self.attacks[attack_index]['damage']

    def get_damage(self, damage_value):
        if self.hit_points <= int(damage_value):
            self.hit_points = 0
        else:
            self.hit_points -= int(damage_value)

    def change_weapon(self, new_weapon):
        self.right_hand_weapon = new_weapon

    def minus_money(self, minus_value):
        self.money -= int(minus_value)

    def plus_money(self, plus_value):
        self.money += int(plus_value)

    def add_hit_points(self, added_hit_points):
        self.hit_points += int(added_hit_points)
        if self.max_hit_points > self.hit_points:
            self.hit_points = self.max_hit_points
        else:
            self.hit_points += int(added_hit_points)

    def level_up(self):
        self.level += 1
        self.strengths += 1
        self.next_level_experience = 100 * self.level
        self.hit_points = self.strengths * 10
        self.max_hit_points = self.strengths * 10

    def set_experience(self, experience_value):
        self.experience = int(experience_value)
        while self.experience >= self.next_level_experience:
            self.experience -= self.next_level_experience
            self.level_up()

    def set_money(self, money_value):
        self.money = self.money + money_value
