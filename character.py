import random
from location_functions import level_count


class Character:
    character_stats = dict(health=190, mana=50, speed=10, luck=3)
    location = 2

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

    def resassign_attributes(self):
        if self.vocation == 'wizard':
            self.character_stats['health'] -= 30
            self.character_stats['mana'] += 30
            self.character_stats['speed'] -= 5
            self.character_stats['luck'] += 5
        elif self.vocation == 'warrior':
            self.character_stats['health'] += 30
            self.character_stats['mana'] -= 30
            self.character_stats['speed'] += 2
            self.character_stats['luck'] += 2
        elif self.vocation == 'archer':
            self.character_stats['health'] -= 30
            self.character_stats['mana'] += 10
            self.character_stats['speed'] += 15
            self.character_stats['luck'] += 15

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
        attack_damage = random.randint(25, 55) + (self.character_stats['luck'] * 90)
        return attack_damage


class Enemy(Character):
    location = level_count()

    def __init__(self, name_list, genders, classes):
        self.name = name_list.pop(random.randint(0, len(name_list)) - 1)
        self.gender = genders[random.randint(0, 2)]
        self.vocation = classes[random.randint(0, 2)]
        self.character_stats = dict(health=100, mana=20, speed=5, luck=1)

    def attack(self):
        attack_damage = random.randint(5, 40)
        return attack_damage

    def move_location(self):
        if self.location >= 4 and self.location <= level_count():
            self.location -= 1
        elif self.location <= 3:
            self.location += (random.randint(3, 5))


