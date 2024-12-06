class Frame:
    pass

named_frames = dict()

class Point:
    def __init__(self, coords, frame):
        self.coords = coords
        self.frame = frame

    def to(self, newframe):
        return Point(self.coords, newframe)


class Directional:
    def __init__(self, coords, frame):
        self.coords = coords
        self.frame = frame

    def to(self, newframe):
        return Point(self.coords, newframe)
