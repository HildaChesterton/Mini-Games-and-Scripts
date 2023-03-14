import random

def play_game():
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)

    while True:
        player_choice = input("Rock, paper, or scissors? ").lower()
        if player_choice not in options:
            print("Invalid input, please enter 'rock', 'paper', or 'scissors'.")
            continue

        if player_choice == computer_choice:
            print(f"It's a tie! Both players chose {player_choice}.")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'paper' and computer_choice == 'rock') or \
             (player_choice == 'scissors' and computer_choice == 'paper'):
            print(f"Congratulations, you won! {player_choice} beats {computer_choice}.")
        else:
            print(f"Sorry, you lost. {computer_choice} beats {player_choice}.")
        break

def main():
    play_game()

if __name__ == "__main__":
    main()
