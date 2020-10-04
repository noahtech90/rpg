import random
import time
from character import Character, Enemy

"""
Character class which creates the story 

Character can attack and defend, similar to a finial fantasy type game

"""
#Each enemy character is given name from below list
enemy_available = ['Baron', 'Ratchet', 'Snitzz', 'Valten']

#Gender Options
genders = ['male', 'female', 'other']

#Player Types
classes = ['warrior', 'wizard', 'archer']


# Intro
print("""You wake up in a dark cave""")
print("")
time.sleep(2)
# Assign Name
raw_name = input('What is your character\'s name? ')
name = raw_name[0].upper() + raw_name[1:].lower()
time.sleep(2)
print("")
# Assign Gender
print("What gender is your character? ")
time.sleep(1)
gender = input("Male                Female                Other ").lower()
time.sleep(2)
print("")

# Assign Player Type
print("""What class is your character? """)
time.sleep(1)
vocation = input('      Wizard            Warrior           Archer ').lower()
print("")
time.sleep(2)

character = Character(name, gender, vocation)


def start_game(character):
    print(f"{character} woke in a dark mysterious cave.  {character.name} knew not where {character.pronoun()} came from, nor what {character.pronoun()} was doing in this desolate place. ")
    time.sleep(2)
    print("")
    print(f"{character.name} drew {character.possesive()} {character.weapon()} and moved towards a faint dripping sound")
    time.sleep(2)
    print(f"Suddenly {character.name} is attacked")

#Create Enemies
first_enemy = Enemy(enemy_available, genders, classes)
second_enemy = Enemy(enemy_available, genders, classes)
third_enemy = Enemy(enemy_available, genders, classes)
fourth_enemy = Enemy(enemy_available, genders, classes)


start_game(character)
print(first_enemy)
