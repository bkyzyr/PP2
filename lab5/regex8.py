import re

def split_at_uppercase(s):
    return re.findall(r"[A-Z][a-z]*", s)

test_string = str(input())
print(split_at_uppercase(test_string))
#"[A-Z][a-z]*" — находит слова, начинающиеся с заглавной
#re.findall() возвращает их список