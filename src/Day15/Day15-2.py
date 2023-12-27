file_path = './src/Day15/Data15.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

data = file_content.split(',')
print(data)

data2 = []

for index, step in enumerate(data):
    if '-' in step:
        data2.append(step.split('-'))
        data2[index].insert(1, '-')
    else:
        data2.append(step.split('='))
        data2[index].insert(1, '=')

# print(data2)

# Plan 
# 1 - create boxes list
# 2 - go through each step in the initialization sequence
# 3 - find label of lens with HASH algorithm from part 1
# 4 - run process for - 
# 5 - run process for =
# 6 - calculate total focusing power of all lenses

# From Part 1
def hashAlgorithm(string, current_value):

    # Steps
    # 1 - find ASCII code
    # 2 - Increase current value by ASCII code 
    # 3 - Set the current value to itself multiplied by 17.
    # 4 - Set the current value to the remainder of dividing itself by 256.

    # 1 
    ascii_code = ord(string)
    # print('1', ascii_code)

    # 2 
    current_value = current_value + ascii_code
    # print('2', current_value)

    # 3
    current_value = current_value * 17
    # print('3', current_value)

    # 4
    current_value = current_value % 256
    # print('4', current_value)

    return current_value

def stepValue(string):
    char_list = list(string)
    current_value = 0
    for char in char_list:
        # all_values.append(hashAlgorithm(char, current_value))
        current_value = hashAlgorithm(char, current_value)
    return current_value



# 1
boxes = [[] for _ in range(256)]

# 2-5
for step in data2:
    lens_label = stepValue(step[0])
    if step[1] == '-':
        for i in range(len(boxes[lens_label])):
            if boxes[lens_label][i][0] == step[0]:
                boxes[lens_label].pop(i)
                # print('box removed')
                break
    elif step[1] == '=':
        box_found = False
        for i in range(len(boxes[lens_label])):
            if boxes[lens_label][i][0] == step[0]:
                boxes[lens_label][i] = step
                box_found = True
                # print('box replaced')
        if box_found == False:
            boxes[lens_label].append(step)
            # print('box added')
    else:
        print('error')

print(boxes)  

# 6
def calculateTotalFocusingPower(boxes):
    total = 0
    for index1, box in enumerate(boxes):
        for index2, lense in enumerate(box):
            # print(lense)
            # print((index1 + 1), index2 + 1, int(lense[2]))
            total += (index1 + 1) * (index2 + 1) * int(lense[2])
    return total


print(calculateTotalFocusingPower(boxes))



