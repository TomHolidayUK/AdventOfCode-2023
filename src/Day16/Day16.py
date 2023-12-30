file_path = './src/Day16/Data16-test.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

data = file_content.split('\n')
# print(data)

matrix = []

for array in data:
    matrix.append(list(array))

print(matrix)

# Plan
# 1 - write find next nodes function
# 2 - create a recursive function that runs through the possible routes as you go through add tiles on the path to energised tiles, if the path comes back to an energised tiles the function can be stopped

start_position = [0, 0]
print('start position:', start_position)
energised_tiles = []

# def findNextNodes(position, direction, chosen_matrix): 
#         # take position and direction as arguments, find valid next positions and next directions

#         next_nodes_data = [] # next position y, next position x, direction (1 = above, 2 = right, 3 = below, 4 = left)

#         if (direction == 1):
#             above_value = chosen_matrix[position[0] - 1][position[1]]
#             # print('above value', above_value)
#             if (above_value == '-'):
#                 # print(`above is valid with '|', next index: [${position[0] - 2}]${position[1]}]`)
#                 next_nodes_data.append([position[0] - 1, position[1], 2])
#                 next_nodes_data.append([position[0] - 1, position[1], 4])
#             elif (above_value == '|'):
#                 # print(`above is valid with '|', next index: [${position[0] - 2}]${position[1]}]`)
#                 next_nodes_data = [position[0] - 1, position[1], 1]
#             elif (above_value == '/'):
#                 # print(`above is valid with '7', next index: [${position[0] - 1}][${position[1] - 1}]`)
#                 next_nodes_data = [position[0] - 1, position[1], 2]
#             elif (above_value == '\\'):
#                 # print(`above is valid with 'F', next index: [${position[0] - 1}][${position[1] + 1}]`)
#                 next_nodes_data = [position[0] - 1, position[1], 4]
#             elif (above_value == 'S'):
#                 return [start_position[0], start_position[1], 3]
        

#         if (direction == 3):
#             below_value = chosen_matrix[position[0] + 1][position[1]]
#             # print('below value', below_value)
#             if (below_value == '-'):
#                 # print(`left is valid with '-', next index: [${position[0]}][${position[1] - 2}]`)
#                 next_nodes_data.append([position[0] + 1, position[1], 2])
#                 next_nodes_data.append([position[0] + 1, position[1], 4])
#             elif (below_value == '|'):
#                 # print(`left is valid with 'L', next index: [${position[0] + 1 - 1}][${position[1] - 1}]`)
#                 next_nodes_data = [position[0] + 1, position[1], 3]
#             elif (below_value == '.'):
#                 # print(`left is valid with 'L', next index: [${position[0] + 1 - 1}][${position[1] - 1}]`)
#                 next_nodes_data = [position[0] + 1, position[1], 3]
#             elif (below_value == '/'):
#                 # print(`left is valid with 'F', next index: [${position[0] + 1 + 1}][${position[1] - 1}]`)
#                 next_nodes_data = [position[0] + 1, position[1], 4]
#             elif (below_value == '\\'):
#                 # print(`left is valid with 'F', next index: [${position[0] + 1 + 1}][${position[1] - 1}]`)
#                 next_nodes_data = [position[0] + 1, position[1], 2]
#             elif (below_value == '#'):
#                 return [start_position[0], start_position[1], 4]
        

#         if (direction == 4):
#             left_value = chosen_matrix[position[0]][position[1] - 1]
#             # print('left value', left_value)
#             if (left_value == '-'):
#                 # print(`left is valid with '-', next index: [${position[0]}][${position[1] - 2}]`)
#                 next_nodes_data = [position[0], position[1] - 1, 4]
#             elif (left_value == '|'):
#                 # print(`left is valid with 'L', next index: [${position[0] - 1}][${position[1] - 1 - 1}]`)
#                 next_nodes_data.append([position[0], position[1] - 1, 3])
#                 next_nodes_data.append([position[0], position[1] - 1, 1])
#             elif (left_value == '/'):
#                 # print(`left is valid with 'F', next index: [${position[0] + 1}][${position[1] - 1 - 1}]`)
#                 next_nodes_data = [position[0], position[1] - 1, 3]
#             elif (left_value == '\\'):
#                 # print(`left is valid with 'F', next index: [${position[0] + 1}][${position[1] - 1 - 1}]`)
#                 next_nodes_data = [position[0], position[1] - 1, 3]
#             elif (left_value == '#'):
#                 return [start_position[0], start_position[1], 4]
        

