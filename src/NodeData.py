class Node:
    def __init__(self, id, pos: tuple = (), tag=-1, info="", weight=0):
        self.id = id
        self.pos = pos
        self.tag = tag
        self.info = info
        self.weight = weight
        self.inEdges = {}
        self.outEdges = {}

    def __lt__(self, compare_node):
        return self.weight < compare_node.weight

    def __str__(self):
        return f"{self.id},{self.pos},{self.tag},{self.info}"

    def __repr__(self):
        return f"{self.id},{self.pos},{self.tag},{self.info}"