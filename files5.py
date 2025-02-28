my_list = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

file_path = input("write the file path where to save the list: ")

with open(file_path, 'w', encoding="utf-8") as file:
    for item in my_list:
        file.write(item + "\n")

print("list is in the file now")
