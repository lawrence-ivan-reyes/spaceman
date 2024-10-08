import random
from ascii_art import draw_spaceman

def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

# function to check if the word has been FULLY guessed
def is_word_guessed(secret_word, letters_guessed):
    for letter in secret_word:
        if letter not in letters_guessed: 
            return False
    return True 

# function to display the CURRENT state of the guessed word
def get_guessed_word(secret_word, letters_guessed):
    guessed_word = ""
    for letter in secret_word: # for every letter in the secret word, check if it's been guessed
        if letter in letters_guessed:
            guessed_word += letter 
        else:
            guessed_word += "_" 
    return guessed_word

# function to check if the guesser letter is in the secret word
def is_guess_in_word(guess, secret_word):
    return guess in secret_word

# main game function
def spaceman():
    while True: # stretch challenge: loop to keep playing if the user chooses 'yes' to playing again at the end
        secret_word = load_word() # now the secret word is loaded here after adding the above stretch challenge
        print("Welcome to Spaceman!")
        print("To play, guess the secret word one letter at a time.\nFor each incorrect guess, a part of the spaceman will be drawn.")
        print(f"\nThe secret word has {len(secret_word)} letters. Good luck and have fun!\n")

        letters_guessed = [] # initializing a list in order to store the letters that have been guessed
        incorrect_guesses = 0 # stretch challenge: initializing this new variable to 0 to satisfy the spaceman ascii art
        max_incorrect_guesses = len(secret_word) # stretch challenge: initializing this variable to help with the ascii art challenge

        # this loop will continue until guesses run out OR until the word has been correctly guessed 
        while incorrect_guesses < max_incorrect_guesses: # to account for the ascii art stretch challenge
            draw_spaceman(incorrect_guesses) # stretch challenge: draw spaceman based on incorrect guesses
            print("Current guess: " + get_guessed_word(secret_word, letters_guessed))
            print(f"You have {max_incorrect_guesses - incorrect_guesses} guesses left!") 

            guess = input("\nPlease guess one letter: ").lower()

            if len(guess) != 1 or not guess.isalpha(): # stretch challenge: this is ensuring a valid input of a SINGLE alphabetic character 
                print("\nInvalid. Please guess a single letter!")
                continue # stretch challenge: goes back to beginning of loop to allow user to enter another guess without reducing guess count

            if guess in letters_guessed:
                print("\nUh-oh. You already guessed that letter!")
                continue # will skip the rest of the loop and ask for another letter

            letters_guessed.append(guess)

            if is_guess_in_word(guess, secret_word):
                print("\nGood guess.")
            else:
                print("\nIncorrect guess.")
                incorrect_guesses += 1 # stretch challenge: incremenent incorrect guesses to draw the spaceman ascii art

            if is_word_guessed(secret_word, letters_guessed):
                print("\nYay! You guessed the secret word: " + secret_word) 
                break # game ends here if the word has been guessed
        else:
            draw_spaceman(incorrect_guesses) # stretch challenge: draw spaceman when user loses game
            print("\nSorry, you lost. The secret word was: " + secret_word) # stretch challenge: shows user secret word when they lose

        # stretch challenge: asking user if they want to play again after the game ends
        play_again = input("\nThanks for playing. Would you like to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! See you next time.")
            break

# start game
spaceman()