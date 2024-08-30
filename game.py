import room

class Game:

    def __init__(self, rooms): #rooms is a list of Room objects
        self.rooms = rooms
        self.currentPosition = self.rooms[0] 
        self.inventory = []

    #player actions
    def move(self, direction: str):
        match direction.lower():
            case "north" | "n":
                if (not self.currentPosition.neighbors 
                    or len(self.currentPosition.neighbors) < 4 
                    or self.currentPosition.neighbors[0] == None):
                    print("can go in that direction")
                else:
                    self.currentPosition = self.currentPosition.neighbors[0]

            case "east" | "e":
                if (not self.currentPosition.neighbors 
                    or len(self.currentPosition.neighbors) < 4 
                    or self.currentPosition.neighbors[1] == None):
                    print("can go in that direction")
                else:
                    self.currentPosition = self.currentPosition.neighbors[1]

            case "south" | "s":
                if (not self.currentPosition.neighbors 
                    or len(self.currentPosition.neighbors) < 4 
                    or self.currentPosition.neighbors[2] == None):
                    print("can go in that direction")
                else:
                    self.currentPosition = self.currentPosition.neighbors[2]

            case "west" | "w":
                if (not self.currentPosition.neighbors 
                    or len(self.currentPosition.neighbors) < 4 
                    or self.currentPosition.neighbors[3] == None):
                    print("can go in that direction")
                else:
                    self.currentPosition = self.currentPosition.neighbors[3]

            case _:
                print("didn't understand that")

    def look(self):
        print(self.currentPosition.description)

    def take(self, item):
        self.inventory.append(item)

    def examine(self, item):
        print(self.currentPosition.items[item])

    def getUserInput(self) -> str:
        return input("> ")

    def getInventory(self):
        print(*self.inventory, sep=", ")

    #main function containing all game play
    def game(self):
        print("opening description")
        #userInput = self.getUserInput().split(" ")
        
        while True:
            userInput = self.getUserInput().split(" ")
            match userInput[0].lower():
                case "quit" | "q":
                    break
                case "look" | "l":
                    self.look()
                case "take" | "t":
                    if not len(userInput) == 2:
                        print("which item were you asking about?")
                    elif userInput[1] in self.currentPosition.items and userInput[1] not in self.inventory:
                        self.take(userInput[1])
                    else:
                        print("that item isn't available")
                case "examine" | "x":
                    if not len(userInput) == 2:
                        print("which item were you asking about?")
                    elif userInput[1] in self.currentPosition.items:
                        self.examine(userInput[1])
                    else:
                        print("that item isn't available")
                case "north" | "n" | "east" | "e" | "south" | "s" | "west" | "w":
                    self.move(userInput[0])
                case "inventory" | "i":
                    self.getInventory()
                case _:
                    print("didn't understand that")
