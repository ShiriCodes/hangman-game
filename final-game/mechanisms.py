"""This file contains the mechanics functions for the Hangman game."""
def check_win(secret_word: str, old_letters_guessed: list[str]) -> bool :
    """Checks if the user guessed all letters of the secret word.
    :param secret_word: The secret word to be guessed.
    :type secret_word: str
    :param old_letters_guessed: List of letters the user already guessed.
    :type old_letters_guessed: list[str]
    :return: True if all letters of the secret word were guessed, False otherwise.
    :rtype: bool
    """
    return '_' not in show_hidden_word(secret_word, old_letters_guessed)


def show_hidden_word(secret_word: str, old_letters_guessed: list[str]) -> str:
    """Returns the current guessed state of the secret word.
    Guessed letters are revealed; unguessed letters are shown as underscores.
    :param secret_word: The secret word to be guessed.
    :type secret_word: str
    :param old_letters_guessed: List of letters the user already guessed.
    :type old_letters_guessed: list[str]
    :return: The current guessed state of the secret word.
    :rtype: str
    """
    secret_word_state = []
    hidden_letter = "_"
    for letter in secret_word:
        if letter in old_letters_guessed:
            secret_word_state.append(letter)
        else:
            secret_word_state.append(hidden_letter)
    return " ".join(secret_word_state)

def check_valid_input(letter_guessed: str, old_letters_guessed: list[str]) -> bool:
    """Checks whether the input is a valid guess:
    - a single English letter
    - not already guessed (case-insensitive)
    :param letter_guessed: The letter guessed by the user.
    :type letter_guessed: str
    :param old_letters_guessed: List of letters already guessed by the user.
    :type old_letters_guessed: list[str]
    :return: True if the input is valid, False otherwise.
    :rtype: bool
    """
    return  (len(letter_guessed) == 1
        and letter_guessed.isalpha()
        and letter_guessed.casefold()  not in [c.casefold() for c in old_letters_guessed]
             )


def try_update_letter_guessed(letter_guessed: str, old_letters_guessed: list[str]) -> bool:
    """Tries to update the list of guessed letters with a new guess.
    If the guess is valid, the letter is added and True is returned.
    Otherwise, prints 'X' and the sorted list of already guessed letters,
    separated by ' -> ', and returns False.
    :param letter_guessed: The letter guessed by the user.
    :type letter_guessed: str
    :param old_letters_guessed: List of letters already guessed by the user.
    :type old_letters_guessed: list[str]
    :return: True if the guess was added, False otherwise.
    :rtype: bool
    """
    if  check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        print("X")
        print(" -> ".join(sorted(c.lower() for c in old_letters_guessed)))
        return False

def choose_word(file_path: str, index: int) -> str:
    """Returns the word at a circular position 'index' (1-based) from a file or default list.
    :param file_path: Path to the words file. If empty, a default word list is used.
    :type file_path: str
    :param index: The index of the word to return (1-based, circular).
    :type index: int
    :return: The chosen word.
    :rtype: str
    """
    if file_path == "":
        words = ["hangman"]
    else:
        with open(file_path, "r", encoding="utf-8") as f:
            words = f.read().split()

    circular_index = (index - 1) % len(words)
    chosen_word = words[circular_index]

    return chosen_word