file_path = './src/Day13/Data13.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

data = file_content.split('\n')

all_sections = []
section = []

for index, line in enumerate(data):
    if line == '':
        all_sections.append(section)
        section = []
    elif index == len(data) - 1:
        section.append(line)
        all_sections.append(section)
    else:
        section.append(line)

# print(all_sections)

def horizontalSymmetry(section):
    # find where rows are equal
    sectionHeight = len(section)
    for i in range(1, len(section)): # iterate through all rows
        if section[i] == section[i-1]: # if two neighbouring rows are equal to each other then check the rows outside until you reach the edge of the section
            if i == 1: # if the line of symmetry is at the start of the section
                return 0.5
            elif i == sectionHeight - 1: # if the line of symmetry is at the end of the section
                return sectionHeight - 1.5
            else:
                # print('horizontal match at:', i, i-1)
                for j in range(1, min(sectionHeight - i, i)): # check all the rows surrounding are also symmetrical, check until reaching the outside of the section
                    if (section[i - 1 - j] != section[i + j]):
                        break
                    elif (section[i - 1 - j] == section[i + j]) and (j == min(sectionHeight - i, i) - 1):
                        return i - 0.5


def verticalSymmetry(section):
    # find where columns are equal
    # do this by inverting the seciton and using the code from before
    InvertedSection = []
    for i in range(len(section[0])):
        section2 = []
        for line in section:
            section2.append(line[i])
        InvertedSection.append(section2)
    InvertedSection = [''.join(line) for line in InvertedSection]
    # print(InvertedSection)
    sectionHeight = len(InvertedSection)
    for i in range(1, len(InvertedSection)): 
        if InvertedSection[i] == InvertedSection[i-1]: 
            if i == 1:
                return 0.5
            elif i == sectionHeight - 1:
                return sectionHeight - 1.5
            else:
                # print('vertical match at:', i, i-1)
                boundary = min(sectionHeight - i, i)
                for j in range(1, boundary):
                    if (InvertedSection[i - 1 - j] != InvertedSection[i + j]):
                        rowIdenticalness = False
                        break
                    elif (InvertedSection[i - 1 - j] == InvertedSection[i + j]) and (j == boundary - 1):
                        return i - 0.5

total = 0

for index, section in enumerate(all_sections):
    # print('section', index)
    # find lines of symmetry
    horizontalLine = horizontalSymmetry(section)
    # print('horizontal:', horizontalLine)
    verticalLine = verticalSymmetry(section)
    # print('vertical:', verticalLine)

    if horizontalLine:
        total += (horizontalLine + 0.5) * 100
    elif verticalLine:
         total += verticalLine + 0.5

print('part 1:', int(total))

# Part 2 

def numberOfDifferences(row1, row2):
    totalDifferences = 0
    for i in range(len(row1)):
        if row1[i] != row2[i]:
            totalDifferences += 1
    return totalDifferences


def horizontalSymmetry2(section):
    # find where rows are equal
    sectionHeight = len(section)
    for i in range(1, len(section)): # iterate through all rows
        smudgeCount = 0 # we need to find exactly one smudge (one error in the symmetry)
        if numberOfDifferences(section[i], section[i-1]) == 1: # all other lines need to be equal
            if i == 1: # if the line of symmetry is at the start of the section
                return 0.5
            elif i == sectionHeight - 1: # if the line of symmetry is at the end of the section
                return sectionHeight - 1.5
            else:
                # print('horizontal match at:', i, i-1)
                for j in range(1, min(sectionHeight - i, i)): # check all the rows surrounding are also symmetrical, check until reaching the outside of the section
                    if (section[i - 1 - j] != section[i + j]):
                        break
                    elif (section[i - 1 - j] == section[i + j]) and (j == min(sectionHeight - i, i) - 1):
                        return i - 0.5
        if (section[i] == section[i-1]): # if two neighbouring rows are equal to each other then check the rows outside until you reach the edge of the section
            # print('horizontal match at:', i, i-1)
            for j in range(1, min(sectionHeight - i, i)): # check all the rows surrounding are also symmetrical, check until reaching the outside of the section
                if (numberOfDifferences(section[i - 1 - j], section[i + j]) > 1): # if 2 rows have more than 1 difference
                    break
                elif (numberOfDifferences(section[i - 1 - j], section[i + j]) == 1) and (j != min(sectionHeight - i, i) - 1): # if 2 rows have 1 difference and are not the final rows
                    smudgeCount += 1
                elif (numberOfDifferences(section[i - 1 - j], section[i + j]) == 1) and (j == min(sectionHeight - i, i) - 1): # if 2 rows have 1 difference and are the final rows
                    return i - 0.5
                elif (section[i - 1 - j] == section[i + j]) and (j == min(sectionHeight - i, i) - 1) and smudgeCount == 1: # if 2 rows are equal and its the final row and smudge count is 1
                    return i - 0.5