#         if (direction == 2):
#             right_value = chosen_matrix[position[0]][position[1] + 1]
#             # print('right value', right_value)
#             if (right_value == '-'):
#                 # print(`right is valid with '-', next index: [${position[0]}][${position[1] + 2}]`)
#                 next_nodes_data = [position[0], position[1] + 1, 2]
#             elif (right_value == '|'):
#                 # print(`right is valid with 'J', next index: [${position[0] - 1}][${position[1] + 1}]`)
#                 next_nodes_data.append([position[0], position[1] + 1, 3])
#                 next_nodes_data.append([position[0], position[1] + 1, 1])
#             elif (right_value == '/'):
#                 # print(`right is valid with '7', next index: [${position[0] + 1}][${position[1] + 1}]`)
#                 next_nodes_data = [position[0], position[1] + 1, 1]
#             elif (right_value == '\\'):
#                 # print(`right is valid with '7', next index: [${position[0] + 1}][${position[1] + 1}]`)
#                 next_nodes_data = [position[0], position[1] + 1, 3]
#             elif (right_value == '#'):
#                 return [start_position[0], start_position[1], 3]
        

#         return next_nodes_data  # next position y, next position x, direction (1 = above, 2 = right, 3 = below, 4 = left)


# def findLength(input_matrix):
def findNextNodes(position, direction, chosen_matrix): 
    print('input:', position, direction)
    # take position and direction as arguments, find valid next positions and next directions

    next_nodes_data = [] # next position y, next position x, direction (1 = above, 2 = right, 3 = below, 4 = left)

    if (direction == 1):
        above_value = chosen_matrix[position[0] - 1][position[1]]
        # print('above value', above_value)
        if (above_value == '-'):
            # print(`above is valid with '|', next index: [${position[0] - 2}]${position[1]}]`)
            next_nodes_data.append([position[0] - 1, position[1], 2])
            next_nodes_data.append([position[0] - 1, position[1], 4])
        elif (above_value == '|'):
            # print(`above is valid with '|', next index: [${position[0] - 2}]${position[1]}]`)
            next_nodes_data = [position[0] - 1, position[1], 1]
        elif (above_value == '.'):
            # print(`left is valid with 'L', next index: [${position[0] + 1 - 1}][${position[1] - 1}]`)
            next_nodes_data = [position[0] - 1, position[1], 1]
        elif (above_value == '/'):
            # print(`above is valid with '7', next index: [${position[0] - 1}][${position[1] - 1}]`)
            next_nodes_data = [position[0] - 1, position[1], 2]
        elif (above_value == '\\'):
            # print(`above is valid with 'F', next index: [${position[0] - 1}][${position[1] + 1}]`)
            next_nodes_data = [position[0] - 1, position[1], 4]
        elif (above_value == 'S'):
            return [start_position[0], start_position[1], 3]
    

    if (direction == 3):
        if position[0] == len(matrix):
            return False
        else:
            below_value = chosen_matrix[position[0] + 1][position[1]]
            # print('below value', below_value)
            if (below_value == '-'):
                # print(`left is valid with '-', next index: [${position[0]}][${position[1] - 2}]`)
                next_nodes_data.append([position[0] + 1, position[1], 2])
                next_nodes_data.append([position[0] - 1, position[1], 4])
            elif (below_value == '|'):
                # print(`left is valid with 'L', next index: [${position[0] + 1 - 1}][${position[1] - 1}]`)
                next_nodes_data = [position[0] + 1, position[1], 3]
            elif (below_value == '.'):
                # print(`left is valid with 'L', next index: [${position[0] + 1 - 1}][${position[1] - 1}]`)
                next_nodes_data = [position[0] + 1, position[1], 3]
            elif (below_value == '/'):
                # print(`left is valid with 'F', next index: [${position[0] + 1 + 1}][${position[1] - 1}]`)
                next_nodes_data = [position[0] + 1, position[1], 4]
            elif (below_value == '\\'):
                # print(`left is valid with 'F', next index: [${position[0] + 1 + 1}][${position[1] - 1}]`)
                next_nodes_data = [position[0] + 1, position[1], 2]
            elif (below_value == '#'):
                return [start_position[0], start_position[1], 4]
    

    if (direction == 4):
        left_value = chosen_matrix[position[0]][position[1] - 1]
        # print('left value', left_value)
        if (left_value == '-'):
            # print(`left is valid with '-', next index: [${position[0]}][${position[1] - 2}]`)
            next_nodes_data = [position[0], position[1] - 1, 4]
        elif (left_value == '|'):
            # print(`left is valid with 'L', next index: [${position[0] - 1}][${position[1] - 1 - 1}]`)
            next_nodes_data.append([position[0], position[1] - 1, 3])
            next_nodes_data.append([position[0], position[1] - 1, 1])
        elif (left_value == '.'):
            # print(`left is valid with 'L', next index: [${position[0] + 1 - 1}][${position[1] - 1}]`)
            next_nodes_data = [position[0], position[1] - 1, 4]
        elif (left_value == '/'):
            # print(`left is valid with 'F', next index: [${position[0] + 1}][${position[1] - 1 - 1}]`)
            next_nodes_data = [position[0], position[1] - 1, 3]
        elif (left_value == '\\'):
            # print(`left is valid with 'F', next index: [${position[0] + 1}][${position[1] - 1 - 1}]`)
            next_nodes_data = [position[0], position[1] - 1, 3]
        elif (left_value == '#'):
            return [start_position[0], start_position[1], 4]
    

    if (direction == 2):
        right_value = chosen_matrix[position[0]][position[1] + 1]
        print('right value', right_value)
        if (right_value == '-'):
            print(f"right is valid with '-', next index: [{position[0]}][{position[1] + 2}]")
            next_nodes_data = [position[0], position[1] + 1, 2]
        elif (right_value == '|'):
            # print(`right is valid with 'J', next index: [${position[0] - 1}][${position[1] + 1}]`)
            next_nodes_data.append([position[0], position[1] + 1, 3])
            next_nodes_data.append([position[0], position[1] - 1, 1])
        elif (right_value == '.'):
            # print(`left is valid with 'L', next index: [${position[0] + 1 - 1}][${position[1] - 1}]`)
            next_nodes_data = [position[0], position[1] + 1, 2]
        elif (right_value == '/'):
            # print(`right is valid with '7', next index: [${position[0] + 1}][${position[1] + 1}]`)
            next_nodes_data = [position[0], position[1] + 1, 1]
        elif (right_value == '\\'):
            # print(`right is valid with '7', next index: [${position[0] + 1}][${position[1] + 1}]`)
            next_nodes_data = [position[0], position[1] + 1, 3]
        elif (right_value == '#'):
            return [start_position[0], start_position[1], 3]
    
    print('final result (next nodes):', next_nodes_data)
    return next_nodes_data  # next position y, next position x, direction (1 = above, 2 = right, 3 = below, 4 = left)


