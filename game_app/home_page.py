import tkinter as tk
from packages.hero.hero_class import Hero

hero_vlad = Hero('Vlad', 100, 'Hand')
hero_valik = Hero('Valik', 100, 'Hand')


class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Please, choose hero, to start", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text=f"{hero_vlad.name}", command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text=f"{hero_valik.name}", command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()
