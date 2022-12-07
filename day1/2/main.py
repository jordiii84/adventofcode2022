f = open("input.txt", "r")
lines = f.readlines()

reindeers=[]
calories=0
for line in lines:
    if line[:-1]=="":
        reindeers.append(calories)
        calories=0
    else:
        calories+=int(line[:-1])

total_calories=max(reindeers)
reindeers.remove(max(reindeers))
total_calories+=max(reindeers)
reindeers.remove(max(reindeers))
total_calories+=max(reindeers)
print(total_calories)
