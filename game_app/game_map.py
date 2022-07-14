import tkinter as tk

from slected_hero import SelectedHero


class GameMap(tk.Frame):

    def __init__(self, parent, controller, heroes):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.heroes = heroes
        self.hero = SelectedHero.selected_hero

        label = tk.Label(self, text=f"{self.hero.name} - {self.hero.weapon.weapon_name} - {self.hero.money}", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button = tk.Button(self, text="Home Page", command=lambda: controller.show_frame("HomePage"))
        button.pack()
