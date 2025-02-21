import re

def camel_to_snake(s):
    return "_".join(re.findall(r"[A-Za-z][a-z]*", s)).lower()

test_string = str(input())
print(camel_to_snake(test_string))
#re.findall(r"[A-Za-z][a-z]*", s) разбивает строку на слова
#"_".join(...) соединяет через _
#.lower() меняет на нижний регистр