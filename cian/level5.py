"""
Program Name: level5.py

Author: Cian Anderson (C22793219) in Group ERROR 451

Program Description:

This is the 5th level out of our six-level game.
This level is designed to side track the player with a more light-hearted atmosphere
It is set in and around a goblin camp and contains a number of Goblin NPC all with their own distinct personality
As the level does not have as much plot relevancy as the previous levels it is based around a central "Main camp" are
this is to allow the player to pick and chose what interactions they want to have while allowing the players focused on
the plot to skip large portions of it.
There are a number of mini-games hidden within interactions with the NPCs through the level to enhance its enjoyability
While not all NPCs are plot relevant interacting with them will slowly review more and more about the Goblin camp and
its residents.
If you wish to skip most of this level talk to the goblin elder in the big hut about "The legendary witch slayer" and
leave for their grave.

Date: 3/12/2023
"""

from sean.locationClass import Location
from cian.characters import NPC
from cian.Dice_minigame import dice_game
from cian.RPS_minigame import Rock_Paper_Scissors_Game
from denis.Player import Player

import time
import pygame


class Level5(Location):
    def __init__(self, player):
        super().__init__("camp",
                         ["outer_camp", "main_camp", "hut_1", "hut_1_inside", "big_hut_outside", "big_hut",
                          "side_main_camp", "grave"],
                         ["Goblin trio", "Dice Goblin", "Goblin Elder"],
                         [])
        self.current_location = "outer_camp"
        self.visited_sublocations = []
        self.player = player
        self.goblin_trio = NPC("Goblin trio",
                               ["\nYou here voices in unison say:\n\"What do you want\"?\n",
                                "You here a high pitched voice from the other side\n\n\"Nobody is home\"!\n",
                                "\nFirst Goblin: \"We heard the elder talk about that\n"
                                "Second Goblin: \"We dont know nothing\"\n"
                                "Third Goblin: \"The elder should be in the big hut\"\n",
                                "\n\"You are not getting we have the door barred\""
                                "!The voices on the other side shout\n"],
                               ["Goblin elder is in the big hut", ],
                               "",
                               ["\nThe door opens slightly and you see 3 Goblins peer through the "
                                "crack nervously\n",
                                "The Goblin trio open the door further and you see 3 identical goblins. "
                                "The only difference is their eye colour\n"])

        self.dice_goblin = NPC("Dicy",
                               [
                                   "\nShady Goblin: Welcome friend!\nIf im not mistaken you\"re new around here. \n"
                                   "\nThe names Dicy\n",
                                   "\nRecon you fancy a game of dice friend?\n",
                                   "\nHow about the ol' rock paper scissors then?\n",
                                   "\nHow about another round?\n",
                                   "\nWell friend you seem mighty well off "
                                   "how abouts i give you some information as a fellow benefactor of life\n",
                                   "\nNow dont go spreading this info around\n",
                                   "\n\n"],
                               ["98% of gamblers give up before they win big"],
                               "",
                               ["He says as he tips his hat"], )

        self.posh_goblin = NPC("Reginald Thornsworth the Refined",
                               ["\n\"Now, now, Grizzle, we ought to listen to their inquiries.\"\n "
                                "\"Pray, what is it that you seek from the elder, my good fellow?\"\n",
                                "\"Pray, good sir, how may we be of service to you on this occasion?\"\n",
                                "\"I say, old chap, one cannot simply waltz over to have a chat with the elder. "
                                "Pray, enlighten us to what urgent matter compels you to seek an audience with "
                                "such haste and gusto?\"\n",
                                "\"Ah, so you've encountered Snatch, Scratch, and Rodrick. If they've sent you, my "
                                "friend, "
                                "it suggests that you are of good character on their part. One could surmise that you "
                                "are not of ill intent, given their commendable judgment in such matters. "
                                "You may enter\"\n"],
                               ["Goblins trios names are Snatch, Scratch, and Rodrick"],
                               "",
                               ["His words are adorned with a touch of sophistication, "
                                "making it clear that he sees himself as a goblin of importance.\n"], )

        self.rough_goblin = NPC("Grizzle \"Knuckles\" O'Connor",
                                ["\"Oi, wagwan? You new 'round 'ere or somethin'? State your ends bruv!\"\n",
                                 "\n\"Yeah, bruv, never clocked that spot, but it don't sound like we got "
                                 "beef with them, "
                                 "ya get me? Anyhows fam, but we can't let you roll up on the elder like that. "
                                 "It's a no-go, ya get me?\"\n",
                                 "\"Look, if you ain't spillin' any details, fam, we ain't just gonna "
                                 "let you slide in like that\"\n",
                                 "\"Yo fam! good to see ya fam!\"\n"],
                                [],
                                "",
                                ["His speech is laced with even more street slang, and there's a casual "
                                 "confidence in his demeanor that suggests he's not one to be messed with. "
                                 "Despite the laid-back approach\n"])

        self.elder_goblin = NPC("Goblin elder",
                                ["\"Take a seat young one tell this old man your tubules\".\nDespite their stature, "
                                 "their raspy yet commanding voice exudes wisdom\n", "\"Tea?\"",
                                 "\"So what troubles such a young soul\"\n",
                                 "\"I have heard may rumors in my 10 long years of life but i have to admit that"
                                 "i have not heard about any cults in this area\"\n",
                                 "\"Now that you mention it i have heard that name somewhere before.... "
                                 "now when was it? Oh yes that was it i believe that i saw that name written on a "
                                 "grave just to the east of camp when i was but a young goblin, what was it 5 years "
                                 "ago. I was lively back then the elder at the time said that i was the most energetic "
                                 "goblin he had ever seen. Look at me getting distracted reminiscing on the past, "
                                 "where was I?.... ah yes the grave its just east of here next to a large oak tree"
                                 " and a cave.\"\n"],
                                ["The Legendary Witch Slayers grave is to the east of camp beside a large tree"],
                                "",
                                ["As you sit he finishes up what he was working on and takes a seat across form "
                                 "you\n",
                                 "He hops down off of his chair and goes over to the cauldron. With one swift movement "
                                 "he produces a mug and dips it into the bubbling liquid. \n"
                                 "He returns to you with the tea? and returns to sitting across from you\n",
                                 "he looks at you with a bit of disappointment\n"], )
        self.max_coins = 100  # coins needed to set of Dicy's bonus dialog
        self.grave_found = False  # has gained info on the graves location
        self.choice = 0
        self.game_run = True

        pygame.mixer.init()  # used for sound

    def level_start(self):
        self.outer_camp()

    @staticmethod
    def grave_play():
        pygame.mixer.music.load("Kung Fu Panda - Master Oogway Suite (Theme).wav")
        pygame.mixer.music.play(loops=0)

    @staticmethod
    def dicy_play():
        pygame.mixer.music.load("Saloon music compilation.mp3")
        pygame.mixer.music.play(loops=0)

    @staticmethod
    def lv5_background_play():
        pygame.mixer.music.load("the-shire-lord-of-the-rings-ambience-and-music-1-hour.mp3")
        pygame.mixer.music.play(loops=0)

    @staticmethod
    def main_music_pause():
        pygame.mixer.music.pause()

    @staticmethod
    def music_unpause():
        pygame.mixer.music.unpause()

    @staticmethod
    def music_stop():
        pygame.mixer.music.stop()

    def outer_camp(self):  # outer camp location used as a secondary hub and as an intro
        while self.game_run:
            self.current_location = "outer_camp"
            if self.current_location not in self.visited_sublocations:  # if you haven't been here before
                self.visited("outer_camp")
                self.lv5_background_play()
                print("\nEmerging from the dense forest, you spot a small goblin camp at the foot of towering cliffs. "
                      "Ramshackle huts, constructed from salvaged materials, form a chaotic maze in the shadows. "
                      "Flickering bonfires illuminate the primitive dwellings. "
                      "You spot 3 shadows dart into the nearest hut.\n")
                time.sleep(4)
            else:
                print("You walk back out of the camp and look back at it, Not much has changed\n")

            while self.current_location == "outer_camp":
                if self.grave_found:  # if info on the grave was found in the big hut
                    self.choice = 0  # reset choice variable
                    while self.choice != "1" or "2" or "3" or "4":  # error check
                        if self.game_run:
                            print("-------------------------------------------------------\n")
                            self.choice = input("What will you do?\n"
                                                "1) Investigate the first Hut\n"
                                                "2) Walk deeper into the camp\n"
                                                "3) Keep observing the camp from outside\n"
                                                "4) Head east to the grave of The Legendary Witch Slayer\n")
                            print("-------------------------------------------------------\n")
                            if self.choice == "1":  # Investigate the first Hut
                                print(
                                    "As you enter the camp you come to the realisation that you cant see any sign of "
                                    "the residents.\n")
                                time.sleep(1)
                                self.hut_1()  # sends to location
                            # to main camp
                            elif self.choice == "2":  # Walk deeper into the camp
                                print("You walk past the first hut and deeper into the town\n")
                                time.sleep(1)
                                self.main_camp()
                            # stay where they are
                            elif self.choice == "3":  # Keep observing the camp from outside
                                self.outer_camp()
                            elif self.choice == "4":  # Head east to the grave of The Legendary Witch Slayer
                                self.grave()
                                return
                        else:
                            break
                else:
                    self.choice = 0  # reset choice variable
                    while self.choice != "1" or "2" or "3":  # error check
                        if self.game_run:
                            print("-------------------------------------------------------\n")
                            self.choice = input("What will you do?\n"
                                                "1) Investigate the first Hut\n"
                                                "2) Walk deeper into the camp\n"
                                                "3) Keep observing the camp from outside\n")
                            print("-------------------------------------------------------\n")
                            # to 1st hut
                            if self.choice == "1":  # Investigate the first Hut
                                print(
                                    "As you enter the camp you come to the realisation that you cant see any sign of "
                                    "the residents.")
                                time.sleep(1)
                                self.hut_1()
                            # to main camp
                            elif self.choice == "2":  # Walk deeper into the camp
                                print("You walk past the first hut and deeper into the town")
                                time.sleep(1)
                                self.main_camp()
                            # stay where they are
                            elif self.choice == "3":  # Keep observing the camp from outside
                                self.outer_camp()
                        else:
                            break

    def hut_1(self):  # first location where you meet the goblin trio and find ot where the elder is
        while self.game_run:
            self.current_location = "hut_1"
            if self.current_location not in self.visited_sublocations:  # if not visited before
                print("You come up to the door of the first hut where you saw the 3 shadows enter\n")
                time.sleep(1)
            else:  # shows aftermath of first interaction if you return
                print("\nAs you approach the hut you see that the door is open and nobody is inside. "
                      "The goblin trio has left\n"
                      "\nYou walk deeper into the camp\n")
                time.sleep(1)
                self.main_camp()

            while self.current_location == "hut_1":
                self.choice = 0  # reset choice variable
                while self.choice != "1" or "2" or "3":  # error check
                    print("-------------------------------------------------------\n")
                    self.choice = input("\nWhat will you do?\n"
                                        "1) Knock on the door\n"
                                        "2) Try to open it\n"
                                        "3) Walk deeper into the camp\n")
                    print("-------------------------------------------------------\n")
                    if self.choice == "1":  # Knock on the door
                        print(self.goblin_trio.dialogue[1])  # Nobody is home dialogue with no name
                        time.sleep(1)
                        self.visited("hut_1")

                    elif self.choice == "2":  # Try to open it
                        print("You try to open the door by force with little success")
                        print(self.goblin_trio.dialogue[3])  # door barred dialogue with no name
                        time.sleep(1)
                    elif self.choice == "3":  # Walk deeper into the camp
                        self.main_camp()

                    self.choice = 0  # reset choice variable
                    while self.choice != "1" or "2" or "3":  # error check
                        print("-------------------------------------------------------\n")
                        self.choice = input("What will you do?\n"
                                            "1) Say that you just want to talk and you mean no harm\n"
                                            "2) Try to open the door\n"
                                            "3) Leave and go further into the town\n")
                        print("-------------------------------------------------------\n")

                        if self.choice == "1":  # Say that you just want to talk and you mean no harm
                            print(self.goblin_trio.actions[0])  # The door opens slightly action
                            print(self.goblin_trio.dialogue[0])  # What do you want dialogue with name
                            time.sleep(1)
                            self.choice = 0  # reset choice variable
                            while self.choice != "1" or "2":  # error check
                                print("-------------------------------------------------------\n")
                                self.choice = input("How do you respond?\n"
                                                    "1) 'I just wanted to see if you have any information on"
                                                    "some missing people'\n"
                                                    "2)'Wrong hut sorry'. Leave and go further into the town\n")
                                print("-------------------------------------------------------\n")
                                # 'I just wanted to see if you have any information on some  missing people'
                                if self.choice == "1":
                                    print(self.goblin_trio.actions[1])  # door opens more action
                                    print(self.goblin_trio.say_dialogue(
                                        self.goblin_trio.dialogue[2]))  # elder location dialogue
                                    time.sleep(1)
                                    self.add_clue(
                                        self.goblin_trio.clues[0])  # adds the location clue "where the elder is"
                                    print(self.review_clues(), "\n")  # displays clues
                                    self.visited("hut_1_inside")  # mark as success for later dialogue
                                    self.choice = 0  # reset choice variable
                                    while self.choice != "1" or "2":  # error check
                                        print("-------------------------------------------------------\n")
                                        self.choice = input("Where will you go next?\n"
                                                            "1) Go back to the outside of the camp.\n"
                                                            "2) Go deeper into the village to find the elder.\n")
                                        print("-------------------------------------------------------\n")
                                        if self.choice == "1":  # Go back to the outside of the camp.
                                            self.outer_camp()
                                        elif self.choice == "2":  # Go deeper into the village to find the elder.
                                            self.main_camp()

                                elif self.choice == "2":  # 'Wrong hut sorry'. Leave and go further into the town
                                    self.main_camp()

                        elif self.choice == "2":  # Try to open the door
                            print("You try to open the door by force with little success")
                            print(self.goblin_trio.say_dialogue(self.goblin_trio.dialogue[3]))  # door barred dialogue
                            time.sleep(1)
                        elif self.choice == "3":  # Leave and go further into the town
                            self.main_camp()

    def main_camp(self):  # main hub location used to get too and from other locations with NPCs / Clues
        while self.game_run:
            self.current_location = "main_camp"
            if self.current_location not in self.visited_sublocations:
                print("You arrive in the center of the camp.\nFrom here you can see the entire camp."
                      "\n\nSome points of interest include:\n"
                      "1. The First Hut\n2. The Big Hut with 2 angry looking goblins guarding the entrance.\n"
                      "3. A Goblin in a long trench coat and large hat "
                      "sitting on the ground with a set of dice in front of him.\n")
                self.visited("main_camp")
                time.sleep(2)
            self.choice = 0  # reset choice variable
            while self.choice != "1" or "2" or "3" or "4":  # error check
                if self.game_run:
                    print("-------------------------------------------------------\n")
                    self.choice = input("\nWhere will you go?\n"
                                        "1) Back to the First Hut\n"
                                        "2) To the Big Hut\n"
                                        "3) Over to the Suspicious Goblin\n"
                                        "4) Leave Camp\n")
                    print("-------------------------------------------------------\n")

                    if self.choice == "1":  # Back to the First Hut
                        self.hut_1()
                    elif self.choice == "2":  # To the Big Hut
                        self.big_hut_outside()
                    elif self.choice == "3":  # Over to the Suspicious Goblin
                        self.side_main_camp()
                    elif self.choice == "4":  # Leave Camp
                        self.outer_camp()
                else:
                    break

    def big_hut_outside(self):  # used to get into the big hut and is where you interact with the guards
        while self.game_run:
            self.current_location = "big_hut_outside"
            if self.current_location not in self.visited_sublocations:
                print("You walk over to the large hut in the center of the camp. "
                      "From a distance, you see the curious pair of goblin guards stationed outside a large hut."
                      "One, a pint-sized figure, catches your eye with stolen finery and an air of aristocratic pride."
                      "His hooked nose supports a tiny monocle.\n")
                time.sleep(1)
                print("On the flip side, another goblin, rough and untamed, captures your attention. Clad in patchwork "
                      "leather, he wields a rusty blade with a menacing air. His body is adorned with crude tattoos "
                      "depicting goblin mischief, forming a stark contrast to his posh companion.\n")
                time.sleep(1)
                print(self.rough_goblin.say_dialogue(self.rough_goblin.dialogue[0]))  # new round here dialogue
                time.sleep(1)
                input("Where are you from?:\n")  # ask for meaningless input for fun
                print(self.rough_goblin.say_dialogue(self.rough_goblin.dialogue[1]))  # cant let you in dialogue
                print(self.rough_goblin.actions[0])  # description of speech pattern
                time.sleep(1)
                print(self.posh_goblin.say_dialogue(self.posh_goblin.dialogue[0]))  # why need to talk to elder dialogue
                print(self.posh_goblin.actions[0])  # description of speech pattern
                time.sleep(1)
                self.visited("big_hut_outside")
            else:
                print("The Guards look at you suspiciously:")
                time.sleep(1)
            if "big_hut" not in self.visited_sublocations:
                self.choice = 0  # reset choice variable
                if self.game_run:
                    while self.choice != "1" or "2" or "3":  # error check
                        if self.game_run:
                            # adds option if you interacted with the goblin trio
                            if "hut_1_inside" in self.visited_sublocations:
                                print("-------------------------------------------------------\n")
                                self.choice = input("\nHow do you respond?\n"
                                                    "1) Go back to camp\n"
                                                    "2) Say that you need to talk to the elder\n"
                                                    "3) Say that you were sent here by the trio of goblins you met "
                                                    "earlier\n")
                                print("-------------------------------------------------------\n")
                            else:  # if not talked to goblin trio
                                print("-------------------------------------------------------\n")
                                self.choice = input("\nHow do you respond?\n"
                                                    "1) Go back to camp\n"
                                                    "2) Say that you need to talk to the elder\n")
                                print("-------------------------------------------------------\n")

                            if self.choice == "1":  # Go back to camp
                                print("You return to the center of camp\n")
                                self.main_camp()
                            elif self.choice == "2":  # Say that you need to talk to the elder
                                print(self.posh_goblin.say_dialogue(
                                    self.posh_goblin.dialogue[1]))  # how can we help dialogue
                                time.sleep(1)
                                self.choice = 0  # reset choice variable
                                while self.choice != "1" or "2":  # error check
                                    if self.game_run:
                                        print("-------------------------------------------------------\n")
                                        self.choice = input("\nWhat do you do?\n"
                                                            "1) Tell the Truth about what you have learnt?\n"
                                                            "2) Insist that you cant tell them and you need to talk to "
                                                            "the elder\n")
                                        print("-------------------------------------------------------\n")
                                        if self.choice == "1":  # Tell the Truth about what you have learnt?
                                            print(
                                                "You relay all of the information you have learned so far and emphasis "
                                                "the urgency of your request")
                                            time.sleep(1)
                                            print("The guards believe your words and step aside to let you in")
                                            time.sleep(1)
                                            self.big_hut()
                                        # Insist that you cant tell them and you need to talk to the elder
                                        elif self.choice == "2":
                                            print(self.rough_goblin.say_dialogue(
                                                self.rough_goblin.dialogue[2]))  # cant let you in dialogue
                                            time.sleep(1)
                                            print("You return to the center of camp\n")
                                            self.main_camp()
                                    else:
                                        break
                            # Say that you were sent here by the trio of goblins you met earlier
                            elif self.choice == "3":
                                print(self.posh_goblin.say_dialogue(
                                    self.posh_goblin.dialogue[3]))  # spoken to the trio dialogue
                                time.sleep(1)
                                self.add_clue(self.posh_goblin.clues[0])  # add goblin trios names to location clues
                                print(self.review_clues(), "\n")  # displays clues
                                time.sleep(1)
                                self.big_hut()
                        else:
                            break
                    else:
                        break
            else:
                print("Both guards step aside as you approch")
                print(self.rough_goblin.say_dialogue(self.rough_goblin.dialogue[3]))  # good to see you again dialogue
                time.sleep(1)
                self.big_hut()
            break

    def big_hut(self, ):  # used to interact with the goblin elder
        while self.game_run:
            self.current_location = "big_hut"
            if self.current_location not in self.visited_sublocations:
                self.visited("big_hut")
                print(
                    "The goblin elder's hut is a cozy chaos of logs, vines, and scattered belongings. A bubbling "
                    "cauldron in one corner scents the air, while a central fire pit lights up a cluttered table with "
                    "maps and trinkets. Mismatched furniture surrounds the fire, and tapestries tell the tribe's "
                    "stories Despite the disorder, there's a communal atmosphere, reflecting the practical and "
                    "resourceful nature of goblin living.\n In the corner of the room working on a fresh tapestry is "
                    "the goblin elder\n")
                time.sleep(2)
                print("The goblin elder, hunched with age, wears a tattered hood and bears tribal markings on a "
                      "weathered face. Sharp, intelligent eyes gleam from under strands of gray hair. "
                      "Adorned in earth-toned garments, the elder carries a staff adorned with feathers and symbols.\n")
                time.sleep(1)
            else:
                print("As you enter\n")
                time.sleep(1)
            print("Without turning around the Elder addresses you\n")
            print(self.elder_goblin.say_dialogue(self.elder_goblin.dialogue[0]))  # how can I help dialogue
            print(self.elder_goblin.actions[0])  # sits on chair action
            time.sleep(1)
            print(self.elder_goblin.say_dialogue(self.elder_goblin.dialogue[1]))  # Tea?
            time.sleep(1)

            self.choice = 0  # reset choice variable
            while self.choice != "1" or "2":  # error check
                if self.game_run:
                    print("-------------------------------------------------------\n")
                    self.choice = input("1) Yes\n"
                                        "2) No\n")
                    print("-------------------------------------------------------\n")
                    if self.choice == "1":  # Yes
                        print(self.elder_goblin.actions[1])  # get tea action
                        time.sleep(2)
                        self.player.add_item("Tea?")  # adds item to player
                        time.sleep(1)
                        break
                    elif self.choice == "2":  # No
                        print(self.elder_goblin.actions[2])  # disappointment action
                        time.sleep(1)
                        break
                else:
                    break
            print(self.elder_goblin.say_dialogue(self.elder_goblin.dialogue[2]))  # what troubles you dialogue
            interacting = True
            while interacting:
                self.choice = 0  # reset choice variable
                while self.choice != "1" or "2" or "3":  # error check
                    if self.game_run:
                        print("-------------------------------------------------------\n")
                        self.choice = input("What would you like to ask the elder?\n"
                                            "1) Do you know anything about a cult that is kidnapping people?\n"
                                            "2) Have you heard of \"The Legendary Witch Slayer\n"
                                            "3) Leave the large hut\n")
                        print("-------------------------------------------------------\n")

                        if self.choice == "1":  # Do you know anything about a cult that is kidnapping people?
                            print(self.elder_goblin.say_dialogue(
                                self.elder_goblin.dialogue[3]))  # not heard anything dialogue
                            time.sleep(2)
                        elif self.choice == "2":  # have you heard of The Legendary Witch Slayer
                            print(self.elder_goblin.say_dialogue(self.elder_goblin.dialogue[4]))  # seen grave dialogue
                            time.sleep(3)
                            self.add_clue(self.elder_goblin.clues[0])  # add grave location to clues
                            print(self.review_clues(), "\n")  # display clues
                            self.grave_found = True  # mark as location found to open up self.choice in Outer camp
                        elif self.choice == "3":  # Leave the large hut
                            interacting = False  # no longer interacting
                            print("You head back to the center of camp\n")
                            time.sleep(1)
                            break
                    else:
                        break
            self.main_camp()

    def side_main_camp(self, ):  # used to interact with dice goblin and mini-games can give set coins to start
        while self.game_run:
            self.music_stop()  # stops current music

            self.dicy_play()
            self.current_location = "side_main_camp"
            if self.current_location not in self.visited_sublocations:
                print("You walk over to the Shady Goblin\n")
                time.sleep(1)
                print(self.dice_goblin.dialogue[0])  # welcome dialogue no name
                time.sleep(1)
                print(self.dice_goblin.actions[0])  # Tips hat action no name
                time.sleep(1)
                self.visited("side_main_camp")

            if self.player.coins == self.max_coins:  # if you have alot of coins he gives you a bit of info and an item
                print(self.dice_goblin.say_dialogue(self.dice_goblin.dialogue[4]))  # why give item dialogue
                time.sleep(1)
                self.add_clue(self.dice_goblin.clues[0])  # adds clue to location clues
                print(self.review_clues(), "\n")  # displays clues so far
                self.player.add_item("1 gold doubloon")  # adds item to player
                print(self.dice_goblin.say_dialogue(self.dice_goblin.dialogue[5]))  # don't tell anyone else dialogue
                time.sleep(1)

            print(self.dice_goblin.say_dialogue(self.dice_goblin.dialogue[1]))  # play dice minigame dialogue
            time.sleep(1)
            play_dice = False
            play_rps = False
            self.choice = 0  # reset choice variable
            while self.choice != "1" or "2":  # error check
                if self.game_run:
                    print("-------------------------------------------------------\n")
                    self.choice = input("1) Yes\n"
                                        "2) No\n")
                    print("-------------------------------------------------------\n")
                    if self.choice == "1":  # Yes
                        dice_game(self.player)  # plays dice minigame
                        play_dice = True
                    elif self.choice == "2":  # No
                        print(self.dice_goblin.say_dialogue(
                            self.dice_goblin.dialogue[2]))  # play R.P.S. minigame dialogue
                        time.sleep(1)
                        self.choice = 0  # reset choice variable
                        while self.choice != "1" or "2":  # error check
                            print("-------------------------------------------------------\n")
                            self.choice = input("1) Yes\n"
                                                "2) No\n")
                            print("-------------------------------------------------------\n")
                            if self.choice == "1":  # Yes
                                Rock_Paper_Scissors_Game(self.player)  # plays R.P.S. minigame
                                play_rps = True
                                break
                            elif self.choice == "2":  # No
                                self.music_stop()  # stops current music

                                self.lv5_background_play()
                                self.main_camp()
                                break
                    if play_dice:
                        print(self.dice_goblin.say_dialogue(self.dice_goblin.dialogue[3]))  # play again dialogue
                        time.sleep(1)
                        self.choice = 0  # reset choice variable
                        while self.choice != "1" or "2":  # error check
                            print("-------------------------------------------------------\n")
                            self.choice = input("play again?:\n"
                                                "1) Yes\n"
                                                "2) No\n")
                            print("-------------------------------------------------------\n")
                            if self.choice == "1":  # Yes
                                dice_game(self.player)
                            elif self.choice == "2":  # No
                                print("You collect your winnings and leave Dicy")
                                self.music_stop()  # stops current music

                                self.lv5_background_play()
                                self.main_camp()
                    elif play_rps:
                        print(self.dice_goblin.say_dialogue(self.dice_goblin.dialogue[3]))  # play again dialogue
                        time.sleep(1)
                        self.choice = 0  # reset choice variable
                        while self.choice != "1" or "2":  # error check
                            print("-------------------------------------------------------\n")
                            self.choice = input("play again?:\n"
                                                "1) Yes\n"
                                                "2) No\n")
                            print("-------------------------------------------------------\n")
                            if self.choice == "1":  # Yes
                                Rock_Paper_Scissors_Game(self.player)
                            elif self.choice == "2":  # No
                                print("You collect your winnings and leave Dicy")
                                self.music_stop()  # stops current music

                                self.lv5_background_play()
                                self.main_camp()
                else:
                    break
                self.music_stop()  # stops current music

                self.lv5_background_play()
                self.main_camp()

    def grave(self):  # used to observe and investigate the grave and to lead to the cave/end
        while self.game_run:
            self.current_location = "grave"
            if self.current_location not in self.visited_sublocations:
                self.visited("grave")
                print("At the base of a sprawling ancient oak tree rests The Legendary Witch Slayer's grave. \n"
                      "The weathered tombstone bears a symbol of a crossed sword and broomstick, marking the hero's "
                      "final battles against darkness.\nMoss-covered and surrounded by the quiet embrace of nature, "
                      "the site is near a mysterious cave entrance—the backdrop to the hero's last epic confrontation. "
                      "\nShadows dance as daylight filters through ancient branches, creating an aura of reverence. "
                      "The air whispers with the hero's legacy, ensuring their tale endures in the heart of the "
                      "enchanted forest.")
                time.sleep(3)
            self.choice = 0  # reset choice variable
            while self.choice != "1" or "2" or "3" or "4":  # error check
                if self.game_run:
                    print("-------------------------------------------------------\n")
                    self.choice = input("What will you do?\n"
                                        "1) Investigate the Grave closer\n"
                                        "2) Sit by the grave for a while\n"
                                        "3) Investigate the Cave\n"
                                        "4) return to camp\n")
                    print("-------------------------------------------------------\n")
                    if self.choice == "1":  # Investigate the Grave closer
                        print(
                            "As you inspect the grave further you spot a scrap of red cloth stuck to a particularly "
                            "rough part")
                        time.sleep(1)
                        if "The Legendary Witch Slayer will save us all message" in self.player.main_clues:
                            print("You remember that this is the same cloth that the cultists wear\n")
                            print("You think to yourself why would this be here on a heroes grave?\n")
                            time.sleep(1)
                            self.player.add_main_clue(
                                "The Legendary Witch Slayer might not be what they seem to be in the legends")
                            self.player.add_item("Red scrap of cloth")
                        else:
                            print("You recognise this cloth but you cant quite remember where")
                            self.player.add_main_clue(
                                "The Legendary Witch Slayer might not be what they seem to be in the legends")
                            self.player.add_item("Red scrap of cloth")
                            time.sleep(1)
                        self.grave()
                    elif self.choice == "2":  # Sit by the grave for a while self.play()
                        self.music_stop()  # stops current music

                        self.grave_play()
                        print(
                            "As you decide to sit by the grave of The Legendary Witch Slayer, time takes on a "
                            "different cadence in this tranquil and sacred place. \n")
                        time.sleep(1)
                        print(
                            "The gentle rustling of leaves overhead creates a soothing melody as sunlight filters "
                            "through the dense canopy, casting dappled patterns on the moss-covered ground.\n ")
                        time.sleep(3)
                        print(
                            "The air carries a subtle fragrance of earth and flowers, blending seamlessly with the "
                            "distant murmur of a crystal-clear stream nearby. Small woodland creatures, curious yet "
                            "unafraid, venture closer to investigate the visitor who has entered their realm.\n ")
                        time.sleep(3)
                        print(
                            "As minutes turn into moments, the atmosphere becomes more charged with an otherworldly "
                            "energy. Shadows playfully dance around the grave, seemingly animated by the spirits of "
                            "the forest. The engraved symbol on the weathered tombstone glows softly as if reflecting "
                            "the hero's enduring presence.\n ")
                        time.sleep(3)
                        print(
                            "In the distance, the mysterious cave entrance stands as a silent gateway to untold "
                            "secrets, occasionally revealing hints of magical whispers and ancient echoes. "
                            "The great oak tree above sways gently in response to a breeze, its leaves creating a "
                            "gentle, melodic rustle—a natural symphony that serenades you in your contemplation.\n ")
                        time.sleep(3)
                        print(
                            "As you sit in quiet reflection, a feeling of connection to the hero's legacy permeates "
                            "the air, bridging the gap between the past and the present. Whether it's the subtle shift "
                            "of sunlight or the occasional fluttering of a butterfly, every detail seems to carry a "
                            "deeper meaning in this hallowed grove. ")
                        time.sleep(3)
                        print("You, immersed in the tranquillity of the moment, may sense a subtle "
                              "reassurance—a reminder that even in stillness, the legends of heroes endure.\n")
                        time.sleep(3)
                        self.choice = 0  # reset choice variable
                        while self.choice != "1":  # error check
                            if self.game_run:
                                print("-------------------------------------------------------\n")
                                self.choice = input("Are you ready to leave the grave\n"
                                                    "1) Yes\n")
                                print("-------------------------------------------------------\n")
                                if self.choice == "1":  # Investigate the Grave closer
                                    self.music_stop()
                                    self.lv5_background_play()
                                    self.grave()
                            else:
                                break
                    elif self.choice == "3":  # Investigate the Cave
                        print("Before you stands the cave mouth framed by moss-covered rocks and veiled in vines."
                              " It beckons with a mysterious allure, its entrance wide and dark, inviting you to "
                              "explore its depths. The shadows within suggest untold secrets, while a gentle breeze "
                              "whispers the promise of undiscovered mysteries concealed within its confines.\n")
                        time.sleep(2)
                        print("As you look closer you notice that there are quite a few fresh footprints in the dirt")
                        time.sleep(1)
                        self.choice = 0  # reset choice variable
                        while self.choice != "1" or "2":  # error check
                            print("-------------------------------------------------------\n")
                            self.choice = input("What will you do?\n"
                                                "1) Enter the cave\n"
                                                "2) Go back to the grave\n")
                            print("-------------------------------------------------------\n")

                            if self.choice == "1":  # Enter the cave
                                self.music_stop()  # stops current music
                                time.sleep(1)
                                self.game_run = False
                                self.summary()
                                break
                            elif self.choice == "2":  # Go back to the grave
                                self.grave()
                        break
                    elif self.choice == "4":  # return to camp
                        print("You leave the grave and return to the center of the camp\n")
                        time.sleep(1)
                        self.main_camp()
                else:
                    break

        # DISPLAY PLAYER, LEVEL SUMMARY

    def summary(self):
        print("\n==================== Level 5 Player Summary ====================")
        # PLAYER NAME DISPLAY
        print(f"Player Name: {self.player.name}")
        # PLAYER FINAL LEVEL COINS
        print(f"Player Coins: {self.player.coins} coins")
        # PLAYER FINAL ITEMS
        print(f"{self.player.show_inventory()}")
        # PLAYER FINAL CLUES
        print(f"\nClues found in this level: {self.review_clues()}")

        print("==================== End of Player Summary ====================\n")


if __name__ == "__main__":
    player = Player("Player Name")
    camp = Level5(0)
    camp.outer_camp()
