import random


class Character:

    def __init__(self, name, gender, help):
        self.name = name
        self.gender = gender
        self.gold = random.randint(5,150000)
        self.help = help
