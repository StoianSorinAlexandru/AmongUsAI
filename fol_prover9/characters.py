class Character:
    def __init__(self, color, position, statement, isImposter):
        self.color = color
        self.alive = True
        self.position = position
        self.statement = statement
        self.isImposter = isImposter

    def tostring(self):
        return "Color: %s, Position: %s, Statement: %s, IsASussyBakka: %s" % (self.color, self.position, self.statement, self.isImposter)