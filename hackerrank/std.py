n = int(input())
arr = [int(i) for i in input().split()]

avg = sum(arr) / len(arr)
sumation = 0
for j in arr:
    sumation += (j - avg)**2
std = (sumation / len(arr))**0.5
print("%.1f" % round(std, 1))
