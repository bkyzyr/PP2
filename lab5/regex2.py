import re

def match_string(s):
    return bool(re.fullmatch("abb|abbb", s))

test_string = str(input())
print(match_string(test_string))