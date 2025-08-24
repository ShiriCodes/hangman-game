def try_update_letter_guessed(letter_guessed: str, old_letters_guessed: list[str]) -> bool:
    """
    If 'letter_guessed' is a single English letter not already guessed (case-insensitive),
    it is added to 'old_letters_guessed' and the function returns True.
    Otherwise, prints 'X' and the sorted list of already guessed letters in lowercase,
    separated by ' -> ', and returns False.

    :param letter_guessed: An english letter.
    :param old_letters_guessed: A list of letters user already guessed.
    :return: True or False
    """

    if  (len(letter_guessed) == 1
        and letter_guessed.isalpha()
        and letter_guessed.casefold()  not in [c.casefold() for c in old_letters_guessed]
             ):
        old_letters_guessed.append(letter_guessed)
        return True

    else:
        print("X")
        print(" -> ".join(sorted(c.lower() for c in old_letters_guessed)))
        return False



def main():
    old_letters = ['a', 'p', 'c', 'f']
    print(try_update_letter_guessed('A',old_letters))
    print(try_update_letter_guessed('s', old_letters))
    print(try_update_letter_guessed('$', old_letters))
    print(try_update_letter_guessed('d', old_letters))
    print(old_letters)





if __name__ == '__main__':
    main()
