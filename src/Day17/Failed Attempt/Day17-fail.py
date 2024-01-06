import copy
import numpy as np
import matplotlib.pyplot as plt

file_path = './src/Day17/Data17-test.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

data = file_content.split('\n')

# matrix = [list(map(int, line)) for line in data]

matrix = []

for array in data:
    line = []
    for i in range(len(data[0])):
        line.append(int(array[i]))
    matrix.append(line)

matrix[0][0] = 0
rows, cols = len(matrix), len(matrix[0])
memo = [[0] * cols for _ in range(rows)]

# Plan - use Dijkstra's Algorithm 
# Need:
# 1 - A stack containing possible routes and their values
# 2 - The current value / position 
# 3 - The original matrix 
# 4 - A length matrix - this will contain the shortest lengths to each position. This will be continually updated
# 5 - A backstep matrix - a list of all the steps taken 
# We continuously search down the shortest path
# If a shorter path is found to a node than that that already exists, replace the length (and the route to get there?)

# Steps:
# 1 - Create auxiliary arrays: lengths, backstep, visited (
# lengths = shortest found distance to that point, intialise with infinities
# backstep/path = which step we moved to from to get to a certain cell, 
# visited = has a cell been visited or not)
# 2 - end condition, run until at the bottom right corner
# 3 - in a while loop:
# check in each 4 directions: up, down, left and right 
# is the square within the boundaries of the grid 
# if so, it checks if the square has NOT been visited AND if the length of the next square is more than the sum of the cost of moving to the right and the current length 
# if the above condition is true: the length of the next square is updated to the sum of the cost of moving to the right and the current length 
# Also, the current square is added to the path
# we also add the current square to the visited array
# set values in the lengths/distances matrix to infinity where the corresponding position is true in the visited matrix
# find the point with the lowest length in the distance matrix

matrix2 = [
    [1, 1, 10, 7, 2],
    [3, 5, 3, 7 ,1],
    [1, 5, 1, 6, 1],
    [6, 5, 2, 6, 1],
    [6, 5, 2, 6, 1]
]

matrix3 = [
    [1, 1, 1, 2, 9],
    [7, 5, 1, 9, 9],
    [1, 1, 1, 9, 9],
    [1, 9, 9, 9, 9],
    [1, 1, 1, 1, 1]
]

# print(matrix)
# print(matrix2)

# ----------

map = matrix

map[0][0] = 0

distances = [[float('inf') for _ in range(len(map[0]))] for _ in range(len(map))]
distances[0][0] = 0
backstep = [[float('nan') for _ in range(len(map[0]))] for _ in range(len(map))]
direction = [[[float('nan'), float('nan')] for _ in range(len(map[0]))] for _ in range(len(map))]
visited = [[False for _ in range(len(map[0]))] for _ in range(len(map))]

print(distances)
print(backstep)
print(visited)

# Start at origin
# Mark current node as visited
# Find valid surrounding nodes
# Update distance values for these surrounding nodes
# Pick node with minimum distance and move to this node
# Repeat the previous 3 steps until at final position

# Run until at final position, because we are exploring the shortest path, we will be at the shortest path

start_position = [0, 0]
current_position = []
current_position = start_position
matrix_size = len(map)

def findSurroundingNodes(position):
    x,y = position[0], position[1]
    surrounding_nodes = [[x+1,y], [x, y+1], [x-1, y], [x, y-1]] # [right, down, left, up]
    if y == 0:
        surrounding_nodes.pop(3)
    if x == 0:
        surrounding_nodes.pop(2)
    if y == matrix_size-1:
        surrounding_nodes.pop(1)
    if x == matrix_size-1:
        surrounding_nodes.pop(0)
    return surrounding_nodes


def findShortestDistance():
    min_value = float('inf')  
    min_position = None 

    # Iterate through the matrix
    for j in range(len(distances)):
        for i in range(len(distances[0])):
            if (distances[i][j] < min_value) and (visited[i][j] != True):
                min_value = distances[i][j]
                min_position = [i, j]
                

    return min_position


def remove_value(matrix, target_value):
    return [elem for elem in matrix if elem != target_value]


# The end critierion for the recursion while loop is when the end goal is at the top of the priority queue or when the priority queue is empty

