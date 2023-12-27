file_path = './src/Day15/Data15.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

data = file_content.split(',')
# print(data)


# Plan 
# 1 - create HASH algorithm function
# 2 - apply to all charachters in a step and find the result
# 3 - find reuslt of all steps and record values
# 4 - sum values

# 1
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

# 2 
def stepValue(string):
    char_list = list(string)
    current_value = 0
    for char in char_list:
        # all_values.append(hashAlgorithm(char, current_value))
        current_value = hashAlgorithm(char, current_value)
    return current_value

# 3
sum = 0
for step in data:
    # print('VALUE', stepValue(step))
    sum += stepValue(step)

print(sum)

