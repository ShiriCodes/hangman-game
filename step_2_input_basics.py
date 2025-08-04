HANGMAN_ASCII_ART = (("Welcome to the game Hangman") +
                     ("""
    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \\ / _' | '_ ' _ \\ / _' | '_ \\
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                        __/ |
                       |___/"""))
print(HANGMAN_ASCII_ART) #printing welcome sign
MAX_TRIES = 6
print(MAX_TRIES) #printing max number
guess = input("Guess a letter:") #asking for a guess input
print(guess) #mirroring guess