while current_position != [matrix_size - 1, matrix_size - 1]:
    print('------------')
    print('current position:', current_position)

    # Find valid surrounding nodes from current position
    surrounding_nodes = findSurroundingNodes(current_position)
  
    # print('backstep:', backstep)
    print('surrounding nodes:', surrounding_nodes)
    

    # Check that you're not going in the same direction for more than 3 consecutive steps
    if direction[current_position[0]][current_position[1]][1] == 3:
        print('DANGER')
        # find direction by looking and the previous positionfrom backstep and ensure it's not in surrounding nodes 
        previous_position = backstep[current_position[0]][current_position[1]]
        print(previous_position)
        if (previous_position[0] == current_position[0] + 1):
            print('up')
            surrounding_nodes = remove_value(surrounding_nodes, [current_position[0] - 1, current_position[1]])
        elif (previous_position[0] == current_position[0] - 1):
            print('down')
            surrounding_nodes = remove_value(surrounding_nodes, [current_position[0] + 1, current_position[1]])
        elif (previous_position[1] == current_position[1] + 1):
            print('left')
            surrounding_nodes = remove_value(surrounding_nodes, [current_position[0], current_position[1] - 1])
        elif (previous_position[1] == current_position[1] - 1):
            print('right')
            surrounding_nodes = remove_value(surrounding_nodes, [current_position[0], current_position[1] + 1])

    print('updated surrounding nodes:', surrounding_nodes)

    # update distance values for surrounding nodes
    for i in range(len(surrounding_nodes)):
        # distance to next node + distance it took to get to current node
        if visited[surrounding_nodes[i][0]][surrounding_nodes[i][1]] == True:
            distances[surrounding_nodes[i][0]][surrounding_nodes[i][1]] = float('inf')
        elif map[surrounding_nodes[i][0]][surrounding_nodes[i][1]] + distances[current_position[0]][current_position[1]] < distances[surrounding_nodes[i][0]][surrounding_nodes[i][1]]:
            distances[surrounding_nodes[i][0]][surrounding_nodes[i][1]] = map[surrounding_nodes[i][0]][surrounding_nodes[i][1]] + distances[current_position[0]][current_position[1]]
            backstep[surrounding_nodes[i][0]][surrounding_nodes[i][1]] = current_position
            if (surrounding_nodes[i][0] == current_position[0] + 1) and (direction[current_position[0]][current_position[1]][0] == 'D'):
                direction[surrounding_nodes[i][0]][surrounding_nodes[i][1]] = ['D', direction[current_position[0]][current_position[1]][1] + 1]
            elif (surrounding_nodes[i][0] == current_position[0] + 1) and not (direction[current_position[0]][current_position[1]][0] == 'D'):
                 direction[surrounding_nodes[i][0]][surrounding_nodes[i][1]] = ['D', 1]
            elif (surrounding_nodes[i][0] == current_position[0] + 1) and current_position == [0, 0]:
                direction[surrounding_nodes[i][0]][surrounding_nodes[i][1]] = ['D', 1]
            elif (surrounding_nodes[i][0] == current_position[0] - 1) and (direction[current_position[0]][current_position[1]][0] == 'U'):
                direction[surrounding_nodes[i][0]][surrounding_nodes[i][1]] = ['U', direction[current_position[0]][current_position[1]][1] + 1]
            elif (surrounding_nodes[i][0] == current_position[0] - 1) and not (direction[current_position[0]][current_position[1]][0] == 'U'):
                 direction[surrounding_nodes[i][0]][surrounding_nodes[i][1]] = ['U', 1]
            elif (surrounding_nodes[i][1] == current_position[1] - 1) and (direction[current_position[0]][current_position[1]][0] == 'L'):
                direction[surrounding_nodes[i][0]][surrounding_nodes[i][1]] = ['L', direction[current_position[0]][current_position[1]][1] + 1]
            elif (surrounding_nodes[i][1] == current_position[1] - 1) and not (direction[current_position[0]][current_position[1]][0] == 'L'):
                 direction[surrounding_nodes[i][0]][surrounding_nodes[i][1]] = ['L', 1]
            elif (surrounding_nodes[i][1] == current_position[1] + 1) and (direction[current_position[0]][current_position[1]][0] == 'R'):
                direction[surrounding_nodes[i][0]][surrounding_nodes[i][1]] = ['R', direction[current_position[0]][current_position[1]][1] + 1]
            elif (surrounding_nodes[i][1] == current_position[1] + 1) and not (direction[current_position[0]][current_position[1]][0] == 'R'):
                 direction[surrounding_nodes[i][0]][surrounding_nodes[i][1]] = ['R', 1]
            elif (surrounding_nodes[i][1] == current_position[1] + 1) and current_position == [0, 0]:
                direction[surrounding_nodes[i][0]][surrounding_nodes[i][1]] = ['R', 1]
        # print('distances of surrounnding nodes:', distances[surrounding_nodes[i][0]][surrounding_nodes[i][1]])

    # print('updated distances:', distances)
    # print('updated directions:', direction)

    # mark current position as visited
    visited[current_position[0]][current_position[1]] = True
    # print('updated visited:', visited)

    # pick node with minimum distance that has not been visited and make this the current position
    print(f'distance at {findShortestDistance()} = {distances[findShortestDistance()[0]][findShortestDistance()[1]]}')
    position_of_shortest_distance = findShortestDistance()
    current_position = [position_of_shortest_distance[0], position_of_shortest_distance[1]]

# print(backstep)
# print(direction)

# Find shortest route from backstep
traceback_position = [matrix_size - 1, matrix_size - 1]
shortest_route =[]
visualisation = [[0] * (matrix_size) for _ in range(matrix_size)]
while traceback_position != [0,0]:
    visualisation[traceback_position[0]][traceback_position[1]] = '*'
    shortest_route.append(traceback_position)
    traceback_position = backstep[traceback_position[0]][traceback_position[1]]

# print(shortest_route)

stringData = '\n'.join([''.join([str(x) for x in row]) for row in visualisation])
print(stringData)

# with open('./src/Day17/data_visualised.txt', 'w', encoding='utf-8') as file:
#     file.write(stringData)
