class Arena:
    def __init__(self, size):
        self.size = size
        self.numtiles = size * size
        self.numstacks = int(self.numtiles * .1)
        self.numwalls = int(self.numtiles * .08)
        self.tiles = {}
        self.stacks = {}
        self.walls = {}