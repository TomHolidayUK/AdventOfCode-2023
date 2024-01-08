file_path = './src/Day18/Data18.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

data = [row.split() for row in file_content.split('\n')]
data2 = [[elem[0], int(elem[1]), elem[2]] for elem in data]

# Plan 
# 1 - Find height and width of loop matrix 
# 2 - Create loop matrix
# 3 - Go through the matrix and work out the volume for each row 

# Part 1
y = 0
x = 0
y_records = []
x_records = []

for elem in data2:
    if elem[0] == 'U':
        y += elem[1]
        y_records.append(y)
    elif elem[0] == 'D':
        y -= elem[1]
        y_records.append(y)
    elif elem[0] == 'R':    
        x += elem[1]
        x_records.append(x)
    elif elem[0] == 'L':    
        x -= elem[1]
        x_records.append(x)


y_max = max(y_records)
x_max = max(x_records)
y_min = min(y_records)
x_min = min(x_records)

# print(y_max)
# print(x_max)
# print(y_min)
# print(x_min)

height = y_max - y_min
width = x_max - x_min 

# print(height)
# print(width)

y_position = y_max
x_position = -x_min

# print(y_position)
# print(x_position)

# Part 2
matrix = [['.' for _ in range(width+1)] for _ in range(height+1)]

# print(matrix)

for elem in data2:
    direction = elem[0]
    distance = elem[1]
    # matrix[y_position][x_position] = '#'
    if direction == 'D':
        for i in range(distance):
            matrix[y_position + i][x_position] = '#'
        y_position += distance
    elif direction == 'U':
        for i in range(distance):
            matrix[y_position - i][x_position] = '#'
        y_position -= distance
    elif direction == 'R':
        for i in range(distance):
            matrix[y_position][x_position + i] = '#'
        x_position += distance
    elif direction == 'L':
        for i in range(distance):
            matrix[y_position][x_position - i] = '#'
        x_position -= distance
    
# print(matrix)

stringData = '\n'.join([''.join([str(x) for x in row]) for row in matrix])
# print(stringData)
file_path2 = './src/Day18/Data18-visualised.txt'
with open(file_path2, 'w') as file:
    file.write(stringData)



# Part 3
    
def toggleBoolean(boolean):
    if boolean == True:
        return False
    elif boolean == False:
        return True

loop_count = 0
inside_count = 0 

# if we have a '#' then some '.''s then a '#' again, the '.''s are insdie the loop

for row_index, line in enumerate(matrix):
    previousChar = False  # record the previous charchter, this is important in determining if we've crossed in or out of the loop 
    insideLoop = False  # a state for if we are in or out of the loop 
    local_count = 0  
    aboveCheck = False  # to confirm that we have crossed into the loop we need to confirm that the loop passes above and below of where we are traversing, if this isn't true then we are just brushing a bend in the loop instead of actually moving into it
    belowCheck = False
    for column_index, char in enumerate(line):
        # count loop
        if char == '#':
            loop_count += 1
            inside_count += local_count
            local_count = 0
            if row_index == 0 or row_index == len(matrix) - 1:
                continue
            else:
                if matrix[row_index - 1][column_index] == '#':
                    aboveCheck = True
                if matrix[row_index + 1][column_index] == '#':
                    belowCheck = True

        # determine if inside the loop - if a '#' is followed by a '.' then the loop boundary has been crossed
    
        if char == '.' and previousChar == '#' and aboveCheck == True and belowCheck == True: 
            insideLoop = toggleBoolean(insideLoop)
            aboveCheck, belowCheck = False, False
        # print('insideLoop:', insideLoop)

        # count the area inside the loop
        if insideLoop == True and char == '.':
            local_count += 1

        previousChar = char
    # print(f'inside_count: {inside_count}. loop count: {loop_count}')


print(loop_count)
print(inside_count)
print(loop_count + inside_count)


# 42590 - too high
# 40557 - too low