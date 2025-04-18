from itertools import permutations
from lexicon import Lexicon
import random
import json

class Scrabbler:
    def __init__(self, lexicon):
        self.lexicon = lexicon
        self.rack = self.generate_rack()

    @staticmethod
    def generate_rack():
        with open("tile_distribution.json", "r") as d:
            tile_distribution = json.load(d)

        tile_bag = sum([[letter] * freq for letter, freq in tile_distribution.items()], start=[])
        return random.sample(tile_bag, k=7)

    def anagrams(self):
        s = ''.join(self.rack)
        alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]

        anagrams_no_b = lambda s : set("".join(t) for t in permutations(s)) & self.lexicon.lexicon
        anagrams_one_b = lambda s : set.union(*[anagrams_no_b(s.replace('?', a)) for a in alphabet])

        blanks = [i for i in range(len(s)) if s[i] == '?']
        if blanks == []:
            return anagrams_no_b(s)
        elif len(blanks) == 1:
            return anagrams_one_b(s)
        else:
            b = blanks.pop()
            replace_ith = lambda s, i, r: s[:i] + r + s[i+1:]
            return set.union(*[anagrams_one_b(replace_ith(s, b, a)) for a in alphabet])

    def has_bingo(self):
        return self.anagrams() != set()

if __name__ == "__main__":
    l = Lexicon("NWL23", "nwl23.json")
    num_bingos = 0
    for i in range(1_000_000):
        if i % 1000 == 0:
            print(i)
        jake = Scrabbler(l)
        if jake.has_bingo():
            num_bingos += 1

    print(f"The probability of starting with a bingo is about {num_bingos / 1_000_000:2f}")
