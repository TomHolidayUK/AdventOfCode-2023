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

matrix2 = [
    [1, 3, 10, 2],
    [2, 5, 1, 1],
    [6, 5, 2, 1],
    [6, 5, 2, 1]
]


fig, ax = plt.subplots(figsize=(10,10))
min_val, max_val = 0, 5
maxnum=20
map = np.random.randint(1, maxnum, size=(max_val, max_val))
map[0,0]=0
map[max_val-1,max_val-1]=0
print(map)

current_cmap = plt.cm.Blues
current_cmap.set_bad(color='red')
# ax.matshow(map, cmap=plt.cm.Blues, vmin=0, vmax=maxnum*2)
ax.matshow(map, cmap=plt.cm.Blues, vmin=0, vmax=np.max(map) * 2)
# plt.show()

print(map)
print(matrix2)
# stringData2 = '\n'.join([''.join(str(x)) for x in map])
# print(stringData2)

#Initialize auxiliary arrays
distmap=np.ones((max_val,max_val),dtype=int)*np.Infinity
distmap[0,0]=0
# print(distmap)
originmap=np.ones((max_val,max_val),dtype=int)*np.nan
# print(originmap)
visited=np.zeros((max_val,max_val),dtype=bool)
# print(visited)
finished = False
x,y=int(0),int(0)
count=0

#Loop Dijkstra until reaching the target cell
while not finished:
  # move to x+1,y
  if x < max_val-1:
    if distmap[x+1,y]>map[x+1,y]+distmap[x,y] and not visited[x+1,y]:
      distmap[x+1,y]=map[x+1,y]+distmap[x,y]
      originmap[x+1,y]=np.ravel_multi_index([x,y], (max_val,max_val))
  # move to x-1,y
  if x>0:
    if distmap[x-1,y]>map[x-1,y]+distmap[x,y] and not visited[x-1,y]:
      distmap[x-1,y]=map[x-1,y]+distmap[x,y]
      originmap[x-1,y]=np.ravel_multi_index([x,y], (max_val,max_val))
  # move to x,y+1
  if y < max_val-1:
    if distmap[x,y+1]>map[x,y+1]+distmap[x,y] and not visited[x,y+1]:
      distmap[x,y+1]=map[x,y+1]+distmap[x,y]
      originmap[x,y+1]=np.ravel_multi_index([x,y], (max_val,max_val))
  # move to x,y-1
  if y>0:
    if distmap[x,y-1]>map[x,y-1]+distmap[x,y] and not visited[x,y-1]:
      distmap[x,y-1]=map[x,y-1]+distmap[x,y]
      originmap[x,y-1]=np.ravel_multi_index([x,y], (max_val,max_val))

  visited[x,y]=True
  dismaptemp=distmap
  dismaptemp[np.where(visited)]=np.Infinity
  # now we find the shortest path so far
  minpost=np.unravel_index(np.argmin(dismaptemp),np.shape(dismaptemp))
  x,y=minpost[0],minpost[1]
  if x==max_val-1 and y==max_val-1:
    finished=True
  count=count+1

#Start backtracking to plot the path  
mattemp=map.astype(float)
x,y=max_val-1,max_val-1
path=[]
mattemp[int(x),int(y)]=np.nan

while x>0.0 or y>0.0:
  path.append([int(x),int(y)])
  xxyy=np.unravel_index(int(originmap[int(x),int(y)]), (max_val,max_val))
  x,y=xxyy[0],xxyy[1]
  mattemp[int(x),int(y)]=np.nan
path.append([int(x),int(y)])

#Output and visualization of the path
current_cmap = plt.cm.Blues
current_cmap.set_bad(color='red')
fig, ax = plt.subplots(figsize=(8,8))
ax.matshow(mattemp,cmap=plt.cm.Blues, vmin=0, vmax=20)
for i in range(max_val):
    for j in range(max_val):
      c = map[j,i]
      ax.text(i, j, str(c), va='center', ha='center')

plt.show()
print('The path length is: '+str(distmap[max_val-1,max_val-1]))
print('The dump/mean path should have been: '+str(maxnum*max_val))