file_path = './src/Day16/Data16-test.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

data = file_content.split('\n')
print(data)