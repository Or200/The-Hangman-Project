import re
import random

with open("data/words.txt") as words_file:
    words = words_file.read()

words_list = re.split(r'\W+', words)[1:-1]

def choose_secret_word(words: list[str]) -> str:
    word_choose = words_list[random.randint(0, (len(words) - 1))]
    return word_choose
