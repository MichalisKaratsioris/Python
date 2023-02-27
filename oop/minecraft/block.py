from mud import Mud
from air import Air

class Block:

    def __init__ (self, type:str):
        match type:
            case "mud": self.Mud()
            case "air": self.Air()

air_b = Block("air")
air_b.color