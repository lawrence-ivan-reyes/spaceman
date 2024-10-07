import random

def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
        return True

def get_guessed_word(secret_word, letters_guessed):
    guessed_word = ""
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word += letter
        else:
            guessed_word += "_"
        return guessed_word

def is_guess_in_word(guess, secret_word):
    return guess in secret_word


def spaceman(secret_word):
    print("Welcome to Spaceman!")
    print("To play, guess the secret word one letter at a time.\nYou have 7 chances, and for each incorrect guess, a part of the spaceman will be drawn.")
    print(f"\nThe secret word has {len(secret_word)} letters. Good luck and have fun!\n")

    letters_guessed = [] 
    guesses_left = 7

    while guesses_left > 0:
        print("\nCurrent guess: " + get_guessed_word(secret_word, letters_guessed))
        print(f"You have {guesses_left} guesses left!")

        guess = input("Please guess one letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid. Please guess a single letter!")
            continue

        if guess in letters_guessed:
            print("Uh-oh. You already guessed that letter!")
            continue

        letters_guessed.append(guess)

        if is_guess_in_word(guess, secret_word):
            print("Good guess!")
        else:
            print("Incorrect guess!")
            guesses_left -= 1

        if is_word_guessed(secret_word, letters_guessed):
            print("Yay! You guessed the word: " + secret_word)
            break
        else:
            print("Sorry, you lost. The secret word was: " + secret_word)

#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)