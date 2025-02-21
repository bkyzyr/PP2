import re

def match_string(s):
    return s[:1].isupper() and s[1:].islower()

test_string = str(input())
print(match_string(test_string))