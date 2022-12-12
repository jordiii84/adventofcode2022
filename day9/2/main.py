def get_direction(point1,point2,direction):
    if abs(point1[0]-point2[0])>1 or abs(point1[1]-point2[1])>1:
        distant_axis="X" if abs(point1[0]-point2[0])>abs(point1[1]-point2[1]) else "Y"
        if distant_axis=="X":
            direction="R" if point2[0]>point1[0] else "L"
        else:
            direction="U" if point2[1]>point1[1] else "D"
    return direction
           
def make_move_head(start,direction):
    if direction==None:
        return start
    if direction=="U":
        new_position=(start[0],start[1]+1)
    elif direction=="D":
        new_position=(start[0],start[1]-1)
    elif direction=="R":
        new_position=(start[0]+1,start[1])
    elif direction=="L":
        new_position=(start[0]-1,start[1])
    return new_position

def make_move_tail(tail,head,direction):
    if abs(tail[0]-head[0])<=1 and abs(tail[1]-head[1])<=1:
        return tail
    elif abs(tail[0]-head[0])>1 and abs(tail[1]-head[1])>1:
        x=int((head[0]+tail[0])/2)
        y=int((head[1]+tail[1])/2)
        new_position=(x,y)
        return(new_position)
    else: 
        if direction=="U":
            new_position=(head[0],head[1]-1)
        elif direction=="D":
            new_position=(head[0],head[1]+1)
        elif direction=="R":
            new_position=(head[0]-1,head[1])
        elif direction=="L":
            new_position=(head[0]+1,head[1])
        return new_position

f = open("input.txt", "r")
lines = f.read().splitlines()

visited=set()
positions={0:(0,0),1:(0,0),2:(0,0),3:(0,0),4:(0,0),5:(0,0),6:(0,0),7:(0,0),8:(0,0),9:(0,0)}
visited.add(positions[9])
for line in lines:
    direction_or=line.split(" ")[0]
    moves=int(line.split(" ")[1])
    for i in range(moves):
        direction=direction_or
        positions[0]=make_move_head(positions[0],direction)
        for i in range(1,10):
            direction=get_direction(positions[i],positions[i-1],direction_or)
            positions[i]=make_move_tail(positions[i],positions[i-1],direction)
        visited.add(positions[9])
print(f"Total of {len(visited)} points visited")