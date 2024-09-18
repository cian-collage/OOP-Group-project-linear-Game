"""
Author : Joshua Sunil Mathew
Program Description: OOP - Python Game Assignment - Challenges for Level 1


Required for Level 1
This is the code for challenges and puzzles within the storyline of Level 1
1. Book Roulette
    - 1. Riddle
    - 2. Word Manipulation
    - 3. History Trivia
2. Glass Ball Catching game, where a number is generated from 1-3 and there are 3
positions for where the ball can land...- the user selects a number tries to catch the ball

"""

#IMPORTS
import random  # Import the random module for generating random numbers.
import time  # Import the time module for adding delays in the game.

# MAIN CHALLENGES CLASS
class Challenges:
    def __init__(self):
        # Define a dictionary of books and their corresponding challenges.
        self.books = {
            "The Mighty Mystery Book": "Solve a Simple Riddle!",
            "The Perplexing Puzzle Book": "Solve a Logical Puzzle",
            "The Heroic History Book": "Answer a historical trivia question!",
        }

    def book_roulette(self):
        # Print introductory messages for the Book Roulette challenge.
        print(f"David the Druid: Welcome to the Book Roulette! A book will be chosen, "
              f"and you'll face the challenge.")
        print("========INSTRUCTIONS===========")
        print("There are 3 books, and the book you receive is random! Solve the given "
              "book puzzle to \nadvance to the final challenge!"
              "\nand earn coins!")

        # Randomly choose a book from the dictionary.
        chosen_book = random.choice(list(self.books.keys()))
        time.sleep(3)
        print("\n3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print(f"You have picked up, '{chosen_book}'.")
        print(f"Challenge: {self.books[chosen_book]}\n")

        # Implement logic to handle different challenges based on the chosen book.
        if chosen_book == "The Mighty Mystery Book":
            self.solve_riddle()
        elif chosen_book == "The Perplexing Puzzle Book":
            self.solve_puzzle()
        elif chosen_book == "The Heroic History Book":
            self.history_trivia()

    def solve_riddle(self):
        print("You open the Mighty Mystery Book, and a riddle is revealed:\n")
        riddle = "What has to be broken before you can use it?"
        print(f"Riddle: {riddle}")
        print("1. Egg \n2. Glass \n3. Heart")

        # Keep prompting the player until they solve the riddle.
        while True:
            # Get the player's answer.
            player_answer = input("Your answer : ").lower()

            # Check if the player's answer is correct.
            if player_answer.lower() == "egg" or player_answer.lower() == '1':
                print("Congratulations! You've solved the puzzle! Here are 3 coins.")
                break
            else:
                print("Unfortunately, that's not the correct answer. Keep trying!")

    def solve_puzzle(self):
        print("Here is your perplexing puzzle: \n")
        time.sleep(1)
        puzzle_description = ("Reorder the letters of the word 'NAANAB' to create the "
                              "name of a certain yellow fruit.")
        print(puzzle_description)

        # Keep prompting the player until they solve the puzzle.
        while True:
            try:
                user_solution = input("Your solution: ").lower()

                # Evaluate the user's solution.
                correct_solution = "banana"  # Example correct solution
                if user_solution == correct_solution:
                    print("Congratulations! You've solved the puzzle. Here are 3 more "
                          "coins.")
                    break
                else:
                    print("Sorry, that's not the correct solution. Keep trying!")
            except Exception as e:
                print(f"An error occurred: {e}. Please enter a valid response.")

    def history_trivia(self):
        print("The Heroic History Book presents you with a historical trivia question "
              "Can you answer it?")
        trivia = ("Which Medieval European Kingdom was known for its legendary kings, "
                  "King Arthur?")
        print(f"Your Question is: {trivia}")
        print("1. France \n2. Spain \n3. England")

        # Keep prompting the player until they answer the trivia question correctly.
        while True:
            # Get the player's answer.
            player_answer = input("Your answer: ").lower()

            # Check if the player's answer is correct.
            if player_answer.lower() == "england" or player_answer.lower() == '3':
                print("Congratulations! You've solved the trivia question! Here are 3 "
                      "more coins.")
                break
            else:
                print("Unfortunately, that's not the correct answer. Keep trying!")

# DRUIDS 's CHALLENGE 1 CLASS
class DruidGame:
    def catch_ball(self):
        # Print introductory messages for the Catch the Crystal Ball challenge.
        print("Challenge 1 is 'Catch the Crystal Ball!'")
        print("========INSTRUCTIONS===========")
        print("The Druid's mystical Crystal Ball will drop from a random position.")
        time.sleep(1)
        print("You will have to choose position 1, 2, or 3 to catch it.")
        time.sleep(3)

        # Keep prompting the player until they catch the Crystal Ball.
        while True:
            correct_position = random.randint(1, 3)

            try:
                player_choice = int(input("\nChoose your position (1, 2, or 3): "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if player_choice == correct_position:
                print("\nCongratulations! You caught the Crystal Ball!")
                break
            else:
                print("Oh no! The Crystal Ball slipped through your fingers.")
