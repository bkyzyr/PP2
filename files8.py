import os  

file_path = input("which path to delete: ")

if os.path.exists(file_path):
    if os.access(file_path, os.R_OK) and os.access(file_path, os.W_OK):
        os.remove(file_path)
        print("file is deleted now")
    else:
        print("file exists but its not accessible")
else:
    print("file does not exist.")
