def calculate_result(register, cycles, line_screen):
    if cycles%40 in range((register-1),(register+2)):
        line_screen+="#"
    else:
        line_screen+=" "
    return line_screen

def print_screen(screen):
    for line_screen in screen:
        line_str=""
        for pixel in line_screen:
            line_str+=pixel
        print(f"{line_str} ----- {len(line_str)}")

f = open("input.txt", "r")
lines = f.read().splitlines()

cycles=0
register=1
screen=[]
line_screen=""
for line in lines:
    command=line.split(" ")[0]
    if command=="noop":
        line_screen=calculate_result(register,cycles,line_screen)
        cycles+=1
        if len(line_screen)==40:
            screen.append(line_screen)
            line_screen=""
    else:
        value_command=int(line.split(" ")[1])
        for i in range(2):
            line_screen=calculate_result(register,cycles,line_screen)
            cycles+=1        
            if len(line_screen)==40:
                screen.append(line_screen)
                line_screen=""
        register+=value_command
result=0

print_screen(screen)