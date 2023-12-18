file_path10 = './src/Day10/data10.txt'

with open(file_path10, 'r', encoding='utf-8') as file:
    file_content = file.read()

# Split the content into lines
lined_data = file_content.split('\n')

matrix = []

for array in lined_data:
    matrix.append(list(array))

# print(matrix)

testdata10 = [
    ['-', 'L', '|', 'F', '7'],
    ['7', 'S', '-', '7', '|'],
    ['L', '|', '7', '|', '|'],
    ['-', 'L', '-', 'J', '|'],
    ['L', '|', '-', 'J', 'F']
]

# const testdata10: string[][] = [
#     ['.', '.', 'F', '7', '.'],
#     ['7', 'F', 'J', '|', '|'],
#     ['S', 'J', '7', 'L', '7'],
#     ['|', 'F', '-', '-', 'J'],
#     ['L', 'J', '-', 'J', 'F']
# ]

steps_total = 0

def findLength(input_matrix):

    # find the starting position
    def findStart(chosen_matrix):
        start_y = 0
        start_x = 0

        for index, row in enumerate(chosen_matrix):
            if 'S' in row:
                start_y = index
                break  

        for index, column in enumerate(chosen_matrix[start_y]):
            if 'S' in column:
                start_x = index
                break  

        return [start_y, start_x]

    start_position = findStart(input_matrix)
    print('start position:', start_position)



    def findNextNode(position, direction, chosen_matrix): 
        # take position and direction as arguments, find valid next positions and next directions

        next_node_data = [] # next position y, next position x, direction (1 = above, 2 = right, 3 = below, 4 = left)

        if (direction == 1):
            above_value = chosen_matrix[position[0] - 1][position[1]]
            # console.log('above value', above_value)
            if (above_value == '|'):
                # console.log(`above is valid with '|', next index: [${position[0] - 2}]${position[1]}]`)
                next_node_data = [position[0] - 1, position[1], 1]
            elif (above_value == '7'):
                # console.log(`above is valid with '7', next index: [${position[0] - 1}][${position[1] - 1}]`)
                next_node_data = [position[0] - 1, position[1], 4]
            elif (above_value == 'F'):
                # console.log(`above is valid with 'F', next index: [${position[0] - 1}][${position[1] + 1}]`)
                next_node_data = [position[0] - 1, position[1], 2]
            elif (above_value == 'S'):
                return [start_position[0], start_position[1], 3]
        

        if (direction == 3):
            below_value = chosen_matrix[position[0] + 1][position[1]]
            # console.log('below value', below_value)
            if (below_value == '|'):
                # console.log(`below is valid with '|', next index: [${position[0] + 2}]${position[1]}]`)
                next_node_data = [position[0] + 1, position[1], 3]
            elif (below_value == 'L'):
                # console.log(`below is valid with 'L', next index: [${position[0] + 1}][${position[1] + 1}]`)
                next_node_data = [position[0] + 1, position[1], 2]
            elif (below_value == 'J'):
                # console.log(`below is valid with 'J', next index: [${position[0] + 1}][${position[1] - 1}]`)
                next_node_data = [position[0] + 1, position[1], 4]
            elif (below_value == 'S'):
                return [start_position[0], start_position[1], 3]
        

        if (direction == 4):
            left_value = chosen_matrix[position[0]][position[1] - 1]
            # console.log('left value', left_value)
            if (left_value == '-'):
                # console.log(`left is valid with '-', next index: [${position[0]}][${position[1] - 2}]`)
                next_node_data = [position[0], position[1] - 1, 4]
            elif (left_value == 'L'):
                # console.log(`left is valid with 'L', next index: [${position[0] - 1}][${position[1] - 1}]`)
                next_node_data = [position[0], position[1] - 1, 1]
            elif (left_value == 'F'):
                # console.log(`left is valid with 'F', next index: [${position[0] + 1}][${position[1] - 1}]`)
                next_node_data = [position[0], position[1] - 1, 3]
            elif (left_value == 'S'):
                return [start_position[0], start_position[1], 4]
        

        if (direction == 2):
            right_value = chosen_matrix[position[0]][position[1] + 1]
            # console.log('right value', right_value)
            if (right_value == '-'):
                # console.log(`right is valid with '-', next index: [${position[0]}][${position[1] + 2}]`)
                next_node_data = [position[0], position[1] + 1, 2]
            elif (right_value == 'J'):
                # console.log(`right is valid with 'J', next index: [${position[0] - 1}][${position[1] + 1}]`)
                next_node_data = [position[0], position[1] + 1, 1]
            elif (right_value == '7'):
                # console.log(`right is valid with '7', next index: [${position[0] + 1}][${position[1] + 1}]`)
                next_node_data = [position[0], position[1] + 1, 3]
            elif (right_value == 'S'):
                return [start_position[0], start_position[1], 3]
        

        return next_node_data  # next position y, next position x, direction (1 = above, 2 = right, 3 = below, 4 = left)

    

    def recursiveFunction(currentPosition, direction, chosen_matrix):
            global steps_total

            print('current value:', matrix[currentPosition[0]][currentPosition[1]])

            next_position_data = findNextNode(currentPosition, direction, chosen_matrix)
            next_y = next_position_data[0];
            next_x = next_position_data[1];
            next_direction = next_position_data[2];
            next_position = [next_y, next_x];
            print(next_position, next_direction)

            if (chosen_matrix[next_y][next_x] == 'S'): # end condition
                steps_total += 1
                print('end')
                return steps_total
        
            steps_total += 1
            print('steps_total', steps_total)
            return recursiveFunction(next_position, next_direction, chosen_matrix)


    return recursiveFunction(start_position, 3, input_matrix)

print(findLength(matrix))