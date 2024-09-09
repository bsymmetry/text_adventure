class Room:

    #name is a str; items is a list of Item objects; neighbors is a list of room objects
    #description is a str
    def __init__(self, name, items, neighbors, description):
        self.name = name
        self.items = items
        self.neighbors = neighbors
        self.description = description


