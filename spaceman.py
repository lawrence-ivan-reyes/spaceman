# ACS 1100: Spaceman - Ivan Reyes

import random
from ascii_art import draw_spaceman

def load_word():
    words_txt = "words.txt"
    infile = open(words_txt, "r")
    words_list = infile.readlines()
    infile.close()
    
    # this is because the words are in words.txt are separated by 1 space
    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    for letter in secret_word: # checking if all of the letters in thge secret word have been guessed
        if letter not in letters_guessed: 
            return False
    return True 

def get_guessed_word(secret_word, letters_guessed):
    guessed_word = "" # creates a string that represents the current guessed state of the secret word
    for letter in secret_word: 
        if letter in letters_guessed:
            guessed_word += letter # reveals the letter if the user guessed correctly
        else:
            guessed_word += "_" # and this is for letters thast haven't been guessed yet
    return guessed_word

def is_guess_in_word(guess, secret_word):
    return guess in secret_word # checking if the user's guess is in the secret word

# main game function
def spaceman():
    while True: # stretch challenge: loop to keep playing if the user chooses 'yes' to playing again at the end
        secret_word = load_word() # now the secret word is loaded here after adding the above stretch challenge
        print("Welcome to Spaceman!")
        print("To play, guess the secret word one letter at a time.\nFor each incorrect guess, a part of the spaceman will be drawn.")
        print(f"\nThe secret word has {len(secret_word)} letters. Good luck and have fun!\n")

        letters_guessed = [] # to store the letters guessed by the user
        incorrect_guesses = 0 # stretch challenge: initializing this new variable to 0 to satisfy the spaceman ascii art
        max_incorrect_guesses = 7 # stretch challenge: initializing this variable to help with the ascii art challenge (since there are 7 stages in the ascii art file)

        # this loop will continue until guesses run out OR until the word has been correctly guessed 
        while incorrect_guesses < max_incorrect_guesses: # to account for the ascii art stretch challenge
            draw_spaceman(incorrect_guesses) # stretch challenge: draw spaceman based on incorrect guesses
            print("Current guess: " + get_guessed_word(secret_word, letters_guessed))
            print(f"You have {max_incorrect_guesses - incorrect_guesses} guesses left!") 

            guess = input("\nPlease guess one letter: ").lower()
            
            # to validate the user's guess
            if len(guess) != 1 or not guess.isalpha(): # stretch challenge: this is ensuring a valid input of a SINGLE alphabetic character 
                print("\nInvalid. Please guess a single letter!")
                continue # stretch challenge: goes back to beginning of loop to allow user to enter another guess without reducing guess count

            if guess in letters_guessed:
                print("\nUh-oh. You already guessed that letter!")
                continue 

            letters_guessed.append(guess)

            if is_guess_in_word(guess, secret_word):
                print("\nGood guess.")
            else:
                print("\nIncorrect guess.")
                incorrect_guesses += 1 # stretch challenge: incremenent incorrect guesses to draw the spaceman ascii art

            if is_word_guessed(secret_word, letters_guessed):
                print("\nYay! You guessed the secret word: " + secret_word) 
                break # exiting the guessing loop if the word was successfully guessed
        else:
            draw_spaceman(incorrect_guesses) # stretch challenge: draw spaceman when user loses game
            print("\nSorry, you lost. The secret word was: " + secret_word) # stretch challenge: shows user secret word when they lose

        # stretch challenge: asking user if they want to play again after the game ends
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nThanks for playing! See you next time.")
            break

# start game
spaceman()