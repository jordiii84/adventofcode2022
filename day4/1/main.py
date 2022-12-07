f = open("input.txt", "r")
lines = f.readlines()

def get_limits(pair):
    digits=pair.split("-")
    return(int(digits[0]),int(digits[1]))

contained=0
for line in lines:
    assigned = line.strip("\n").split(",")
    elv1=get_limits(assigned[0])
    elv2=get_limits(assigned[1])
    if elv1[0]<=elv2[0] and elv1[1]>=elv2[1]:
        contained+=1
        print(f"{assigned} Si"  )
    elif elv2[0]<=elv1[0] and elv2[1]>=elv1[1]:
        contained+=1
        print(f"{assigned} Si"  )
    else:
        print(f"{assigned} No"  )

print(contained)   
