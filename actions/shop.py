class Shop:
    def __init__(self, weapons, foods, hero):
        self.weapons = weapons
        self.foods = foods
        self.hero = hero

    # def shop_item(self, section_name, items_array):
    #     print(f'---/  {section_name}  /---')
    #     print(f'Your money: {self.hero.money}')
    #     for array_item in items_array:
    #         array_item_index = items_array['index']
    #         array_item_item = items_array['item']
    #         print(f'{array_item_item.weapon_name} --- ${array_item_item.price} [{array_item_index}]')

    def weapon_shop(self):
        print('---/  Weapons  /---')
        print(f'Your money: {self.hero.money}')
        for weapon in self.weapons:
            weapon_index = weapon['index']
            weapon_item = weapon['item']
            print(f'{weapon_item.weapon_name} --- ${weapon_item.price} [{weapon_index}]')

        print('Back [0]')
        selected_weapon_index = int(input('Select weapon: '))

        if selected_weapon_index != 0:
            selected_weapon = self.weapons[selected_weapon_index - 1]['item']
            if self.hero.money > selected_weapon.price:
                self.hero.minus_money(selected_weapon.price)
                self.hero.change_right_hand_weapon(selected_weapon.price)
            else:
                print('You have no money!')
        else:
            print('Back!')

    def food_shop(self):
        print('---/  Food  /---')
        print(f'Your money: {self.hero.money}')

        for food in self.foods:
            food_index = food['index']
            food_item = food['item']
            print(f'{food_item.name} --- ${food_item.price} [{food_index}]')

        print('Back [0]')
        selected_food_index = int(input('Select food: '))

        if selected_food_index != 0:
            selected_food = self.foods[selected_food_index - 1]['food']
            if self.hero.money > selected_food.price and hero.hit_points:
                self.hero.minus_money(selected_food.price)
                self.hero.add_hip_points(selected_food.recovery_value)
            else:
                print('You have no money!')
        else:
            print('Back!')

    def enter_to_shop(self):
        while True:
            print('---/  SHOP  /---')
            print('Seller: Welcome in my shop!')
            print('Weapon [1]')
            print('Food [2]')
            print('Exit [3]')
            shop_map = input('Select shop option: ')

            if shop_map == '1':
                self.weapon_shop()
            elif shop_map == '2':
                self.food_shop()
            else:
                break
