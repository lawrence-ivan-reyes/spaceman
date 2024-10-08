import random

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
        if letter not in letters_guessed: # if any letter of the secret word hasn't been guessed, return False
            return False
    return True # if all letters are guessed, return True

# function to display the CURRENT state of the guessed word
def get_guessed_word(secret_word, letters_guessed):
    guessed_word = ""
    for letter in secret_word: # for every letter in the secret word, check if it's been guessed
        if letter in letters_guessed:
            guessed_word += letter # if guessed, add the letter to the guessed word string
        else:
            guessed_word += "_" # if not guessed, show an underscore instead
    return guessed_word

# function to check if the guesser letter is in the secret word
def is_guess_in_word(guess, secret_word):
    return guess in secret_word

# main game function
def spaceman(secret_word):
    print("Welcome to Spaceman!")
    print("To play, guess the secret word one letter at a time.\nYou have 7 chances, and for each incorrect guess, a part of the spaceman will be drawn.")
    print(f"\nThe secret word has {len(secret_word)} letters. Good luck and have fun!\n")

    letters_guessed = [] # initializing a list in order to store the letters that have been guessed
    guesses_left = 7 # player starts with 7 guesses

    # this loop will continue until guesses run out OR until the word has been correctly guessed 
    while guesses_left > 0:
        print("Current guess: " + get_guessed_word(secret_word, letters_guessed))
        print(f"You have {guesses_left} guesses left!")

        guess = input("\nPlease guess one letter: ").lower()

        if len(guess) != 1 or not guess.isalpha(): # this is ensuring a valid input of a SINGLE alphabetic character 
            print("\nInvalid. Please guess a single letter!")
            continue 

        if guess in letters_guessed:
            print("\nUh-oh. You already guessed that letter!")
            continue # will skip the rest of the loop and ask for another letter

        letters_guessed.append(guess)

        if is_guess_in_word(guess, secret_word):
            print("\nGood guess!")
        else:
            print("\nIncorrect guess.")
            guesses_left -= 1

        if is_word_guessed(secret_word, letters_guessed):
            print("Yay! You guessed the secret word: " + secret_word)
            break # game ends here if the word has been guessed
    else:
        print("Sorry, you lost. The secret word was: " + secret_word) # only happens if the player runs out of guesses

secret_word = load_word()
spaceman(secret_word)