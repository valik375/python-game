from food.food import Food

class Chicken(Food):
    def __init__(self, name, recovery_value, price):
        Food.__init__(self, name, recovery_value, price)

class Bread(Food):
    def __init__(self, name, recovery_value, price):
        Food.__init__(self, name, recovery_value, price)
