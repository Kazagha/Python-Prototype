from Char import char
from Spell import spell
from Cast import cast

import random

class game:

    player = None
    enemy = None

    def __init__(self):
        self.setup()

    def setup(self):

        # Setup the player character
        #self.player = char(input('Character Name: '))
        self.player = char('Kazagha', 100)

        # Select an enemy at random
        self.enemy = self.random_enemy()

    def random_enemy(self):
        enemies = ['Ork','Goblin','Giant Spider','Bandit','Hill Giant','Stone Giant','Frost Giant','Fire Giant',
                   'Cloud Giant', 'Storm Giant']

        return char(random.choice(enemies), 50)

if __name__ == "__main__":
    the_game = game()

    with the_game.player as char:
        print(char.name)

        fireball = spell('Fireball', damage=10)
        icebolt = spell('Icebolt', damage=5)

        print(f'{fireball.damage} vs {icebolt.damage}')

        with cast(fireball) as c:
            with cast(c, icebolt) as d:
                print(f'{c.damage} vs. {d.damage}')
                d.cast()
