from .words import *

def init_state(secret: tuple, max_tries: int):
    my_dict = {
        "secret": secret[0],
        "display": secret[1],
        "guessed": set(),
        "wrong_guesses": 0,
        "max tries": max_tries
    }
    return my_dict

def validate_guess(ch: str, guessed: set[str]) -> tuple[bool, str]:
    if ch in guessed:
        return True, f"the letter is guessed"
    return False, f"{ch} is add"

def apply_guess(state: dict, ch: str) -> bool:
    return ch in state["secret"]

def is_won(state: dict) -> bool:
    return state["secret"] == "".join(state["display"])

def is_lost(state: dict) -> bool:
    return state["wrong_guesses"] >= state["max_tries"]
         
def render_display(state: dict) -> str:
    new_display = state["display"]
    for char in state["guessed"]:
       if char in state["secret"]:
            for idx , val in enumerate(state["secret"]):
                if val == char:
                    new_display[idx] = char

    state["display"] = new_display

               
def render_summary(state: dict) -> str:
    return f'the secret word is {state["secret"]}, your guesses is {state["guessed"]}'


        


