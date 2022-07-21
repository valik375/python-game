import tkinter as tk
from functools import partial

from slected_hero import SelectedHero
from game_map import GameMap
from packages.weapon.weapons import Weapon

weapons_list = []
axe = Weapon('Axe', 30, 30, 25)
sword = Weapon('Sword', 20, 20, 20)
knife = Weapon('Knife', 10, 10, 10)

for weapon in (axe, sword, knife):
    weapons_list.append(weapon)


class ShopPage(tk.Frame):

    def __init__(self, parent, controller, heroes):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.heroes = heroes
        self.hero = SelectedHero.selected_hero

        label = tk.Label(self, text=f"Hello, {self.hero.name}!!! Welcome in game shop.", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label = tk.Label(self, text=f"Buy a weapon to start playing...", font=controller.text_font)
        label.pack(side="top", fill="x", pady=20)

        for item in weapons_list:
            shop_item_button = tk.Button(self, text=f"{item.weapon_name}", command=partial(self.buy_item_in_shop, item, item.price, self.hero.money))
            shop_item_button.pack(side="top", fill=None, pady=10)
            label = tk.Label(self, text=f"{item.price}$", font=controller.text_font)
            label.pack()

        button = tk.Button(self, text="Start Game", command=partial(self.start_game, parent))
        button.pack(side="bottom", fill=None, pady=50)

    def buy_item_in_shop(self, item, weapon_cost, hero_price):
        if weapon_cost < hero_price:
            self.hero.weapon = item
            self.hero.money -= weapon_cost
            print(self.hero.money)
        else:
            print('You dont have money for this')

    def start_game(self, parent):
        self.controller.create_frame(parent, GameMap)
        self.controller.show_frame("GameMap")

