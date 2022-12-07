f = open("input.txt", "r")
lines = f.read().splitlines()

reindeers=[]
calories=0
for line in lines:
    if line=="":
        reindeers.append(calories)
        calories=0
    else:
        calories+=int(line)

print(max(reindeers))
