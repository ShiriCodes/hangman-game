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

def print_hangman(num_of_tries):
    """Prints hangman photo based on number of tries"""
    for line in HANGMAN_PHOTOS[num_of_tries]:
        print(line)

def main():
    print_hangman(0)
    print_hangman(1)
    print_hangman(2)
    print_hangman(3)
    print_hangman(4)
    print_hangman(5)
    print_hangman(6)


if __name__ == '__main__':
    main()