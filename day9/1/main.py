def make_move_head(start,direction):
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

f = open("input_test.txt", "r")
lines = f.read().splitlines()

visited=set()
head_position=(0,0)
tail_position=(0,0)
visited.add(tail_position)
for line in lines:
    direction=line.split(" ")[0]
    moves=int(line.split(" ")[1])
    for i in range(moves):
        head_position=make_move_head(head_position,direction)
        tail_position=make_move_tail(tail_position,head_position,direction)
        visited.add(tail_position)
        print(f"H:{head_position} - T {tail_position}")

print(f"Total of {len(visited)} points visited")
# print(visited)