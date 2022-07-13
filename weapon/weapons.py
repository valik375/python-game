from abc import ABC, abstractmethod


class Weapon(ABC):

    def __init__(self, name, damage, stamina, price):
        super().__init__()
        self.name = name
        self.damage = damage
        self.stamina = stamina
        self.price = price

    @abstractmethod
    def hit(self):
        pass


class Axe(Weapon):

    def hit(self):
        print(f'{self.name} - {self.damage} damage')


class Sword(Weapon):

    def hit(self):
        print(f'{self.name} - {self.damage} damage')

