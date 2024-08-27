#!/usr/bin/python
from room import Room

class Main:

    def main():
       
        rooms = []

        #create rooms
        items = {}
        neighbors = []
        description = "description of living room"
        livingRoom = Room("livingRoom", items, neighbors, description)
        rooms.append(livingRoom)
       
        items = {}
        neighbors = []
        description = "description of bedroom"
        bedroom = Room("livingRoom", items, neighbors, description)
        rooms.append(bedroom)

        items = {}
        neighbors = []
        description = "description of family room"
        familyRoom = Room("livingRoom", items, neighbors, description)
        rooms.append(familyRoom)

        items = {}
        neighbors = []
        description = "description of hall"
        hall = Room("livingRoom", items, neighbors, description)
        rooms.append(hall)

        items = {}
        neighbors = []
        description = "description of kitchen"
        kitchen = Room("livingRoom", items, neighbors, description)
        rooms.append(kitchen)

        #initialize game
        game(rooms)



    if __name__ == "__main__":
        main()
