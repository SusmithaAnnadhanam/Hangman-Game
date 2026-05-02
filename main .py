import random
import hangmanStages
import wordsHangman
import random
logo = r"""
 _    _                                         

| |  | |                                        
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| |  | | (_| | | | | (_| | | | | | | (_| | | | |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |                      
                    |___/                       
"""
print(logo)
lives = 6
chosen_word = random.choice(wordsHangman.words)
display = ["_" for _ in chosen_word]
guessed_letters = [] 

game_over = False

while not game_over:
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'. Try a different letter!")
        continue
    guessed_letters.append(guess)
    if guess in chosen_word:
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                display[position] = guess
        print("Good job!")
    else:
        lives -= 1
        print(f"'{guess}' is not in the word. You lose a life.")
    print(hangmanStages.stages[lives])
    print(f"Word: {' '.join(display)}")
    print(f"Guessed so far: {', '.join(guessed_letters)}") 
    print(f"Lives remaining: {lives}")
    if "_" not in display:
        game_over = True
        print("Congratulations, you win!")
    elif lives == 0:
        game_over = True
        print(f"Game over. The word was: {chosen_word}")
