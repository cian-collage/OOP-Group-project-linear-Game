"""
Author : Joshua Sunil Mathew
Program Description: OOP - Python Game Assignment - Final Duel Class Challenge 3


Required for Level 1
This is the code for challenge 3 of Level 1's duel with the knight
==========RULES==========================

# A NUMBER IS RANDOMLY GENERATED, from 1 to 3

# THE USER IS PROMPTED TO ENTER A NUMBER - if it IS EQUAL to the random number,
# THAT MUCH DAMAGE IS DONE TO THE KNIGHT

# IF NUMBER IS WRONG, THE RANDOM NUMBER IS THE DAMAGE DONE TO YOURSELF.

the function returns true or false depending on if this is completed
There is also a level skip, functionality if the challenge is proved to difficult
but you do not receive the item for completing this level

==========================================


"""
# IMPORTS
import pygame
import random
import time

# MAIN DUEL CLASS
class Duel:
    def __init__(self):
        # CHARACTER HEALTHS - starting
        self.player_health = 5
        self.knight_health = 5
    def display_health_bars(self):
        #DISPLAYING CHARACTER HEALTH, IN A VISUAL FORMAT w/ *
        # it prints asterisks, for the amount of player health
        print(f"Player's Health: {'*' * self.player_health}")
        print(f"Knight's Health: {'*' * self.knight_health}")
        print("\n")

    # GUESSING LOGIC
    def player_attack(self):
        try:
            player_guess = int(input("Guess a number between 1 and 3: "))
            if 1 <= player_guess <= 3: # GUESSING BOUNDARY
                return player_guess
            else:
                print("Invalid guess. Please enter a number between 1 and 3.")
                return self.player_attack()
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")
            return self.player_attack()

    def duel(self):
        print("The duel begins between you and the King's Knight!")
        time.sleep(3)
        print("\n3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1\n")
        time.sleep(1)

        while self.player_health > 0 and self.knight_health > 0:
            self.display_health_bars()

            # Player's turn
            player_damage = self.player_attack()
            knight_guess = random.randint(1, 3)

            if player_damage == knight_guess:
                self.knight_health -= player_damage
                print(f"You hit the knight for {player_damage} damage!")
            else:
                self.player_health -= knight_guess
                print(f"The knight counterattacks for {knight_guess} damage!")

            # Check for winner
            if self.player_health <= 0:
                print("You have been defeated. The knight is victorious!")

                # Ask if the player wants to try again
                try_again = input("Do you want to try again? (yes/no): ")
                if try_again.lower() == 'yes' or try_again.lower() == 'y':
                    self.player_health = 5
                    self.knight_health = 5
                    print("Guess, you didnt have enough!")
                else:
                    print("You must defeat the knight to complete Level 1 !")
                    print("Would you like to skip - (you will not recieve the Chaos "
                          "Sword)?")
                    skip = input("Do you want to skip? (yes/no): ")
                    if skip.lower() == 'yes' or skip.lower() == 'y':
                        print("returning...\n")
                        return False
                    else:
                        self.player_health = 5
                        self.knight_health = 5
                        self.duel()

            elif self.knight_health <= 0:
                print("Congratulations! You have defeated the King's Knight!")
                return True
