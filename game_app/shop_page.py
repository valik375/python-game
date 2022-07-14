import tkinter as tk
from home_page import SelectedHero


class ShopPage(tk.Frame):

    def __init__(self, parent, controller, heroes):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.heroes = heroes
        self.hero = SelectedHero.selected_hero

        label = tk.Label(self, text=f"Shop", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        label = tk.Label(self, text="Hello, {} !!! Buy something".format(self.hero.name if self.hero else ''),
                         font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button = tk.Button(self, text="Continue", command=lambda: controller.show_frame("GameMap"))
        button.pack()
