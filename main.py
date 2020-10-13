# Import Libraries
import random
import time

from character import Character, Enemy
from location_functions import index_to_descript, location_scenery, location_bonus, location_name, \
    find_contiguous_levels, level_interest

"""
Project implements OOP design to dynamically create an RPG like story

Character can attack and defend, similar to a final fantasy type game

Enemies inherit from the Character class

Turn based game that allows you to travel

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

"""

Initial Character Setup Section Currently Commented Out 

For Testing

"""
# Intro
print("""You wake up in a dark cave \n""")
time.sleep(2)
# Assign Name
raw_name = input('What is your character\'s name? \n')
# raw_name = "Noah"
name = raw_name[0].upper() + raw_name[1:].lower()
time.sleep(2)

# Assign Gender
print("What gender is your character? \n")
time.sleep(1)
gender = input("Male                Female                Other \n").lower()
# gender = 'male'
time.sleep(2)

# Assign Player Type
print("""What class is your character? """)
time.sleep(1)
vocation = input('Wizard            Warrior           Archer \n').lower()

# vocation = 'wizard'
time.sleep(2)

character = Character(name, gender, vocation)


def start_game(main_character):
    print(
        f"{main_character} woke in a dark mysterious cave.  {main_character.name} knew not where {main_character.pronoun()} came from, nor what {main_character.pronoun()} was doing in this desolate place. \n")
    time.sleep(3)
    print(f"{main_character.name} drew {main_character.possesive()} {main_character.weapon()} and moved towards a "
          f"faint dripping sound \n")
    time.sleep(2)
    print(
        f"Suddenly, a snarling hideous creature clutching its {first_enemy.weapon()} jumped out, {first_enemy} lunges "
        f"towards {main_character.name} \n")
    first_battle(main_character)


def first_battle(main_character):
    # Battle Loop
    while main_character.character_stats['health'] > 0 and first_enemy.character_stats['health'] > 0:
        deciding = True
        decision = input('Attack         Counter          Heal ').lower()
        while deciding:
            if decision == 'attack':
                first_enemy.character_stats['health'] -= main_character.attack()
                deciding = False
            elif decision == 'counter':
                attempt = first_enemy.character_stats['luck'] * random.randint(1, 5)
                if attempt > 4:
                    first_enemy.character_stats['health'] -= 100
                deciding = False
            elif decision == 'heal':
                main_character.character_stats['health'] += 10
                deciding = False
            else:
                decision = input('Attack         Counter          Heal ').lower()

        if first_enemy.character_stats['health'] > 0:
            main_character.character_stats['health'] -= first_enemy.attack()

        time.sleep(1)

        # Show Enemy and Player Stats
        print(f"\n\n{main_character}: " + str(main_character.character_stats) + "\n")
        print(f"{first_enemy}: " + str(first_enemy.character_stats) + "\n")

        time.sleep(2)

    if main_character.character_stats['health'] > 0:
        # Move Character
        print(f"{main_character} defeated the wretched creature, the monster lay near death \n")
        time.sleep(2)
        print(
            f'{first_enemy.name} "I am not the last poor {main_character.name}, there are 3 more looking for you..." \n')
        time.sleep(3)
        print(f"The creature passed on leaving {main_character.name} to ponder what had been said \n")
        time.sleep(3)
        print(f"{main_character.name} left the cave and began to chart {main_character.possesive()} quest \n")
        time.sleep(3)
        move_character(main_character)
    # First Potential Loss of Game
    else:
        time.sleep(2)
        print(f"\n{main_character} has fallen")
        print(f"\n :( ")
        time.sleep(5)

def battle_sequence(main_character, enemy):



def character_enemy_overlap(main_character, enemy_list):
    for enemy in enemy_list:
        if enemy.location == main_character:
        battle_sequence(main_character, enemy)


def move_character(main_character):
    # Character decides where to go

    # Find bordering levels
    print(f"Where should {main_character.name} go? \n")
    time.sleep(1)
    direction_one, direction_two = find_contiguous_levels(main_character.location)
    print("")
    time.sleep(2)
    if direction_two == None:
        only_level = location_name(index_to_descript(direction_one))
        print(f"Your character can only go to {only_level}")
        ready = input("Are you ready? ")
        main_character.location = direction_one
    elif direction_one == None:
        only_level = location_name(index_to_descript(direction_two))
        print(f"Your character can only go to {only_level}")
        ready = input("Are you ready? ")
        main_character.location = direction_two

    else:
        level_one = location_name(index_to_descript(direction_one))
        level_two = location_name(index_to_descript(direction_two))
        decision = int(input(f"1. {level_one}            or          2. {level_two} "))
        while decision != 1 or decision != 2:
            if decision == 1:
                main_character.location = direction_one
            elif decision == 2:
                main_character.location = direction_two
            else:
                decision = int(input(f"1. {level_one}            or          2. {level_two} "))

    # Access Level Object
    print("")
    interact_level(main_character)


def check_level_bonus(main_character):
    current_location_bonus = location_bonus(index_to_descript(main_character.location))
    time.sleep(3)
    print("\n")
    if current_location_bonus is not None:
        print(current_location_bonus + "\n")
    time.sleep(2)


def interact_level(main_character):
    current_level = index_to_descript(main_character.location)
    level_name = location_name(current_level)
    action = level_interest(current_level)

    print(f"{main_character.name} arrived at {level_name}\n")
    time.sleep(3)
    print(f"{main_character.name} finds " + location_scenery(current_level))
    time.sleep(2)
    if check_level_bonus(main_character) is not None:
        print(check_level_bonus(main_character))

    print(f"{main_character.name} decides {action}")
    move_character(main_character)


def travel_loop(main_character):
    playing = True
    while playing:
        second_enemy.move_location()
        third_enemy.move_location()
        fourth_enemy.move_location()
        move_character(main_character)


# Create Enemies
first_enemy = Enemy(enemy_available, genders, classes)
second_enemy = Enemy(enemy_available, genders, classes)
third_enemy = Enemy(enemy_available, genders, classes)
fourth_enemy = Enemy(enemy_available, genders, classes)

enemy_list = [second_enemy, third_enemy, fourth_enemy]

# Initiate Story
start_game(character)
# travel_loop(character)
