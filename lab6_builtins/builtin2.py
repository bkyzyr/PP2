s = str(input())
upper_count = sum(map(str.isupper, s))  
lower_count = sum(map(str.islower, s)) 
    
print("upper case letters:", upper_count)
print("lower case letters:", lower_count)