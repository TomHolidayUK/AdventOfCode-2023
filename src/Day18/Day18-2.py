file_path = './src/Day18/Data18.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

data = [row.split() for row in file_content.split('\n')]
data2 = [elem[2] for elem in data]
data3 = [[int(elem[2:7], 16), int(elem[7])] for elem in data2]
print(data3)

# Applying code from Part 1 doesn't work, creating a matrix nd calculating from that doesn't scale to the large distances in part 2
# Therefore we need to be more clever
# After looking online I found out that we can use Shoelace Theory (to find the area of the interior) and Pick's Theorem (to relate the boundary length to the area of the interior)

# Shoelace theory: the internal Area = 0.5 * the sum of (x * (y_next - y_prev))
x, y = 0, 0
y_record = [0]
x_record = [0]
for elem in data3:
    if elem[1] == 1:
        y += elem[0]
    elif elem[1] == 3:
        y -= elem[0]
    elif elem[1] == 0:    
        x += elem[0]
    elif elem[1] == 2:    
        x -= elem[0]
    y_record.append(y)
    x_record.append(x)

print(y_record)
print(x_record)

internal_area = 0

for i in range(len(data3)):
    if i == 0:
        print('test')
        internal_area += x_record[i] * (y_record[i+1] - y_record[-1])
    elif i == len(data3) - 1:
        print('test2')
        internal_area += x_record[i] * (y_record[0] - y_record[i-1])
    else:  
        internal_area += x_record[i] * (y_record[i+1] - y_record[i-1])
    print(internal_area)

print('internal area:', internal_area / 2)

# Pick's theorem: internal area = number of inside points +  0.5 * number of boundary points - 1
# Therefore: number of inside points = internal area - (0.5 * number of boundary points) + 1

boundary_length = 0
for elem in data3:
    boundary_length += elem[0]

print('boundary length:', boundary_length)

inside_points = (internal_area / 2) - (0.5 * boundary_length) + 1

print('inside points:', inside_points)

print('total area:', int(inside_points + boundary_length))

# 3010445298 - too low