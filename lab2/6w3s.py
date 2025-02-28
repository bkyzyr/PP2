list = ["pineapple", "apple", "watermelon"]
tropical = ["mango", "pineapple", "papaya"]
list.extend(tropical)
print("extended list: " , list)
list[0] = "banana"
list.insert(1, "cherry")
print("inserted list: " ,list)
if "watermelon" in list:
    print("YES, it's in the list")