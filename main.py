from hangman.my_words import *
from hangman.my_game import apply_guess, update_guessed, render_display, init_state, update_wrong_guessed, choose_secret_word, is_won
from hangman.my_io import print_status, print_result, prompt_guess

def play(words: list[str], max_tries: int = 6) -> None:
    game_word = choose_secret_word(words)
    word_dict = init_state(game_word, max_tries)
    print(game_word)
    # print(word_dict)
    while True:
        
        char_input = prompt_guess()
        if apply_guess(word_dict, char_input):
            update_guessed(word_dict, char_input)
            render_display(word_dict)
            print_status(word_dict)
            print_result(word_dict)
            if is_won(word_dict):
                print_result(word_dict)
                break
        else:
            update_guessed(word_dict, char_input)
            update_wrong_guessed(word_dict, char_input)
            print_status(word_dict)


if __name__ == "__main__":
    # play(words_list, 10)
    print_result({'secret': 'floor', 'display': ['_', '_', '_', '_', '_'], 'guessed': set(), 'wrong_guesses': 0, 'max tries': 10})


