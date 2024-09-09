import room

class Game:

    def __init__(self, rooms): #rooms is a list of Room objects
        self.rooms = rooms
        self.currentPosition = self.rooms[0] 
        self.inventory = []
        self.currentItem = None

    #player actions
    def move(self, direction: str):
        match direction.lower():
            case "north" | "n":
                if self.currentPosition.neighbors[0]:
                    print("can't go in that direction")
                else:
                    self.currentPosition = self.currentPosition.neighbors[0]

            case "east" | "e":
                if self.currentPosition.neighbors[1]:
                    print("can't go in that direction")
                else:
                    self.currentPosition = self.currentPosition.neighbors[1]

            case "south" | "s":
                if self.currentPosition.neighbors[2]:
                    print("can't go in that direction")
                else:
                    self.currentPosition = self.currentPosition.neighbors[2]

            case "west" | "w":
                if self.currentPosition.neighbors[3]: 
                    print("can't go in that direction")
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

    def use(self, item):
        if item.use == None:
           print("item  can't be used")
        if item in self.inventory and self.currentItem.use == item:
           print(self.currentItem.useDescription)

    #main function containing all game play
    def game(self):
        print("opening description")
        
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
                case "use" | "u":
                    self.use(userInput[1])
                case _:
                    print("didn't understand that")
