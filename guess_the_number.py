import random

def guess_number():
    number = random.randint(1, 100)
    guess = None
    guess_count = 0

    while guess != number:
        guess = input("Guess a number between 1 and 100: ")
        if not guess.isdigit():
            print("Invalid input, please enter a number.")
            continue
        guess = int(guess)
        guess_count += 1
        if guess < number:
            print("Too low, try again.")
        elif guess > number:
            print("Too high, try again.")
        else:
            print(f"Congratulations, you guessed the number in {guess_count} guesses!")

def main():
    guess_number()

if __name__ == "__main__":
    main()
