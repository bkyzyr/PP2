def is_palindrome(input_string):
    cleaned_string = ""
    for char in input_string:
        cleaned_string += char.lower()
    
    return cleaned_string == cleaned_string[::-1]

user_input = input()
if is_palindrome(user_input):
    print("palindrome")
else:
    print("not a palindrome")