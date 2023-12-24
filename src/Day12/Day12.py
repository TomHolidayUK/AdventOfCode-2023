file_path = './src/Day12/Data12-test.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

data = file_content.split('\n')

def findNumberOfArrangements(configuration, numbers):

    if configuration == "":
        print('test2')
        return 1 if not numbers else 0
    
    # if configuration == "" and numbers:
    #     print('test2')
    #     return 0
    
    if not numbers:
        return 0 if '#' in configuration else 1
    
    totalArrangements = 0

    print(configuration)
    print(numbers)
    print(totalArrangements)

    if configuration[0] == '?' or configuration[0] == '.':
        totalArrangements += findNumberOfArrangements(configuration[1:], numbers)

    if configuration[0] == '#' or configuration[0] == '?':
        condition1 = (numbers[0] <= len(configuration))
        condition2 = ('.' not in configuration[:numbers[0]])
        condition3 = ((numbers[0] == len(configuration)) or (configuration[numbers[0]] != '#'))
        print(condition1, condition2, condition3)
        if condition1 and condition2 and condition3:
             totalArrangements += findNumberOfArrangements(configuration[numbers[0] + 1:], numbers[1:])
        else:
            return 0

    return totalArrangements

total = 0 

for line in data:
    configuration, numbers = line.split(' ')
    numbers = tuple(map(int, numbers.split(',')))
    # print(findNumberOfArrangements(configuration, numbers))
    print('new')
    total += findNumberOfArrangements(configuration, numbers)

print(total)









