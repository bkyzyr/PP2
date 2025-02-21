import re

def match_string(s):
    return bool(re.fullmatch(r"a.*b", s)) # .* любой текст (ноль или другие символы) a это на что должно начинаться b это должно заканчиваться

test_string = str(input())
print(match_string(test_string))