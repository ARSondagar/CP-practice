size = int(input())
s = input()
slvl = 0
vlly = 0
for i in s:
    if i == 'U':
        slvl += 1
    else:
        slvl -= 1
    if i == 'U' and slvl == 0:
        vlly += 1
print(vlly)
