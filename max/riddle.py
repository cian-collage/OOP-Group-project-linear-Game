"""
Program Name: riddle.py

Program Description:

This is a minigame module in the game
that the players play to engage themselves in the solving a riddle from the drunken elves
When they solve a riddle they receive a clue from them this is done 3 times.

Author: Max Ceban
Date: 30/11/2023
"""


def riddle_game():
    print("Time to solve the riddle!")

    # This is the original riddle for the user
    riddle = ("In dungeons deep or towers high,\nI flicker, dance, and catch the eye.\nA guardian in armor clad, "
              "Yet a servant to both good and bad.\nWhat am I?")

    print(riddle)

    # Attempts user has taken
    attempts = 0

    hint = "I stand tall, wax-clad, a silent sentinel, illuminating the shadows with my flickering dance."

    # Lets the user guess in the riddle game
    while True:
        print("Hint: ", hint)
        guess = input("What you think is the answer?\n")

        if guess.lower() == "candle" or guess.capitalize() == "CANDLE":
            print(f"Wise adventurer you are correct its a candle")
            break
        else:
            print(f"Incorrect guess try again")
            attempts += 1
            print("Hint: ", hint)


if __name__ == "__main__":
    riddle_game()
