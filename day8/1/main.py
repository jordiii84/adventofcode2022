def is_visible(tree, neighbours):
    for neighbour in neighbours:
        if neighbour>=tree:
            return False
    return True

def print_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

f = open("input.txt", "r")
lines = f.read().splitlines()

map_trees = [[0 for _ in range(len(lines[0]))] for _ in range(len(lines))]
for i in range(len(lines)):
    for j in range(len(lines[0])):
        map_trees[i][j]=int(lines[i][j])

print_matrix(map_trees)

visible=0
for i in range(len(map_trees)):
    for j in range(len(map_trees[0])):
        print(f" [{i}] [{j}] {map_trees[i][j]}")
        tree=map_trees[i][j]
        negat_x=[map_trees[i][k] for k in range(0,j)]
        posit_x=[map_trees[i][k] for k in range(j+1,len(map_trees))]
        negat_y=[map_trees[k][j] for k in range(0,i)]
        posit_y=[map_trees[k][j] for k in range(i+1,len(map_trees[0]))]
        if is_visible(tree,negat_x) or is_visible(tree,posit_x) or is_visible(tree,negat_y) or is_visible(tree,posit_y):
            visible+=1
        

print(f"Total of {visible} visible trees")