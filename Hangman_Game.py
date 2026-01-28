import random

def play_hangman():
    words = ["python", "coding", "loop", "screen", "keyboard"]
    secret_word = random.choice(words)
    
    attempts_left = 6
    guessed_letters = []
    
    display_word = ['_'] * len(secret_word)

    print("Welcome to Hangman!")
    print(f"The word has {len(secret_word)} letters.")
    print("-------------------------------")

    while attempts_left > 0:
        print(f"\nWord: {' '.join(display_word)}")
        print(f"Attempts left: {attempts_left}")
        print(f"Guessed so far: {', '.join(guessed_letters)}")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print(">> Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print(f">> You already guessed '{guess}'. Try a different one.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print(f">> Good job! '{guess}' is in the word.")
            
            for index, letter in enumerate(secret_word):
                if letter == guess:
                    display_word[index] = guess
            
            if '_' not in display_word:
                print("\n-------------------------------")
                print(f"Congratulations! You guessed the word: {secret_word}")
                return True
        else:
            print(f">> Sorry, '{guess}' is not there.")
            attempts_left -= 1

    if attempts_left == 0:
        print("\n-------------------------------")
        print("Game Over! You ran out of attempts.")
        print(f"The word was: {secret_word}")
        return False

if __name__ == "__main__":
    while True:
        won = play_hangman()
        
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break
        print("\n" + "="*40 + "\n")
