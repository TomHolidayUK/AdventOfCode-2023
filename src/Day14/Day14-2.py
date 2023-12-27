import copy

file_path = './src/Day14/Data14.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

data = file_content.split('\n')

matrix = []
for el in data:
        matrix.append([x for x in el])
# print(matrix)

# Plan
# For each row start at the bottom and go up
# If there is a O count it and replace it with a '.', when you reach a # or the end, add the relevant number of O

# north west south east

def North(localMatrix):
    for i in range(len(matrix[0])):
        count = 0
        # print('i', i)
        for j in range(len(matrix) - 1, -1, -1):
            # print(localMatrix[j][i])
            # print('j', j)
            if localMatrix[j][i] == 'O' and j > 0:
                # print('test1', j)
                count += 1
                localMatrix[j][i] = '.'
            elif localMatrix[j][i] == '#' and count > 0:
                # print('test2', j)
                for k in range(j + 1, j + count + 1):
                    # print(k)
                    localMatrix[k][i] = 'O'
                count = 0 
            elif localMatrix[j][i] == 'O' and j == 0:
                # print('test3', j)
                for k in range(j, j + count + 1):
                    # print(k)
                    localMatrix[k][i] = 'O'
                count = 0 
            elif localMatrix[j][i] == '.' and j == 0 and count > 0:
                # print('test4', j)
                for k in range(j, j + count):
                    # print(k)
                    localMatrix[k][i] = 'O'
                count = 0 
        # print(localMatrix)
    return localMatrix

def West(localMatrix):
    for i in range(len(matrix)):
        count = 0
        # print('i', i)
        for j in range(len(matrix[0]) - 1, -1, -1):
            # print(localMatrix[i][j])
            # print('j', j)
            if localMatrix[i][j] == 'O' and j > 0:
                # print('test1', j)
                count += 1
                localMatrix[i][j] = '.'
            elif localMatrix[i][j] == '#' and count > 0:
                # print('test2', j)
                for k in range(j + 1, j + count + 1):
                    # print(k)
                    localMatrix[i][k] = 'O'
                count = 0 
            elif localMatrix[i][j] == 'O' and j == 0:
                # print('test3', j)
                for k in range(j, j + count + 1):
                    # print(k)
                    localMatrix[i][k] = 'O'
                count = 0 
            elif localMatrix[i][j] == '.' and j == 0 and count > 0:
                # print('test4', j)
                for k in range(j, j + count):
                    # print(k)
                    localMatrix[i][k] = 'O'
                count = 0 
        # print(localMatrix)
    return localMatrix

def South(localMatrix):
    for i in range(len(matrix[0])):
        count = 0
        # print('i', i)
        for j in range(len(matrix)):
            # print(localMatrix[j][i])
            # print('j', j)
            # print('length', len(matrix))
            if localMatrix[j][i] == 'O' and j < len(matrix) - 1:
                # print('test1', j)
                count += 1
                localMatrix[j][i] = '.'
            elif localMatrix[j][i] == '#' and count > 0:
                # print('test2', j)
                for k in range(j - 1, j - count - 1, -1):
                    # print(k)
                    localMatrix[k][i] = 'O'
                count = 0 
            elif localMatrix[j][i] == 'O' and j == len(matrix) - 1:
                # print('test3', j)
                for k in range(j, j - count - 1, -1):
                    # print(k)
                    localMatrix[k][i] = 'O'
                count = 0 
            elif localMatrix[j][i] == '.' and j == len(matrix) - 1 and count > 0:
                # print('test4', j)
                for k in range(j, j - count, -1):
                    # print(k)
                    localMatrix[k][i] = 'O'
                count = 0 
    return localMatrix

def East(localMatrix):
    for i in range(len(localMatrix)):
        count = 0
        # print('i', i)
        for j in range(len(localMatrix[0])):
            # print(localMatrix[i][j])
            # print('j', j)
            if localMatrix[i][j] == 'O' and j < len(localMatrix[0]) - 1:
                # print('test1', j)
                count += 1
                localMatrix[i][j] = '.'
            elif localMatrix[i][j] == '#' and count > 0:
                # print('test2', j)
                for k in range(j - 1, j - count - 1, -1):
                    # print(k)
                    localMatrix[i][k] = 'O'
                count = 0 
            elif localMatrix[i][j] == 'O' and j == len(localMatrix[0]) - 1:
                # print('test3', j)
                for k in range(j, j - count - 1, -1):
                    # print(k)
                    localMatrix[i][k] = 'O'
                count = 0 
            elif localMatrix[i][j] == '.' and j == len(localMatrix[0]) - 1 and count > 0:
                # print('test4', j)
                for k in range(j, j - count, -1):
                    # print(k)
                    localMatrix[i][k] = 'O'
                count = 0 
        # print(localMatrix)
    return localMatrix

numberOfCycles = 0 

def numberOfRocks(inputMatrix):
    count = 0
    for row in inputMatrix:
        for char in row:
            if char == 'O':
                count += 1 
    return count

print('starting number of rocks:', numberOfRocks(matrix))

def identicalMatrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return False

    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            if matrix1[i][j] != matrix2[i][j]:
                return False

    return True

def scoreCalculator(matrix):
    matrixLength = len(matrix)
    total = 0
    for index, row in enumerate(matrix):
        for char in row:
            if char == 'O':
                total += (matrixLength - index)
    return total
                


def Cycle(inputMatrix):
    # while numberOfCycles <= 2:
    initialMatrix = copy.deepcopy(inputMatrix)
    global numberOfCycles
    result1 = North(inputMatrix)
    # print(numberOfRocks(result1))
    # print('\n'.join([''.join(x) for x in result1]))
    # print('----------------')
    result2 = West(result1)
    # print(numberOfRocks(result2))
    # print('\n'.join([''.join(x) for x in result2]))
    # print('----------------')
    result3 = South(result2)
    # print(numberOfRocks(result3))
    # print('\n'.join([''.join(x) for x in result3]))
    # print('----------------')
    result4 = East(result3)
    # print('number of rocks:', numberOfRocks(result4))
    numberOfCycles += 1
    print(f'At cycle {numberOfCycles} the score = {scoreCalculator(result4)}')
    # stringData = '\n'.join([''.join(x) for x in result4])
    # print(stringData)
    # print('number of cycles:', numberOfCycles)
    # print('*****************')
    if identicalMatrices(result4, initialMatrix):
        print(f'Equilibrium has been reached at {numberOfCycles} number of cycles')
        print('Output:')
        return result4
    elif numberOfCycles < 5000:
        return Cycle(result4)
    else:
        return result4


finalResult = Cycle(matrix)

stringData = '\n'.join([''.join(x) for x in finalResult])
print('number of cycles:', numberOfCycles)
print(stringData);

# from observing the test data (the score every cycle) it can be seen that it reaches an equilibrium where it repeats every 7 cycles
# 1000000001 is divisbible by 7 
# 973 is also divisible by 7 
# therefore at (973 - 1 = 972) the score is 64, therefore it will be the same at 1000000000

# in the real data:
# it can be seen that it reaches an equilibrium where it repeats every 33 cycles
def findNextDividor(iterator, divisor):
    if iterator % divisor == 0:
        print(iterator)
        return iterator
    else:
        iterator += 1
        return findNextDividor(iterator, divisor)
print(findNextDividor(933, 34))
# 1000000010 is divisible by 34 
# 952 is also divisible by 34
# therefore at (952 - 10 = 942) the score is 112452, therefore it will be the same at 1000000000

