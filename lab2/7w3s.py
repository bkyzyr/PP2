names = ["kate", "Danyel", "Alex"]
newlst = []
for n in names:
    if "l" in n:
        newlst.append(n)

print(newlst)

#shorter: newlst = [n for n in names if "a" in n]