# from random import randint
# from hero.hero_class import Hero
# from weapon.weapons import Axe, Sword
# from food.dishes import Chicken, Bread
# from actions.shop import Shop
#
# axe = Axe('Axe', 20, 15, 51)
# sword = Sword('Sword', 13, 10, 36)
# super_axe = Axe('Super Axe', 25, 35, 84)
# super_sword = Sword('Super Sword', 19, 22, 51)
#
# chicken = Chicken('Chicken', 50, 10)
# bread = Bread('Bread', 30, 6)
# super_chicken = Chicken('Super Chicken', 120, 20)
# super_bread = Bread('Super Bread', 90, 21)
#
# weapon_array = []
# weapon_array.append(dict(index=1, item=axe))
# weapon_array.append(dict(index=2, item=sword))
# weapon_array.append(dict(index=3, item=super_axe))
# weapon_array.append(dict(index=4, item=super_sword))
#
# food_array = []
# food_array.append(dict(index=1, item=chicken))
# food_array.append(dict(index=2, item=bread))
# food_array.append(dict(index=3, item=super_chicken))
# food_array.append(dict(index=4, item=super_bread))
#
# hero = Hero('Petro Poroshenko', 1000000, sword)
# shop = Shop(weapon_array, food_array, hero)

# shop.enter_to_shop()

# while True:
#     world_action = int(randint(0, 10))
#     if world_action == 0:
#         print('Shop')
#         shop.enter_to_shop()
#         continue
#     elif world_action == 1:
#         print('Monster')
#     else:
#         input('Walking...')


class Human:
    def walk(self):
        print('Human walk')


class Dog:
    def walk(self):
        print('Dog walk')


class Cat:
    def walk(self):
        print('Cat walk')


class Robot(Human, Dog, Cat):
    def __init__(self):
        super(Robot, self).walk()
        super(Human, self).walk()
        super(Dog, self).walk()


rob = Robot()



