import random


def roll_dice():
    # Welcome message
    print("Welcome to Roll the Dice!")

    # Initialize win counters
    player_wins = 0
    red_cloak_wins = 0

    # Continue the game until either the player or red cloak wins 3 rounds
    while player_wins < 3 and red_cloak_wins < 3:
        input("Press Enter to roll the dice...")

        # Roll the dice for the player
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        total = dice_1 + dice_2

        # Display the player's roll
        print(f"You rolled: {dice_1} and {dice_2}")
        print(f"Total: {total}")

        # Ask the player to guess if the next roll will be 'higher' or 'lower'
        guess = input("Do you think the next roll will be 'higher' or 'lower'? ").lower()

        # Roll the dice for the red cloak
        new_dice_1 = random.randint(1, 6)
        new_dice_2 = random.randint(1, 6)
        new_total = new_dice_1 + new_dice_2

        # Display the red cloak's roll
        print(f"You rolled: {new_dice_1} and {new_dice_2}")
        print(f"Total: {new_total}")

        # Determine the winner of the round
        if (new_total > total and guess == 'higher') or (new_total < total and guess == 'lower'):
            print("Correct! You guessed right.")
            player_wins += 1
        else:
            print("Incorrect! Red cloak man wins this round.")
            red_cloak_wins += 1

        # Display the current score
        print(f"Your wins: {player_wins}, Red cloak man's wins: {red_cloak_wins}")

    # Display the game outcome
    if player_wins == 3:
        print("Congratulations! You win! The man in the red cloak concedes defeat.")
        return "Prized Dagger"
    else:
        print("Game over! The man in the red cloak has defeated you.")
        return None

# Run the game if the script is executed directly
if __name__ == "__main__":
    roll_dice()
