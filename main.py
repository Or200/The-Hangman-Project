from hangman.words import *
from hangman.game import *

if __name__ == "__main__":
    geese = init_state(choose_secret_word(words_list), 10)
    print(geese)
    render_display(geese)
    print(geese)
