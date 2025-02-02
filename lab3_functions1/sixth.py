def reverse_sentence():
    user_input = input()
    
    reversed_sentence = ' '.join(user_input.split()[::-1])
    
    return reversed_sentence

result = reverse_sentence()
print(result)
