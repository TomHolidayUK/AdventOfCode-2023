file_path = './src/Day16/Data16.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

data = file_content.split('\n')
# print(data)

matrix = []

for array in data:
    matrix.append(list(array))

# print(matrix)

# energised_tiles = []
# route_data = [] # This is used to store data about the route whcih is used to prevent the route looping infinitely
# routes_to_explore = []

# # def findLength(input_matrix):
# def findNextNodes(position, direction, chosen_matrix): 
#     print('current position + direction:', position, direction)
#     # take position and direction as arguments, find valid next positions and next directions

#     next_nodes_data = [] # next position y, next position x, direction (1 = above, 2 = right, 3 = below, 4 = left)

#     if (direction == 1):
#         if position[0] <= 0:
#             print('REACHED THE EDGE, ROUTE TERMINATED (TOP)')
#             return False
#         else:
#             above_value = chosen_matrix[position[0] - 1][position[1]]
#             # print('above value', above_value)
#             if (above_value == '-'):
#                 next_nodes_data.append([position[0] - 1, position[1], 2])
#                 next_nodes_data.append([position[0] - 1, position[1], 4])
#             elif (above_value == '|'):
#                 next_nodes_data = [position[0] - 1, position[1], 1]
#             elif (above_value == '.'):
#                 next_nodes_data = [position[0] - 1, position[1], 1]
#             elif (above_value == '/'):
#                 next_nodes_data = [position[0] - 1, position[1], 2]
#             elif (above_value == '\\'):
#                 next_nodes_data = [position[0] - 1, position[1], 4]
    

#     if (direction == 3):
#         if position[0] >= len(matrix) - 1:
#             print('REACHED THE EDGE, ROUTE TERMINATED (BOTTOM)')
#             return False
#         else:
#             below_value = chosen_matrix[position[0] + 1][position[1]]
#             # print('below value', below_value)
#             if (below_value == '-'):
#                 next_nodes_data.append([position[0] + 1, position[1], 2])
#                 next_nodes_data.append([position[0] + 1, position[1], 4])
#             elif (below_value == '|'):
#                 next_nodes_data = [position[0] + 1, position[1], 3]
#             elif (below_value == '.'):
#                 next_nodes_data = [position[0] + 1, position[1], 3]
#             elif (below_value == '/'):
#                 next_nodes_data = [position[0] + 1, position[1], 4]
#             elif (below_value == '\\'):
#                 next_nodes_data = [position[0] + 1, position[1], 2]
    

#     if (direction == 4):
#         if position[1] <= 0:
#             print('REACHED THE EDGE, ROUTE TERMINATED (LEFT)')
#             return False
#         else:
#             left_value = chosen_matrix[position[0]][position[1] - 1]
#             # print('left value', left_value)
#             if (left_value == '-'):
#                 next_nodes_data = [position[0], position[1] - 1, 4]
#             elif (left_value == '|'):
#                 next_nodes_data.append([position[0], position[1] - 1, 3])
#                 next_nodes_data.append([position[0], position[1] - 1, 1])
#             elif (left_value == '.'):
#                 next_nodes_data = [position[0], position[1] - 1, 4]
#             elif (left_value == '/'):
#                 next_nodes_data = [position[0], position[1] - 1, 3]
#             elif (left_value == '\\'):
#                 next_nodes_data = [position[0], position[1] - 1, 1]
    

#     if (direction == 2):
#         if position[1] >= len(matrix[0]) - 1:
#             print('REACHED THE EDGE, ROUTE TERMINATED (RIGHT)')
#             return False
#         else:
#             right_value = chosen_matrix[position[0]][position[1] + 1]
#             # print('right value', right_value)
#             if (right_value == '-'):
#                 next_nodes_data = [position[0], position[1] + 1, 2]
#             elif (right_value == '|'):
#                 next_nodes_data.append([position[0], position[1] + 1, 3])
#                 next_nodes_data.append([position[0], position[1] + 1, 1])
#             elif (right_value == '.'):
#                 next_nodes_data = [position[0], position[1] + 1, 2]
#             elif (right_value == '/'):
#                 next_nodes_data = [position[0], position[1] + 1, 1]
#             elif (right_value == '\\'):
#                 next_nodes_data = [position[0], position[1] + 1, 3]
    
