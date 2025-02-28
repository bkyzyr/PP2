source_file = input("the source file path: ")
destination_file = input("destination of file path: ")

src = open(source_file, 'r', encoding="utf-8")
content = src.read()
src.close()

dest = open(destination_file, 'w', encoding="utf-8")
dest.write(content)
dest.close()

print("file is copied now")
