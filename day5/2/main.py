f = open("input_test.txt", "r")
lines = f.read().splitlines()

def get_stacks(lines):
    i=0
    stacks=[]
    for line in lines:
        if line.startswith(" 1"):
            stacks_brutes=line.strip("\n").split(" ")
            for stack in stacks_brutes:   
                if stack!="":
                    stacks.append([])
            break
        i+=1  
    print(stacks)
    while(i>0):
        line=lines[i-1].strip("\n")
        j=0
        for stack in stacks:
            item=(line[j*4+1])
            if item!=' ':
                stacks[j].append(item)
            j+=1
        i-=1    
            
            
    return stacks,i

def make_move():
    pass

stacks,i=get_stacks(lines)

for line in lines:
    if line.startswith("move"):
        action=line.strip("\n").split(" ")
        temp=[]
        for i in range(int(action[1])):
            item=stacks[int(action[3])-1].pop()
            temp.append(item)
        for i in range(len(temp)):
            item=temp.pop()
            stacks[int(action[5])-1].append(item)

print(stacks)

output=""
for stack in stacks:
    output+=stack[len(stack)-1]
print(output)