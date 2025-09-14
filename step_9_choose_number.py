import tempfile
import os

def choose_word(file_path, index):
    """Return the number of unique words and the word at circular position 'index' (1-based)."""
    with open(file_path, "r", encoding="utf-8") as f:
        words = f.read().split()

    unique_words_num = len(set(words))
    circular_index = (index - 1) % len(words)
    chosen_word = words[circular_index]

    return (unique_words_num, chosen_word)


def main():
    test_data = "hangman song most broadly is a song hangman work music work broadly is typically"
    tmp_file = tempfile.NamedTemporaryFile("w+", encoding="utf-8", delete=False)
    try:
        tmp_file.write(test_data)
        tmp_file.close()

        result1 = choose_word(tmp_file.name, 3)
        assert result1 == (9, 'most'), f"Expected (9, 'most'), got {result1}"

        result2 = choose_word(tmp_file.name, 15)
        assert result2 == (9, 'hangman'), f"Expected (9, 'hangman'), got {result2}"

        print("✅ All tests passed!")

    finally:
        os.remove(tmp_file.name)


if __name__ == "__main__":
    main()