def verticalSymmetry2(section):
    # find where columns are equal
    # do this by inverting the seciton and using the code from before
    InvertedSection = []
    for i in range(len(section[0])):
        section2 = []
        for line in section:
            section2.append(line[i])
        InvertedSection.append(section2)
    InvertedSection = [''.join(line) for line in InvertedSection]
    # print(InvertedSection)
    sectionHeight = len(InvertedSection)
    for i in range(1, len(InvertedSection)): # iterate through all rows
        smudgeCount = 0 # we need to find exactly one smudge (one error in the symmetry)
        if numberOfDifferences(InvertedSection[i], InvertedSection[i-1]) == 1: # all other lines need to be equal
            if i == 1: # if the line of symmetry is at the start of the section
                return 0.5
            elif i == sectionHeight - 1: # if the line of symmetry is at the end of the section
                return sectionHeight - 1.5
            else:
                # print('horizontal match at:', i, i-1)
                for j in range(1, min(sectionHeight - i, i)): # check all the rows surrounding are also symmetrical, check until reaching the outside of the section
                    if (InvertedSection[i - 1 - j] != InvertedSection[i + j]):
                        break
                    elif (InvertedSection[i - 1 - j] == InvertedSection[i + j]) and (j == min(sectionHeight - i, i) - 1):
                        return i - 0.5
        if (InvertedSection[i] == InvertedSection[i-1]): # if two neighbouring rows are equal to each other then check the rows outside until you reach the edge of the section
            # print('horizontal match at:', i, i-1)
            for j in range(1, min(sectionHeight - i, i)): # check all the rows surrounding are also symmetrical, check until reaching the outside of the section
                if (numberOfDifferences(InvertedSection[i - 1 - j], InvertedSection[i + j]) > 1): # if 2 rows have more than 1 difference
                    break
                elif (numberOfDifferences(InvertedSection[i - 1 - j], InvertedSection[i + j]) == 1) and (j != min(sectionHeight - i, i) - 1): # if 2 rows have 1 difference and are not the final rows
                    smudgeCount += 1
                elif (numberOfDifferences(InvertedSection[i - 1 - j], InvertedSection[i + j]) == 1) and (j == min(sectionHeight - i, i) - 1): # if 2 rows have 1 difference and are the final rows
                    return i - 0.5
                elif (InvertedSection[i - 1 - j] == InvertedSection[i + j]) and (j == min(sectionHeight - i, i) - 1) and smudgeCount == 1: # if 2 rows are equal and its the final row and smudge count is 1
                    return i - 0.5


total2 = 0

for index, section in enumerate(all_sections):
    # print('section', index)
    # find lines of symmetry
    horizontalLine2 = horizontalSymmetry2(section)
    # print('horizontal:', horizontalLine2)
    verticalLine2 = verticalSymmetry2(section)
    # print('vertical:', verticalLine2)

    if horizontalLine2:
        total2 += (horizontalLine2 + 0.5) * 100
    elif verticalLine2:
         total2 += verticalLine2 + 0.5
    else:
        print('FAAAAAIIIIIIILLLLLLL')

print('part 2:', int(total2))