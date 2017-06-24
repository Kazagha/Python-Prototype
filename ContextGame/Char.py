class char:

    name = ''
    HP = 0

    def __init__(self, name, HP):
        self.name = name

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def casts(self, spell, target=None):
        print(f'{self.name} casts {spell.name}')

