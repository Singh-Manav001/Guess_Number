import random
secret_number = random.randint(1,100)  # Predefined number for simplicity
attempts = 0
max_attempts = 7

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100. You have 7 attempts.")

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1
    
    if guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100.")
        continue
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number in", attempts, "attempts.")
        break

if attempts == max_attempts and guess != secret_number:
    print("Game Over! The number was", secret_number, ".")