class Hero:
    def __init__(self, name, money, left_hand_weapon, right_hand_weapon):
        self.name = name
        self.level = 1
        self.level_points = 1
        self.next_level_experience = 100
        self.experience = 0
        self.strengths = 10
        self.agility = 10
        self.intelegent = 10
        self.money = money
        self.left_hand_weapon = left_hand_weapon
        self.right_hand_weapon = right_hand_weapon

    def left_hand_hit(self):
        self.left_hand_weapon.hit()

    #         self.get_stamina() -= left_hand_weapon.stamina

    def right_hand_hit(self):
        self.right_hand_weapon.hit()

    #         self.get_stamina() -= right_hand_weapon.stamina

    def change_left_hand_weapon(self, new_weapon):
        self.left_hand_weapon = new_weapon

    def change_right_hand_weapon(self, new_weapon):
        self.right_hand_weapon = new_weapon

    def minus_money(self, minus_value):
        self.money -= int(minus_value)

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
        print('Agility select [2]')
        print('Intelegent select [3]')
        print('Exit [3 - 9 or 0]')

        while self.level_points != 0:
            print(f'Available skill points: {self.level_points}')
            selected_perk = int(input('Select perk: '))
            if selected_perk == 1:
                self.strengths += 1
                self.level_points -= 1
            elif selected_perk == 2:
                self.agility += 1
                self.level_points -= 1
            elif selected_perk == 3:
                self.intelegent += 1
                self.level_points -= 1
            else:
                break
