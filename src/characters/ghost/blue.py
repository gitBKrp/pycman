from src.movable import Movable


class GhostBlue(Movable):
    def __init__(self):
        Movable.__init__(self, 1, 1)
        pass

    def step(self):
        pass