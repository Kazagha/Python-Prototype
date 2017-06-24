from Char import char

import random

class game:

    player = None
    enemy = None

    def __init__(self):
        self.setup()

    def setup(self):

        # Setup the player character
        self.player = char(input('Character Name: '))

        # Select an enemy at random
        self.enemy = self.random_enemy()

    def random_enemy(self):
        enemies = ['Ork','Goblin','Giant Spider','Bandit','Hill Giant','Stone Giant','Frost Giant','Fire Giant',
                   'Cloud Giant', 'Storm Giant']

        return char(random.choice(enemies))

if __name__ == "__main__":
    the_game = game()


