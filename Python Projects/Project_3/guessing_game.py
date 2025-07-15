import random 

easy_words = ["apple", "train", "tiger", "money", "india"]
medium_words = ["python", "bottle", "monkey", "planet", "laptop"]
hard_words = ["elephant", "diamond", "umbrella", "computer", "mountain"]

print("Welcome to the password guessing game")
print("Choose a difficulty level: easy, medium or hard")

level = input('Enter difficulty: ').lower()
if level == "easy":
    secret_word = random.choice(easy_words)
elif level == "medium":
    secret_word = random.choice(medium_words)
elif level == "hard":
    secret_word = random.choice(hard_words)
else:
    print("Invalid choice. Defaulting to easy level")
    secret_word = random.choice(easy_words)
    
attempts = 0
print("\nGuess the secret password!")

while True:
    guess = input("Enter your guess: ").lower()
    attempts += 1
    if guess == secret_word:
        print(f"Congratulations! You guessed the password in {attempts} attempts.")
        break
    
    hint = ""
    
    for i in range(len(secret_word)):
        if i < len(guess) and guess[i] == secret_word[i]:
            hint += guess[i]
        else:
            hint += "_"
    print("Hint:" + hint)
    
    if attempts == 5:
        print("You have reached the maximum number of attempts. The password was:", secret_word)
        break
    
    print("Game Over.")