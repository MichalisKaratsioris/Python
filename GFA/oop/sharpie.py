class Sharpie:

    def __init__(self, color:str, width:int, inkAmount=100):
        self.width = width
        self.color = color
        self.inkAmount = inkAmount

    def use(self):
        self.inkAmount -= 10


s = Sharpie("black", 10)
print(s.inkAmount)
print(s.width)
print(s.color)
s.use()
print(s.inkAmount)
print(s.width)
print(s.color)