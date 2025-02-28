from pathlib import Path

path = Path(input("Enter the path to check: "))

if path.exists():
    print("path exists")
    print("directory portion:", path.parent)
    print("filename:", path.name)
else:
    print("path does not exist.")
