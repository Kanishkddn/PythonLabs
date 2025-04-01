def choose_word():
    words = ["python", "hangman", "computer", "programming", "developer"]
    return words[len(words) % 5]  # A simple way to pick a word without random

def display(word, guessed_letters):
    result = ""
    for letter in word:
        if letter in guessed_letters:
            result += letter + " "
        else:
            result += "_ "
    return result.strip()

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    
    while attempts > 0:
        print("\nWord:", display(word, guessed_letters))
        print(f"Attempts left: {attempts}")
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not ('a' <= guess <= 'z'):
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print("Wrong guess!")

        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            break
    else:
        print("\nGame Over! The word was:", word)

if __name__ == "__main__":
    hangman()
