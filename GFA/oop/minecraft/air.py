from block import Block


class Air(Block):

    def __init__(self):
        self.type = "air"
        self.color = "transparent"
        self.lightTransmission = 100
        self.canBeCrossed = True
        self.blocksPermitted = ["mud", "brick", "glass", "door", "window", "gold"]

