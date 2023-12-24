file_path10 = './src/Day11/Data11.txt'

with open(file_path10, 'r', encoding='utf-8') as file:
    file_content = file.read()

data = file_content.split('\n')
matrix = []
for el in data:
        matrix.append([x for x in el])
# print(matrix)

# Plan
# 1 - find location of galaxies
# 2 - find free rows and columns
# 3 - expand universe
# 4 - find new location of galaxies
# 5 - find distance between galaxies

# Step 1 
galaxy_y_coordinates = []
galaxy_x_coordinates = []
for index_y, row in enumerate(matrix):
    for index_x, column in enumerate(row):
        if (matrix[index_y][index_x] == '#'):
            galaxy_y_coordinates.append(index_y)
            galaxy_x_coordinates.append(index_x)


# Step 2 
universe_height =len(matrix)
universe_width =len(matrix[0])

free_columns = []
free_rows = []

for row in range(universe_height):
    if row not in galaxy_y_coordinates:
        free_rows.append(row)

for column in range(universe_width):
    if column not in galaxy_x_coordinates:
        free_columns.append(column)

print('free rows', free_rows)
print('free_columns', free_columns)




# Step 3
for row in matrix:
    offset1 = 1
    for column in free_columns:
        row.insert(column + offset1, '.')
        offset1 += 1

for index_y, row in enumerate(matrix):
    offset2 = 1
    if index_y in free_rows:
        matrix.insert(index_y + offset2, (['.'] * len(row)))
        offset2 += 1

stringData = '\n'.join([''.join(x) for x in matrix])
print(stringData);

with open('./src/Day11/data_visualised.txt', 'w', encoding='utf-8') as file:
    file.write(stringData)
        
# Step 4
new_galaxy_positions = []
for index_y, row in enumerate(matrix):
    for index_x, column in enumerate(row):
        if (matrix[index_y][index_x] == '#'):
            new_galaxy_positions.append([index_y, index_x])

# print(new_galaxy_positions)

# Step 5
def findDistance(position1, position2):
    x_distance = abs(position1[1] - position2[1])
    y_distance = abs(position1[0] - position2[0])
    total_distance = x_distance + y_distance
    return total_distance

# print(findDistance([11, 5], [6, 1]))
# print(findDistance([10, 9], [7, 12]))

number_of_galaxies = len(new_galaxy_positions)
# print(number_of_galaxies)
number_of_pairs = int(((number_of_galaxies - 1) * (number_of_galaxies)) / 2)
# print(number_of_pairs)

galaxy_pairs = []

for i in range(number_of_galaxies):
    for j in range(i + 1, number_of_galaxies):  # Start from i+1 to avoid galaxy_pairs with repeated numbers
        galaxy_pairs.append([new_galaxy_positions[i], new_galaxy_positions[j]])

# print(galaxy_pairs)

distance_total = 0

for pair in galaxy_pairs:
    distance_total += findDistance(pair[0], pair[1])

print(distance_total)

