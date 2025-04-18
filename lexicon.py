import random
import json

class Lexicon:
    def __init__(self, dict_name, dict_file):
        self.dict_name = dict_name
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

if __name__ == "__main__":
    l = Lexicon("NWL23", "nwl23.json")
    two_letter_words = l.len_k_words(2)
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    two_letter_words_no_vowels = [w for w in two_letter_words if len([v for v in vowels if v in w]) == 0]
    print(two_letter_words_no_vowels)
