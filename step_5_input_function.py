def is_valid_input(letter_guessed):
    """
    This function is meant for validating input,
    which is meant to be 1 letter long and not contain special symbols

    :param letter_guessed: A string to be validated.
    :type letter_guessed: str
    :return: True if the input is a single letter, False otherwise.
    :rtype: bool
    """
    return len(letter_guessed) == 1 and letter_guessed.isalpha()

def main():
    print(is_valid_input('a'))  # True
    print(is_valid_input('A'))  # True
    print(is_valid_input('$'))  # False
    print(is_valid_input("ab"))  # False
    print(is_valid_input("app$"))  # False


if __name__ == '__main__':
    main()
