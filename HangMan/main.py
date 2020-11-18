import random
from hangman_art import stages, logo
from hangman_hard import word_list
from hangman_easy import word_list_easy

from replit import clear

print(logo)
game_is_finished = False
lives = len(stages) - 1
choice = input("Please enter your choice - easy or hard: ")

if choice == "easy":
  chosen_word = random.choice(word_list_easy)
else:
  chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"

while not game_is_finished:
    guess = input("Guess a letter: ").lower()

    #Use the clear() function imported from replit to clear the output between guesses.
    clear()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print(f"You lose :(, word was {chosen_word}")

    if not "_" in display:
        game_is_finished = True
        print("You win.")

    print(stages[lives])
