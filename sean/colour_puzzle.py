import random


class ColoredSlabPuzzle:
    def __init__(self, my_location_class, available_colors=None):
        # Initialize the ColoredSlabPuzzle instance with a list of available colors and a solution
        if available_colors is None:
            available_colors = ["Red", "Blue", "Yellow", "Green", "Purple", "Orange", "Black"]
        self.available_colors = available_colors
        self.solution = ["Blue", "Red", "Yellow"]
        self.slabs_order = self.shuffle_slabs()  # Shuffle the order of slabs for the player
        self.won = False
        self.player = my_location_class

    def shuffle_slabs(self):
        # Shuffle the order of slabs for the player to figure out
        shuffled_order = random.sample(self.available_colors, len(self.available_colors))
        return shuffled_order

    def display_slabs_order(self):
        # Display the current order of colored slabs to the player
        print("\nCurrent Order of Colored Slabs:")
        print(" | ".join(self.slabs_order[:3]))
        print()

    def play_puzzle(self):
        # Main function to play the Colored Slab Puzzle
        print("Welcome to the Colored Slab Puzzle!")
        print("Place the colored slabs in the correct order to unlock the door.")
        print("The solution is a sequence of three colors.")

        while True:
            self.display_slabs_order()  # Show the current order of slabs
            print("1) Enter your guess\n"
                  "2) See available colours\n"
                  "3) Review Clues\n"
                  "4) Quit\n")
            user_choice = input("Choose an option (1, 2, 3 or 4): ")

            if user_choice == "1":
                # Player enters their guess and checks if it matches the solution
                user_input = input(
                    "Enter your guess (comma-separated colors, e.g., Purple, Black, Yellow): ").strip().split(',')
                user_input = [color.strip().capitalize() for color in user_input]

                if self.check_solution(user_input):
                    print("You see that a piece of the wall beside you came away.")
                    print("You find a city pass in the opening of the wall.")
                    self.won = True
                    break
                else:
                    print("Incorrect order. Try again.")
            elif user_choice == "2":
                # Display the available colors to the player
                print(self.available_colors)
            elif user_choice == "3":
                # Review clues provided by the player's location
                print(self.player)
            elif user_choice == "4":
                # Quit the puzzle
                print("Quitting the puzzle.")
                return None
            else:
                # Handle invalid choices
                print("Invalid choice. Please choose 1, 2, 3, or 4.")

        if self.won:
            return "City Pass"
        else:
            return None

    def check_solution(self, user_input):
        # Check if the user's input matches the solution
        return user_input == self.solution


# Only run the puzzle if this script is executed directly
if __name__ == "__main__":
    # Create an instance of the ColoredSlabPuzzle and initialize it with a string "Clues"
    puzzle = ColoredSlabPuzzle("Clues")
