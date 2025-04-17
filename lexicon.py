from itertools import permutations
import random
import json

class Lexicon:
    def __init__(self, dict_name, dict_file):
        self.dict_name = dict_name
        self.alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)] + ['?']

        with open(f"dictionaries/{dict_file}", "r") as d:
            self.lexicon = set(json.load(d))

    def __str__(self):
        num_words = len(self.lexicon)
        random_word = random.choice(list(self.lexicon))

        s = (f"*-*-*-*-*-*-*-*-*-*-*-*\nLexicon: {self.dict_name}\nNumber of words: {num_words}"
            + f"\nRandom word: {random_word}\n*-*-*-*-*-*-*-*-*-*-*-*")

        return s

    def __contains__(self, w):
        return w.lower() in self.lexicon

    def __iter__(self):
        return iter(self.lexicon)

    def len_k_words(self, k):
        k_words = [w for w in self if len(w) == k]
        k_words.sort()
        return k_words

    def anagrams(self, s):
        alphabet = [a for a in self.alphabet if a != '?']

        anagrams_no_b = lambda s : set("".join(t) for t in permutations(s)) & self.lexicon
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

if __name__ == "__main__":
    l = Lexicon("NWL23", "nwl23.json")
    s = 'z??'
    print(l.anagrams(s))
