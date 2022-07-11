class Shop:
    def __init__(self, weapons, hero):
        self.weapons = weapons
        self.hero = hero

    def weapon_shop(self):
        print('---/  Weapons  /---')
        print(f'Your money: {self.hero.money}')
        for weapon in self.weapons:
            weapon_index = weapon['index']
            weapon_item = weapon['item']
            print(f'{weapon_item.weapon_name} --- ${weapon_item.price} [{weapon_index}]')

        print('Back [0]')
        selected_weapon_index = int(input('Select weapon: '))
        print('Left hand [1]')
        print('Right hand [2]')
        selected_hand = int(input('Select hand: '))

        selected_weapon = self.weapons[selected_weapon_index]['item']

        if self.hero.money > selected_weapon.price:
            self.hero.minus_money(selected_weapon.price)
            if selected_hand == 1:
                self.hero.change_left_hand_weapon(selected_weapon)
            else:
                self.hero.change_right_hand_weapon(selected_weapon)
        else:
            print('You have no money!')

    def enter_to_shop(self):
        while True:
            print('---/  SHOP  /---')
            print('Seller: Welcome in my shop!')
            print('Weapon [1]')
            print('Exit [3]')
            shop_map = input('Select shop option: ')

            if shop_map == '1':
                self.weapon_shop()
            else:
                break
