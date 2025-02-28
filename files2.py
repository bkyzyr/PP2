from pathlib import Path
path = Path(input())
print("existence: ", path.exists())
print("readability: ", path.is_file() or path.is_dir())
print("writability:", path.exists() and path.stat().st_mode)
print("execution:", path.exists() and path.stat().st_mode)