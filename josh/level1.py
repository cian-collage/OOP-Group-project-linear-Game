"""
Author : Joshua Sunil Mathew
Program Description: OOP - Python Game Assignment (Cult of Shadows)

Level 1
The Citadel : The player admires the portraits on the wall and is approached by the
knight(NPC)
- Then leads to the druid's quarters where the option is given to accept the quest
- The Druid has 3 challenges for the player in 3 rooms within the Citadel,
Druid's Quarters, The Great Library, The Armory
Each challenge has an assortment of puzzles for the player to complete,
leading to the reward of coins / clues
However the Final Level - is a duel with knight, to earn the a weapon!
The with all the clues, coins received
the player heads to the City Walls - Seán's Level 2

Developed by Error 451

"""
#  GAME IMPORTS
import time

# REMOVING PYGAME INTRO MESSAGE
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

#IMPORT PYGAME
import pygame.mixer

from cian.characters import NPC
from sean.locationClass import Location
from denis.Player import Player
from josh.challenges import DruidGame, Challenges
from josh.FinalDuel import Duel


#  LEVEL 1 CLASS
class Level1(Location):
    def __init__(self, player):
        # INHERITS FROM DENIS'S PLAYER CLASS
        super().__init__("Citadel",
                         ['Hall of Warriors', 'Grand Library', 'Armory',
                          'Druids Quarter'],
                         ["Sir Smith", "Scribe"], [])
        # LOCATION TRACKER
        self.current_location = self.sublocation[0]

        # PLAYER INSTANTIATION
        self.player = player

        # NPC CLASS 1 : The King's Knight, Sir Smith
        self.knight = NPC("Sir Smith",
                          "It was a horrible sight,"
                          " I remember each and every one of them", "near the City"
                                                                    " Gates", "",
                          "")
        # NPC CLASS 2 : Library Scribe, Cedric
        self.scribe = NPC("Cedric the Scribe",
                          "I've been doing some spring cleaning, sir!",
                          "hooded figures dwelling near the City",
                          "Forbidden Manuscript",
                          "")

        # NPC CLASS 3: The Druid, David
        self.druid = NPC("David the Druid",
                         f"Ive been expecting you {player.name},"
                         f" We have a bit of a situation",
                         "",
                         "Chaos Sword", "")

        # LEVEL ELEMENTS INSTANTIATIONS
        self.library1 = Challenges()
        self.druidgame = DruidGame()
        self.finalduel = Duel()

        # LEVEL STATE FLAGS
        self.__game_started = False
        self.interacted_scribe = False
        self.interacted_knight = False
        self.interacted_druid = False
        self.challengeAccepted = False
        self.level_running = True

        pygame.mixer.init()

    #  START GAME INTRO WHEN LEVEL START
    def level_start(self):
        self.gameintro()

    ### PYGAME AUDIO METHODS
    def playsoundIntro(self):
        pygame.mixer.music.load("Title Theme.wav")
        pygame.mixer.music.play(loops=0)

    def minigamesound(self):
        pygame.mixer.music.load("Minigame.wav")
        pygame.mixer.music.play(loops=0)

    def playsoundduel(self):
        pygame.mixer.music.load("Battle.wav")
        pygame.mixer.music.play(loops=0)

    def gameplayaudio(self):
        pygame.mixer.music.load("gameplay.mp3")
        pygame.mixer.music.play(loops=1)

    def stopmusics(self):
        pygame.mixer.music.stop()

    ### PYGAME AUDIO METHODS

    #  GAME INTRO METHOD
    def update(self):
        # Check if the game has not started
        if not self.__game_started:
            # Set a maximum number of retries for user input
            max_retries = 3
            retries = 0

            # Loop to repeatedly prompt the user until valid input or maximum retries are reached
            while retries < max_retries:
                try:
                    # Get user input
                    player_input = input("Press 'q' to quit or 's' to start: ")

                    # Check user input and take appropriate actions
                    if player_input.lower() == "q":
                        print("Till another time, adventurer!")
                        self.__running = False
                        exit()
                    elif player_input.lower() == "s":
                        print("Ready your weapons, gather your resolve and "
                              "step into the unknown!")
                        self.__game_started = True
                        time.sleep(2)
                        self.hallofwarriors()
                        break
                    else:
                        # Raise a ValueError for invalid input
                        raise ValueError("Invalid Input! Please enter 'q' or 's'.")
                except ValueError as e:
                    # Handle the ValueError exception by printing the error message
                    print(e)
                    retries += 1
            else:
                # If too many invalid attempts, exit the game
                print("Too many invalid attempts. Exiting the game.")
                exit()

    #  BEGIN GAME INTRO TITLES
    def gameintro(self):
        self.playsoundIntro()
        # #  MAIN GAME TITLES, SUBTITLE, AUTHORS
        print("===================================")
        print("         Cult of Shadows          ")
        print(" an adventure, developed by Error 451")
        print("===================================")

        time.sleep(1)

        print("\nYou are about to embark on a quest veiled in the shadows.")
        time.sleep(1)
        print("Each level flows through the storyline, and you will be "
              "faced with puzzles"
              "\nand challenges!")

        time.sleep(1)
        self.update()


        time.sleep(1)

        print("===================================")

        #  END OF GAME INTRO

    # DISPLAY PLAYER, LEVEL SUMMARY
    def summary(self):
        print("\n==================== Level 1 Player Summary ====================")
        # PLAYER NAME DISPLAY
        print(f"Player Name: {self.player.name}")
        time.sleep(1)
        # PLAYER FINAL LEVEL COINS
        print(f"Player Coins: {self.player.coins} coins")
        time.sleep(1)
        # PLAYER FINAL ITEMS
        self.player.show_inventory()
        time.sleep(1)
        # PLAYER FINAL CLUES
        print(f"\nClues found in this level: {self.review_clues()}")
        time.sleep(1)

        print("==================== End of Player Summary ====================\n")
        time.sleep(1)
        self.stopmusics()


    # SUBLEVEL 1 METHOD FOR LEVEL 1
    def hallofwarriors(self):
        # ASSIGN LOCATION to CURRENT LOCATION
        self.stopmusics()
        pygame.mixer.music.set_volume(5)
        self.gameplayaudio()
        self.current_location = self.sublocation[0]
        print("==================================")
        print(f"(Location: {self.current_location} - AD 734)")
        print("==================================")
        time.sleep(2)
        print("\nAs you walk down the dimly lit hallway of the citadel, "
              "the flickering torchlights cast an eerie glow on the frames that"
              " line the walls")

        time.sleep(1)
        print(
            "The Fallen Men - each portrait captures a haunting image,"
            " frozen in time. You feel the weight of the unknown pressing on you"
            ", and \nquestions flood through your mind.")

        time.sleep(1)
        print("As you stare, The King's Knight approaches...")
        #  LOGIC TO INTERACT WITH KNIGHT
        while True:
            player_choice = input("\n(Would you like to speak to the knight?)"
                                  " 'y for yes' or 'n' for no : ")

            # CHECKING USER INPUT FOR MIXED INPUTS
            if player_choice.lower() == 'y' or player_choice.lower() == 'yes':
                time.sleep(1)
                print(f"\n{self.knight.interact()}")
                time.sleep(2)
                print(f"{self.player.name}: Do you know of where it happened?")
                time.sleep(2)
                print(
                    self.knight.say_dialogue("The battle was near the the city "
                                             "gates!\n"))
                time.sleep(3)
                self.add_clue(self.knight.clue())
                # KNIGHT INTERACTED: YES?
                self.interacted_knight = True
                time.sleep(1)
                print("\n(You earned 2 coins for interacting with the knight!)")
                #  GIVE PLAYER COINS
                self.player.coins += 2
                time.sleep(1)
                #  DISPLAY COINS
                print(f"(You have: {self.player.coins} coins collected)\n")
                time.sleep(1)
                break

            # ELSE CHOICE
            elif player_choice.lower() == 'n' or player_choice.lower() == 'no':
                print("(You must speak to the knight; he may have some insights...)")

            # ERROR CATCHING
            else:
                print("(Invalid Option, Try Again!)")

        # SETUP NEXT SUBLEVEL
        print("You walk towards the Druid's Quarters")
        # MINI LOADING ELEMENT
        print("Walking...")
        # LOADING DELAY
        time.sleep(3)
        # CALL NEXT SUBLEVEL
        self.druidquarter()

    # SUBLEVEL 3 METHOD FOR LEVEL 1

    def grandlibrary(self):
        # UPDATE LOCATION
        self.current_location = self.sublocation[1]
        print("==================================")
        print(f"Location : {self.current_location}")
        print("===================================\n")
        #  DIALOGUE
        print("(You approach Cedric, The Library Scribe)\n")
        time.sleep(2)
        print(self.scribe.interact())
        time.sleep(1)
        print(self.druid.say_dialogue("Great Work, - I need those scriptures for the "
                                      "next sermon!"))
        time.sleep(1)

        print(self.scribe.say_dialogue(f"I will make sure that they are ready to go "
                                       f"for you sir!,"
                                       f" Anyways! What brings you and "
                                       f"{self.player.name} to the library?"))
        time.sleep(1)
        print(self.druid.say_dialogue("A light reading per say, doth no harm!\n"))
        time.sleep(1)
        print(self.druid.say_dialogue(
            f"now {self.player.name}, onto Challenge 2 of your test!\n"))
        self.minigamesound()
        self.library1.book_roulette()
        self.stopmusics()
        pygame.mixer.music.set_volume(5)
        self.gameplayaudio()

        # ADD COINS TO PLAYER INVENTORY
        self.player.coins = self.player.coins + 3
        time.sleep(1)
        print(f"You have: {self.player.coins} coins collected\n")
        print(self.scribe.say_dialogue(
            "Wow, that was impressive, - I may have some information "
            "for you to help you on journey\n"))
        print(self.scribe.say_dialogue("I don't know much, "
                                       "but I did read of some hooded people dwelling, "
                                       "in the City\n"))
        self.add_clue(self.scribe.clue())


        #  SCRIBE INTERACTED: YES
        self.interacted_scribe = True
        time.sleep(1)

        #  SET UP FOR SUBLEVEL 3
        print(self.druid.say_dialogue(
            "I hear the King's Knight has heard your success and would like to speak "
            "with you..."))
        time.sleep(1)
        print(self.druid.say_dialogue("proceed to the Armory, for your final "
                                      "Challenge!"))
        # LOADING ELEMENT
        print("Heading to the Armory...")
        # LOADING DELAY - (time to walk from this location to there)
        time.sleep(5)
        self.armory()

    # SUBLEVEL 4 for LEVEL 1
    def armory(self):

        # UPDATE LOCATION
        self.current_location = self.sublocation[2]
        print("==================================")
        print(f"\n(Location: {self.current_location})")
        print("===================================\n")
        time.sleep(1)

        # DIALOGUE
        print(self.knight.say_dialogue("Welcome to the Armory!\n"))
        print(self.knight.say_dialogue("Your Final Task, to Prove yourself worthy is "
                                       "to face me!"))
        time.sleep(1)
        print(self.knight.say_dialogue("Lets see, how good you really are!"))
        time.sleep(1)
        print(self.knight.say_dialogue("I challenge you to a duel!"))
        time.sleep(1)
        print(self.knight.say_dialogue("Winner gets the greatest weapon, passed down "
                                       "from generation to generation: 'The Chaos "
                                       "Sword!"))

        # SET UP INSTANCE OF SELF.FINAL DUEL from josh/FINAL DUEL.py
        pygame.mixer.music.set_volume(7.5)
        self.playsoundduel()
        self.level_running = self.finalduel.duel()
        self.stopmusics()
        self.gameplayaudio()
        time.sleep(1)

        #  CHECK IF KNIGHT WAS NOT DEFEATED / LEVEL SKIP
        if not self.level_running:  # if it is false

            # #  if the player loses to the knight
            print(self.knight.say_dialogue("Well, Maybe you may not be capable - "
                                           "but i do see heart in you..."))
            print(self.knight.say_dialogue("You have a long adventure ahead of you, "
                                           "my friend!"))
            # player does not recieve intended item!
            print("\nKnight Duel - was skipped! - item not granted ")

            #  CLOSING DIALOGUE/SETUP TO LEVEL 2 - Seán

            print(
                self.druid.say_dialogue("You have certainly, exceeded my expectations!"))

            print(self.knight.say_dialogue(f"Best of Luck, {self.player.name}"))
            print(self.druid.say_dialogue(f"Best of Luck, {self.player.name}"))

            print(f"{self.player.name}: Let us head to the city!\n")

        #  CHECK IF KNIGHT WAS DEFEATED! - PLAYER CAN GO TO THE NEXT LEVEL!
        else:


            # CHANGE INTERACTION LOGIC
            self.interacted_knight = True
            time.sleep(1)

            # ADD COINS FOR COMPLETEING FINAL DUEL
            self.player.coins = self.player.coins + 10
            print("\nYou have been awarded 10 coins!")

            time.sleep(1)
            print(f"You have: {self.player.coins} coins collected\n")

            #  CLOSING DIALOGUE
            print(self.knight.say_dialogue(
                "You have certainly, exceeded my expectations!"))
            print(self.knight.say_dialogue(
                "You have a long adventure ahead of you, my friend!\n"))

            #  GIVES THE PLAYER THE CHAOS SWORD
            self.player.add_item('Chaos Sword')
            print("Chaos Sword Added to Inventory!")

            #  CHECK IF ITS ADDED
            self.player.show_inventory()

            #  LEVEL CLOSING REMARKS
            print(
                self.druid.say_dialogue("You are an excellent candidate for "
                                        "this quest!"))

            print(self.druid.say_dialogue(f"I wish you, Best of Luck,"
                                          f" {self.player.name}"))
            print(self.knight.say_dialogue(f"Best of Luck, Sir, {self.player.name}"))

            print(f"{self.player.name}: All the clues involve the city...\n")

            #  SHOW LEVEL SUMMARY
            self.stopmusics()
            self.playsoundIntro()
            time.sleep(1)
            self.summary()




    # SUB LEVEL 2 METHOD - LEVEL 1
    def druidquarter(self):
        # UPDATE LOCATION
        self.current_location = self.sublocation[3]

        time.sleep(3)
        print("==================================")
        print(f"(Location: {self.current_location})")
        print("==================================\n")
        time.sleep(1)

        #  INITIAL DRUID INTERATION
        print(self.druid.interact())
        time.sleep(1)

        print(f"{self.player.name}: I have heard the stories, truly saddening! - why "
              f"was I summoned here today?")
        time.sleep(1)

        print(self.druid.say_dialogue(
            "We need an answer to all of this, why us of all people - THAT is why YOU "
            "are here!\n"))
        time.sleep(1)

        print(self.druid.say_dialogue("I have a quest for you, whether you choose to "
                                      "accept it"))
        time.sleep(1)

        #  ASK USER TO ACCEPT THE QUEST OF THE ADVENTURE GAME
        while True:
            player_choice = input("Would you like to accept the quest? -> 'y' for yes "
                                  "or 'n' for no: ")
            print("\n")
            if player_choice.lower() == 'y':
                time.sleep(1)

                print(self.druid.say_dialogue("The Shadowbound Covenant have been "
                                              "the main link to "
                                              "our missing people,"
                                              "\nThey are a group of hooded people, "
                                              "hiding within our society"
                                              "\nWe have held our silence "
                                              "for too long and longed for someone "
                                              "to step up!\n"))
                self.challengeAccepted = True
                time.sleep(4)

                print(self.druid.say_dialogue("But before you begin you must prove to "
                                              "me that you are capable to embark on "
                                              "this quest\n"))
                time.sleep(1)
                print(self.druid.say_dialogue("It will test your mental, physical and "
                                              "quick thinking abilities\n"))
                time.sleep(2)
                self.stopmusics()
                pygame.mixer.music.set_volume(7.5)
                self.minigamesound()
                self.druidgame.catch_ball()
                self.stopmusics()
                self.gameplayaudio()
                time.sleep(1)

                #  ADDS INITIAL COINS FOR CLEARING LEVEL CHALLENGE 1
                time.sleep(1)
                self.player.coins = self.player.coins + 3
                print("\nYou have been awarded 3 coins!")
                time.sleep(1)
                print(f"You have: {self.player.coins} coins collected")
                time.sleep(1)
                print(f"\n{self.druid.name}: Great Catches, {self.player.name}! - Let "
                      f"us head to the Grand Library, for your next challenge")
                print("\nWalking...")
                time.sleep(4)
                break
            #  IF USER DOES NOT ACCEPT THE DRUID's QUEST - user is prompted to make the
            #  correct choice!
            else:
                print(self.druid.say_dialogue("Maybe I had made a mistake in summoning "
                                              "you..."))
                print("\n(You must complete the Druid's Activities "
                      "to continue further in this level!)")

        #  CALL SUBLEVEL 3 THE LIBRARY WHEN LEVEL IS COMPLETED
        self.grandlibrary()


if __name__ == "__main__":
    #  PLAYER NAME SELECTION
    print("[Adjust your Device Volume - for the best experience]")
    player = input("\nEnter a player name to immerse yourself in the story: ")
    player1 = Player(f"{player}")

    time.sleep(1)  # DELAY BETWEEN TEXT

    #  MAKE PLAYER COINS 0
    player1.coins = 0

    #  PASS PLAYER TO LEVEL 1
    level1 = Level1(player1)

    #  INSTANCE OF GAME INTRO - GAME TITLE & INTRO
    level1.gameintro()
