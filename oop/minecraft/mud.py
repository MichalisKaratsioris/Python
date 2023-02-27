from block import Block


class Mud(Block):

    def __init__(self):
        self.type = "mud"
        self.color = "dark grey"
        self.lightTransmission = 0
        self.canBeCrossed = False
        self.blocksPermitted = ["brick", "air", "lava", "door", "window", "gold"]

