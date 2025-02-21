import re

def match_string(s):
    return "_" in s and s.islower()

test_string= str(input())
print(match_string(test_string))
