'''import random
print("Welcome to the number guessing game!")

print("I am thinking of a number between 1 and 100.")
level = input("Choose a difficulty level: easy or hard")

number1 = random.choice(range(1, 100))

if level == "easy":
    print("You have 10 attempts to guess the number.")

    for i in range(10):
        guess = int(input("Guess the number: "))
        if guess != number1:
            if guess > number1:
                print("Too high!")
            elif guess < number1:
                print("Too low!")
        elif guess == number1:
            print("You guessed correctly. You win!")
            break
    else:
        print("You ran out of attempts . You lose!")
else:
    print("You have 5 attempts to guess the number.")

    for i in range(5):
        guess = int(input("Guess the number: "))
        if guess != number1:
            if guess > number1:
                print("Too high!")
            elif guess < number1:
                print("Too low!")
        elif guess == number1:
            print("You guessed correctly. You win!")
            break
    else:
        print("You ran out of attempts. You lose!")'''

# With Functions
import random
def get_attempts(level):
    if level == "easy":
        return 10
    else:
        return 5

def get_level():
    while True:
        level = input("Choose a difficulty level: easy or hard").strip().lower()
        if level in ("easy", "hard") :
            return level
        print("Invalid input. Please type 'easy' or 'hard'")

def play_game(number,attempts):
    for i in range(attempts):
        remaining = attempts - i
        print(f"Attempts remaining: {remaining}")

        guess = int(input("Guess the number: "))
        if guess == number:
            print("You guessed correctly. You win!")
        elif guess > number:
            print("Too high!")
        else:
            print("Too low!")
    print("You ran out of attempts. You lose!")
    return False

def main():
    print("Welcome to the number guessing game!")
    print("I am thinking of a number between 1 and 100.")

    level = get_level()
    attempts = get_attempts(level)
    number = random.randint(1, 100)
    play_game(number,attempts)

main()