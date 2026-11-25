
import random

# Step 1: Create a list of 5 words
words = ["python", "apple", "computer", "school", "mobile"]

# Step 2: Select a random word
secret_word = random.choice(words)

# Step 3: Store guessed letters
guessed_letters = []

# Step 4: Set maximum incorrect attempts
attempts = 6

print("==============================")
print("       HANGMAN GAME")
print("==============================")
print("Guess the secret word!")
print("You have 6 incorrect attempts.")

# Step 5: Start the game
while attempts > 0:

    display_word = ""

    # Show guessed letters and hidden letters
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Attempts remaining:", attempts)

    # Check whether the player won
    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You WON!")
        break

    # Get user input
    guess = input("Guess a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter!")
        continue

    # Check repeated guesses
    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue

    guessed_letters.append(guess)

    # Check the guessed letter
    if guess in secret_word:
        print("Correct guess!")
    else:
        print("Wrong guess!")
        attempts -= 1

# Step 6: Display losing message
else:
    print("\nGAME OVER!")
    print("The correct word was:", secret_word)

print("\nThank you for playing!")
