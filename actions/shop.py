class Shop:
    def __init__(self, weapons, foods, hero):
        self.weapons = weapons
        self.foods = foods
        self.hero = hero

    def shop_section(self, section_name, items_array):
        print(f'---/  {section_name}  /---')
        print(f'Your money: {self.hero.money}')
        for item in items_array:
            array_item_index = item['index']
            array_item_item = item['item']
            print(f'{array_item_item.name} --- ${array_item_item.price} [{array_item_index}]')

        print('Back [0]')
        selected_item_index = int(input('Select index: '))
        if selected_item_index != 0:
            selected_item = items_array[selected_item_index - 1]['item']
            if self.hero.money > selected_item.price:
                self.hero.minus_money(selected_item.price)
                if section_name == 'Weapon':
                    self.hero.change_right_hand_weapon(selected_item.price)
                else:
                    self.hero.add_hit_points(selected_item.recovery_value)
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
            shop_map = int(input('Select shop option: '))

            if shop_map == 1:
                self.shop_section('Weapon', self.weapons)
            elif shop_map == 2:
                self.shop_section('Food', self.foods)
            else:
                break
