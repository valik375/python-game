import tkinter as tk


class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Please, choose hero, to start", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Vlad", command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Valik", command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()
