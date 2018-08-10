# Libraries Included:
# Numpy, Scipy, Scikit, Pandas
from random import randint

## Classes

#room
class Location:
    #constructor
    def __init__(self,x,y):
        self.x = x
        self.y = y 

        
# this can be used for boss and human        
class Player:
    def __init__(self,currentRoom,str):
        self.currentRoom = Location()
        self.str = "hi"


## Functions
#create map array and return it
def create_map():
    # generate a 3x3 map
    map = []
    for x in range(3):
        for y in range(3):
            newRoom = Location(x,y)
            map.append(newRoom)
    return map

#TODO: Pass in a map object/array and check inside of that
def spawn():
        spawnX = randint(0,9)
        spawnY = randint(0,9)
        spawnLocation = Location(spawnX, spawnY)
        return spawnLocation
            
        
def move(direction, cur, map):
    # w = up, d = right, s = down, a = left    
    goodRoom = False
    while(not goodRoom):
        newCur = cur
        if direction == 'w':
            newCur.y += 1
        elif direction == 'd':
            newCur.x += 1
        elif direction == 's':
            newCur.y += -1
        elif direction == 'a':
            newCur.x += -1

        if cur in map:
            goodRoom = True
        else:
            newCur = cur
            
    return newCur
        
## End Functions       

# main function
def game():
    map = create_map()    
    for room in map :
        print("(" + str(room.x) + "," + str(room.y) + ")") 
    
    #create player
    playerSpawnRoom = spawn()
    print("Spawned in room: " + str(playerSpawnRoom.x) + str(playerSpawnRoom.y))
    player = Player(playerSpawnRoom,"sup")
    
    newLoc = move('w', player.currentLocation, map)
    print("Player moved to: " + str(newLoc.x) + str(newLoc.y))
    
    
    
game()    
 
