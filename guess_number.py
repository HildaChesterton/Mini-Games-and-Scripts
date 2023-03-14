import random

def play_game():
    answer = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100. Can you guess what it is?")
    num_guesses = 0
    while True:
        guess = input("Enter your guess: ")
        num_guesses += 1
        try:
            guess = int(guess)
        except ValueError:
            print("That's not a valid number, please try again.")
            continue
        if guess < 1 or guess > 100:
            print("Your guess is out of range, please try again.")
        elif guess < answer:
            print("Your guess is too low, try again.")
        elif guess > answer:
            print("Your guess is too high, try again.")
        else:
            print("Congratulations, you guessed the number in", num_guesses, "guesses!")
            break

def main():
    play_game()

if __name__ == "__main__":
    main()
