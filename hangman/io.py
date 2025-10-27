
def prompt_guess() -> str:
    while True:
        char_input = input("Please input char: ")
        if char_input.isalpha():
            return char_input
        print("Error - add 1 char in abc")

def print_status(state: dict) -> None:
    print(f"your word is {"".join(state["display"])}, your guesses is {state["guessed"]}, your Remaining tries is {state["max tries"] - state["wrong_guesses"]}")

