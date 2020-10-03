import random
import time

"""
Character class which creates the story 

Character can attack and defend, similar to a finial fantasy type game

"""


class Character:
    character_stats = dict(health=100, mana=50, speed=10, luck=1)

    def __init__(self, name, gender, vocation):
        self.name = name
        self.gender = gender
        self.vocation = vocation
        self.gold = random.randint(5, 150000)

    def __str__(self):
        capitalized_vocation = self.vocation[0].upper() + self.vocation[1:]
        return f"   {self.name} the {capitalized_vocation}"

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
        attack_damage = random.randint(15, 30)
        return attack_damage


# Intro
print("""You wake up in a dark cave""")
print("")
time.sleep(2)
# Assign Name
raw_name = input('What is your character\'s name? ')
name = raw_name[0].upper() + raw_name[1:].lower()
time.sleep(2)
# Assign Gender
print("What gender is your character? ")
gender = input("Male                Female                Other").lower()
time.sleep(2)
# Assign Player Type
print("""What class is your character? """)
vocation = input('      Wizard            Warrior           Archer').lower()
print("")
time.sleep(2)

character = Character(name, gender, vocation)


def start_game(character):
    print(
        f"{character} embarked on {character.possesive()} quest.  {character.name} knew only that there was a battle coming.")
    time.sleep(2)
    print("")
    print(f"\t{character} drew {character.possesive()} {character.weapon()} and headed down the road")
    time.sleep(2)


start_game(character)
