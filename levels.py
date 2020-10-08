"""
List of levels for Character to Travel Through

Player location determines surrounding sotry

"""

class Level(object):
    def __init__(self, player):
        self.player = player
        self.next = None
        self.backwards = None

class DoublyLinkedLevelList(object):
    def __init__(self):
        self.start_level = None



list = LinkedList()
player_one = Player(1)


print(list)

