def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

def main():
    user_input = input()
    
    nums = list(map(int, user_input.split()))
    
    result = has_33(nums)
    print(result)

main()
