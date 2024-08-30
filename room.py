class Room:

    #name is a str; items is a dict with str keys and str values; neighbors is a list containing room objects
    #description is a str
    def __init__(self, name, items, neighbors, description):
        self.name = name
        self.items = items
        self.neighbors = neighbors
        self.description = description


