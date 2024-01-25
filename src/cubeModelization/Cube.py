from src.cubeModelization.Face import Face


class Cube:

    def __init__(self):
        """
        Constructor
        """
        self.faces = [Face([["GREEN", "GREEN", "GREEN"], ["GREEN", "GREEN", "GREEN"], ["GREEN", "GREEN", "GREEN"]]),
                      Face([["BLUE", "BLUE", "BLUE"], ["BLUE", "BLUE", "BLUE"], ["BLUE", "BLUE", "BLUE"]]),
                      Face([["RED", "RED", "RED"], ["RED", "RED", "RED"], ["RED", "RED", "RED"]]),
                      Face([["ORANGE", "ORANGE", "ORANGE"], ["ORANGE", "ORANGE", "ORANGE"],
                            ["ORANGE", "ORANGE", "ORANGE"]]),
                      Face([["YELLOW", "YELLOW", "YELLOW"], ["YELLOW", "YELLOW", "YELLOW"],
                            ["YELLOW", "YELLOW", "YELLOW"]]),
                      Face([["WHITE", "WHITE", "WHITE"], ["WHITE", "WHITE", "WHITE"], ["WHITE", "WHITE", "WHITE"]])]
        self.faces[0].setNeighbors([self.faces[2], self.faces[4], self.faces[3], self.faces[5]])

        self.faces[1].setNeighbors([self.faces[2], self.faces[5], self.faces[3], self.faces[4]])

        self.faces[2].setNeighbors([self.faces[0], self.faces[4], self.faces[1], self.faces[5]])

        self.faces[3].setNeighbors([self.faces[0], self.faces[5], self.faces[1], self.faces[4]])

        self.faces[4].setNeighbors([self.faces[0], self.faces[2], self.faces[1], self.faces[3]])

        self.faces[5].setNeighbors([self.faces[0], self.faces[3], self.faces[1], self.faces[2]])

    def getFaces(self):
        return self.faces

    def setFaces(self, faces):
        self.faces = faces

    def getFace(self, index):
        return self.faces[index]

    def setFace(self, index, face):
        self.faces[index] = face

    def getFaceByColor(self, color):
        for face in self.faces:
            if face.getColor() == color:
                return face
        return None

    # comment what this function do below
    def getFaceByIndex(self, index):
        return self.faces[index]

    def getFaceIndex(self, face):
        for i in range(6):
            if self.faces[i] == face:
                return i
        return -1

    def getFaceByNeighbor(self, neighbor):
        for face in self.faces:
            if neighbor in face.getNeighbors():
                return face
        return None

    def getFaceByNeighbors(self, neighbors):
        for face in self.faces:
            if face.getNeighbors() == neighbors:
                return face
        return None

    def getFaceByColors(self, colors):
        for face in self.faces:
            if face.getColors() == colors:
                return face
        return None
