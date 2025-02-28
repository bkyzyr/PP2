text = str(input())

is_palindrome = text.lower() == text[::-1].lower()

print(is_palindrome)
