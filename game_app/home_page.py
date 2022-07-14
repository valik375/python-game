import tkinter as tk
from functools import partial

from shop_page import ShopPage
from slected_hero import SelectedHero


class HomePage(tk.Frame):

    def __init__(self, parent, controller, heroes):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.heroes = heroes

        label = tk.Label(self, text="Welcome in Shit Game!!!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        label = tk.Label(self, text="Please, choose hero to start", font=controller.text_font)
        label.pack(side="top", fill="x", pady=10)

        for hero in heroes:
            select_hero_button = tk.Button(self, text=f"{hero.name}", command=partial(self.select_hero, parent, hero))
            select_hero_button.pack()

    def select_hero(self, par, hero):
        SelectedHero.selected_hero = hero
        self.controller.create_frame(par, ShopPage)
        self.controller.show_frame("ShopPage")

