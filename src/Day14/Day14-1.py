file_path = './src/Day14/Data14.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

data = file_content.split('\n')

# print(data)

# Plan
# Invert data because it is easier to work with 
# For each row start at the bottom and go up
# If there is a O count it, when you reach a # or the end, work out the associated valueCount by relating the count to the line position

invertedData = []
for i in range(len(data[0])):
    section2 = []
    for line in data:
        section2.append(line[i])
    invertedData.append(section2)
invertedData = [''.join(line) for line in invertedData]
print(invertedData)

def calculateValue(count, distanceFromSouthEdge):
    total = 0
    for i in range(distanceFromSouthEdge, distanceFromSouthEdge - count, -1):
        # print('i', i)
        total += i
    return total

valueCount = 0

length = len(invertedData[0])

for line in invertedData:
    count = 0
    for i in range(length - 1, -1, -1):
        # print(line[i], i)
        if (line[i] == 'O') and (i != 0):
            count += 1
        elif (line[i] == '#' and count > 0):
            # print(count)
            # print(length - i - 1)
            # print(calculateValue(count, length - i - 1))
            valueCount += calculateValue(count, length - i - 1)
            count = 0
        elif (line[i] == 'O' and i == 0):
            # print(count)
            valueCount += calculateValue(count + 1, length - i)
        elif (line[i] == '.' and i == 0 and count > 0):
            # print(count)
            valueCount += calculateValue(count, length - i)
    print(valueCount)

print('final:', valueCount)





