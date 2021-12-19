class Node:
    def __init__(self, id, pos, tag=-1, info=""):
        self.id = id
        self.pos = pos
        self.tag = tag
        self.info = info

    def __str__(self):
        return f"{self.id},{self.pos},{self.tag},{self.info}"

    def __repr__(self):
        return f"{self.id},{self.pos},{self.tag},{self.info}"