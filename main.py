from monsters.enemy import Monster
from monsters.enemy import Boss
from hero.hero_class import Hero
from weapon.weapons import Axe, Sword
from food.dishes import Chicken, Bread
from actions.shop import Shop
from actions.fight import fight_process

axe = Axe('Axe', 20, 15, 51)
sword = Sword('Sword', 13, 10, 36)
super_axe = Axe('Super Axe', 25, 35, 84)
super_sword = Sword('Super Sword', 19, 22, 51)

chicken = Chicken('Chicken', 50, 10)
bread = Bread('Bread', 30, 6)
super_chicken = Chicken('Super Chicken', 120, 20)
super_bread = Bread('Super Bread', 90, 21)

weapon_array = [dict(index=1, item=axe), dict(index=2, item=sword),
                dict(index=3, item=super_axe), dict(index=4, item=super_sword)]

food_array = [dict(index=1, item=chicken), dict(index=2, item=bread),
              dict(index=3, item=super_chicken),
              dict(index=4, item=super_bread)]

hero = Hero('Petro Poroshenko', 1000000, sword)
shop = Shop(weapon_array, food_array, hero)

for index in range(5):
    oleg_level = index + 1
    oleg_dialogs = ['На тобi КУРВА!', 'Отримуй!', 'Джета топ!', 'Получай!']
    oleg_crip = Monster(f'Oleg {oleg_level}', oleg_level, oleg_dialogs)
    print(f'Бiйка з {oleg_crip.name}')

    fight_process(hero, oleg_crip, shop)

ihor_dialog = ['Не iнтересно', 'Слабенько', 'Ну таке на 3', 'Iди роби хiдер']
ihor = Boss('IGIBO', 1, ihor_dialog)
fight_process(hero, ihor, shop)
