class Face:
    # colors = [["WHITE", "WHITE", "WHITE"], ["WHITE", "WHITE", "WHITE"], ["WHITE", "WHITE", "WHITE"]]
    colors = [[], [], []]
    # neighbors = [Face, Face, Face, Face] = [top, right, bottom, left]
    neighbors = []

    def __init__(self, colors):
        """
        Constructor
        :param colors:
        a 3x3 matrix of colors
        """
        self.colors = colors

    def getColors(self):
        return self.colors

    def setColors(self, colors):
        self.colors = colors

    def __str__(self):
        return str(self.colors)

    def getColor(self, x, y):
        return self.colors[x][y]

    def setColor(self, x, y, color):
        self.colors[x][y] = color

    def getFaceColor(self):
        return self.colors[1][1]

    def getNeighbors(self):
        return self.neighbors

    def setNeighbors(self, neighbors):
        self.neighbors = neighbors

    def getNeighbor(self, index):
        return self.neighbors[index]

    def getNeighborIndex(self, neighbor):
        for i in range(4):
            if self.neighbors[i] == neighbor:
                return i
        return -1
