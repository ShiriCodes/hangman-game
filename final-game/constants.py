"""This file contains the constants for the Hangman game."""
#user interface messages:
FILE_PATH_REQUEST = "Enter file path: "
WORD_INDEX_REQUEST = "Enter index: "
LETTER_REQUEST = "Guess a letter: "
START_MESSAGE = "Let's start!"
INVALID_GUESS_MESSAGE = "X"
BAD_GUESS_MESSAGE = ":("
WINNING_MESSAGE = "WIN"
LOSING_MESSAGE = "LOSE"

#no. of maximum tries before a player loses:
MAX_TRIES = 6

#welcome to game graphic:
HANGMAN_ASCII_ART = """Welcome to the game Hangman.
                     
 _    _
| |  | |
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
|  __  |/ _' | '_ \\ / _' | '_ ' _ \\ / _' | '_ \\
| |  | | (_| | | | | (_| | | | | | | (_| | | | |
|_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                     __/ |
                    |___/"""

#hangman graphic for different stages in the game.
HANGMAN_PHOTOS = {
    0: [
        "    x-------x",
        ""
    ],

    1: [
        "    x-------x",
        "    |",
        "    |",
        "    |",
        "    |",
        "    |"
    ],

    2: [
        "    x-------x",
        "    |       |",
        "    |       0",
        "    |",
        "    |",
        "    |"
    ],

    3: [
        "    x-------x",
        "    |       |",
        "    |       0",
        "    |       |",
        "    |",
        "    |"
    ],

    4: [
        "    x-------x",
        "    |       |",
        "    |       0",
        "    |      /|\\",
        "    |",
        "    |"
    ],

    5: [
        "    x-------x",
        "    |       |",
        "    |       0",
        "    |      /|\\",
        "    |      /",
        "    |"
    ],

    6: [
        "    x-------x",
        "    |       |",
        "    |       0",
        "    |      /|\\",
        "    |      / \\",
        "    |"
    ]
}
