def get_distance(tree, neighbours):
    distance=0
    for neighbour in neighbours:
        distance+=1
        if neighbour>=tree:
            break
    return distance

def print_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])
f = open("input.txt", "r")
lines = f.read().splitlines()

map_trees = [[0 for _ in range(len(lines[0]))] for _ in range(len(lines))]
for i in range(len(lines)):
    for j in range(len(lines[0])):
        map_trees[i][j]=int(lines[i][j])

result=0
for i in range(len(map_trees)):
    for j in range(len(map_trees[0])):
        tree=map_trees[i][j]
        negat_x=reversed([map_trees[i][k] for k in range(0,j)])
        posit_x=[map_trees[i][k] for k in range(j+1,len(map_trees))]
        negat_y=reversed([map_trees[k][j] for k in range(0,i)])
        posit_y=[map_trees[k][j] for k in range(i+1,len(map_trees[0]))]
        distance = get_distance(tree,negat_x) * get_distance(tree,posit_x) * get_distance(tree,negat_y) * get_distance(tree,posit_y)
        if distance>result:
            result=distance  
        
print(f"Scenic score: {result}")