"""
List of levels for Character to Travel Through

Player location determines surrounding sotry

"""
import json

def index_to_level(player_index):
    index_to_level_descript = {
        1: 'level_one',
        2: 'level_two',
        3: 'level_three',
        4: 'level_four',
    }
    return index_to_level_descript[player_index]


def establish_location(level):

    with open('locations.json') as f:
        story = json.load(f)
        return story['locations'][level]['scenery']







