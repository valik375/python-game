from abc import ABC, abstractmethod


class Weapon(ABC):

    def __init__(self, weapon_name, damage, stamina, price):
        super().__init__()
        self.weapon_name = weapon_name
        self.damage = damage
        self.stamina = stamina
        self.price = price

    @abstractmethod
    def hit(self):
        pass


class Axe(Weapon):

    def hit(self):
        print(f'{self.weapon_name} - {self.damage} damage')


class Sword(Weapon):

    def hit(self):
        print(f'{self.weapon_name} - {self.damage} damage')

