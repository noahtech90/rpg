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
    }

    level_description = index_to_level_descript[player_index]
    return level_description


# Accessing JSON to view stored levels
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
