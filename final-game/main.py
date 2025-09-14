"""This file contains the main logic for the Hangman game."""
from constants import FILE_PATH_REQUEST, WORD_INDEX_REQUEST, LETTER_REQUEST, START_MESSAGE, INVALID_GUESS_MESSAGE, BAD_GUESS_MESSAGE, WINNING_MESSAGE, LOSING_MESSAGE, HANGMAN_PHOTOS, HANGMAN_ASCII_ART, MAX_TRIES
from mechanisms import check_win, show_hidden_word, check_valid_input, try_update_letter_guessed, choose_word

def welcome(option: int = 1) -> None:
    """Displays a welcome message or the start prompt based on the given option.
    :param option: 1 for ASCII art and max tries, 2 for start message.
    :type option: int
    :return: None
    :rtype: None
    """
    if option == 1:
        print(HANGMAN_ASCII_ART)
        print(MAX_TRIES)
    if option == 2:
        print(START_MESSAGE)

def input_request(request: str, expected_type= str, sanitize: bool = False):
    """Handles user input requests, with optional type casting and sanitization.
    :param request: The input prompt text.
    :type request: str
    :param expected_type: The expected type of input (default: str).
    :type expected_type: type
    :param sanitize: If True, the input is converted to lowercase.
    :type sanitize: bool
    :return: The user input, cast to the expected type.
    :rtype: str | int
    """
    if expected_type == int:
        return int(input(request))
    elif sanitize:
        return input(request).lower()
    return input(request)

def print_hangman(num_of_tries: int) -> None:
    """Prints the hangman photo corresponding to the number of tries.
    :param num_of_tries: The current number of incorrect guesses.
    :type num_of_tries: int
    :return: None
    :rtype: None
    """
    for line in HANGMAN_PHOTOS[num_of_tries]:
        print(line)

def run_game() -> None:
    """Runs the main Hangman game loop.
    Handles user guesses, checks win/lose conditions,
    and prints game progress until the game ends.
    :return: None
    :rtype: None
    """
    old_letters_guessed = []
    tries = 0
    welcome()
    secret_word = choose_word(input_request(FILE_PATH_REQUEST), input_request(WORD_INDEX_REQUEST, int))
    welcome(2)
    print_hangman(tries)
    print(show_hidden_word(secret_word, old_letters_guessed))

    while tries < MAX_TRIES:
        letter_guessed = input_request(LETTER_REQUEST, sanitize=True)

        if not check_valid_input(letter_guessed, old_letters_guessed):
            print(INVALID_GUESS_MESSAGE)

            print(" -> ".join(sorted(c.lower() for c in old_letters_guessed)))
            continue

        try_update_letter_guessed(letter_guessed, old_letters_guessed)

        if letter_guessed.casefold() not in [c.casefold() for c in secret_word]:
            print(BAD_GUESS_MESSAGE)
            tries += 1
            print_hangman(tries)

        print(show_hidden_word(secret_word, old_letters_guessed))

        if check_win(secret_word, old_letters_guessed):
            print(WINNING_MESSAGE)
            break

    else:
        print(LOSING_MESSAGE)

def main():
    run_game()

if __name__ == '__main__':
    main()