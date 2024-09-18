"""
Program Name: level3.py

Author: Max Ceban

Program Description:

This is the third level out of our six-level game.
This level will mess with the player/Red Herring.
This is set in the middle of the town in which the player will need to solve riddles by npcs.
The clues collected throughout the level will lead to a plot twist in our player's quest.
The player can react with the merchants and can buy items that can enhance gameplay.

Date: 25/11/2023
"""
# Import the necessary dependencies, Location, Player, and NPC classes
from denis.Player import Player
from sean.locationClass import Location
from sean.fight import fight, User, CultMember
from cian.characters import NPC
from max.minigame import cipher_decryption_game
from max.riddle import riddle_game

import time
import pygame


class Level3(Location):
    """
        This class represents the third level of the game and inherits from the Location class.
        It includes specific locations and NPCs for the level.
    """

    def __init__(self, player):
        """
           Initializes a Level3 instance with the specified player.

           Args:
           - player: An instance of the Player class representing the player in the game
        """

        # Call the constructor of the superclass (Location) with initial values
        super().__init__("Town Center", ["Market", "Crown and Chalice Inn", "Haven's Port"],
                         ["Textile Merchant", "BlackSmith", "Potion Mixer", "Street Performers",
                          "Tavern keeper"], [])

        # Initialize player, current_location, and side_quest_enabled attributes
        self.player = player
        self.current_location = self.sublocation[0]
        self.side_quest_enabled = False

        # Initialize NPCs with specific attributes
        self.blacksmith = NPC("Astrid Steelheart",
                              ["Welcome to the Iron-heart Forge. What brings you here today adventurer? "
                               "\nNew armor, maybe new tools or a legendary sword for you?"],
                              "Seen some cloaked folks gone to the potion mixer for some potions.", "Sword",
                              "")

        self.textile_merchant = NPC("Elara Looming",
                                    ["Dear patrons, welcome to the world of wonder!\n"
                                     "Step into the world of Velvet Haven Textiles, where every thread tells a story "
                                     "and every fabric whispers its unique story."], "Paper with the cult logo",
                                    "Fur coat", "")

        self.potion_mixer = NPC("Gwyneth Gerald",
                                ["Ah, hello, adventurer! Enter the mystical embrace of Gwyneth's sorcery.\n"
                                 "There, the air is filled with the enchanting essence of unknown possibilities."],
                                "Deciphered Message", "Spellbook", "")

        self.street_performer = NPC("The juggler",
                                    ["Yeah, saw someone briefly, but they vanished into the crowd. Might "
                                     "be nothing"], "Cloaked figure near fountain", " ", "")

        self.drunken_elf1 = NPC("Aricen Emberheart",
                                ["You know what's the best part about being an elf? We're like, "
                                 "timeless, man. I've got all the time in the world to enjoy "
                                 "this tavern!"], "", "",
                                ["swaying on the stool"])

        self.drunken_elf2 = NPC("Clarista Starfall", ["Timeless? I think you've had too much elven wine, friend. "
                                                      "You've got tomorrow morning catching up with you."],
                                "", "", ["raising an eyebrow"])

        self.drunken_elf3 = NPC("Thandor Dawnwhisper",
                                ["Present, future, who cares? I'm just here for the company and the questionable "
                                 "decisions!"], "", "", ["joining the conversation"])

        # Create a list containing instances of the NPC class representing drunken elves in the tavern
        self.drunken_elves = [self.drunken_elf1, self.drunken_elf2, self.drunken_elf3]

        self.tavern_keeper = NPC("Finnegan McCathy", ["Ceád míle fáilte to all ye weary wanderer!."],
                                 "Cult heading to the port", "", "Leaned me on me glaring to my soul")

        self.cult_member = NPC("Cult Member", " ", "", "Map leading the player", "")

        self.craftsman = NPC("Malik Thompson",
                             ["Greetings, friend! What brings you to my humble abode?",
                              "Are you in need of a piece that tells a story or seeking the magic that can be found "
                              "in the heart of crafted wonders?"], "", "Feathernutter",
                             ["Protecting Feathernutter", "Humming a rhythm", "Playing an instrument"])

        # Boolean variables set to False to track interactions with NPCs
        self.__blacksmith_interacted = False
        self.__textile_merchant_interacted = False
        self.__potion_mixer_interacted = False
        self.__street_performer_interacted = False
        self.__drunken_elves_interacted = False
        self.__tavern_keeper_interacted = False
        self.__craftsman_interacted = False

    @staticmethod
    def play_theme_song():
        pygame.mixer.init()
        pygame.mixer.music.load("main_theme_level3.mp3")
        pygame.mixer.music.play(loops=10)  #

    @staticmethod
    def play_tavern_song():
        pygame.mixer.init()
        pygame.mixer.music.load("tavern_theme.mp3")
        pygame.mixer.music.play(loops=10)  #

    @staticmethod
    def play_boss_theme():
        pygame.mixer.init()
        pygame.mixer.music.load("boss_music_theme.mp3")
        pygame.mixer.music.play(loops=10)  #

    def summary(self):
        print("\n==================== Level 3 Player Summary ====================")
        # PLAYER NAME DISPLAY
        print(f"Player Name: {self.player.name}")
        # PLAYER FINAL LEVEL COINS
        print(f"Player Coins: {self.player.coins} coins")
        # PLAYER FINAL ITEMS
        print(f"{self.player.show_inventory()}")
        # PLAYER FINAL CLUES
        print(f"\nClues found in this level: {self.review_clues()}")

        print("==================== End of Player Summary ====================\n")

    def level_start(self):
        """
            Initiates the start of Level 3, providing a descriptive narrative of the town center
            and invoking the 'market' method to proceed with the gameplay.
        """
        print(f"You steps afoot to the town center of Eldenhaven lively {self.current_location}"
              f" square after finding a way in,\n"
              f"where colourful stalls filled with treasure, the savory wonderful scent of roasting meats, "
              f"\nwith mesmerising street performances happening at the minute with camaraderie underneath the cold "
              f"snowy night.")

        time.sleep(2)
        self.market()

    def market(self):
        """
            Manages the gameplay interactions within the Market location.

            The method presents a loop where the player can choose actions such as exploring the market,
            going to the tavern, or heading to the port.
            Depending on the chosen action, it updates the
            current location and invokes corresponding methods to progress the gameplay.
        """
        self.play_theme_song()

        while self.current_location == self.sublocation[0]:
            action = input("\nWhat will you do? 🤔,\n"
                           "1) Take a look around the market 🤑\n"
                           "2) Go to the tavern 🍻\n"
                           "3) Go to the Port ⚓\n")
            if action == "1":
                if self.sublocation[0] not in self.visited_sublocations:
                    # Player decides to explore the market
                    print("\nYou decide to take a look around the market square it lays a symphony of sights, sounds, "
                          "and scent before you. You are mesmerised by the selection of medieval marvels.\n")
                    time.sleep(2)
                    print("A muscular blacksmith with a forge, wearing glittering sets of armour and superbly "
                          "manufactured weapons. 🦾\n")
                    time.sleep(2)
                    print("A lively stand decked out in finely woven textiles, selling anything from sumptuous silks to"
                          "long-lasting woollens. 👚\n")
                    time.sleep(2)
                    print("On the other side we see a mysterious figure with cauldrons create magical concoctions "
                          "ready to bewitch anyone. 🧙‍♀️\n")
                    time.sleep(2)
                    print(
                        "In the centre of the marketplace though not traditional merchants , \nthese street performers"
                        " add a dynamic element to this marketplace through their skills entertaining a crowd of "
                        "people. 🤡\n")
                    time.sleep(2)
                    Level3.market_square(self)
                else:
                    Level3.market_square(self)
            elif action == "2":
                if "The Legendary Witch Slayer will save us all message" in self.player.main_clues:
                    if self.sublocation[1] not in self.visited_sublocations:
                        # Player decides to go to the tavern
                        self.current_location = self.sublocation[1]
                        print(f"You decide to head to the {self.current_location} "
                              f"hoping to find the clues 🔍 to continue your quest.\n"
                              f"As you open the tavern door you see that's it filled with life as the melody playing"
                              f"\nLaughter echoed off the wooden wall with such a song of a drinking making the patrons"
                              f" stomping their feet in unison")
                        Level3.tavern(self)
                    else:
                        Level3.tavern(self)
                else:
                    print("I should look around the market ❌")
            elif action == "3":
                if "The Legendary Witch Slayer will save us all message" in self.player.main_clues:
                    # The Player decides to go to the port
                    self.current_location = self.sublocation[2]
                    print("Welcome to Haven's Harbour, a medieval harbour full of marine legends and lively commerce.\n"
                          "Sturdy ships with aged sails dock next to cobblestone alleys where merchants peddle strange "
                          "items.\n")

                    time.sleep(2)

                    print(
                        "Locals who rely on the sea for their livelihood, bringing in fresh catches to supply the town "
                        "and its taverns. 🎣\n")
                    time.sleep(2)
                    print("Defenders of the port, maintaining order and ensuring the safety of its inhabitants. 💂‍♂️\n")
                    time.sleep(2)
                    Level3.port(self)
                else:
                    print("I should look around the market ❌")

    def market_square(self):
        """
           Manages interactions within the Market Square, allowing the player to choose NPCs to interact with.

           The method presents a menu where the player can choose to interact with different characters in the market,
           such as the blacksmith, textile merchant, potion mixer, street performers,
           or leave the market square.
           It handles user input validation and prevents double interactions with the same NPC.
        """
        while self.current_location == self.sublocation[0]:
            try:
                character = int(input("\nWho do you want to interact with: 🗣️\n"
                                      "1) Blacksmith 🖤 \n"
                                      "2) Textile Merchant 👚\n"
                                      "3) Potion Mixer 🧙‍♀️\n"
                                      "4) See the street performers 🤡\n"
                                      "5) Leave the market square. 🚶\n"))
                match character:
                    case 1:
                        print("\n")
                        if not self.__blacksmith_interacted:
                            Level3.interact_with_blacksmith(self)
                        else:
                            print(f"You already interacted with {self.blacksmith.name} 🗣️")
                    case 2:
                        print("\n")
                        if not self.__textile_merchant_interacted:
                            Level3.interact_with_textile_merchant(self)
                        else:
                            print(f"You already interacted with {self.textile_merchant.name} 🗣️")
                    case 3:
                        print("\n")
                        if not self.__potion_mixer_interacted:
                            Level3.interact_with_potion_mixer(self)
                        else:
                            print(f"You already interacted with {self.potion_mixer.name} 🗣️")
                    case 4:
                        print("\n")
                        if not self.__street_performer_interacted:
                            Level3.interact_with_street_performers(self)
                        else:
                            print(f"You already interacted with {self.street_performer.name} 🗣️")
                    case 5:
                        if "The Legendary Witch Slayer will save us all message" in self.player.main_clues:
                            Level3.visited(self, self.current_location)
                            Level3.market(self)
                        else:
                            print("Im missing something key here 🤔💭")
                            Level3.market_square(self)
                        break
                    case _:
                        print("Invalid choice ❌")
            except ValueError as ve:
                print(f"{ve} invalid input it must be a number 1️⃣2️⃣3️⃣")

    def interact_with_blacksmith(self):
        """
            Facilitates the player's interaction with the blacksmith NPC.

            The method initiates a conversation with the blacksmith, providing dialogue options.
            It allows the player to inquire about the cult, ask about forging a sword, or leave the blacksmith.
            Depending on the chosen interaction, the method updates the player's inventory, coins, and clues.
        """
        print(self.blacksmith.say_dialogue(self.blacksmith.dialogue[0]))  # BLACKSMITH SPEAKS VOICE-LINE
        time.sleep(2)

        while not self.__blacksmith_interacted:
            interaction = int(input(f"\n1.) Question {self.blacksmith.name} about the cult\n"
                                    f"2.) Ask about forging a sword\n"
                                    f"3.) Leave the blacksmith\n"))
            if interaction == 1:
                if "Blacksmith's observation on the potion mixer" not in self.clues:
                    print(f"{self.player.name}: Have you heard about the Shadowbound Covenant around abducting people "
                          "recently. 🤔💭")
                    time.sleep(2)
                    print(self.blacksmith.say_dialogue("Yeah the market have been talking about the news."))
                    time.sleep(2)
                    print(self.blacksmith.say_dialogue("One of the merchants reported that they have went to "
                                                       f"the potion mixer as of recently."))
                    time.sleep(2)
                    Level3.add_clue(self, "Blacksmith's observation on the potion mixer")
                    print(Level3.review_clues(self))
                    time.sleep(2)
                else:
                    print("Don't ask the questions twice")
                    time.sleep(2)
            elif interaction == 2:
                if self.blacksmith.items not in self.player.inventory:
                    print(self.blacksmith.say_dialogue("Ohh you interested in crafting an fine piece metal then"
                                                       " you have to pay for it, it'll be 100 coins please."))
                    time.sleep(2)
                    # An extra option depending on the score of the player
                    action = input(f"Want to purchase a sword for 100 coins? ⚔️\n"
                                   "Yes: Y\n"
                                   "No: N\n")
                    if action.lower() == "y":
                        if self.player.coins >= 100:
                            print(self.blacksmith.say_dialogue("Here's your new sword wanderer "
                                                               "your sword will be essential future battle."))
                            time.sleep(2)
                            self.player.coins = self.player.coins - 100
                            print(f"New balance: {self.player.coins}")
                            print(self.blacksmith.say_dialogue(f"The sword suits you traveler, this "
                                                               f"will help you for sure"))
                            time.sleep(2)
                            self.player.add_item(self.blacksmith.items)
                            self.player.show_inventory()
                        else:
                            print(self.blacksmith.say_dialogue("You don't have enough coins for the sword. 💵"))
                            time.sleep(2)
                    elif action.lower() == "n":
                        pass
                    else:
                        print("Invalid option")
                        time.sleep(2)
                else:
                    print(self.blacksmith.say_dialogue("You have a sword already adventurer!"))
                    time.sleep(2)
            elif interaction == 3:
                print(self.blacksmith.say_dialogue("I wish the best of luck in your future journey."))
                time.sleep(2)
                self.__blacksmith_interacted = True
                self.__potion_mixer_interacted = False
            else:
                print("Invalid option")

    def interact_with_textile_merchant(self):
        """
            Facilitates the player's interaction with the textile merchant NPC.

            The method initiates a conversation with the textile merchant, providing dialogue options.
            It allows the player to inquire about the newest trends, ask questions, or leave the textile merchant.
            Depending on the chosen interaction, the method updates the player's inventory, coins, and clues,
            and may trigger a side quest involving finding the missing chicken Fluffernutter.
        """
        if "Fluffernutter the Chicken" not in self.player.inventory and not self.side_quest_enabled:
            print(self.textile_merchant.say_dialogue(self.textile_merchant.dialogue[0]))

            while not self.__textile_merchant_interacted:
                interaction = int(input(f"\n1.) Ask about the newest trends in the shop\n"
                                        f"2.) Question {self.textile_merchant.name}\n"
                                        f"3.) Leave the textile merchant\n"))
                # Checks if the user has found the clue already
                # Else tell the user that you have the clue already
                if interaction == 1:
                    if self.textile_merchant.items not in self.player.inventory:
                        print(self.textile_merchant.say_dialogue(
                            "Discover our collection of popular trends in intricate embroidery, sumptuous velvet, "
                            "and natural, earthy tones.\nYou can also expect shimmering metallic threads, breathable "
                            "linens, and gorgeous brocade fabrics, each fabric unique in its own way.\nIt tells a story"
                            " of elegance."))

                        time.sleep(2)

                        action = input("You take a gander around the shop and seek upon a fur coat for 100 coins.\n"
                                       "Do you wish to purchase it?\n"
                                       "Yes: Y\n"
                                       "No : N\n")

                        if action.lower() == "y":
                            if self.player.coins >= 100:
                                print(
                                    self.textile_merchant.say_dialogue(f"I see the fur coat interests you, this is "
                                                                       f"yours now wanderer it might help in the "
                                                                       f"extreme weather conditions ahead of your "
                                                                       f"journey."))
                                time.sleep(2)
                                self.player.add_item(self.textile_merchant.items)
                                self.player.show_inventory()
                            else:
                                print(
                                    self.textile_merchant.say_dialogue("You do not have another coins for the fur "
                                                                       "coat,\nadventurer perhaps maybe you can find "
                                                                       "my missing cherished chicken Fluffernutter, "
                                                                       "and my heart aches without its presence.\n"
                                                                       "I may provide a extra reward onto of this as "
                                                                       "well."))  # SIDE QUEST FOR THE LEVEL

                                time.sleep(2)
                                action = input("Do want to take part in the side quest?\n"
                                               "Yes: Y\n"
                                               "No: N\n")
                                if action.lower() == "y" or action.capitalize() == "Y":
                                    print(self.textile_merchant.say_dialogue(
                                        "Oh, thank the stars! You're a true lifesaver "
                                        "for agreeing to help me with my little "
                                        "feathered friend.\n"
                                        "My prized chicken, Fluffernutter, has gone "
                                        "missing, and I've been in a complete tizzy.\n"))
                                    time.sleep(2)
                                    print(f"\n{self.player.name}: No worries! I'm happy to help."
                                          f"\nWhere should I start looking?")
                                    time.sleep(2)
                                    print(self.textile_merchant.say_dialogue("Thank you for taking on the "
                                                                             "quest!\nFluffernutter was last seen at "
                                                                             "the port.\nPlease take this feed to "
                                                                             "lure them back.\nI'll reward you "
                                                                             "generously once you bring my chicken "
                                                                             "home safely. Good luck, and may your "
                                                                             "journey be swift!"))
                                    time.sleep(2)
                                    print(
                                        f"{self.player.name}: I'll find Fluffernutter and bring them back, don't worry!")
                                    print("We leave the shop knowing we have a side quest to do!")
                                    time.sleep(2)
                                    self.side_quest_enabled = True
                                    self.__textile_merchant_interacted = True
                                    self.__craftsman_interacted = False
                                    Level3.visited(self, self.current_location)
                                    Level3.market(self)
                        elif action.lower() == "n":
                            pass
                        else:
                            print("Invalid option")
                            time.sleep(2)
                    else:
                        print(self.textile_merchant.say_dialogue("You have a fur coat already adventurer!"))
                        time.sleep(2)
                elif interaction == 2:
                    if "Paper with the cult logo" not in self.clues:
                        print(self.textile_merchant.say_dialogue("Oh yes those people, one of the members a few days \n"
                                                                 "ago tried to influence me to join the cult and left me"
                                                                 " this.\n"))
                        time.sleep(2)
                        print(f"{self.textile_merchant.name} hands you a {self.textile_merchant.clues}")
                        time.sleep(2)
                        Level3.add_clue(self, self.textile_merchant.clues)
                        print(Level3.review_clues(self))
                    else:
                        print("Don't ask the questions twice")
                        time.sleep(2)
                elif interaction == 3:
                    print(self.textile_merchant.perform_action(
                        "Waves nervously as I leave the stores maybe its just \n"
                        "something in his mind"))
                    time.sleep(2)
                    self.__textile_merchant_interacted = True
        else:
            print(self.textile_merchant.say_dialogue("Thanks a bunch for rescuing my wayward chicken. "
                                                     "To show my appreciation, here's a sturdy armor for you – "
                                                     "and a pouch with 75 coins.\n"
                                                     "Never expected a chicken chase to turn into such an adventure!\n"
                                                     "If you ever need more help or encounter more feathered mischief, "
                                                     "you know where to find me.\nSafe travels!"))
            time.sleep(2)
            self.player.remove_item("Fluffernutter the Chicken")
            self.player.add_item("Armor")
            self.player.show_inventory()
            self.player.name = self.player.name + 75
            self.side_quest_enabled = False

    def interact_with_potion_mixer(self):
        """
            Facilitates the player's interaction with the potion mixer NPC.

            The method initiates a conversation with the potion mixer, providing dialogue options.
            It allows the player to ask about ingredients, ask questions, or leave the potion mixer.
            Depending on the chosen interaction, the method updates the player's inventory, coins, and clues.
        """
        print(self.potion_mixer.say_dialogue(self.potion_mixer.dialogue[0]))

        time.sleep(2)

        while not self.__potion_mixer_interacted:
            interaction = int(input(f"\n1.) Ask about the ingredient\n"
                                    f"2.) Question {self.potion_mixer.name}\n"
                                    f"3.) Leave the potion mixer\n"))
            if interaction == 1:
                print(self.potion_mixer.say_dialogue("These ingredients I use here are not the herbs and "
                                                     "powders you find in this realm, these are blessed by the "
                                                     "lord that watches above us.\nIf I reveal too much it might "
                                                     "be the end of this town. \nSomethings are left untouched."))
                time.sleep(2)
            elif interaction == 2:
                if "Blacksmith's observation on the potion mixer" in self.clues:
                    if self.potion_mixer.items not in self.player.inventory:
                        print(f"{self.player.name}: I have some questions for you to answer about the "
                              f"Shadowbound Covenant")
                        time.sleep(2)
                        print(self.potion_mixer.perform_action("Looks at me terrifying as she screeches some "
                                                               "encrypted message as she runs away\n"))
                        time.sleep(2)
                        print("Let's decipher what she said:\n")
                        cipher_decryption_game()
                        self.player.add_main_clue("The Legendary Witch Slayer will save us all message")
                        self.player.show_main_clues()
                        print(f"You pick up some {self.potion_mixer.items} and decide to keep it.")
                        time.sleep(2)
                        self.player.add_item(self.potion_mixer.items)
                        self.player.show_inventory()
                        self.__potion_mixer_interacted = True
                    else:
                        print(f"{self.potion_mixer.name} is gone")
                        time.sleep(2)
                else:
                    print("There's something I need to know first")
                    self.__blacksmith_interacted = False
            elif interaction == 3:
                print(self.potion_mixer.perform_action("Glares at you as you walk away from her"))
                time.sleep(2)
                self.__potion_mixer_interacted = True

        Level3.market_square(self)

    def interact_with_street_performers(self):
        """
            Facilitates the player's interaction with the street performers NPC.

            The method narrates the player's approach to the street performers, gathering information from the audience
            about a cloaked figure near the fountain during the performance.
            It adds a relevant clue to the player's inventory.
            The player expresses gratitude, contemplating whether the sighting was a deliberate distraction.
        """
        print(f"As {self.player.name} approaches the spectacular street performers, drawn by their routine.\n"
              f"You began hearing the audience about a cloaked figure during the performance near the fountain of "
              f"the market square.\nAnything you noticed?")
        time.sleep(2)
        print(self.street_performer.interact())
        Level3.add_clue(self, "Cloaked figure near fountain")
        print(Level3.review_clues(self))
        time.sleep(2)
        print(f"As {self.player.name} thanked them, they couldn't stop wondering if this coincidental sighting"
              " was a deliberate distraction.")
        time.sleep(2)
        self.__street_performer_interacted = True

    def tavern(self):
        """
            Manages the player's activities within the Crown and Chalice Inn.

            The method allows the player to interact with the drunken elves, visit the bar, or leave the tavern.
            It handles user input, invoking specific methods based on the chosen action.
        """
        self.play_tavern_song()
        time.sleep(2)

        while self.current_location == self.sublocation[1]:
            try:
                action = int(input("\nWhat will you do?,\n"
                                   "1) Interact with the drunken elves 🧝🧝‍♂️🧝‍\n"
                                   "2) Head to the bar\n"
                                   "3) Leave the tavern\n"))
                match action:
                    case 1:
                        if not self.__drunken_elves_interacted:
                            Level3.interact_with_elves(self)
                        else:
                            print("You interacted with the elves already")
                    case 2:
                        if not self.__tavern_keeper_interacted:
                            Level3.bar(self)
                        else:
                            print("You interacted with the tavern keeper already")
                    case 3:
                        Level3.visited(self, self.current_location)
                        self.current_location = self.sublocation[0]
                        Level3.market(self)
                    case _:
                        print("Invalid option ❌")
            except ValueError as ve:
                print(f"{ve} input should be a number 1️⃣2️⃣3️⃣")

    def interact_with_elves(self):
        """
        Facilitates the player's interaction with the drunken elves in the Crown and Chalice Inn.

        The method initiates a conversation with the elves, providing options to inquire about the tavern's history,
        engage in a riddle game, or leave the elves alone.
        It manages the flow of dialogue and updates the player's clues.
        """
        for elf in self.drunken_elves:
            print(elf.say_dialogue(elf.dialogue))
            time.sleep(2)
            print(elf.perform_action(elf.actions))

        print("\n")

        while self.current_location == self.sublocation[1]:
            interaction = int(input(f"1.) Ask about the tavern's history ⏳\n"
                                    f"2.) Question the elves 🧝🧝‍♂️🧝‍♀️\n"
                                    f"3.) Leave the elves alone 🚶\n"))
            if interaction == 1:
                print(
                    self.drunken_elf1.say_dialogue(
                        "Established in 1685, The Crown and Chalice Inn 👑 in Eldenhaven is a "
                        "historic hub, \n once a haven for travelers and now a charming "
                        "space for"
                        "locals and visitors. The inn's name, 'The Crown and Chalice,"
                        "' \n nods to the town's noble heritage. With its exposed beams and "
                        "faded"
                        "tapestries, the inn invites patrons to step into Eldenhaven's rich "
                        "history\n"))
                time.sleep(2)
                print(self.drunken_elf2.say_dialogue("Hey adventurer Why did the ghost refuse to haunt The Crown and "
                                                     "Chalice Inn?\n"))
                time.sleep(2)
                print(self.drunken_elf3.say_dialogue("Because the spirits were too high, and he couldn't find a "
                                                     "'boo'-th to himself\\n"))

                print("(They clink mugs and burst into laughter, to the bemusement of other tavern patrons.) 🍻")
                time.sleep(2)
            elif interaction == 2:
                if "Elves' observation on the tavern keeper" not in self.clues:
                    print(self.drunken_elf2.say_dialogue("Hark, ye noble celebrant! Prepare thy wit for a riddle from "
                                                         "days of yore!\nWhat be the thing with a golden head, "
                                                         "silver tail, and no body, yet it dances through the air "
                                                         "with a"
                                                         "fiery trail? \nEngage thy mind in this medieval mystery and "
                                                         "let"
                                                         "the revelry continue!\n"))
                    time.sleep(2)

                    print(self.drunken_elf2.perform_action("leaning against my face."))

                    time.sleep(2)

                    action = input("Want to try and solve it? 'y' or 'n':\n")

                    if action.lower() == "y" or action.capitalize() == "Y":
                        time.sleep(2)
                        riddle_game()
                        print(self.drunken_elf1.say_dialogue("Congrats, Riddle Master! You've cracked the "
                                                             "medieval mysteries like a goofy genius!\n May your "
                                                             "candles always burn bright,\nhorses gallop swift, "
                                                             "and dragons... well,\nstay mythical and mysterious! "
                                                             "Keep rocking those riddles with a touch of "
                                                             "goofiness!\n"
                                                             "#RiddleChampion"))
                        time.sleep(2)
                        print(self.drunken_elf2.say_dialogue("We heard a cult member's discuss with the tavern "
                                                             "keeper"
                                                             " on booking the venue soon speak with the keeper"))
                        time.sleep(2)
                        Level3.add_clue(self, "Elves' observation on the tavern keeper")
                        print(Level3.review_clues(self))
                    elif action.lower() == "n" or action.capitalize() == "N":
                        pass
                else:
                    print("You solved the riddle already!")
            elif interaction == 3:
                self.__drunken_elves_interacted = True
                Level3.tavern(self)
            else:
                print("Invalid option ❌")
                time.sleep(2)

    def bar(self):
        """
        Manages the player's interaction with the tavern keeper in the Crown and Chalice Inn.

        The method checks if the player has acquired the elves' observation about the tavern keeper before initiating
        a conversation.
        It provides context to the player based on the obtained clue and guides them through the dialogue.
        The tavern keeper reveals information about the Shadowbound Covenant terrorizing Eldenhaven
        and warns the player about
        the cult's activities at the port.
        The method updates the player's clues accordingly.
        """
        if "Elves' observation on the tavern keeper" not in self.clues:
            print(f"{self.player.name}: I feel like there's something I need to know before I do this")
            self.__drunken_elves_interacted = False
            time.sleep(2)
        else:
            print("You have the observation from the elves in which you go to the Tavern Keeper")
            time.sleep(2)
            print(self.tavern_keeper.say_dialogue(self.tavern_keeper.dialogue[0]), "\u2618\ufe0f")
            time.sleep(2)
            print(
                f"{self.player.name}: I've been hearing around from the locals that "
                f"the Shadowbound Covenant is terrorizing this "
                f"Eldenhaven \nabducting people and committing satanic rituals to them,\nyou seem to know something "
                f"\U0001F914")
            time.sleep(2)
            print(
                self.tavern_keeper.say_dialogue("Aye, I've heard of the Shadowbound Covenant terrorizing Eldenhaven.\n"
                                                "Whispers speak of abductions and dark rituals.\nTread carefully, "
                                                "friend.\nThe cult operates in shadows at the port, "
                                                "and prying eyes may attract their malevolent gaze."))
            time.sleep(2)
            Level3.add_clue(self, "Cult at the port")
            print(Level3.review_clues(self))
            self.__tavern_keeper_interacted = True

    def port(self):
        """
        Manages the player's interaction with Haven's Port, a medieval harbor with marine legends and lively commerce.

        The method provides an atmospheric description of the port, introducing ships, merchants, and defenders.
        If the clue "Cult at the port" is not in the player's clues, it allows the player to interact with the craftsman
        or leave the port.
        If the clue is present, it describes a confrontation with a clandestine cult engaged in an ominous
        ritual.

        The player confronts the cult, leading to a fight scenario.
        If the player succeeds, they receive a reward, and the method proceeds to the ending of the level.
        """
        if "Cult at the port" not in self.clues:
            while self.current_location == self.sublocation[2]:
                try:
                    action = int(input("\nWhat will you do?,\n"
                                       "1) Interact with the Craftsman 🗣️\n"
                                       "2) Leave Haven's Port 🚶\n"))
                    match action:
                        case 1:
                            if not self.__craftsman_interacted:
                                self.interact_with_craftsman()
                                time.sleep(2)
                            else:
                                print("You interacted with the craftsman already")
                                time.sleep(2)
                        case 2:
                            Level3.visited(self, self.current_location)
                            self.current_location = self.sublocation[0]
                            Level3.market(self)
                        case _:
                            print("Invalid option")
                except ValueError as ve:
                    print(f"{ve} input needs to be a integer")
        else:
            self.play_boss_theme()
            print(
                "Beneath the moonlit port, the cult engaged in an ominous ritual. ☦️\n"
                f"{self.player.name} confronted them, demanding answers.\n"
                "Interfering with our sacred gathering, detective? the cult leader hissed.\n"
                f"Undeterred, {self.player.name} stood firm.\n"
                "Laughter echoed as the cult chanted, conjuring an eerie ambiance.\n"
                f"Tension peaked, and a cult member lunged at {self.player.name}. 😱\n")
            time.sleep(5)

            user = User(self.player.name)
            cult_member = CultMember()
            final_fight = fight(user, cult_member)

            if final_fight:
                self.player.add_item(final_fight)
                self.player.show_inventory()
                self.player.coins = self.player.coins + 200
                Level3.ending(self)
            Level3.market(self)

    def interact_with_craftsman(self):
        """
        Manages the player's interaction with the craftsman near the port.

        If the side quest is enabled, the player encounters a burly craftsman holding Fluffernutter the Chicken.
        The craftsman demands a toll of 35 coins for Fluffernutter's freedom.
        The player can choose to pay or decline.
        If paid, the craftsman releases Fluffernutter, and the player receives the chicken back.
        If declined,
        Fluffernutter
        remains with the craftsman until the toll is paid.
        The method updates the player's inventory and coins accordingly.

        If the side quest is not enabled, the player experiences a vibrant workshop with a skilled craftsman working on
        metal and wood.
        The craftsman shares dialogue reflecting pride, heritage, and the rich traditions of their
        African roots.

        After the interaction, the craftsman's status is marked as interacted.
        """
        if self.side_quest_enabled:
            print("As you approach Fluffernutter near the port, you notice a burly craftsman holding the chicken in "
                  "his hands, a mischievous glint in his eyes.")

            print("Well, well, what have we here? Seems like you're looking for this feathery friend. If you want "
                  "your precious chicken back, you'll have to pay a toll of 35 coins.\nFluffernutter's freedom comes "
                  "at a price, my friend")

            action = input("Fluffernutter squawks as if in agreement. What's your response? 🐔\n"
                           "Yes: Y\n"
                           "No: N\n")

            if action.lower() == "y" or action.capitalize() == "Y":
                if self.player.coins >= 35:
                    print(f"{self.player.name} reach into their pouch and count out the required 35 coins."
                          f"\nWith a reluctant sigh,they hand the coins over to the craftsman, who smirks triumphantly."
                          f"😏")
                    time.sleep(2)
                    print(self.craftsman.say_dialogue("Smart choice, my friend. Fluffernutter is free to go."))
                    time.sleep(2)
                    print(self.craftsman.perform_action("the craftsman releases the chicken, who scurries back to the "
                                                        "player."))
                    time.sleep(2)
                    self.player.add_item("Fluffernutter the Chicken")
                    self.player.show_inventory()
                    self.player.name = self.player.name - 35
                    print("Coins: ", self.player.name)
                    time.sleep(2)
                    self.__textile_merchant_interacted = False
                    print(f"I can bring him back now to {self.textile_merchant.name}")
                    time.sleep(2)
                else:
                    print(self.craftsman.say_dialogue("Well, well. Seems like you're a bit short on funds. I can't "
                                                      "just release Fluffernutter for free, you know.\n You've got one "
                                                      "options: scrounge up the coins. Otherwise, your feathery "
                                                      "friend stays in my grasp. 😈"))
                    time.sleep(2)
            elif action.lower() == "n" or action.capitalize() == "N":
                print(self.craftsman.say_dialogue("Stubborn, aren't you? Well, if you won't pay.\nFluffernutter stays "
                                                  "with me until you pay up."))
                time.sleep(2)
            else:
                print("Invalid Input")
                time.sleep(2)
        else:
            print(
                "As you approach the vibrant workshop, the rhythmic sound of metal hitting metal and the sweet scent of"
                " exotic woods will greet you.\n"
                "The artist, a sturdy figure with warm earth-toned skin and decorated with colorful fabrics, "
                "looks up from his work as you enter.")
            time.sleep(2)

            print(self.craftsman.say_dialogue(self.craftsman.dialogue[0]))
            time.sleep(2)
            print(self.craftsman.say_dialogue(self.craftsman.dialogue[1]))
            time.sleep(2)

            print("Their eyes are filled with wisdom and a deep understanding of the craft, reflecting the pride and "
                  "heritage attached to each piece.\nIt is clear that this artist's work not only reflects his know-how"
                  "but also carries with it the rich traditions and stories of his African roots.")
            time.sleep(2)

        self.__craftsman_interacted = True

    def ending(self):
        """
        Presents the conclusion of the level, providing details on the subdued cult member's cryptic map.
        The map reveals a path through a mushroom forest and a goblin camp,
        guiding the player to the cult's hidden home
        base.
        As the player ventures through enchanted landscapes, the air thickens with mystery, setting the stage for a
        perilous journey into the heart of darkness.
        """
        print("The subdued cult member, in possession of a cryptic map, also clutched a mysterious "
              "red cloth held by a cult member.\n"
              "The map revealed a path through a mushroom forest and a goblin camp.\n"
              "Undeterred, the detective follows the mystical trail, unfolding the cult's hidden home base.\n"
              "As they venture through enchanted landscapes, the red cloth becomes a key, "
              "guiding them through the twists and turns.\n"
              "The air thickens with mystery, setting the stage for a perilous journey into the heart of darkness.")

        self.player.add_main_clue("A cryptic map")
        self.player.add_main_clue("Red Cloth")
        self.summary()
        pygame.mixer.music.stop()
        print("\n")


if __name__ == "__main__":
    player = Player("")
    level3 = Level3(player)  # Provide a name for the player
    level3.level_start()
    level3.market()
