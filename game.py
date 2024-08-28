class Game:

    def __init__(self, rooms: List[Room]):
        self.rooms = rooms
        currentPosition = self.rooms[0] #is this going to be a problem given that I initilaized to None?
        inventory = []

    #player actions
    def move(direction: str):
        match direction.lower():
            case "north" | "n":
                currentPosition = currentPosition.neighbors[0]

            case "east" | "e":
                currentPosition = currentPosition.neighbors[1]

            case "south" | "s":
                currentPosition = currentPosition.neighbors[2]

            case "west" | "w":
                currentPosition = currentPosition.neighbors[3]

            case _:
                print("didn't understand that")

    def look():
        print(currentPosition.description)

    def take(item):
        inventory.append(item)

    def examine(item):
        print(currentPosition.items[item])

    def getUserInput() -> str:
        return input("> ")

    def inventory():
        print(inventory)

    #main function containing all game play
    def game():
        print("opening description")
        userInput = getuserInput().split(" ")
        
        while:
            match userInput[0].lower():
                case "quit" | "q":
                    break
                case "look" | "l":
                    look()
                case "take" | "t":
                    if userInput[1] in currentPosition and userInput[1] not in inventory:
                        take(userInput[1])
                    else:
                        print("that item isn't available")
                case "examine" | "x":
                    if userInput[1] in currentPosition:
                        examine(userInput[1])
                    else:
                        print("that item isn't available")
                case "north" | "n" | "east" | "e" | "south" | "s" | "west" | "w":
                    move(userInput[0])
                case "inventory" | "i":
                    inventory()
                case _:
                    print("didn't understand that")
