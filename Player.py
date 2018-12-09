class Player(playerName, lat, long , isHunter):
    
    def __init__(self, playerName, lat, long, isHunter):
        name = playerName
        currentLat = lat
        currentLong = long
        self.isHunter = isHunter
        win = false
        if(isHunter):
            player = Hunter
        else:
            player = Prey
        notfications = Notifications

    def setWin(self):
        win = true

    def hasMoved(self): #if the player has moved, return true.
        return GPS.haveIMoved(self.name)


    def setHunter(): #switch from prey to hunter when caught
        if(isHunter==false):
            isHunter = true

    def isPreyNearby(self):
        return GPS.preyInRange(self.name)



        



    
        







