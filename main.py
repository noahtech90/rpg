import random


class Character:

    def __init__(self, name, gender, vocation):
        self.name = name
        self.gender = gender
        self.vocation = vocation
        self.gold = random.randint(5,150000)

    def __str__(self):
        return f"{self.name} the {self.vocation}"

