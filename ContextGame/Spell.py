class spell:

    def __init__(self, name, damage=None):
        self.name = name
        self.damage = damage

    def __enter__(self):
        print('Incanting...')
        self.damage = self.damage +  2
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'Healing for 2 points of health')
        #self.damage = 0#
        self.damage = self.damage + 2

    def __add__(self, other):
        #print(f'Spell name {self.name} and {other.name}')
        new_spell = spell(f'{self.name} with {other.name}')
        new_spell.damage = self.damage + other.damage
        return new_spell

    def cast(self):
        print(f'Casting {self.name} for {self.damage} damage')