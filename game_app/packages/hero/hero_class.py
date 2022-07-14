class Hero:
    def __init__(self, name, money, weapon):
        self.name = name
        self.level = 1
        self.level_points = 1
        self.next_level_experience = 100
        self.experience = 0

        self.strengths = 10

        self.max_hit_points = self.strengths * 10
        self.hit_points = self.strengths * 10

        self.money = money
        self.weapon = weapon

    def hero_hit(self):
        self.weapon.hit()

    def change_weapon(self, new_weapon):
        self.weapon = new_weapon

    def minus_money(self, minus_value):
        self.money -= int(minus_value)

    def add_hit_points(self, added_hit_points):
        self.hit_points += int(added_hit_points)
        if self.max_hit_points > self.hit_points:
            self.hit_points = self.max_hit_points
        else:
            self.hit_points += int(added_hit_points)

    def get_damage(self, damage_value):
        if self.hit_points <= damage_value:
            self.hit_points = 0
            print('You die')
        else:
            self.hit_points -= damage_value

    def level_up(self):
        self.level += 1
        self.level_points += 1
        self.next_level_experience = 100 * self.level

    def set_experience(self, experience_value):
        self.experience = int(experience_value)
        while self.experience >= self.next_level_experience:
            self.experience -= self.next_level_experience
            self.level_up()

    def set_perks(self):
        print('--- Perks ---')
        print('')
        print('Strengths select [1]')
        print('Exit [3 - 9 or 0]')

        while self.level_points != 0:
            print(f'Available skill points: {self.level_points}')
            selected_perk = int(input('Select perk: '))
            if selected_perk == 1:
                self.strengths += 1
                self.max_hit_points = self.strengths * 10
                self.hit_points = self.strengths * 10
                self.level_points -= 1
            else:
                break
