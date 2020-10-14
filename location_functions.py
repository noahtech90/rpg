"""
List of levels for Character to Travel Through

Player location determines surrounding story

"""
import json


# Convert location attribute to level description
def index_to_descript(player_index):
    index_to_level_descript = {
        1: 'level_one',
        2: 'level_two',
        3: 'level_three',
        4: 'level_four',
        5: 'level_five',
        6: 'level_six',
        7: 'level_seven',
        8: 'level_eight',
    }

    level_description = index_to_level_descript[player_index]
    return level_description


def find_contiguous_levels(player_index):
    if player_index > 1 and player_index < 8:
        i = player_index - 1
        j = player_index + 1
    elif player_index == 1:
        i = player_index + 1
        j = None
    else:
        i = None
        j = player_index - 1

    return i, j

def level_interest(level):
    with open('locations.json') as f:
        story = json.load(f)
        return story['locations'][level]['interest']

# Level Description Functions
def location_scenery(level):
    with open('locations.json') as f:
        story = json.load(f)
        return story['locations'][level]['scenery']


def location_name(level):
    with open('locations.json') as f:
        story = json.load(f)
        return story['locations'][level]['name']


def location_bonus(level):
    with open('locations.json') as f:
        story = json.load(f)
        if 'bonus' in story['locations'][level]:
            return story['locations'][level]['bonus']
        else:
            return None
