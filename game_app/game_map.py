import tkinter as tk


class GameMap(tk.Frame):

    def __init__(self, parent, controller, heroes):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.heroes = heroes

        label = tk.Label(self, text="Select enemy to start", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button = tk.Button(self, text="Home Page", command=lambda: controller.show_frame("HomePage"))
        button.pack()
