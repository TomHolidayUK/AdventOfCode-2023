# THIS SCRIPT DOESN'T WORK CORRECTLY


file_path10 = './src/Day10/perimeterWithDirections.txt'

with open(file_path10, 'r', encoding='utf-8') as file:
    file_content = file.read()

# Split the content into lines
lined_data = file_content.split('\n')
matrix = [x.split(',') for x in lined_data]

matrixNumerical = [
    [int(row[0]), int(row[1]), int(row[2]), row[3]]
    for row in matrix
]

print(matrixNumerical)

matrix_width = 140
matrix_height = 140

# create matrix of dots
dots_matrix = []
for i in range(140):
    dots_row = []
    for j in range(140):
        dots_row.append('.')
    dots_matrix.append(dots_row)




# Need to follow the loop/perimeter and add the empty nodes to the left of the line to the node inside the loop
# When adding, need to check that node hasn't already been added

nodesInsideLoop = []

def isPartOfLoop(position_to_check): 
    for lst in matrixNumerical:
        if lst[0] == position_to_check[0] and lst[1] == position_to_check[1]:
            return True
    return False

def alreadyAdded(position_to_check):
    if position_to_check in nodesInsideLoop:
        return True
    return False


# matrixNumerical.forEach(el => {
#     # print(el)
#     # direction = el[2]
#     if (el[2] == 1) {
#         left_position[] = [el[0], el[1] - 1] # check node to the left (depending on current position and direciton)
#         if ((isPartOfLoop(left_position)  == False)and !(lreadyAdded(left_position))  == False){ # check that it is not part of the loop AND check that it has not already been added to nodesInsideLoop
#             nodesInsideLoop.append(left_position)
#         }
#     elif (el[2] == 3) {
#         left_position[] = [el[0], el[1] + 1] 
#         if ((isPartOfLoop(left_position)  == False)and !(lreadyAdded(left_position))  == False){ 
#             nodesInsideLoop.append(left_position)
#         }
#     elif (el[2] == 2) {
#         left_position[] = [el[0] - 1, el[1]] 
#         if ((isPartOfLoop(left_position)  == False)and !(lreadyAdded(left_position))  == False){ 
#             nodesInsideLoop.append(left_position)
#         }
#     elif (el[2] == 4) {
#         left_position[] = [el[0] + 1, el[1]] 
#         if ((isPartOfLoop(left_position)  == False)and !(lreadyAdded(left_position))  == False){ 
#             nodesInsideLoop.append(left_position)
#         }
#     }
# })


for el in matrixNumerical:
    if ((el[2] == 1) and (el[3] != ' J')):
        right_position = [el[0], el[1] + 1] # check node to the right (depending on current position and direciton)
        if ((isPartOfLoop(right_position) == False) and (alreadyAdded(right_position) == False)): # check that it is not part of the loop AND check that it has not already been added to nodesInsideLoop
            nodesInsideLoop.append(right_position)
    elif ((el[2] == 1) and (el[3] == ' J')):
        right_position1 = [el[0], el[1] + 1] 
        right_position2 = [el[0] + 1, el[1]] 
        right_position3 = [el[0] + 1, el[1] + 1]
        if ((isPartOfLoop(right_position1) == False) and (alreadyAdded(right_position) == False)): 
            nodesInsideLoop.append(right_position1)
        if ((isPartOfLoop(right_position2) == False) and (alreadyAdded(right_position) == False)): 
            nodesInsideLoop.append(right_position2)
        if ((isPartOfLoop(right_position3) == False) and (alreadyAdded(right_position) == False)): 
            nodesInsideLoop.append(right_position3)
    elif ((el[2] == 3) and (el[3] != ' F')):
        right_position = [el[0], el[1] - 1] 
        if ((isPartOfLoop(right_position) == False) and (alreadyAdded(right_position) == False)): 
            nodesInsideLoop.append(right_position)
    elif ((el[2] == 3) and (el[3] == ' F')):
        right_position1 = [el[0], el[1] - 1] 
        right_position2 = [el[0] - 1, el[1]] 
        right_position3 = [el[0] - 1, el[1] - 1]
        if ((isPartOfLoop(right_position1) == False) and (alreadyAdded(right_position) == False)): 
            nodesInsideLoop.append(right_position1)
        if ((isPartOfLoop(right_position2) == False) and (alreadyAdded(right_position) == False)): 
            nodesInsideLoop.append(right_position2)
        if ((isPartOfLoop(right_position3) == False) and (alreadyAdded(right_position) == False)): 
            nodesInsideLoop.append(right_position3)
    elif ((el[2] == 2) and (el[3] != ' L')):
        right_position = [el[0] + 1, el[1]] 
        if ((isPartOfLoop(right_position) == False) and (alreadyAdded(right_position) == False)): 
            nodesInsideLoop.append(right_position)
    elif ((el[2] == 2) and (el[3] == ' L')):
        right_position1 = [el[0] + 1, el[1]] 
        right_position2 = [el[0], el[1] - 1] 
        right_position3 = [el[0] + 1, el[1] - 1]
        if ((isPartOfLoop(right_position1) == False) and (alreadyAdded(right_position) == False)): 
            nodesInsideLoop.append(right_position1)
        if ((isPartOfLoop(right_position2) == False) and (alreadyAdded(right_position) == False)): 
            nodesInsideLoop.append(right_position2)
        if ((isPartOfLoop(right_position3) == False) and (alreadyAdded(right_position) == False)): 
            nodesInsideLoop.append(right_position3)
    elif ((el[2] == 4) and (el[3] != ' 7')):
        right_position = [el[0] - 1, el[1]] 
        if ((isPartOfLoop(right_position) == False) and (alreadyAdded(right_position) == False)): 
            nodesInsideLoop.append(right_position)
    elif ((el[2] == 4) and (el[3] == ' 7')):
        right_position1 = [el[0] - 1, el[1]] 
        right_position2 = [el[0], el[1] + 1] 
        right_position3 = [el[0] - 1, el[1] + 1]
        if ((isPartOfLoop(right_position1) == False) and (alreadyAdded(right_position) == False)): 
            nodesInsideLoop.append(right_position1)
        if ((isPartOfLoop(right_position2) == False) and (alreadyAdded(right_position) == False)): 
            nodesInsideLoop.append(right_position2)
        if ((isPartOfLoop(right_position3) == False) and (alreadyAdded(right_position) == False)): 
            nodesInsideLoop.append(right_position3)



# print(nodesInsideLoop)
unique_list = []
for item in nodesInsideLoop:
    if item not in unique_list:
        unique_list.append(item)
# unique_list = list(set(nodesInsideLoop))
print(unique_list)

final_result10_2 = len(unique_list)
print(final_result10_2)


# Plot data
for el in matrixNumerical:
     dots_matrix[el[0]][el[1]] = 'X'

for el in nodesInsideLoop:
    dots_matrix[el[0]][el[1]] = '-'

stringData = '\n'.join([''.join(x) for x in dots_matrix])
print(stringData);

with open('./src/Day10/data_visualised.txt', 'w', encoding='utf-8') as file:
    file.write(stringData)

# nodesInsideLoop counts the nodes that are 1 step inside of the loop, this accounts for many of them 
# However if you visually represent the loop (with dots_matrix and data_visualised.txt) you see that there is a big area of nodes in the middle that are inside the loop but not a part of it 
# To get the final total, count the amount of nodes in this zone and add to nodesInsideLoop

# 291 + 274 = 565 too high
# 500 too low


