# Hangman Python Game

A classic command-line implementation of the Hangman word-guessing game. This project features ASCII art visuals and modular Python logic.

## 🚀 Features
- **Randomized Gameplay**: Pulls words from a dedicated word list module.
- **Visual Progress**: Displays the hangman gallows status using ASCII art.
- **Duplicate Prevention**: Tracks your previous guesses and prevents you from losing lives on repeat letters.
- **Real-time Feedback**: Shows lives remaining, letters guessed, and current word progress.

## 📁 Project Files
- `main.py`: The primary script that runs the game loop.
- `wordsHangman.py`: A Python module containing the list of secret words.
- `hangmanStages.py`: A Python module containing the ASCII stages of the hangman.

## 🛠️ Requirements
- Python 3.x

## 🕹️ How to Run
1. Ensure you have `main.py`, `wordsHangman.py`, and `hangmanStages.py` in the same directory.
2. Open your terminal or command prompt.
3. Run the following command:
   ```bash
   python main.py
   ```

## 📜 Rules
1. You start with **6 lives**.
2. Guess one letter at a time to uncover the secret word.
3. Each incorrect guess results in the loss of one life and the progression of the hangman drawing.
4. You win if you reveal all the letters in the word.
5. You lose if the hangman is fully drawn (0 lives remaining).

---
*Created as a Python logic exercise.*
