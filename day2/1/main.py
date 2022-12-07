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
    if letter=="A" or letter=="X":
        return "Rock"
    elif letter=="B" or letter=="Y":
        return "Paper"
    elif letter=="C" or letter=="Z":
        return "Scissors"

score=0
for line in lines:
    moves = line.strip("\n").split(" ")
    print(moves)
    print(f"{translate(moves[0])} vs {translate(moves[1])}")
    print(f"Score: {get_value(moves[1])+1} + {get_result(get_value(moves[0]),get_value(moves[1]))}")
    score+=get_value(moves[1])+1
    score+=get_result(get_value(moves[0]),get_value(moves[1]))

print(score)
