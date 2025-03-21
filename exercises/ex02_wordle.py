"""This is the Worlde project for Comp110"""

__author__ = "730768516"


def main(secret: str) -> None:
    """Entrypoint of program and main game loop"""
    turns: int = 1
    maximum_turns: int = 6
    win: bool = False
    """These say that you start with 1 turn and you have max 6 and the program stops when you win"""

    while turns <= maximum_turns and not win:
        print(f"=== Turn {turns}/{maximum_turns} ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {turns}/6 turns!")
            win = True
        turns = turns + 1
        if not win:
            print("X/6 - Sorry, try again tomorrow!")


"""This is saying that you get a number of turns starting with 1 and up to 6. While the number is less than 6
you get to keep trying and it will say your turns/6. Then it will take you guess and 'codify' the emoji results
of the guess vs the actual of the secret word by making us of the 'emojified' function. Finally, it win
it will say you won in x amount of turn or if you lose it is x/6 and the try again tmr"""


def contains_char(word: str, character: str) -> bool:
    """This will check if the character matches at a given index in the word."""
    assert len(character) == 1, f"len('{character}') is not 1"
    index = 0
    while index < len(word):
        if word[index] == character:
            return True
        index = index + 1
    return False


"""This essentially checks the length of the word to compare to given word """


def emojified(guess: str, secret_word: str) -> str:
    # Takes the guess and compares it with the secret word and returns a white, green, or yellow emoji box
    assert len(guess) == len(secret_word), "Guess must be same length as sectret"
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    """These are the emoji colors of the boxes which tell you if your word is correct or not"""
    word = ""
    index = 0
    while index < len(guess):
        if guess[index] == secret_word[index]:
            word = word + GREEN_BOX
        elif contains_char(secret_word, guess[index]):
            word = word + YELLOW_BOX
        else:
            word = word + WHITE_BOX
        index = index + 1
    return word


"""Takes the whole thing of i = i + 1 from class until it is = to intended output where it moves to false"""
"""This takes the index of the guess word and compares to the secret word and results in the color of the box"""


def input_guess(words_length: int) -> str:
    guess = input(f"Enter a {words_length} character word: ")
    """This takes the word length from the guess"""
    while len(guess) != words_length:
        guess = input(f"That wasn't {words_length} chars! Try again: ")
    return guess


"""This basically just takes the length of the guess and compares it to length of word to see if it matches"""
"""Pretty much says that the guess as an int needs to match int of the secret word"""


if __name__ == "_main_":
    main(secret="codes")