#     print('next:', next_nodes_data)
#     return next_nodes_data  # next position y, next position x, direction (1 = above, 2 = right, 3 = below, 4 = left)




# def is_looping(matrix, target_node):
#     for node in matrix:
#         if target_node == node:
#             return True
#     return False



# def recursiveFunction(currentPosition, direction, chosen_matrix):
#     print('--------')
#     print('current value:', matrix[currentPosition[0]][currentPosition[1]])
#     energised_tiles.append([currentPosition[0], currentPosition[1]])
#     route_data.append([currentPosition[0], currentPosition[1], direction])
#     next_positions_data = findNextNodes(currentPosition, direction, chosen_matrix)

#     # Check if there are more than one next positions
#     if next_positions_data == False:
#         return energised_tiles
#     elif all(isinstance(sublist, list) for sublist in next_positions_data) and type(next_positions_data) is list: # check if there's 2 next positions
#         print('2 next positions')
#         next_y2 = next_positions_data[1][0]
#         next_x2 = next_positions_data[1][1]
#         next_direction2 = next_positions_data[1][2]
#         next_position2 = [next_y2, next_x2]
#         routes_to_explore.append([next_position2[0], next_position2[1], next_direction2])
#         print(routes_to_explore)
#         # ------------
#         next_y = next_positions_data[0][0]
#         next_x = next_positions_data[0][1]
#         next_direction = next_positions_data[0][2]
#         next_position = [next_y, next_x]
#         if is_looping(route_data, [next_y, next_x, next_direction]):
#             print('Repeating!!! Stop!!!')
#         else:
#             recursiveFunction(next_position, next_direction, chosen_matrix) 
#     else:
#         # print('1 next position')
#         next_y = next_positions_data[0]
#         next_x = next_positions_data[1]
#         next_direction = next_positions_data[2]
#         next_position = [next_y, next_x]
#         if is_looping(route_data, [next_y, next_x, next_direction]):
#             print('Repeating!!! Stop!!!')
#         else:
#             recursiveFunction(next_position, next_direction, chosen_matrix)




# # print(recursiveFunction(start_position, 3, matrix))

# print(routes_to_explore)

# while routes_to_explore:
#     chosen_route = routes_to_explore[-1]
#     routes_to_explore.pop()
#     recursiveFunction([chosen_route[0], chosen_route[1]], chosen_route[2], matrix)
#     print('test')

# matrix_visualised = []

# for i in range(len(matrix)):
#     string = []
#     for j in range(len(matrix[0])):
#         string.append('.')
#     matrix_visualised.append(string)

# for position in energised_tiles:
#     matrix_visualised[position[0]][position[1]] = '#'

# # print(energised_tiles)
# stringData2 = '\n'.join([''.join(x) for x in matrix_visualised])
# print(stringData2)

# count = 0
# for i in range(len(matrix_visualised)):
#     for j in range(len(matrix_visualised[0])):
#         if matrix_visualised[i][j] == '#':
#             count += 1

# print(count)

