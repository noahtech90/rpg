
#Import Libraries
import random
import time

from character import Character, Enemy
from levels import index_to_level, establish_location

"""
Project implements OOP design to dynamically create an RPG like story

Character can attack and defend, similar to a final fantasy type game

Enemies inherit from the Character class

May be a turn based game that allows you to travel

There are four enemies on the map

Each turn you will move and they will move

You don't know where they are and win the game by defeating all 4
"""
# Each enemy character is given name from below list
enemy_available = ['Baron', 'Ratchet', 'Snitzz', 'Valten']

# Gender Options
genders = ['male', 'female', 'other']

# Player Types
classes = ['warrior', 'wizard', 'archer']

# Intro
#print("""You wake up in a dark cave""")
#print("")
#time.sleep(2)
# Assign Name
#raw_name = input('What is your character\'s name? ')
raw_name = "Noah"
name = raw_name[0].upper() + raw_name[1:].lower()
#time.sleep(2)
#print("")

# Assign Gender
#print("What gender is your character? ")
#time.sleep(1)
#gender = input("Male                Female                Other ").lower()
gender = 'male'
#time.sleep(2)
#print("")

# Assign Player Type
#print("""What class is your character? """)
#time.sleep(1)
#vocation = input('Wizard            Warrior           Archer ').lower()

vocation = 'wizard'
#print("")
#time.sleep(2)

character = Character(name, gender, vocation)


def start_game(main_character):
    print(
        f"{main_character} woke in a dark mysterious cave.  {main_character.name} knew not where {main_character.pronoun()} came from, nor what {main_character.pronoun()} was doing in this desolate place. ")
    time.sleep(3)
    print("")
    print(f"{main_character.name} drew {main_character.possesive()} {main_character.weapon()} and moved towards a "
          f"faint dripping sound")
    time.sleep(2)
    print("")
    print(
        f"Suddenly, a snarling hideous creature clutching its {first_enemy.weapon()} jumped out, {first_enemy} lunges "
        f"towards {main_character.name}")
    first_battle(main_character)


def first_battle(main_character):
    while main_character.character_stats['health'] > 0 and first_enemy.character_stats['health'] > 0:
        decision = input('Attack         Counter          Heal').lower()
        if decision == 'attack':
            first_enemy.character_stats['health'] -= main_character.attack()
        elif decision == 'counter':
            attempt = first_enemy.character_stats['luck'] * random.randint(1, 5)
            if attempt > 4:
                first_enemy.character_stats['health'] -= 100
        elif decision == 'heal':
            main_character.character_stats['health'] += 10
        if first_enemy.character_stats['health'] > 0:
            main_character.character_stats['health'] -= first_enemy.attack()

        print("")
        print("")
        time.sleep(1)
        print(f"{main_character}: " + str(main_character.character_stats))
        print("")
        print(f"{first_enemy}: " + str(first_enemy.character_stats))
        print("")
        print("")
        time.sleep(2)

def first_move(main_character):

    #Move Character
    main_character.location = main_character.move_position(1)

    #Obtain index to travel through stored Story
    current_index = main_character.location
    current_level = index_to_level(current_index)
    print(establish_location(current_level))

# Create Enemies
first_enemy = Enemy(enemy_available, genders, classes)
second_enemy = Enemy(enemy_available, genders, classes)
third_enemy = Enemy(enemy_available, genders, classes)
fourth_enemy = Enemy(enemy_available, genders, classes)

# Initiate Story
#start_game(character)
first_move(character)
