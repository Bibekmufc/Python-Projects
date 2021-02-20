import random
import os
from hangman_art import stages, logo
from hangman_words import word_list


lives = 6

chosen_word = random.choice(word_list)

print(logo)

# Testing code

# emoty list
display = []

# Displaying ____ according to the length of the word
for _ in range(len(chosen_word)):
    display += "_"

#default state of game
end_of_game = False

#game running
while not end_of_game:
    # User inputs their guess letter
    guess = input("Guess a letter: ").lower()

    #os.system('cls')

    #if guessed letter already guessed
    if guess in display:
        print(f"You've already guessed {guess}")

    #alert user to only enter 1 letter and no numbers
    if not(len(guess) == 1):
        print("You can only type 1 letter")
        continue
    elif not(guess.lower() in "abcdefghijklmnopqrstuvwxyz"):
        print("You can only type alphabets, not number!")
        continue
    else:
        # Check guessed word
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
    print(f"{' '.join(display)}")



    #if guessed letter not in the word
    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is not in the word. You lose a life")
        if lives == 0:
            end_of_game = True
            print("You lose")
            print(f'The word is {chosen_word}.')


    #Win condition
    if "_" not in display:
        end_of_game = True
        print("You've won!")

    #display the lives in ASCII format
    print(stages[lives])


input('Press Enter to Exit...')
