class cast:

    spell_outer = ''
    spell_inner = ''

    def __init__(self, spell_inner, spell_outer = None):
        self.spell_inner = spell_inner
        self.spell_outer = spell_outer

    def __enter__(self):
        if(self.spell_outer == None):
            #return self.spell_inner
            with self.spell_inner as s:
                return s
        else:
            spell =  self.spell_inner + self.spell_outer
            with spell as s:
                return s

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def cast(self):
        print(f'Casting... {self.spell.name}')