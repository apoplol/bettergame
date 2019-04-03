# Libraries Included:
# Numpy, Scipy, Scikit, Pandas
from random import randint
import time
import os
import sys
import platform

# GLOBALS
xbound = 0
ybound = 0

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
        self.currentRoom = currentRoom
        self.str = "hi"


##GLOBAL HELPER FUNCTIONS

# for ucuntu
def clear():
    if platform.system() == "Linux":
        absolutely_unused_variable = os.system("clear")
    elif platform.system() == "Windows":
        absolutely_unused_variable = os.system("cls")


## Functions
#create map array and return it
def create_map(xbound,ybound):
    # generate a 3x3 map
    map = []
    for y in range(ybound):
        for x in range(xbound):
            newRoom = Location(x,y)
            map.append(newRoom)
    return map

def draw_map(map, playerLocation):
    #TODO: pass the map through to be able to draw it (assuming it will be more complex than a square)
    printStr = ""
    numsPerRow = xbound
    numsInRow = 1

    for i in range(0,len(map)):
        item = "Z"
        if map[i].x == playerLocation.x and map[i].y == playerLocation.y:
            item = "X"
        else:
            item = "O"

        if numsInRow % numsPerRow == 0:
            printStr += "{0}\n".format(item)
            numsInRow = 1
        else:
            printStr += "{0}\t".format(item)
            numsInRow += 1
    print(printStr)



def show_manual():
    print("read the fucking manual")
    print("_______________________")
    print("movement:")
    print("  w: up")
    print("  s: down")
    print("  a: left")
    print("  d: right")
    print("man: show manual")
    print("map: show map")    
    print("q: quit")
    #TODO: "inventory system"

#TODO: Pass in a map object/array and check inside of that
def spawn():
        spawnX = randint(0,xbound)
        spawnY = randint(0,ybound)
        spawnLocation = Location(spawnX, spawnY)
        return spawnLocation
            
        
def move(direction, cur):
    # w = up, d = right, s = down, a = left    
    #print("xbound: " + str(xbound))
    #print("ybound: " +str(ybound))    
    newCur = cur
    if direction in "wasd":
        if direction == 'w' and cur.y > 0:
            newCur.y -= 1
        elif direction == 's' and cur.y < ybound:
            newCur.y += 1
        elif direction == 'a' and cur.x > 0:
            newCur.x -= 1
        elif direction == 'd' and cur.x < xbound:
            newCur.x += 1
        else:
            print("hit the edge of the map")                    
    return newCur

        
def intro():
    loading = "LOADING"
    randint(0,80)
    for i in range(0,8):
        x = randint(1,30)
        print('~' * x + loading[0:i])
        time.sleep(0.1)
    absolutely_unused_variable = os.system("cls")
    print("~"*33 + "WELCOME TO HELL" + "~"*32)


def power_off():
    dot = "."
    for i in range(0,5):
        absolutely_unused_variable = os.system("cls")
        print("Powering off" + dot * i)    
        time.sleep(0.5)

    print("peace")
    sys.exit()


## End Functions       

# main function
def game():
    global xbound;
    global ybound;    
    xbound = int(input("set map SIZE:  "))
    ybound = xbound

    peter = ["up","down","left","right","forward","backward","backwards","jump"]

    #intro
    intro()

    map = create_map(xbound,ybound)

    print("MAP SIZE: " + str(xbound) + " by " + str(ybound))
    #for room in map :
        #print("(" + str(room.x) + "," + str(room.y) + ")") 
    
    #create player
    playerSpawnRoom = spawn()
    print("Spawned in room: " + str(playerSpawnRoom.x) + str(playerSpawnRoom.y))
    player = Player(playerSpawnRoom,"sup")
        
    play = True;

    while play:
        print("~" * 80)
        choice = input("WHICH WAY (wasd): ")
        if choice == "man":
            show_manual()
        elif choice in peter:
            print("peter")
        elif choice == ("q"):
            power_off()
        elif choice == "map":
            draw_map(map, player.currentRoom)
        else:
            newLoc = move(choice, player.currentRoom)
            print("Player at: " + str(player.currentRoom.x)+str(player.currentRoom.y))

    
    
game()    
 
