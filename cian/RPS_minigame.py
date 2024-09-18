"""
Program Name: RPS_minigame.py

Author: Cian Anderson (C22793219) in Group ERROR 451

Program Description:
This is the Rock Papaer Scissors mini game method it allows the player to input a "Bet" that is taken from the players coins.
You compeat agains the Dice Goblin by choiseing 1 of 3 options and compairing them to the opponents choice.
If the player wins the "Bet" is dubbled and added back to them.
If the player loses the "Bet" is not re added to the coin total.
Date: 3/12/2023
"""

import random


def Rock_Paper_Scissors_Game(player):

    bet = int(input(f"You have {player.coins} coins\nhow many coins would you like to bet:\n"))  # input bet

    while bet > player.coins:  # makes sure player has enough coins
        if player.coins > 0:  #  if coins is > 0
            bet = int(input(f"You only have {player.coins} coins \nhow many coins would you like to bet:\n"))
        else:
            print("You have 0 coins so you can't play")
            break

    player.coins = player.coins-bet  # take bet away from coin total

    choice = input("1) Rock\n2) Paper\n3) Scissors\n")  # take in player options
    player_choice = ""  # initialize player choice
    opponent_choice = ""  # initialize opponent choice

    choice = 0  # reset choice variable
    while choice != "1" or "2" or "3" or "4":  # error check
        if choice == "1":
            player_choice = "Rock"
        elif choice == "2":
            player_choice = "Paper"
        elif choice == "3":
            player_choice = "Scissors"

        choice = random.randint(1, 3)  # Generate opponent choice 1 to 3 

        if choice == 1:
            opponent_choice = "Rock"
        elif choice == 2:
            opponent_choice = "Paper"
        elif choice == 3:
            opponent_choice = "Scissors"

    print("\nYour Choice:", player_choice)  # display player choice

    print("\nOpponents Choice:", opponent_choice, "\n")  # display opponent choice

    if player_choice == opponent_choice:  # if the same
        print(f"Both players selected {opponent_choice}. It's a tie!")
        Rock_Paper_Scissors_Game(player)  # restart game


    elif player_choice == "Rock":  # if Rock = player choice
        if opponent_choice == "scissors":  #  if Scissors = opponets choice
            print("Rock smashes scissors! You win!")
            bet = int(bet) * 2  # bet X2
            print("You get", bet, "coins")
        else:  # if Paper = opponets choice
            print("Paper covers rock! You lose.")
            bet = 0 

    elif player_choice == "Paper":  # if Paper = player choice
        if opponent_choice == "Rock":  # if Rock = opponets choice
            print("Paper covers rock! You win!")
            bet = int(bet) * 2  # bet X2
            print("You get", bet, "coins")
        else:  # if Scissors = opponets choice
            print("Scissors cuts paper! You lose.")
            bet = 0

    elif player_choice == "scissors":  # if Scissors = Players choice
        if opponent_choice == "Paper":  # if Paper = opponets choice
            print("Scissors cuts paper! You win!")
            bet = int(bet) * 2 # bet X2
            print("You get", bet, "coins")
        else:  # if Rock = opponets choice
            print("Rock smashes scissors! You lose.")
            bet = 0

    player.coins = player.coins + bet  # add bet to current coins
    return # leave game



if __name__ == "__main__":
    Rock_Paper_Scissors_Game()