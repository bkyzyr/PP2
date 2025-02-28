import os

path = input("Enter the directory path: ")
directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
print("directories:", directories)

files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
print("files:",files)

all_items = os.listdir(path)
print(all_items)
