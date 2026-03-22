class Remote():
    def isLeftPressed(self):
        return True

class Player:
    def moveRight(self):
        print("Move Right")

    def moveLeft(self):
        print("Move Left")

    def moveUp(self):
        print("Move Up")

    def moveDown(self):
        print("Move Down")

Remote1 = Remote()
Player1 = Player()

if Remote1.isLeftPressed():
    Player1.moveLeft()
