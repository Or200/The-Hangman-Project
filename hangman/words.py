import re
import random

with open("data/words.txt") as words_file:
    words = words_file.read()

words_list = re.split(r'\W+', words)[1:-1]

def choose_secret_word(words: list[str]) -> tuple[str, list]:
    display_char = []
    word_choose = words_list[random.randint(0, (len(words) - 1))]
    for i in range(len(word_choose)):
        display_char.append("_")
    
    return word_choose, display_char



