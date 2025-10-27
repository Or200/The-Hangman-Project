from hangman.words import *
from hangman.game import apply_guess, update_guessed, render_display, init_state, update_wrong_guessed, choose_secret_word, is_won, is_lost
from hangman.io import print_status, print_result, prompt_guess

def play(words: list[str], max_tries: int = 6) -> None:
    game_word = choose_secret_word(words)
    word_dict = init_state(game_word, max_tries)
    # print(game_word)
    # print(word_dict)
    while True:
        
        char_input = prompt_guess()
        if apply_guess(word_dict, char_input):
            update_guessed(word_dict, char_input)
            render_display(word_dict)
            print_status(word_dict)
            if is_won(word_dict):
                print_result(word_dict)
                break
        else:
            update_guessed(word_dict, char_input)
            update_wrong_guessed(word_dict, char_input)
            print_status(word_dict)
            if is_lost(word_dict):
                print_result(word_dict)
                break


if __name__ == "__main__":
    play(words_list, 10)
