import tkinter as tk
from tkinter import font as tkfont

from packages.hero.hero_class import Hero
from home_page import HomePage

hero_vlad = Hero('Vlad', 100, 'Hand')
hero_valik = Hero('Valik', 100, 'Hand')
hero_list = [hero_vlad, hero_valik]


class GameApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.text_font = tkfont.Font(family='Helvetica', size=16, weight="normal", slant="italic")

        window = tk.Frame(self)
        window.pack(side="top", fill="both", expand=True)
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)

        self.frames = {}

        self.create_frame(window, HomePage)
        self.show_frame("HomePage")

    def create_frame(self, par, page):
        page_name = page.__name__
        frame = page(parent=par, controller=self, heroes=hero_list)
        self.frames[page_name] = frame
        frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    app = GameApp()
    app.geometry('1000x600')
    app.title('Shit Game')
    app.mainloop()
