import tkinter as tk
from functools import partial


class HomePage(tk.Frame):

    def __init__(self, parent, controller, heroes):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.heroes = heroes

        label = tk.Label(self, text="Please, choose hero, to start", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        for hero in heroes:
            select_hero_button = tk.Button(self, text=f"{hero.name}", command=partial(self.select_hero, hero))
            select_hero_button.pack()

    def select_hero(self, hero):
        SelectedHero.selected_hero = hero
        print(SelectedHero.selected_hero.name)
        self.controller.show_frame("ShopPage")


class SelectedHero:
    selected_hero = None
