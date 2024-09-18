"""
Program Name: Dice_minigame.py

Author: Cian Anderson (C22793219) in Group ERROR 451

Program Description:
This is the Dice mini game method it allows the player to input a "Bet" that is taken from the players coins.
You compeat agains the Dice Goblin by by rolling 2 dice each and comparing the sums of them.
If the player wins the "Bet" is dubbled and added back to them.
If the player loses the "Bet" is not re added to the coin total.
Date: 3/12/2023
"""

import random


def dice_game(player):

    bet = int(input(f"You have {player.coins} coins\nhow many coins would you like to bet:\n"))  # input bet

    while bet > player.coins:  # makes sure player has enough coins
        if player.coins > 0:  #  if coins is > 0
            bet = int(input(f"You only have {player.coins} coins \nhow many coins would you like to bet:\n"))
        else:
            print("You have 0 coins so you can't play")
            break
    player.coins = player.coins-bet  # take bet away from coin total

    player_dice1 = random.randint(1, 6)  # roll dice 1
    player_dice2 = random.randint(1, 6)  # roll dice 2
    total_player_dice = player_dice1 + player_dice2   # get dice sum

    opponent_dice1 = random.randint(1, 6)  # roll dice 1
    opponent_dice2 = random.randint(1, 6)  # roll dice 2
    total_opponent_dice = opponent_dice1 + opponent_dice2  # get dice su,

    print("\nYour Dice:")
    print("Dice 1:", [player_dice1], "\nDice 2:", [player_dice2], "\nTotal:", [total_player_dice])  # print player rolls

    print("\nOpponents Dice:")
    print("Dice 1:", [opponent_dice1], "\nDice 2:", [opponent_dice2], "\nTotal:", [total_opponent_dice])  # print opponent rolls

    if total_player_dice > total_opponent_dice:  # if win
        print("\nYou Win")
        bet = int(bet) * 2  # dubble bet
        print("You get", bet, "coins")

    elif total_player_dice == total_opponent_dice:  # if draw
        print("\nDraw!\nGo Again")
        dice_game()  # restart game

    else:  # if lose
        print("\nYou Lost")
        bet = 0  # make bet 0

    player.coins = player.coins + bet  # add bet to player coins
    print(f"\nYou have {player.coins} coins\n")   # print player coin total
    return  # exit game


if __name__ == "__main__":
    dice_game()