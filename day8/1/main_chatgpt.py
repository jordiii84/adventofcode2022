f = open("input.txt", "r")
rows = f.read().splitlines()

# Create an empty grid
grid = []

# Loop through each row and convert it to a list of integers
for row in rows:
  grid.append([int(ch) for ch in row])

# Initialize a counter variable to keep track of the number of visible trees
visible_tree_count = 0

# Loop through each tree in the grid
for y in range(len(grid)):
  for x in range(len(grid[y])):
    tree_height = grid[y][x]

    # Check if the tree is taller than all of the other trees in the same row and column
    is_visible = True
    for i in range(len(grid)):
      if grid[i][x] > tree_height:
        is_visible = False
        break

    for i in range(len(grid[y])):
      if grid[y][i] > tree_height:
        is_visible = False
        break

    # If the tree is visible, increment the counter
    if is_visible:
      visible_tree_count += 1

# Return the number of visible trees
print(visible_tree_count)
