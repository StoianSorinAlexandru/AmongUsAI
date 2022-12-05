class Character:
    def __init__(self, color, position, lastPosition, statement, isImposter, alive, index):
        self.color = color
        self.alive = alive
        self.position = position
        self.statement = statement
        self.lastPosition = lastPosition
        self.isImpostor = isImposter
        self.index = index

    def setLastStatement(self, statement):
        self.lastPosition = statement

    def setStatement(self, statement):
        self.statement = statement

    def setAlive(self, alive):
        self.alive = alive

    def setPositon(self, position):
        self.position = position

    def tostring(self):
        return "Index: %s, Color: %s, Position: %s, Statement: %s, LastPosition: %s, IsASussyBakka: %s, IsAlive: %s" % (self.index, self.color, self.position, self.statement, self.lastPosition, self.isImpostor, self.alive)