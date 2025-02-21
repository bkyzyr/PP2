import re

def snake_to_camel(s):
    return "".join(word.title() for word in re.split(r"_+", s))

test_string = str(input())
print(snake_to_camel(test_string))

#re.split(r"_+", s) — разбивает строку по _
#word.title() — делает первую букву каждого слова upper
#"".join(...) — соединяет слова без пробелов