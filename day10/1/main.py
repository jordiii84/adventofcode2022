def calculate_result(values,positions):
    result=0
    for position in positions:
        result+=(values[position-1]*position)
   
    return result

f = open("input.txt", "r")
lines = f.read().splitlines()

values=[]
cycles=0
register=1
for line in lines:
    command=line.split(" ")[0]
    if command=="noop":
        cycles+=1
        values.append(register)
    else:
        value=int(line.split(" ")[1])
        for i in range(2):
            cycles+=1
            values.append(register)
        register+=value

result=0

result=calculate_result(values,(20,60,100,140,180,220))
print(result)