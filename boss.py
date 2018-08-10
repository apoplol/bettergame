from random import randint

class Location:

    def __init__(self, x, y):
        self.x = 0
        self.y = 0

    #def show_all(self):
    #    print(self.X, self.Y)

def spawn(gameMap):
  #pass an array of rooms (gameMap)
  numOfRooms = len(gameMap)
  spawnRoomIndex = randint(0, numOfRooms)
  
  #grab Location object at gameMap index
  spawnRoomObj = gameMap[spawnRoomIndex]  
  
  #might not need these if returning Location object
  roomX = spawnRoomObj.x
  roomY = spawnRoomObj.y

  return spawnRoomObj

#maybe make gameMap into an object containing array and sizes
def move(gameMap, currentPos, maxX, maxY):
  curX = currentPos.x
  curY = currentPos.y
  newPos = Location(curX, curX)
  foundRoom = False

  while not foundRoom:
    direction = randint(0,3)
    #check bounds
    if (direction == 0 and curY == 0) or (direction == 1 and curX == maxX) or (direction == 2 and curY == 0) or (direction == 3 and curX == 0):
      #skip loop iteration, do not increment count
      continue
    
    else:
      if direction == 0:
        curY += 1
      elif direction == 1:
        curX += 1
      elif direction == 2:
        curY -= 1
      elif direction == 3:
        curX -= 1     

      #create a new room with the attempted move, and see if it exists in our map
      newPos = Location(curX, curY)          
      if(any(newPos.x == curX for x in gameMap) and any(newPos.y == curX for x in gameMap)):
        foundRoom = True
  return newPos
  