def recursiveFunction(currentPosition, direction, chosen_matrix):

        print('current value:', matrix[currentPosition[0]][currentPosition[1]])
        matrix[currentPosition[0]][currentPosition[1]] = '#'

        next_positions_data = findNextNodes(currentPosition, direction, chosen_matrix)
        # Check if there are more than one next positions
        # next_direction = 0
        # next_position = []
        if all(isinstance(sublist, list) for sublist in next_positions_data) and type(next_positions_data) is list:
            print('2 next positions')
            next_y = next_positions_data[0][0]
            next_x = next_positions_data[0][1]
            next_direction = next_positions_data[0][2]
            next_position = [next_y, next_x]
            if next_y < 0 or next_x < 0 or next_y >= len(matrix) or next_x >= len(matrix[0]):
                print('You have reached the edge of board')
            else:
                print('next position, next direction', next_position, next_direction)
                if matrix[currentPosition[0]][currentPosition[1]] == '#' and matrix[next_y][next_x] == '#': # end condition
                    print('end')
                    return matrix
                recursiveFunction(next_position, next_direction, chosen_matrix) 
            # ------------
            next_y2 = next_positions_data[1][0]
            next_x2 = next_positions_data[1][1]
            next_direction2 = next_positions_data[1][2]
            next_position2 = [next_y2, next_x2]
            if next_y2 < 0 or next_x2 < 0 or next_y2 >= len(matrix) or next_x2 >= len(matrix[0]):
                print('You have reached the edge of board')
            else:
                print('next position, next direction', next_position2, next_direction2)
                if matrix[currentPosition[0]][currentPosition[1]] == '#' and matrix[next_y2][next_x2] == '#': # end condition
                    print('end')
                    return matrix
                recursiveFunction(next_position2, next_direction2, chosen_matrix) 
        else:
            print('1 next position')
            next_y = next_positions_data[0]
            next_x = next_positions_data[1]
            next_direction = next_positions_data[2]
            next_position = [next_y, next_x]
            if next_y < 0 or next_x < 0 or next_y >= len(matrix) or next_x >= len(matrix[0]):
                print('You have reached the edge of board')
            else:
                print('next position, next direction', next_position, next_direction)
                if matrix[currentPosition[0]][currentPosition[1]] == '#' and matrix[next_y][next_x] == '#': # end condition
                    print('end')
                    return matrix
                recursiveFunction(next_position, next_direction, chosen_matrix)


    # return recursiveFunction(start_position, 2, input_matrix)

# print(findLength(matrix))
# print(findNextNodes(start_position, 2, matrix))
# print(findNextNodes([7, 1], 2, matrix))
print(recursiveFunction(start_position, 2, matrix))

# print(findNextNodes(start_position, 2, data))
# print(findNextNodes([0, 1], 3, data))
# y , x, direction

# print(findLength(start_position, 2, data))
# print(findLength([0, 1], 3, data))
