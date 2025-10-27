
def prompt_guess() -> str:
    while True:
        char_input = input("Please input char: ")
        if char_input.isalpha():
            return char_input
        print("Error - add 1 char in abc")
