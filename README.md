# Hangman Game - Python Implementation

This repository documents the **step-by-step development** of the classic Hangman game in Python.  
It started as a series of small exercises and gradually evolved into a complete, modular, and interactive game.

---

## 📁 Contents

### Development Steps
* **step_1_welcome.py** – prints the welcome screen and Hangman illustrations  
* **step_2_input_basics.py** – defines constants and gets first user input  
* **step_3_display_word.py** – displays hidden word as underscores  
* **step_4_input_validation.py** – adds error handling for invalid guesses  
* **step_5_input_function.py** – wraps input validation into a reusable function with documentation  
* **step_6_guess_validation.py** – checks guessed letters, updates guessed letters list, prints feedback if invalid  
* **step_7.1_show_hidden_word.py** – displays the current state of the secret word  
* **step_7.2_show_hidden_word_check_win.py** – displays the guessed state of the secret word and checks for a win  
* **step_8_print_hangman.py** – saves ASCII art of hangman as a constant and prints art based on number of tries  
* **step_9_choose_number.py** – implements a function that returns the number of unique words and the word at the given circular index  

### Final Version
* **/final-game/constants.py** – stores ASCII art and default word list  
* **/final-game/mechanics.py** – core game logic (input validation, word selection, win/loss checks)  
* **/final-game/main.py** – main entry point that ties everything together  

---

## 🎮 How to Run (final game)

Clone the repository and run the final version (from the repository root):

```bash
git clone https://github.com/YOUR_USERNAME/hangman-game.git
cd hangman-game/final-game      # or `cd hangman-game\final-game` on Windows
python main.py                  # or `python3 main.py` on macOS / Linux
```
# Notes

* The program will prompt for a words file path and a word index.

* If you created a words.txt in the repository root, and you run main.py from final-game, enter ../words.txt when prompted for the file path.

* If you run main.py from the repository root (cd hangman-game), enter final-game/words.txt (or final-game\words.txt on Windows).

Example words.txt content (space-separated words):

```
cat dog mom balloon child hangman
```
Example interaction:
```
Enter file path: ../words.txt

Enter index: 1
```
Recommended Python: Python 3.8+. Use python on Windows or python3 on macOS/Linux depending on your environment.

# ✅ Example Output (final game)
```
Welcome to Hangman!
Guess the word:
_ _ _ _ _

Enter a letter:
```
# 🧩 Skills Demonstrated
* Modular program design

* Error handling and input validation

* File I/O and word selection from text files

* Use of sets, lists, and string operations

* Step-by-step development process leading to a working game
