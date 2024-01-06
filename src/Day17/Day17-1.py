from heapq import heappush, heappop

file_path = './src/Day17/Data17.txt'

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

print(matrix)

# Plan - use Dijkstra's Algorithm 
# Need:
# 1 - A priority queue 
# 2 - An account of the squares that has been visited
# Continuously search down the shortest path

visited = set() # mark squares that have been visited
pq = [(0, 0, 0, 0, 0, 0)] # priority queue (initialised with starting conditions) 

while pq: # loop whilst priority queue is not empty
    hl, r, c, dr, dc, n = heappop(pq) # remove the current paramters from the priority queue
    # heat loss, row, column, direction row, direction column, number of consecutive moves in same direction

    if r == len(matrix) - 1 and c == len(matrix[0]) - 1: # if at the goal, return heat loss
        print(hl)
        break

    if (r, c, dr, dc, n) in visited: # if the position from the same direction has already been visited, continue
        continue
    else:
        visited.add((r, c, dr, dc, n)) # else add to visited

    # going straight
    if n < 3 and (dr, dc) != (0, 0): # check that there is a direction and that the number of consecutive moves in the same direciton is less than 3
        # define next position
        nr = r + dr 
        nc = c + dc
        if 0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]): # check the next position is valid
            heappush(pq, (hl + matrix[nr][nc], nr, nc, dr, dc, n + 1)) # if so add to priority queue (add the heat loss to the value of the the next location in the data matrix)
    
    # turning
    for ndr, ndc in [(0, 1), (1, 0), (0, -1), (-1, 0)]: # calculate next possible direction
        if ((ndr, ndc) != (dr, dc)) and ((ndr, ndc) != (-dr, -dc)): # exclude going straight because this is checked above and exclude going back in the opposite direction
            nr = r + ndr
            nc = c + ndc
            if 0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]):
                heappush(pq, (hl + matrix[nr][nc], nr, nc, ndr, ndc, 1)) # add to priority queue (we have turned so n = 1)