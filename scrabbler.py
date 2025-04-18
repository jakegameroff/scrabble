from itertools import permutations
from lexicon import Lexicon
import random
import json

class Scrabbler:
    def __init__(self, lexicon):
        self.lexicon = lexicon
        self.generate_rack()

    def generate_rack(self):
        self.rack = random.sample(self.lexicon.tile_bag, k=7)
    
    def set_rack(self, rack):
        self.rack = rack

    def anagrams(self, s=""):
        if len(s) == 0:
            s = ''.join(self.rack)
        alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

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