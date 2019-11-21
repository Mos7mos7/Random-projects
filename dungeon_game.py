import random
import os

CELLS=[(0,0),(1,0),(2,0),(3,0),(4,0),
       (0,1),(1,1),(2,1),(3,1),(4,1),
       (0,2),(1,2),(2,2),(3,2),(4,2),
       (0,3),(1,3),(2,3),(3,3),(4,3),
       (0,4),(1,4),(2,4),(3,4),(4,4)]

def clear_screen():
    os.system("cls" if os.name=='nt' else 'clear')
def get_locations():
    return random.sample(CELLS,3)

def move_player(player,move):
    x,y=player
    if move=="left":
        x-=1
    if move=="right":
        x+=1
    if move=="up":
        y-=1
    if move=="down":
        y+=1
    return x,y


def get_moves(player):
    moves=["left","right","up","down"]
    x,y=player
    if x==0:
        moves.remove("left")
    if x==4:
        moves.remove("right")
    if y==0:
        moves.remove("up")
    if y==4:
        moves.remove("down")
    return moves
def draw_map(player):
    print(" _"*5)
    tile="|{}"
    for cell in CELLS:
        x,y=cell
        if x<4:
            line_end=""
            if cell==player:
                output=tile.format("x")
            else:
                output=tile.format("_")
        else:
            line_end="\n"
            if cell == player:
                output=tile.format("x|")
            else:
                output=tile.format("_|")
        print(output,end=line_end)


monster, door , player=get_locations()
while True:
    draw_map(player)
    valid_moves=get_moves(player)
    print("welcome to dungeon")
    print(f"you are currently in room {player}")
    print(f"you can move {','.join(valid_moves)}")
    print("Enter Quit to exit game")

    move=input("> ")
    
    if move=="quit" or move=="QUIT":
        break
    if move in valid_moves:
        player= move_player(player,move) 
        if player == monster:
           print("you lose ")
           break
        if player == door: 
            print("you win ")
            break
        