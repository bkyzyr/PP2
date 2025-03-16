def func(nums):
    uslovie = [0, 0, 7]
    index = 0
 
    for input in nums:
        if input == uslovie[index]:
            index += 1
        if index == len(uslovie): 
            return True
    return False
user_input = input()

nums = list(map(int, user_input.split()))

print(func(nums))