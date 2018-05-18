from Arena import Arena
from Stack import Stack
from Tile import Tile
from Wall import Wall
import random

# set gameover to False
gameover = False

# create initial Arena
arena1 = Arena(15)

# populate the Arena's tile dictionary with Tile objects
for i in range(arena1.numtiles):
    arena1.tiles[i] = Tile(i)

# populate the Arena's wall dictionary with Wall objects
for w in range(arena1.numwalls):
    arena1.walls[w] = Wall(w)

# populate the Arena's stack dictionary with Stack objects
for k in range(arena1.numstacks):
    randsize = random.randint(10, 20)
    arena1.stacks[k] = Stack(k, randsize)

# get list of unique tile positions for stacks
alltiles = [x for x in arena1.tiles]
alltiles.remove(112)
stackpositions = random.sample(alltiles, arena1.numstacks)

# remove stack positions from alltiles
for stacktile in stackpositions:
    alltiles.remove(stacktile)

# get list of unique tile positions for walls from filtered alltiles
wallpositions = []
choice = 0
for z in range(arena1.numwalls):
    choice = random.choice(alltiles)
    wallpositions.append(choice)

# assign a tile position to each stack in the Arena
for l in range(arena1.numstacks):
    arena1.stacks[l].tileposition = stackpositions.pop()

# assign a tile position to each wall in the Arena
for y in range(arena1.numwalls):
    arena1.walls[y].tileposition = wallpositions.pop()

# toggle hasStack for each tile that has a stack
for n in range(arena1.numstacks):
    arena1.tiles[arena1.stacks[n].tileposition].hasStack = True

# toggle hasWall for each tile that has a wall
for u in range(arena1.numwalls):
    arena1.tiles[arena1.walls[u].tileposition].isWall = True

# toggle hasPlayer for the center tile
arena1.tiles[112].hasPlayer = True


# a function that tests whether a tile contains a stack, player, or wall
def testforstack(tile):
    if tile.hasPlayer and tile.hasStack:
        return "!"
    elif tile.isWall:
        return "x"
    elif tile.hasStack:
        return "m"
    elif tile.hasPlayer:
        return "!"
    else: return "o"


# a function that prints the Arena
def printboard():
    # build a long list of tested tiles
    testedlist = [testforstack(tile) for id, tile in arena1.tiles.items()]

    # divide the tested list into rows of 15
    rows = [testedlist[x:x+15] for x in range(0, len(testedlist), 15)]

    # print rows as a grid
    for row in rows:
        print(" ".join(row))


# a function that gets the tile number occupied by the player
def findplayer():
    playerlocation = 0
    for id, tile in arena1.tiles.items():
        if tile.hasPlayer:
            playerlocation = id
    return playerlocation


# main combat function
def docombat(stack):
    pogsflipped = 0
    win = False
    for g in range(stack.size):
        roll = random.randint(0, 1)
        if roll == 1:
            pogsflipped += 1
    if pogsflipped > (stack.size / 2):
        win = True
    return win


# main game loop
while not gameover:
    # print Arena
    print('hey')
    printboard()
    # check for stacks on initial center tile
    playerlocation = findplayer()
    if arena1.tiles[playerlocation].hasStack:
        print('Poggers!')
        for id, stack in arena1.stacks.items():
            if stack.tileposition == playerlocation:
                stacktofight = stack
        win = docombat(stacktofight)
        if win:
            print("You have slain the monster!")
        else: print ("Your attack was unsuccessful.")

    print("Monsters remaining: ", arena1.numstacks)
    # get player movement input
    playerinput = input("n,s,e,w to move")

    # North
    if playerinput.lower() == "n":
        playerlocation = findplayer()
        if (playerlocation > 14) and (arena1.tiles[playerlocation - 15].isWall == False):
            newplayerlocation = playerlocation - 15
        else: print("You hit a wall and fall over like a dummy, dummy!")
        arena1.tiles[playerlocation].hasPlayer = False
        arena1.tiles[newplayerlocation].hasPlayer = True
    # South
    elif playerinput.lower() == "s":
        playerlocation = findplayer()
        if (playerlocation < 210) and (arena1.tiles[playerlocation + 15].isWall == False):
            newplayerlocation = playerlocation +15
        else: print("You hit a wall and fall over like a dummy, dummy!")
        arena1.tiles[playerlocation].hasPlayer = False
        arena1.tiles[newplayerlocation].hasPlayer = True
    # East
    elif playerinput.lower() == "e":
        playerlocation = findplayer()
        if ((playerlocation + 1) % 15 == 0) or (arena1.tiles[playerlocation + 1].isWall == True):
            print("You hit a wall and fall over like a dummy, dummy!")
        else:
            newplayerlocation = playerlocation + 1
            arena1.tiles[playerlocation].hasPlayer = False
            arena1.tiles[newplayerlocation].hasPlayer = True
    # West
    elif playerinput.lower() == "w":
        playerlocation = findplayer()
        if (playerlocation % 15 == 0) or (arena1.tiles[playerlocation - 1].isWall == True):
            print("You hit a wall and fall over like a dummy, dummy!")
        else:
            newplayerlocation = playerlocation - 1
            arena1.tiles[playerlocation].hasPlayer = False
            arena1.tiles[newplayerlocation].hasPlayer = True
















