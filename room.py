Class Room:

    def __init__(self, name: str, items: dict[str, str], neighbors: List[Room], description: str):
        self.name = name
        self.item = items
        self.neighbors = neighbors
        self.description = description