def findValue(startPosition, startDirection):
    energised_tiles = []
    route_data = [] # This is used to store data about the route whcih is used to prevent the route looping infinitely
    routes_to_explore = []

    # def findLength(input_matrix):
    def findNextNodes(position, direction): 
        # print('current position + direction:', position, direction)
        # take position and direction as arguments, find valid next positions and next directions

        next_nodes_data = [] # next position y, next position x, direction (1 = above, 2 = right, 3 = below, 4 = left)

        if (direction == 1):
            if position[0] <= 0:
                # print('REACHED THE EDGE, ROUTE TERMINATED (TOP)')
                return False
            else:
                above_value = matrix[position[0] - 1][position[1]]
                # print('above value', above_value)
                if (above_value == '-'):
                    next_nodes_data.append([position[0] - 1, position[1], 2])
                    next_nodes_data.append([position[0] - 1, position[1], 4])
                elif (above_value == '|'):
                    next_nodes_data = [position[0] - 1, position[1], 1]
                elif (above_value == '.'):
                    next_nodes_data = [position[0] - 1, position[1], 1]
                elif (above_value == '/'):
                    next_nodes_data = [position[0] - 1, position[1], 2]
                elif (above_value == '\\'):
                    next_nodes_data = [position[0] - 1, position[1], 4]
        

        if (direction == 3):
            if position[0] >= len(matrix) - 1:
                # print('REACHED THE EDGE, ROUTE TERMINATED (BOTTOM)')
                return False
            else:
                below_value = matrix[position[0] + 1][position[1]]
                # print('below value', below_value)
                if (below_value == '-'):
                    next_nodes_data.append([position[0] + 1, position[1], 2])
                    next_nodes_data.append([position[0] + 1, position[1], 4])
                elif (below_value == '|'):
                    next_nodes_data = [position[0] + 1, position[1], 3]
                elif (below_value == '.'):
                    next_nodes_data = [position[0] + 1, position[1], 3]
                elif (below_value == '/'):
                    next_nodes_data = [position[0] + 1, position[1], 4]
                elif (below_value == '\\'):
                    next_nodes_data = [position[0] + 1, position[1], 2]
        

        if (direction == 4):
            if position[1] <= 0:
                # print('REACHED THE EDGE, ROUTE TERMINATED (LEFT)')
                return False
            else:
                left_value = matrix[position[0]][position[1] - 1]
                # print('left value', left_value)
                if (left_value == '-'):
                    next_nodes_data = [position[0], position[1] - 1, 4]
                elif (left_value == '|'):
                    next_nodes_data.append([position[0], position[1] - 1, 3])
                    next_nodes_data.append([position[0], position[1] - 1, 1])
                elif (left_value == '.'):
                    next_nodes_data = [position[0], position[1] - 1, 4]
                elif (left_value == '/'):
                    next_nodes_data = [position[0], position[1] - 1, 3]
                elif (left_value == '\\'):
                    next_nodes_data = [position[0], position[1] - 1, 1]
        

        if (direction == 2):
            if position[1] >= len(matrix[0]) - 1:
                # print('REACHED THE EDGE, ROUTE TERMINATED (RIGHT)')
                return False
            else:
                right_value = matrix[position[0]][position[1] + 1]
                # print('right value', right_value)
                if (right_value == '-'):
                    next_nodes_data = [position[0], position[1] + 1, 2]
                elif (right_value == '|'):
                    next_nodes_data.append([position[0], position[1] + 1, 3])
                    next_nodes_data.append([position[0], position[1] + 1, 1])
                elif (right_value == '.'):
                    next_nodes_data = [position[0], position[1] + 1, 2]
                elif (right_value == '/'):
                    next_nodes_data = [position[0], position[1] + 1, 1]
                elif (right_value == '\\'):
                    next_nodes_data = [position[0], position[1] + 1, 3]
        
        # print('next:', next_nodes_data)
        return next_nodes_data  # next position y, next position x, direction (1 = above, 2 = right, 3 = below, 4 = left)

    def is_looping(matrix, target_node):
        for node in matrix:
            if target_node == node:
                return True
        return False

    def recursiveFunction(currentPosition, direction):
        # print('--------')
        # print('current value:', matrix[currentPosition[0]][currentPosition[1]])
        energised_tiles.append([currentPosition[0], currentPosition[1]])
        route_data.append([currentPosition[0], currentPosition[1], direction])
        next_positions_data = findNextNodes(currentPosition, direction)

        # Check if there are more than one next positions
        if next_positions_data == False:
            return energised_tiles
        elif all(isinstance(sublist, list) for sublist in next_positions_data) and type(next_positions_data) is list: # check if there's 2 next positions
            # print('2 next positions')
            next_y2 = next_positions_data[1][0]
            next_x2 = next_positions_data[1][1]
            next_direction2 = next_positions_data[1][2]
            next_position2 = [next_y2, next_x2]
            routes_to_explore.append([next_position2[0], next_position2[1], next_direction2])
            # print(routes_to_explore)
            # ------------
            next_y = next_positions_data[0][0]
            next_x = next_positions_data[0][1]
            next_direction = next_positions_data[0][2]
            next_position = [next_y, next_x]
            if is_looping(route_data, [next_y, next_x, next_direction]):
                # print('Repeating!!! Stop!!!')
                pass
            else:
                recursiveFunction(next_position, next_direction) 
        else:
            # print('1 next position')
            next_y = next_positions_data[0]
            next_x = next_positions_data[1]
            next_direction = next_positions_data[2]
            next_position = [next_y, next_x]
            if is_looping(route_data, [next_y, next_x, next_direction]):
                # print('Repeating!!! Stop!!!')
                pass
            else:
                recursiveFunction(next_position, next_direction)


    recursiveFunction(startPosition, startDirection)

    while routes_to_explore:
        chosen_route = routes_to_explore[-1]
        routes_to_explore.pop()
        recursiveFunction([chosen_route[0], chosen_route[1]], chosen_route[2])

    matrix_visualised = []

    for i in range(len(matrix)):
        string = []
        for j in range(len(matrix[0])):
            string.append('.')
        matrix_visualised.append(string)

    for position in energised_tiles:
        matrix_visualised[position[0]][position[1]] = '#'

    # stringData2 = '\n'.join([''.join(x) for x in matrix_visualised])
    # print(stringData2)
    # print('-------------')

    count = 0
    for i in range(len(matrix_visualised)):
        for j in range(len(matrix_visualised[0])):
            if matrix_visualised[i][j] == '#':
                count += 1

    print('count:', count)
    return count
    


