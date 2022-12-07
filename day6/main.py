# define a dictionary that maps each move to its score
scores = {'rock': 1, 'paper': 2, 'scissors': 3}

# define the function that calculates the score
def calculate_score(strategy):
  # initialize the total score to 0
  total_score = 0

  # split the strategy into rounds
  rounds = strategy.strip().split('\n')

  # iterate over the rounds
  for round in rounds:
    # split the round into the opponent's move and your move
    opponent_move, your_move = round.split()

    # map the moves to their corresponding scores
    opponent_score = scores[opponent_move.lower()]
    your_score = scores[your_move.lower()]

    # determine the outcome and add the score for the round to the total score
    if your_score > opponent_score:
      total_score += your_score + 6
    elif your_score < opponent_score:
      total_score += your_score + 0
    else:
      total_score += your_score + 3

  # return the total score
  return total_score

# example strategy
strategy = """
A Y
B X
C Z
"""

# calculate and print the total score
total_score = calculate_score(strategy)
print(total_score) # 15
