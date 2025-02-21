import re

def add_spaces(s):
    return " ".join(re.findall(r"[A-Z][a-z]*", s))

test_string = str(input())
print(add_spaces(test_string))