matrix_height = len(matrix)
matrix_width = len(matrix[0])
checks_required =  2 * matrix_height + 2 * matrix_width
highest_value = 0
total_checks = 0

# left side 
for i in range(matrix_height):
    value = findValue([i, 0], 2)
    if value > highest_value:
        highest_value = value
        total_checks += 1 
        print(f'{total_checks}/{checks_required} checks complete. Highest value so far: {highest_value}')
    else:
        total_checks += 1 
        print(f'{total_checks}/{checks_required} checks complete. Highest value so far: {highest_value}')

# right side 
for i in range(matrix_height):
    value = findValue([i, matrix_width - 1], 4)
    if value > highest_value:
        highest_value = value
        total_checks += 1 
        print(f'{total_checks}/{checks_required} checks complete. Highest value so far: {highest_value}')
    else:
        total_checks += 1 
        print(f'{total_checks}/{checks_required} checks complete. Highest value so far: {highest_value}')

# top side 
for i in range(matrix_width):
    value = findValue([0, i], 3)
    if value > highest_value:
        highest_value = value
        total_checks += 1 
        print(f'{total_checks}/{checks_required} checks complete. Highest value so far: {highest_value}')
    else:
        total_checks += 1 
        print(f'{total_checks}/{checks_required} checks complete. Highest value so far: {highest_value}')

# bottom side 
for i in range(matrix_width):
    value = findValue([matrix_height - 1, i], 1)
    if value > highest_value:
        highest_value = value
        total_checks += 1 
        print(f'{total_checks}/{checks_required} checks complete. Highest value so far: {highest_value}')
    else:
        total_checks += 1 
        print(f'{total_checks}/{checks_required} checks complete. Highest value so far: {highest_value}')
    

print(highest_value)