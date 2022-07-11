from random import randint
from hero.hero_class import Hero
from weapon.weapons import Axe, Sword
from food.dishes import Chicken, Bread
from actions.shop import Shop
from enemies.enemies import Enemy, Boss

axe = Axe('Axe', 20, 15, 51)
sword = Sword('Sword', 13, 10, 36)
super_axe = Axe('Super Axe', 25, 35, 84)
super_sword = Sword('Super Sword', 19, 22, 51)

chicken = Chicken('Chicken', 50, 10)
bread = Bread('Bread', 30, 6)

enemy = Enemy('Swiper', 100, 10, 25, 150)

weapon_array = []

weapon_array.append(dict(index=1, item=axe))
weapon_array.append(dict(index=2, item=sword))
weapon_array.append(dict(index=3, item=super_axe))
weapon_array.append(dict(index=4, item=super_sword))

hero = Hero('Petro Poroshenko', 1000000, axe, sword)

shop = Shop(weapon_array, hero)

hero.set_experience(340)
hero.set_perks()

print(hero.experience)
print(hero.strengths)
print(hero.next_level_experience)
print('HP: ', hero.strengths * 10)

while True:
    world_action = int(randint(0, 10))
    if world_action == 0:
        print(hero.right_hand_weapon.weapon_name)
        print('Shop')
        shop.enter_to_shop()
        print(hero.right_hand_weapon.weapon_name)
        continue
    elif world_action == 1:
        print(f'Monster {enemy.name}')
    else:
        input('Walking...')
