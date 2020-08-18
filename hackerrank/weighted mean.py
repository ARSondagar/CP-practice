
size = int(input())
x = [int(i) for i in input().split()]
w = [int(j) for j in input().split()]
sm = 0
for m in range(size):
    sm += x[m]*w[m]
wm = sm / sum(w)
print("%.1f" % round(wm, 1))
