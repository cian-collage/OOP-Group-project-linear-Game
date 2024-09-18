class Location:
    def __init__(self, location, sublocation, location_npcs, clues):
        # Initialize location attributes
        self.location = location
        self.sublocation = sublocation
        self.location_NPCs = location_npcs
        self.clues = clues
        self.visited_sublocations = []

    def add_clue(self, clue):
        # Add a new clue to the location if it's not already present
        if clue not in self.clues:
            print("New Clue! - ", clue)
            self.clues.append(clue)

    def review_clues(self):
        # Get the list of clues associated with the location
        return self.clues

    def location_npcs(self, npc):
        # Add an NPC to the location
        self.location_NPCs.append(npc)

    def general_location(self):
        # Get a general description of the location
        return f"You are in {self.location}"

    def specific_location(self):
        # Get a list of sublocations within the current location
        return self.sublocation

    def visited(self, location):
        # Mark a sublocation as visited
        self.visited_sublocations.append(location)

    def view_visited_locations(self):
        # Get a list of visited sublocations
        return f"You have visited {self.visited_sublocations}"

    def whoishere(self):
        # Get a list of NPCs present in the location
        return self.location_NPCs
