def show_hidden_word(secret_word: str, old_letters_guessed: list[str]):
    """
    Returns a string representing the current guessed state of secret_word.
    Letters that have been guessed are shown; others are shown as underscores.
    """
    secret_word_state = []
    hidden_letter = "_"
    for letter in secret_word:
        if letter in old_letters_guessed:
            secret_word_state.append(letter)
        else:
            secret_word_state.append(hidden_letter)
    return " ".join(secret_word_state)

def check_win(secret_word: str, old_letters_guessed: list[str]):
    """Checks if user guessed all letters of secret word."""
    return '_' not in show_hidden_word(secret_word,old_letters_guessed)


def main():
    secret_word = 'Apple'
    old_letters_list = ['p','o','s']
    print(show_hidden_word(secret_word, old_letters_list))
    print(check_win(secret_word, old_letters_list))

if __name__ == '__main__':
    main()