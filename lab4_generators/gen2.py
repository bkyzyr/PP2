n = int(input())
res = []
for i in range(0, n+1, 2):
    res.append(str(i))
print(",".join(res))