f = open("input.txt", "r")
lines = f.readlines()

def get_result(player1, player2):
    diff=(player2-player1)%3
    if diff==0:
        return 3
    elif diff==1:
        return 6
    elif diff==2:
        return 0

def get_value(letter):
    if letter=="A" or letter=="X":
        return 0
    elif letter=="B" or letter=="Y":
        return 1
    elif letter=="C" or letter=="Z":
        return 2
        
def translate(letter):
    if letter=="A" or letter=="X" or letter==0:
        return "Rock"
    elif letter=="B" or letter=="Y" or letter==1:
        return "Paper"
    elif letter=="C" or letter=="Z" or letter==2:
        return "Scissors"

def get_my_move(rival, result):
    if result=="X":
        return (rival-1)%3
    elif result=="Y":
        return rival
    elif result=="Z":
        return (rival+1)%3

score=0
for line in lines:
    round = line.strip("\n").split(" ")
    print(round)
    his_move=get_value(round[0])
    print(his_move)
    my_move=get_my_move(get_value(round[0]),round[1])
    print(my_move)
    print(f"{translate(his_move)} vs {translate(my_move)}")
    # print(f"Score: {get_value(my_move)+1} + {get_result(get_value(his_move),get_value(my_move))}")
    score+=(my_move)+1
    score+=get_result(his_move,my_move)

print(score)
