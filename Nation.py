from Language import Language


class Nation():
    def __init__(self, color, capital):
        self.color = color
        self.capital = capital

        self.language = Language()
        self.name = self.language.genName()
