file_path = input()

try:
    with open(file_path, 'r', encoding="utf-8") as file:
        line_count = sum(1 for line in file)
    print("number of lines:", line_count)
except FileNotFoundError:
    print("file doesn't exist")