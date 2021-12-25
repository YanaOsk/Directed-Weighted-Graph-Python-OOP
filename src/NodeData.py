from filecmp import cmp



class Node:
    def __init__(self, node_id, pos: tuple = (), tag=-1, weight: int = 0):
        self.id = node_id
        self.pos = pos
        self.tag = tag
        self.weight = weight
        self.inEdges = {}
        self.outEdges = {}

    def getKey(self):
        return self.id
    def getLoc(self):
        return self.pos
    def getWeight(self):
        return self.weight
    def getTag(self):
        return self.tag

    def __lt__(self, compare_node):
        return self.weight < compare_node.weight


    def __str__(self):
        return f"{self.id},{self.pos},{self.tag}"

    def __repr__(self):
        return f"{self.id},{self.pos},{self.tag}"
