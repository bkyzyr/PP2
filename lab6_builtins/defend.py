import re

inputt = input()
searchh = bool(re.match(r"*@example.com", inputt))
print(searchh)