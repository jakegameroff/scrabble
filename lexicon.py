import random
import json

class Lexicon:
    def __init__(self, dict_name, dict_file):
        self.dict_name = dict_name
        with open(f"data/dictionaries/{dict_file}", "r") as d:
            self.lexicon = set([w.upper() for w in json.load(d)])

        with open("data/tile_distribution.json", "r") as d:
            tile_distribution = json.load(d)
            self.tile_distribution = tile_distribution
            self.tile_bag = sum([[letter] * freq for letter, freq in tile_distribution.items()], start=[])

    def __str__(self):
        num_words = len(self.lexicon)
        random_word = random.choice(list(self.lexicon))

        s = (f"*-*-*-*-*-*-*-*-*-*-*-*\nLexicon: {self.dict_name}\nNumber of words: {num_words}"
            + f"\nRandom word: {random_word}\n*-*-*-*-*-*-*-*-*-*-*-*")

        return s

    def __contains__(self, w):
        return w.upper() in self.lexicon

    def __iter__(self):
        return iter(self.lexicon)

    def len_k_words(self, k):
        k_words = [w for w in self if len(w) == k]
        k_words.sort()
        return k_words
        

if __name__ == "__main__":
    l = Lexicon("NWL23", "nwl23.json")
    two_letter_words = l.len_k_words(2)
    vowels = ['A', 'E', 'I', 'O', 'U', 'Y']
    two_letter_words_no_vowels = [w for w in two_letter_words if len([v for v in vowels if v in w]) == 0]
    print(two_letter_words_no_vowels)
