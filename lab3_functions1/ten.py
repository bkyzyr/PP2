def uniqueness(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

user_input = input()

input_list = user_input.split()

result = uniqueness(input_list)
print(result)
