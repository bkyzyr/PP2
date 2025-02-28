for char in range(65, 91):
    filename = f"{chr(char)}.txt"
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(f"it's file {filename}\n")  
    print(f"name of the file: {filename}")