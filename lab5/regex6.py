import re

def replace_chars(s):
    return re.sub(r"[ ,.]", ":", s) # r"[ ,.]" — ищет пробелы,запятые,точки а re.sub заменяет их на :

test_string = str(input())
print(replace_chars(test_string))  
