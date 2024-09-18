"""
Program Name: characters.py

Author: Cian Anderson (C22793219) in Group ERROR 451

Program Description:
This is the character class that is used by all levels for the NPCs
it holds Interactions, Clues,  Dialogue and Items.
It allows for perform_action and say_dialogue.
Date: 3/12/2023
"""

from abc import ABC, abstractmethod


class Character(ABC):
    @property
    def actions(self):
        return self._actions

    def __init__(self, name, dialogue, clue, item, action):
        self.name = name
        self.dialogue = dialogue
        self._interacted = False
        self.clues = clue
        self.items = item
        self.actions = action

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}"

    def __eq__(self, other):
        if isinstance(other, Character):
            return self.name == other.name
        return False

    def __lt__(self, other):
        if isinstance(other, Character):
            return self.name < other.name
        return False

    @abstractmethod  # Declares an abstract method using a decorator.
    def perform_action(self, action):
        pass

    @abstractmethod
    def say_dialogue(self, dialogue):
        pass

    def interact(self):
        if not self._interacted:
            interaction = f"{self.name}: {self.dialogue}" # sets interaction
            self._interacted = True
        else:
            interaction = f"You have already talked to {self.name}" # sets interaction

        return interaction # returns the interaction set above

    def clue(self):
        pass
        # add clue to clue list from NPC

    def dialogue(self):
        return self.dialogue # returns list of dialogue

    def items(self):
        return self.items  # returns list of items

    @actions.setter
    def actions(self, value):  # list of actions
        self._actions = value


class NPC(Character):

    def perform_action(self, action):
        return f"{self.name} {action}." # Gives NPC name and action they did

    def say_dialogue(self, dialogue):
        return f"{self.name}: {dialogue}" # Gives NPC name and dialogue the said

    def interact(self):
        interact = super().interact()
        return interact

    def clue(self):
        return self.clues  # returns clue list
