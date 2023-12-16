file_path9 = './src/Day9/data9.txt'

with open(file_path9, 'r', encoding='utf-8') as file:
    file_content9 = file.read()

# Split the content into lines
lined_data9 = file_content9.split('\n')

data_array = map(lambda x: x.split(' '), lined_data9)
squared_numbers_list = list(data_array)

array_of_arrays_of_integers = [[int(element) for element in inner_array] for inner_array in squared_numbers_list]


# print(array_of_arrays_of_integers)

testdata9 = [
    [0, 3, 6, 9, 12, 15],
    [1, 3, 6, 10, 15, 21],
    [10, 13, 16, 21, 30, 45]
]

all_all_differences =  []

for array in array_of_arrays_of_integers:
    all_differences = [array]

    def find_differences(array):
        differences = [array[i+1] - array[i] for i in range(len(array)-1)]
        all_differences.append(differences)
        if all(diff == 0 for diff in differences):
            return all_differences
        else:
            return find_differences(differences)

    all_all_differences.append(find_differences(array))

print(all_all_differences)


def find_new_end(input_array):
    final_value = 0

    input_array[-1].append(0)

    for i in range(len(input_array)-2, -1, -1):
        new_value = input_array[i][0] - input_array[i+1][0]
        if i == 0:
            final_value = new_value
        input_array[i].insert(0, new_value)
    print(final_value)
    return final_value


accumulator = 0

for i in range(len(array_of_arrays_of_integers)):
    accumulator += find_new_end(all_all_differences[i])

print(accumulator)



