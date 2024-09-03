#!/usr/bin/python
from room import Room
from game import Game

class Main:

    def main():
       
        #get rooms to create
        roomNames = []
        rooms = []
        with open('roomsList.txt', encoding="utf-8") as f:
            line = f.readline()
            while line:
                roomNames.append(line.rstrip())
                line = f.readline()
        #create rooms
        for r in roomNames:
            items = {}
            with open(r + 'Items.txt', encoding="utf-8") as f:
                line = f.readline()
                while line:
                    parts = line.split(": ")
                    items[parts[0]] = parts[1]
                    line = f.readline()
        
            neighbors = []
            with open(r + 'Neighbors.txt', encoding="utf-8") as f:
                line = f.readline()
                while line:
                    if line == "None":
                        neighbors.append(None)
                    else:
                        neighbors.append(line)
                    line = f.readline()
                while len(neighbors) < 4:
                    neighbors.append(None)
        
            with open(r + 'Desc.txt', encoding="utf-8") as f:
                description = f.read() 
            room = Room(r, items, neighbors, description)
            rooms.append(room)
            print(*room.neighbors)
       
        #initialize game
        startGame = Game(rooms)
        startGame.game()



    if __name__ == "__main__":
        main()
