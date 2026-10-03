import random

# List of 5 predefined words
words = ["python", "java", "computer", "program", "coding"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum incorrect guesses
max_attempts = 6
wrong_guesses = 0

# Display word with blanks
display_word = ["_"] * len(word)

print("================================")
print("       WELCOME TO HANGMAN")
print("================================")
print("Guess the word one letter at a time!")
print("You have 6 incorrect guesses.\n")

# Main game loop
while wrong_guesses < max_attempts and "_" in display_word:

    print("Word:", " ".join(display_word))
    print("Guessed letters:", " ".join(guessed_letters))
    print("Incorrect guesses left:", max_attempts - wrong_guesses)

    guess = input("Enter a letter: ").lower()

    # Check if input is a single alphabet
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.\n")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter. Try again.\n")
        continue

    guessed_letters.append(guess)

    # Correct guess
    if guess in word:
        print("Correct guess!\n")

        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess

    # Incorrect guess
    else:
        wrong_guesses += 1
        print("Wrong guess!\n")

# Game result
if "_" not in display_word:
    print("================================")
    print("🎉 Congratulations! You won!")
    print("The word was:", word)
    print("================================")

else:
    print("================================")
    print("Game Over!")
    print("The correct word was:", word)
    print("================================")