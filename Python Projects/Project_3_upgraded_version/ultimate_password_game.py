import random
import time
from random_word import RandomWords
from colorama import Fore, Style, init
from PyDictionary import PyDictionary

# Initialize
init(autoreset=True)
r = RandomWords()
dictionary = PyDictionary()

HISTORY_FILE = "Python Projects\\Project_3_upgraded_version\\history.txt"
high_score = None  # global high score

def get_random_word(min_length=4, max_length=10):
    """
    Get a random word from API which has a meaning.
    If API fails or no valid word found, return from fallback list.
    """
    fallback_words = ["apple", "train", "planet", "python", "monkey", "tiger", "laptop"]
    try:
        attempts = 0
        while attempts < 20:  # safety limit
            word = r.get_random_word()
            if word and min_length <= len(word) <= max_length:
                meaning = dictionary.meaning(word)
                if meaning:  # found meaning
                    return word.lower()
            attempts += 1
        # fallback: pick random real word from list
        return random.choice(fallback_words)
    except:
        return random.choice(fallback_words)

def generate_word_list(count, min_len, max_len):
    return [get_random_word(min_len, max_len) for _ in range(count)]

def print_welcome():
    print(Fore.CYAN + "="*60)
    print(Fore.GREEN + "🎉 Welcome to the Ultimate Password Guessing Game! 🎉")
    print(Fore.YELLOW + "Guess the password based on difficulty level and see the meaning later!")
    print(Fore.CYAN + "="*60)

def save_history(level, secret_word, attempts, time_taken):
    with open(HISTORY_FILE, "a") as file:
        file.write(f"Level: {level.title()}, Word: {secret_word}, Attempts: {attempts}, Time: {time_taken:.2f}s\n")

def show_meaning(word):
    print(Fore.MAGENTA + "\n📚 Meaning of the word:")
    meaning = dictionary.meaning(word)
    if meaning:
        for part, defs in meaning.items():
            print(f"{part}: {defs[0]}")
            break  # just show first definition
    else:
        print("No meaning found.")

def play_game():
    global high_score

    easy_words = generate_word_list(5, 4, 5)
    medium_words = generate_word_list(5, 6, 7)
    hard_words = generate_word_list(5, 8, 10)

    print_welcome()

    level = input(Fore.CYAN + 'Enter difficulty (easy / medium / hard): ').lower()

    if level == "easy":
        secret_word = random.choice(easy_words)
        max_attempts = 6
    elif level == "medium":
        secret_word = random.choice(medium_words)
        max_attempts = 7
    elif level == "hard":
        secret_word = random.choice(hard_words)
        max_attempts = 8
    else:
        print(Fore.RED + "❗ Invalid choice. Defaulting to easy level.")
        secret_word = random.choice(easy_words)
        max_attempts = 6

    print(Fore.YELLOW + f"\n✨ Level selected: {level.title()}. I've chosen a secret password. It has {len(secret_word)} letters! You have {max_attempts} attempts!\n")


    attempts = 0
    start_time = time.time()

    while attempts < max_attempts:
        guess = input(Fore.BLUE + f"Attempt {attempts+1}/{max_attempts} - Enter your guess: ").lower()
        attempts += 1

        if guess == secret_word:
            time_taken = time.time() - start_time
            print(Fore.GREEN + f"\n✅ Congratulations! You guessed the password in {attempts} attempts and {time_taken:.2f}s! 🎉")

            # High score check
            if high_score is None or attempts < high_score:
                high_score = attempts
                print(Fore.LIGHTGREEN_EX + f"🏆 New High Score! Fewest attempts so far: {high_score}")

            save_history(level, secret_word, attempts, time_taken)
            show_meaning(secret_word)
            break

        # Generate hint
        hint = ''.join([guess[i] if i < len(secret_word) and i < len(guess) and guess[i] == secret_word[i] else '_' 
                        for i in range(len(secret_word))])
        print(Fore.YELLOW + f"❓ Hint: {hint}")

        if attempts < max_attempts:
            print(Fore.LIGHTCYAN_EX + f"🔁 Attempts left: {max_attempts - attempts}\n")
        else:
            print(Fore.RED + "\n❌ You've reached the maximum number of attempts.")
            print(Fore.RED + f"The secret password was: '{secret_word}'")
            save_history(level, secret_word, attempts, time.time() - start_time)
            show_meaning(secret_word)

            # 👉 YEH NEW LINE add ki hai:
            print(Fore.MAGENTA + "🤖 The computer won this time! Better luck next time!")

    print(Fore.CYAN + "\n⭐ Game Over ⭐\n")

if __name__ == "__main__":
    while True:
        play_game()
        again = input(Fore.CYAN + "Do you want to play again? (y/n): ").lower()
        if again != 'y':
            print(Fore.MAGENTA + "👋 Thanks for playing! Check 'history.txt' for your game history. Goodbye!")
            break
