import random
import time

class Character:
    character_stats = dict(health=100, mana=50, speed=10, luck=1)

    def __init__(self, name, gender, vocation):
        self.name = name
        self.gender = gender
        self.vocation = vocation
        self.gold = random.randint(5, 150000)

    def __str__(self):
        capitalized_vocation = self.vocation[0].upper() + self.vocation[1:]
        return f"{self.name} the {capitalized_vocation}"

    def pronoun(self):
        if self.gender == 'male':
            return "he"
        elif self.gender == 'female':
            return "she"
        else:
            return "they"

    def possesive(self):
        if self.gender == 'male':
            return "his"
        elif self.gender == 'female':
            return "her"
        else:
            return "their"

    def weapon(self):

        if self.vocation == 'wizard':
            return "staff"
        elif self.vocation == 'warrior':
            return "sword"
        elif self.vocation == 'archer':
            return "bow"
        else:
            return "bear"

    def attack(self):
        attack_damage = random.randint(15, 30) + (self.character_stats['luck'] * 1.2)
        return attack_damage

class Enemy(Character):


    def __init__(self, name_list, genders, classes):
        self.name = name_list.pop(random.randint(0, len(name_list)) - 1)
        self.gender = genders[random.randint(0,2)]
        self.vocation = classes[random.randint(0,2)]



