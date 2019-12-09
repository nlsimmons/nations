import random

consts = ("b", "c", "d", "f", "g", "h", "i", "j", "k", "l", "m", "n", "p", "q",
          "r", "s", "t", "v", "w", "x", "y", "z")
vowels = ("a", "e", "i", "o", "u")


def zipf(items):
    q = []
    c = 1
    length = len(items)
    for item in items:
        r = round(length / c * 100)
        for _ in range(r):
            q.append(item)
        c += 1
    return random.choice(q)


class Language():
    def __init__(self):
        self.phonemes = []
        self.wordlen = random.randint(3, 6)
        for c in consts:
            for v in vowels:
                self.phonemes.append(c + v)
                self.phonemes.append(v + c)
        random.shuffle(self.phonemes)
        self.name = self.genName()

    def getPhoneme(self):
        return zipf(self.phonemes)

    def genWord(self):
        w = ""
        ll = self.wordlen - 2
        ul = self.wordlen + 2
        for _ in range(random.randrange(ll, ul)):
            w += self.getPhoneme()
        return w

    def genName(self):
        return self.genWord().title()
